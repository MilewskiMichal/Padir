# Popup „Zmieniamy halę!” (spectra-popup 2606)

- 14.10.2026: pierwsza wersja (styl i skrypt Spectry) pokazywała się jako goły tekst nad nagłówkiem, bo LiteSpeed serwuje tylko wcześniej policzony UCSS i opóźnia skrypty. Wyłączona po ok. 10 minutach.
- 14.10.2026: wersja z własnym arkuszem i skryptem (popup_hala.py) włączona. Popup był na wszystkich 49 sprawdzonych adresach.
- 16.10.2026, 22:06 UTC (17.10 00:06 w Warszawie): popup wyłączony (`popup_hala.py --wylacz`). Strony /, /kontakt/, /blog/, /wycinanie-laserowe/ bez popupu. 10 wpisów blogowych miało w cache LiteSpeeda kopię z popupem (niewidocznym, bo skrypt usuwa go po terminie); ich cache wyczyszczony zapisem bez zmian. Po tym na 47 opublikowanych adresach nie ma kodu popupu.
