#!/usr/bin/env python3
"""Artykuł nr 6 (WhitePress): dane artykułu. Budowę robi wspolne/budowa.py.

    python3 zbuduj.py

Wynik w katalogu nadrzędnym: podglad.html, DO-WKLEJENIA.md, artykul.docx,
INSTRUKCJA-CLAUDE-W-CHROME.md i paczka whitepress-artykul-06.zip (poza gitem).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "wspolne"))
from budowa import zbuduj  # noqa: E402

NR = 6
PACZKA = "whitepress-artykul-06"
TEMAT = "poradnika o wycinaniu laserem dla projektantów i majsterkowiczów"
TEMATYKA = "design i wnętrza, majsterkowanie i DIY, hobby, technologia, reklama i marketing, poradniki"

TYTUL = "Wycinanie laserem z plexi i sklejki: jak przygotować plik, żeby nie przepłacić"
LEAD = ("Za wycinanie laserem płaci się głównie za czas pracy maszyny, a ten w dużej mierze zależy "
        "od pliku. Te same litery z plexi mogą kosztować więcej tylko dlatego, że w projekcie zostały "
        "zdublowane linie albo niepotrzebne detale. Pokazujemy, co podnosi koszt, jak przygotować "
        "projekt i czego spodziewać się po plexi, sklejce i MDF.")

ZDJECIE_GLOWNE = {
    "plik": "zdjecia/zdjecie-glowne-napis-tea-plexi-lustrzana-padir.jpg",
    "alt": "Przestrzenny napis Tea wycięty laserem z lustrzanej plexi na sklejce",
    "podpis": "Napis z lustrzanej plexi na sklejce, wycięty laserem. Fot. Padir",
}
OBRAZY = {  # w kolejności, w jakiej stoją w tekście
    "ig1": {"plik": "infografiki/ig1-co-podnosi-cene-ciecia-laserem.png",
            "alt": "Infografika: sześć rzeczy, które podnoszą cenę cięcia laserem",
            "podpis": "Na większość tych kosztów masz wpływ już w pliku. Grafika: Padir"},
    "drzewko": {"plik": "zdjecia/azurowe-drzewko-sklejka-padir.jpg",
                "alt": "Ażurowe drzewko z sowami wycięte laserem ze sklejki",
                "podpis": "Ażur ze sklejki: im więcej drobnych wycięć, tym dłużej pracuje laser. Fot. Padir"},
    "ig2": {"plik": "infografiki/ig2-plik-do-ciecia-lista-kontrolna.png",
            "alt": "Infografika: lista kontrolna pliku do cięcia laserem, z przykładem mostków w literze O",
            "podpis": "Co sprawdzić w pliku przed wysłaniem do cięcia. Grafika: Padir"},
    "ig3": {"plik": "infografiki/ig3-plexi-sklejka-mdf-krawedz.png",
            "alt": "Infografika: jak po cięciu laserem wygląda krawędź plexi, sklejki, MDF i laminatu",
            "podpis": "Krawędź po cięciu zależy od materiału. Grafika: Padir"},
    "zebatki": {"plik": "zdjecia/zebatki-sklejka-wpusty-padir.jpg",
                "alt": "Ruchomy model zębatek ze sklejki złożony na wpusty",
                "podpis": "Model zębatek ze sklejki, składany na wpusty. Fot. Padir"},
}
LINKI = [  # w kolejności ważności: przy mniejszej liczbie linków zostają pierwsze
    ("wycinanie laserem", "https://grawerowanie-laserowe.pl/wycinanie-laserowe/", "fraza"),
    ("pracownia Padir", "https://grawerowanie-laserowe.pl/", "marka, strona główna"),
    ("plexi, sklejka i laminat",
     "https://grawerowanie-laserowe.pl/blog/wycinanie-laserowe-precyzyjne-ciecie-plexi-sklejki-i-laminatu-na-zamowienie/",
     "opisowy"),
]

if __name__ == "__main__":
    zbuduj(sys.modules[__name__])
