#!/usr/bin/env python3
"""Podmienia lewy gorny kafel w hero /wycinanie-laserowe/ (strona 1019).

Bylo:  podswietlana litera „R” (plexi + LED)
Jest:  ruchomy model zebatek ze sklejki

Wybor po obejrzeniu wszystkich 19 realizacji z kategorii wycinanie,
w kwadratowym kadrze, bo kafel przycina zdjecie do kwadratu ze srodka:
  - zebatki: czytelne w kwadracie, neutralne tlo, od razu widac precyzje
    ciecia. Pozostale trzy kafle to zloty Guerlain, sloneczna scianka
    Bondi Sands i kolorowe drzewko, wiec spokojny kafel daje im oddech.
  - odrzucone: prototyp stojaka (tylko 225 x 300 px), drzewka z sowami
    (niemal to samo co drzewko juz stojace w hero), logo BOKO (kadr ucina
    litery), pszczola (Guerlain obok tez ma pszczole).

Zmienia sie TYLKO kafel w <header>. Litera „R” w galerii zostaje, bo to
prawdziwa realizacja. Zebatki sa juz w galerii, wiec po zmianie wystepuja
dwa razy (hero + galeria), dokladnie jak pozostale trzy zdjecia z hero.

Atrybuty ladowania (`loading="eager" fetchpriority="high" data-no-lazy="1"`)
i `data-pdw-zoom` zostaja nietkniete: podmieniamy tylko src i alt.

    python3 hero_wycinanie_kafel.py            # próba na sucho
    python3 hero_wycinanie_kafel.py --wdroz
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call

STRONA = 1019
STARY_SRC = "https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-podswietlana-litera-r.jpg"
STARY_ALT = "Podświetlana litera R LED"
NOWY_SRC = "https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-ruchomy-model-zebatek.jpg"
NOWY_ALT = "Ruchomy model zębatek wycięty ze sklejki"
KOPIA = os.path.join(HERE, "backup-1019-przed-zmiana-kafla-hero.json")


def bledy_sprawdzarki(tresc):
    """Zwraca liste bledow sprawdzarki, zeby porownac przed i po."""
    plik = os.path.join(HERE, "_tmp-1019.html")
    open(plik, "w", encoding="utf-8").write(tresc)
    w = subprocess.run([sys.executable, "-I", os.path.join(HERE, "sprawdz_szkic.py"), plik, "--json"],
                       capture_output=True, text=True)
    os.remove(plik)
    return [b["opis"] for b in json.loads(w.stdout)["bledy"]]


def main(na_sucho=True):
    st, p = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=id,link,status,content")
    stara = p["content"]["raw"]

    naglowek = re.search(r"<header\b.*?</header>", stara, re.S)
    if not naglowek:
        sys.exit("nie znalazłem <header> na stronie")
    h = naglowek.group(0)
    kafel = re.search(r'<img src="' + re.escape(STARY_SRC) + r'"[^>]*>', h)
    if not kafel:
        sys.exit("w hero nie ma kafla z literą R")
    if f'alt="{STARY_ALT}"' not in kafel.group(0):
        sys.exit(f"kafel ma inny alt niż oczekiwany: {kafel.group(0)[:160]}")
    nowy_kafel = (kafel.group(0)
                  .replace(f'src="{STARY_SRC}"', f'src="{NOWY_SRC}"')
                  .replace(f'alt="{STARY_ALT}"', f'alt="{NOWY_ALT}"'))
    nowy_h = h.replace(kafel.group(0), nowy_kafel, 1)
    nowa = stara[:naglowek.start()] + nowy_h + stara[naglowek.end():]

    print(f"strona {STRONA}: {p['link']}  [{p['status']}]")
    print(f"  kafel przed: {kafel.group(0)[:120]}…")
    print(f"  kafel po:    {nowy_kafel[:120]}…")
    print(f"  litera R na stronie: {stara.count(STARY_SRC.rsplit('/',1)[1].rsplit('.',1)[0])} -> "
          f"{nowa.count(STARY_SRC.rsplit('/',1)[1].rsplit('.',1)[0])} (zostaje w galerii)")
    print(f"  zębatki na stronie:  {stara.count('ruchomy-model-zebatek')} -> {nowa.count('ruchomy-model-zebatek')}")

    # zabezpieczenia: zmiana tylko w hero i nic poza src/alt jednego kafla
    zarzuty = []
    if stara[:naglowek.start()] != nowa[:naglowek.start()]:
        zarzuty.append("zmieniło się coś przed hero")
    if stara[naglowek.end():] != nowa[naglowek.start() + len(nowy_h):]:
        zarzuty.append("zmieniło się coś po hero")
    for atr in ('loading="eager"', 'fetchpriority="high"', 'data-no-lazy="1"', "data-pdw-zoom"):
        if atr not in nowy_kafel:
            zarzuty.append(f"kafel stracił {atr}")
    przed, po = bledy_sprawdzarki(stara), bledy_sprawdzarki(nowa)
    nowe_bledy = [b for b in po if b not in przed]
    if nowe_bledy:
        zarzuty += [f"nowy błąd sprawdzarki: {b}" for b in nowe_bledy]
    print(f"\n  sprawdzarka: błędów przed {len(przed)}, po {len(po)}, nowych {len(nowe_bledy)}")
    if przed:
        print("  (błędy istniejące wcześniej, nie z tej zmiany:)")
        for b in przed:
            print(f"     · {b[:110]}")

    if zarzuty:
        for z in zarzuty:
            print("  ✗", z)
        sys.exit("PRZERYWAM.")
    print("  zmiana dotyczy wyłącznie src i alt jednego kafla w hero")

    if na_sucho:
        print("\n(PRÓBA NA SUCHO, nic nie zapisano)")
        return
    if not os.path.exists(KOPIA):
        json.dump({"id": STRONA, "content": stara}, open(KOPIA, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\nkopia: {os.path.basename(KOPIA)}")
    st2, r = call("POST", f"/wp/v2/pages/{STRONA}", body={"content": nowa})
    print(f"zapis: HTTP {st2}, status {r.get('status') if isinstance(r, dict) else '?'}")
    if st2 != 200:
        sys.exit(json.dumps(r, ensure_ascii=False)[:300])


if __name__ == "__main__":
    main(na_sucho="--wdroz" not in sys.argv)
