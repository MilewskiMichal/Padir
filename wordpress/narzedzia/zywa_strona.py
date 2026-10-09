#!/usr/bin/env python3
"""Lokalna kopia OPUBLIKOWANEJ strony (arkusze, fonty, zdjecia na dysku),
zeby przegladarka w tym srodowisku pokazala ja jak gosciowi.

    python3 zywa_strona.py URL PREFIKS
"""
import os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from podglad_szkicu import pobierz, lokalizuj

def main():
    url, prefiks = sys.argv[1], sys.argv[2]
    h = pobierz(url + ("&" if "?" in url else "?") + "odswiez=" + str(int(time.time())))
    if not h:
        sys.exit("nie pobrano " + url)
    h, ile = lokalizuj(h)
    open(prefiks + ".html", "w", encoding="utf-8").write(h)
    print(os.path.abspath(prefiks + ".html"), ile)

if __name__ == "__main__":
    main()
