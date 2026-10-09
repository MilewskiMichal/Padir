#!/usr/bin/env python3
"""Zapisuje szkic strony do WordPressa jako NIEOPUBLIKOWANY.

    python3 szkic_wdroz.py grawerowanie            # próba na sucho
    python3 szkic_wdroz.py grawerowanie --wdroz

Bezpieczniki, w tej kolejnosci:
  1. Tresc musi przejsc `sprawdz_szkic.py --szkic`. Inaczej nic nie idzie.
  2. Skrypt NIGDY nie dotyka stron produkcyjnych 456 i 1011. Szuka szkicu
     po slugu `<...>-szkic` i statusie `draft`; jesli takiego nie ma,
     zaklada nowa strone. Identyfikatory produkcyjne sa na liscie zakazanej.
  3. Po zapisie sprawdza w odpowiedzi API, ze status to `draft`.
     Gdyby WordPress z jakiegos powodu opublikowal strone, skrypt od razu
     cofa ja do szkicu i krzyczy.
  4. Przed nadpisaniem istniejacego szkicu robi kopie poprzedniej wersji.

Wzor to szkic 2530 „wycinanie-laserowe-szkic”: ten sam szablon
`page-no-title`, bo nowy uklad ma wlasny naglowek.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call

STRONY = {
    "grawerowanie": {"slug": "grawerowanie-laserowe-szkic",
                     "tytul": "Grawerowanie laserowe (szkic do akceptacji)"},
    "frezowanie": {"slug": "frezowanie-cnc-szkic",
                   "tytul": "Frezowanie CNC (szkic do akceptacji)"},
}
PRODUKCYJNE = {456, 1011, 1019, 1397}
SZABLON = "page-no-title"


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in STRONY:
        print(__doc__)
        sys.exit(2)
    klucz = sys.argv[1]
    na_sucho = "--wdroz" not in sys.argv
    cfg = STRONY[klucz]
    plik = os.path.join(HERE, "praca", klucz, "strona.html")
    tresc = open(plik, encoding="utf-8").read()

    print(f"szkic: {klucz}  ({len(tresc)} znaków)")
    wynik = subprocess.run([sys.executable, "-I", os.path.join(HERE, "sprawdz_szkic.py"),
                            plik, "--szkic"], capture_output=True, text=True)
    print("  " + wynik.stdout.strip().splitlines()[0])
    if wynik.returncode != 0:
        print(wynik.stdout)
        print("PRZERYWAM: sprawdzarka zgłasza błędy.")
        sys.exit(1)
    print("  sprawdzarka: czysto")

    st, istniejace = call("GET", f"/wp/v2/pages?slug={cfg['slug']}&status=draft,pending,private,publish"
                                 f"&context=edit&_fields=id,slug,status,link,content")
    istniejace = istniejace if st == 200 else []
    if istniejace:
        p = istniejace[0]
        if p["id"] in PRODUKCYJNE:
            sys.exit(f"PRZERYWAM: slug {cfg['slug']} wskazuje na stronę produkcyjną {p['id']}")
        if p["status"] != "draft":
            sys.exit(f"PRZERYWAM: strona {p['id']} ma status {p['status']}, a miał być szkic")
        print(f"  istniejący szkic: {p['id']} [{p['status']}]")
    else:
        p = None
        print("  szkicu jeszcze nie ma, zostanie założony")

    if na_sucho:
        print("\n(PRÓBA NA SUCHO, nic nie zapisano)")
        return

    if p:
        kopia = os.path.join(HERE, "praca", klucz, f"backup-szkic-{p['id']}.json")
        json.dump({"id": p["id"], "content": p["content"]["raw"]},
                  open(kopia, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"  kopia poprzedniej wersji: {os.path.relpath(kopia, HERE)}")

    cialo = {"title": cfg["tytul"], "slug": cfg["slug"], "status": "draft",
             "template": SZABLON, "content": tresc, "comment_status": "closed"}
    st2, r = call("POST", f"/wp/v2/pages/{p['id']}" if p else "/wp/v2/pages", body=cialo)
    print(f"\nzapis: HTTP {st2}")
    if st2 not in (200, 201):
        print(json.dumps(r, ensure_ascii=False)[:500])
        sys.exit(1)
    if r.get("status") != "draft":
        call("POST", f"/wp/v2/pages/{r['id']}", body={"status": "draft"})
        sys.exit(f"ALARM: strona {r['id']} miała status {r.get('status')}, cofnięta do szkicu")
    if r["id"] in PRODUKCYJNE:
        sys.exit(f"ALARM: zapis trafił w stronę produkcyjną {r['id']}")
    print(f"  id: {r['id']}   status: {r['status']}   szablon: {r.get('template')}")
    print(f"  podgląd w panelu: https://grawerowanie-laserowe.pl/?page_id={r['id']}&preview=true")
    json.dump({"id": r["id"], "slug": cfg["slug"]},
              open(os.path.join(HERE, "praca", klucz, "szkic-id.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
