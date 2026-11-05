#!/usr/bin/env python3
"""Frezowanie CNC (strona 1011): zdjęcie na karcie „Usługi dla HoReCa”.

Było:  napis przestrzenny „Tea” (lustrzana plexi na sklejce). Zleceniodawca:
       napis był cięty laserem, nie frezowany, więc nie może ilustrować frezowania.
Jest:  frez CNC prowadzi łukowy rowek w drewnianej płycie klejonej (media 2256,
       praca Padiru). Pasuje do opisu karty („deski do serwisu, elementy wystroju”),
       nie występuje jeszcze na tej stronie i różni się od zdjęcia na karcie przemysłu.

Zmienia się tylko src i alt tego jednego <img>. Reszta strony bez zmian.

    python3 podmiana_tea_horeca.py            # próba na sucho
    python3 podmiana_tea_horeca.py --wdroz
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call  # noqa: E402

STRONA = 1011
STARY = ('<img src="https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-napis-przestrzenny-tea.jpg" '
         'alt="Napis przestrzenny z plexi lustrzanej"')
NOWY = ('<img src="https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/cnc-drewno.jpg" '
        'alt="Frez CNC prowadzi łukowy rowek w drewnianej płycie klejonej"')
KOPIA = os.path.join(HERE, "backup-1011-przed-podmiana-tea.json")


def main(wdroz):
    st, p = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=id,link,status,modified,content")
    stara = p["content"]["raw"]
    if stara.count(STARY) != 1:
        sys.exit(f"oczekiwałem dokładnie 1 wystąpienia starego <img>, jest {stara.count(STARY)}")
    nowa = stara.replace(STARY, NOWY)
    print(f"strona {STRONA} [{p['status']}] {p['link']}: zmiana {len(stara)} -> {len(nowa)} znaków")
    if not wdroz:
        print("próba na sucho, nic nie zapisano")
        return
    with open(KOPIA, "w", encoding="utf-8") as f:
        json.dump({"id": STRONA, "modified": p["modified"], "content_raw": stara}, f, ensure_ascii=False)
    st, wynik = call("POST", f"/wp/v2/pages/{STRONA}", {"content": nowa})
    print("zapis: HTTP", st)
    st, po = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=content")
    raw = po["content"]["raw"]
    print("po zapisie: Tea", "napis-przestrzenny-tea" in raw, "| cnc-drewno", "cnc-drewno.jpg" in raw)


if __name__ == "__main__":
    main("--wdroz" in sys.argv)
