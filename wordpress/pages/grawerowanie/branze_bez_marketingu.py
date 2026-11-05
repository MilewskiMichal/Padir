#!/usr/bin/env python3
"""Grawerowanie laserowe (456), sekcja „Branże, w których grawerujemy”: tekst zgodny z kartą
Marketing bez linku (strona /uslugi-dla-marketingu/ jest jeszcze szkicem).

  - zdanie nad kartami obiecywało osobną stronę dla każdej z trzech branż,
  - akapit karty Marketing miał dolny margines pod link, którego nie ma.

Po publikacji strony marketingu wrócić do poprzedniej wersji (link w karcie, stare zdanie,
margines 14px). Kopia przed zmianą: backup-456-przed-branze-bez-marketingu.json.

    python3 branze_bez_marketingu.py            # próba na sucho
    python3 branze_bez_marketingu.py --wdroz
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call  # noqa: E402

STRONA = 456
KOPIA = os.path.join(HERE, "backup-456-przed-branze-bez-marketingu.json")
ZAMIANY = [
    (">Każda z trzech branż ma u nas osobną stronę z ofertą i przykładami.</p>",
     ">Dla przemysłu oraz hoteli i restauracji mamy osobne strony z ofertą i przykładami.</p>"),
    ('margin: 0px 0px 14px;">Statuetki i puchary na gale i konkursy',
     'margin: 0px;">Statuetki i puchary na gale i konkursy'),
]


def main(wdroz):
    st, p = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=id,status,modified,content")
    stara = p["content"]["raw"]
    nowa = stara
    for a, b in ZAMIANY:
        if nowa.count(a) != 1:
            sys.exit(f"oczekiwałem 1 wystąpienia: {a[:60]}")
        nowa = nowa.replace(a, b)
    print(f"strona {STRONA}: {len(stara)} -> {len(nowa)} znaków, zamian: {len(ZAMIANY)}")
    if not wdroz:
        print("próba na sucho, nic nie zapisano")
        return
    with open(KOPIA, "w", encoding="utf-8") as f:
        json.dump({"id": STRONA, "modified": p["modified"], "content_raw": stara}, f, ensure_ascii=False)
    st, _ = call("POST", f"/wp/v2/pages/{STRONA}", {"content": nowa})
    st2, po = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=content")
    print("zapis: HTTP", st, "| treść zgodna:", po["content"]["raw"] == nowa)


if __name__ == "__main__":
    main("--wdroz" in sys.argv)
