#!/usr/bin/env python3
"""Artykuł nr 1 (WhitePress): dane artykułu. Budowę robi wspolne/budowa.py.

    python3 zbuduj.py

Wynik w katalogu nadrzędnym: podglad.html, DO-WKLEJENIA.md, artykul.docx,
INSTRUKCJA-CLAUDE-W-CHROME.md i paczka whitepress-artykul-01.zip (poza gitem).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "wspolne"))
from budowa import zbuduj  # noqa: E402

NR = 1
PACZKA = "whitepress-artykul-01"
TEMAT = "poradnika o grawerowaniu"
TEMATYKA = "dom i ogród, majsterkowanie i DIY, hobby, technologia, poradniki, lifestyle"

TYTUL = "Grawerowanie laserowe krok po kroku: od pomysłu do gotowego przedmiotu"
LEAD = ("Logo na kieliszku, imię na nożu, numer seryjny na tabliczce. Wszystko to powstaje "
        "w podobny sposób, a o tym, czy znak wyjdzie wyraźny, decyduje głównie to, co dzieje się "
        "przed uruchomieniem lasera. Przechodzimy przez całą drogę zlecenia, od wyboru materiału "
        "po odbiór, i pokazujemy błędy, które najczęściej ją wydłużają.")

ZDJECIE_GLOWNE = {
    "plik": "zdjecia/zdjecie-glowne-kieliszek-grawer-padir.jpg",
    "alt": "Kieliszek do wina z grawerowanym laserowo logo Padir",
    "podpis": "Grawer na szkle daje matową, mleczną powierzchnię. Fot. Padir",
}
OBRAZY = {  # w kolejności, w jakiej stoją w tekście
    "ig1": {"plik": "infografiki/ig1-grawerowanie-laserowe-6-krokow.png",
            "alt": "Infografika: grawerowanie laserowe w 6 krokach, od materiału do odbioru",
            "podpis": "Cała droga zlecenia w sześciu krokach. Grafika: Padir"},
    "kubek": {"plik": "zdjecia/kubek-termiczny-grawer-padir.jpg",
              "alt": "Czarny kubek termiczny z grawerowanym logo Padir",
              "podpis": "Czarny kubek termiczny z wygrawerowanym logo. Fot. Padir"},
    "ig2": {"plik": "infografiki/ig2-plik-do-graweru-lista-kontrolna.png",
            "alt": "Infografika: lista kontrolna pliku do grawerowania laserowego",
            "podpis": "Co sprawdzić w pliku przed wysłaniem do pracowni. Grafika: Padir"},
    "ig3": {"plik": "infografiki/ig3-laser-co2-czy-fiber.png",
            "alt": "Infografika: który laser do jakiego materiału, CO2 czy fiber",
            "podpis": "Laser CO2 pracuje na drewnie, szkle i tworzywach, fiber na gołym metalu. Grafika: Padir"},
}
LINKI = [  # w kolejności ważności: przy mniejszej liczbie linków zostają pierwsze
    ("grawerowanie laserowe", "https://grawerowanie-laserowe.pl/grawerowanie-laserowe/", "fraza"),
    ("Padir", "https://grawerowanie-laserowe.pl/", "marka, strona główna"),
    ("jak przygotować plik do graweru",
     "https://grawerowanie-laserowe.pl/blog/jak-przygotowac-projekt-do-grawerowania-laserowego/", "opisowy"),
]

if __name__ == "__main__":
    zbuduj(sys.modules[__name__])
