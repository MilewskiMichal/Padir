#!/usr/bin/env python3
"""Zapisuje wpis na blogu do WordPressa jako SZKIC (status draft).

    python3 wpis_wdroz.py grawer-sprzet-do-kawy            # próba na sucho
    python3 wpis_wdroz.py grawer-sprzet-do-kawy --wdroz

Katalog wpisu `<klucz>/` zawiera:
  wpis.json        slug, tytuł, zajawka, kategorie, obrazek wyróżniający, pola Yoast
  tresc-body.html  treść wpisu (bez arkusza i bez opakowania)
Skrypt skleja `tresc.html`: blok HTML, kontener .padir-art, wspólny arkusz
`styl-padir-art.css` (z wpisu 2550) plus dopisek z wpis.json, treść z twardymi
spacjami po jednoliterowych wyrazach.

Bezpieczniki:
  1. Treść musi przejść `sprawdz_szkic.py --wpis` z 0 błędów.
  2. Skrypt nigdy nie dotyka wpisu, który nie jest szkicem (publish, future,
     pending, private): wtedy przerywa.
  3. Przed nadpisaniem istniejącego szkicu robi kopię `<klucz>/backup-wpis-<id>.json`.
  4. Po zapisie sprawdza status draft i zgodność treści z plikiem.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORDPRESS = os.path.dirname(HERE)
sys.path.insert(0, WORDPRESS)
from wp import call  # noqa: E402

SPRAWDZARKA = os.path.join(WORDPRESS, "narzedzia", "sprawdz_szkic.py")


def nb(tekst):
    """Twarda spacja po jednoliterowych wyrazach, tylko w tekście poza znacznikami."""
    def w_tekscie(m):
        t = m.group(0)
        for _ in range(2):
            t = re.sub(r'(^|[\s(„>])([aiouwzAIOUWZ]) ', '\\1\\2 ', t)
        return t
    return re.sub(r'>[^<]+', w_tekscie, tekst)


def sklej(klucz, cfg):
    styl = open(os.path.join(HERE, "styl-padir-art.css"), encoding="utf-8").read().strip()
    if cfg.get("css_dopisek"):
        styl = styl.replace("</style>", "\n" + cfg["css_dopisek"].strip() + "\n</style>")
    body = open(os.path.join(HERE, klucz, "tresc-body.html"), encoding="utf-8").read().strip()
    return ("<!-- wp:html -->\n<div class=\"padir-art\">\n" + styl + "\n\n" + nb(body)
            + "\n\n</div>\n<!-- /wp:html -->")


def main():
    if len(sys.argv) < 2 or not os.path.isfile(os.path.join(HERE, sys.argv[1], "wpis.json")):
        print(__doc__)
        sys.exit(2)
    klucz = sys.argv[1]
    na_sucho = "--wdroz" not in sys.argv
    cfg = json.load(open(os.path.join(HERE, klucz, "wpis.json"), encoding="utf-8"))
    tresc = sklej(klucz, cfg)
    plik = os.path.join(HERE, klucz, "tresc.html")
    open(plik, "w", encoding="utf-8").write(tresc)
    for pole in ("tytul", "zajawka"):
        if any(z in cfg[pole] for z in "—–"):
            sys.exit(f"PRZERYWAM: pauza w polu {pole}")
    for k, v in cfg.get("yoast", {}).items():
        if any(z in v for z in "—–"):
            sys.exit(f"PRZERYWAM: pauza w polu Yoast {k}")

    print(f"wpis: {klucz}  ({len(tresc)} znaków)")
    w = subprocess.run([sys.executable, "-I", SPRAWDZARKA, plik, "--szkic", "--wpis"], capture_output=True, text=True)
    print("  " + w.stdout.strip().splitlines()[0])
    if w.returncode != 0:
        print(w.stdout)
        sys.exit("PRZERYWAM: sprawdzarka zgłasza błędy.")
    print("  sprawdzarka: czysto")

    st, ist = call("GET", f"/wp/v2/posts?slug={cfg['slug']}&status=draft,pending,private,publish,future"
                          f"&context=edit&_fields=id,status,link,content")
    ist = ist if st == 200 else []
    p = ist[0] if ist else None
    if p and p["status"] != "draft":
        sys.exit(f"PRZERYWAM: wpis {p['id']} ma status {p['status']}; ten skrypt zmienia tylko szkice")
    print(f"  {'istniejący szkic: ' + str(p['id']) if p else 'szkicu jeszcze nie ma, zostanie założony'}")
    if na_sucho:
        print("\n(PRÓBA NA SUCHO, nic nie zapisano)")
        return

    if p:
        kopia = os.path.join(HERE, klucz, f"backup-wpis-{p['id']}.json")
        json.dump({"id": p["id"], "content": p["content"]["raw"]}, open(kopia, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"  kopia poprzedniej wersji: {os.path.relpath(kopia, HERE)}")
    cialo = {"title": cfg["tytul"], "slug": cfg["slug"], "status": "draft", "content": tresc,
             "excerpt": cfg["zajawka"], "categories": cfg["kategorie"], "comment_status": "closed",
             "meta": {f"_yoast_wpseo_{k}": v for k, v in cfg.get("yoast", {}).items()}}
    if cfg.get("obrazek"):
        cialo["featured_media"] = cfg["obrazek"]
    st2, r = call("POST", f"/wp/v2/posts/{p['id']}" if p else "/wp/v2/posts", body=cialo)
    print(f"\nzapis: HTTP {st2}")
    if st2 not in (200, 201):
        print(json.dumps(r, ensure_ascii=False)[:500])
        sys.exit(1)
    if r.get("status") != "draft":
        call("POST", f"/wp/v2/posts/{r['id']}", body={"status": "draft"})
        sys.exit(f"ALARM: wpis {r['id']} miał status {r.get('status')}, cofnięty do szkicu")
    st3, po = call("GET", f"/wp/v2/posts/{r['id']}?context=edit&_fields=id,status,content,meta,featured_media")
    zgodna = po["content"]["raw"] == tresc
    print(f"  id: {r['id']}   status: {po['status']}   treść zgodna z plikiem: {zgodna}   obrazek: {po['featured_media']}")
    print(f"  Yoast: { {k: v for k, v in po.get('meta', {}).items() if 'yoast' in k} }")
    print(f"  podgląd w panelu: https://grawerowanie-laserowe.pl/?p={r['id']}&preview=true")
    json.dump({"id": r["id"], "slug": cfg["slug"]}, open(os.path.join(HERE, klucz, "wpis-id.json"), "w"), indent=1)
    if not zgodna:
        sys.exit("UWAGA: treść w WordPressie różni się od pliku")


if __name__ == "__main__":
    main()
