#!/usr/bin/env python3
"""Publikacja nowej strony Grawerowanie laserowe: treść szkicu 2584 trafia na stronę 456.

Zgoda zleceniodawcy: 05.11.2026 („ta nowa zakładka ... jest okej, możesz ją już publikować
i podmienić za obecnie istniejącą”).

Strona 456 zostaje tą samą stroną: ten sam adres /grawerowanie-laserowe/, te same podstrony
(prezenty 1812, grawerowanie na nożu 2228), ta sama pozycja w menu, ten sam tytuł, obrazek
wyróżniający i ustawienia Yoast (tytuł SEO i opis). Zmienia się:
  - treść: ze szkicu 2584,
  - szablon: page-no-title (jak 1019), bo stary szablon dokłada drugi <h1>.

Jedna zmiana treści względem szkicu: karta „Marketing i wydarzenia” traci link
„Grawer dla marketingu”, bo strona /uslugi-dla-marketingu/ (2602) jest jeszcze szkicem
(decyzja zleceniodawcy 05.11.2026: karta bez linku do czasu publikacji strony marketingu).

Przed zapisem treść musi przejść sprawdz_szkic.py w trybie produkcyjnym (bez --szkic) z 0 błędów.

    python3 publikacja_grawerowania.py            # próba na sucho
    python3 publikacja_grawerowania.py --wdroz
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call  # noqa: E402

SZKIC, STRONA = 2584, 456
SZABLON = "page-no-title"
KOPIA = os.path.join(HERE, "backup-456-przed-publikacja-nowej-strony.json")
LINK_MARKETING = re.compile(r'\s*<a href="/uslugi-dla-marketingu/"[^>]*>.*?</a>', re.S)


def sprawdz(tresc):
    plik = os.path.join(HERE, "_tmp-456.html")
    with open(plik, "w", encoding="utf-8") as f:
        f.write(tresc)
    w = subprocess.run([sys.executable, "-I", os.path.join(HERE, "sprawdz_szkic.py"), plik, "--json"],
                       capture_output=True, text=True)
    os.remove(plik)
    wynik = json.loads(w.stdout)
    return [b["opis"] for b in wynik["bledy"]], [o["opis"] for o in wynik.get("ostrzezenia", [])]


def main(wdroz):
    st, szkic = call("GET", f"/wp/v2/pages/{SZKIC}?context=edit&_fields=id,status,content")
    tresc = szkic["content"]["raw"]
    tresc, n = LINK_MARKETING.subn("", tresc)
    if n != 1:
        sys.exit(f"oczekiwałem dokładnie 1 linku do /uslugi-dla-marketingu/, jest {n}")
    if "uslugi-dla-marketingu" in tresc:
        sys.exit("w treści został inny odnośnik do /uslugi-dla-marketingu/")
    bledy, ostrz = sprawdz(tresc)
    print(f"treść: {len(tresc)} znaków, sprawdzarka: {len(bledy)} błędów, {len(ostrz)} ostrzeżeń")
    for b in bledy + ostrz:
        print("  ", b)
    if bledy:
        sys.exit("sprawdzarka zgłasza błędy, nic nie zapisuję")

    st, stara = call("GET", f"/wp/v2/pages/{STRONA}?context=edit"
                            "&_fields=id,status,slug,link,parent,template,title,featured_media,modified,content")
    # Dane strukturalne Service ze starej strony przechodzą bez zmian (szkic ich nie miał).
    ld = re.findall(r'<!-- wp:html -->\s*<script type="application/ld\+json"[^>]*>.*?</script>\s*<!-- /wp:html -->',
                    stara["content"]["raw"], re.S)
    if len(ld) != 1 or '"@type":"Service"' not in ld[0]:
        sys.exit(f"oczekiwałem 1 bloku JSON-LD Service na stronie {STRONA}, jest {len(ld)}")
    tresc = tresc.rstrip() + "\n\n" + ld[0] + "\n"
    bledy, _ = sprawdz(tresc)
    if bledy:
        sys.exit("po dołożeniu JSON-LD sprawdzarka zgłasza błędy: " + "; ".join(bledy))
    print(f"strona {STRONA} [{stara['status']}] {stara['link']}: szablon {stara['template']} -> {SZABLON}, "
          f"treść {len(stara['content']['raw'])} -> {len(tresc)} znaków")
    if not wdroz:
        print("próba na sucho, nic nie zapisano")
        return

    with open(KOPIA, "w", encoding="utf-8") as f:
        json.dump({"id": STRONA, "modified": stara["modified"], "template": stara["template"],
                   "title": stara["title"]["raw"], "featured_media": stara["featured_media"],
                   "content_raw": stara["content"]["raw"]}, f, ensure_ascii=False)
    print("kopia:", KOPIA)
    st, _ = call("POST", f"/wp/v2/pages/{STRONA}", {"content": tresc, "template": SZABLON})
    print("zapis: HTTP", st)
    st, po = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=status,slug,template,title,content")
    print(f"po zapisie: {po['status']} {po['slug']} szablon={po['template']} tytuł={po['title']['raw']!r} "
          f"treść zgodna={po['content']['raw'] == tresc}")


if __name__ == "__main__":
    main("--wdroz" in sys.argv)
