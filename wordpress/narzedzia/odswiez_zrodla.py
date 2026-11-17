#!/usr/bin/env python3
"""Odswieza lokalny spis serwisu, z ktorego korzysta sprawdz_szkic.py i kontaktowka.py.

    python3 odswiez_zrodla.py

Zapisuje do `narzedzia/zrodla/` (katalog jest w .gitignore):
  SPIS.json   strony i wpisy w kazdym statusie: id, typ, slug, link, status, tytul
  media.json  biblioteka mediow: id, url, url_medium, alt, szerokosc, wysokosc

Bez tych plikow sprawdzarka pomija kontrole linkow wewnetrznych i adresow
zdjec (zglasza wtedy ostrzezenie `zrodla`). Uruchamiaj przed kazda wieksza
zmiana tresci, bo spis starzeje sie z kazda publikacja.

Tylko odczyt: skrypt niczego w WordPressie nie zmienia.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # tu leży wp.py
from wp import call  # noqa: E402

CEL = os.path.join(HERE, "zrodla")
STATUSY = "publish,draft,pending,private,future"


def wszystko(sciezka):
    wynik, strona = [], 1
    while True:
        laczenie = "&" if "?" in sciezka else "?"
        st, dane = call("GET", f"{sciezka}{laczenie}per_page=100&page={strona}")
        if st == 400 or (st == 200 and not dane):
            break
        if st != 200:
            sys.exit(f"HTTP {st} dla {sciezka}: {str(dane)[:200]}")
        wynik.extend(dane)
        if len(dane) < 100:
            break
        strona += 1
    return wynik


def main():
    os.makedirs(CEL, exist_ok=True)
    spis = []
    for typ in ("pages", "posts"):
        for p in wszystko(f"/wp/v2/{typ}?status={STATUSY}&context=edit&_fields=id,type,slug,link,status,title"):
            spis.append({"id": p["id"], "typ": p.get("type"), "slug": p["slug"], "link": p["link"],
                         "status": p["status"], "tytul": (p.get("title") or {}).get("raw", "")})
    media = []
    for m in wszystko("/wp/v2/media?_fields=id,source_url,alt_text,media_details"):
        md = m.get("media_details") or {}
        medium = ((md.get("sizes") or {}).get("medium") or {}).get("source_url")
        media.append({"id": m["id"], "url": m["source_url"], "url_medium": medium,
                      "alt": m.get("alt_text", ""), "szerokosc": md.get("width"), "wysokosc": md.get("height")})
    with open(os.path.join(CEL, "SPIS.json"), "w", encoding="utf-8") as f:
        json.dump(spis, f, ensure_ascii=False, indent=1)
    with open(os.path.join(CEL, "media.json"), "w", encoding="utf-8") as f:
        json.dump(media, f, ensure_ascii=False, indent=1)
    print(f"SPIS.json: {len(spis)} stron i wpisów, media.json: {len(media)} plików -> {CEL}")


if __name__ == "__main__":
    main()
