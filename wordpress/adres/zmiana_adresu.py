#!/usr/bin/env python3
"""Nowy adres po przeprowadzce (19.10.2026): Matuszewska 14, Hala D, wjazd T1.

Podmienia wszystkie znane zapisy starego wejscia (budynek C2 / brama lub
wejscie T9 oraz budynek B8 / wejscie 1A) w stronach, szkicach i szablonach.
Kazda zamiana ma oczekiwana liczbe wystapien, a poza nimi tresc musi
zostac bajt w bajt taka sama.

    python3 zmiana_adresu.py            # proba na sucho
    python3 zmiana_adresu.py --wdroz
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from wp import call

NOWY = "Hala D, wjazd T1"
ZAMIANY = [
    ("(budynek C2 brama T9)", f"({NOWY})"),
    ("(budynek C2, brama T9)", f"({NOWY})"),            # dane strukturalne na Kontakcie
    ("Budynek C2, Brama T9", NOWY),
    ("Budynek C2, wejście T9", NOWY),
    ("Budynek B8, wejście 1A lub brama po drugiej stronie hali", NOWY),
    ("(Budynek B8)", f"({NOWY})"),
]
CELE = [  # (typ REST, id, {stary zapis: ile razy})
    ("pages", 20, {"(budynek C2 brama T9)": 1, "(budynek C2, brama T9)": 1, "Budynek C2, Brama T9": 1}),
    ("pages", 1019, {"Budynek C2, wejście T9": 1}),
    ("pages", 1011, {"Budynek C2, wejście T9": 1}),
    ("pages", 456, {"Budynek C2, wejście T9": 1}),
    ("pages", 1812, {"Budynek B8, wejście 1A lub brama po drugiej stronie hali": 1}),
    ("pages", 2228, {"Budynek B8, wejście 1A lub brama po drugiej stronie hali": 1}),
    ("pages", 2584, {"Budynek C2, wejście T9": 1}),
    ("pages", 2585, {"Budynek C2, wejście T9": 1}),
    ("pages", 2530, {"Budynek C2, wejście T9": 1}),
    ("templates", "twentytwentyfour//home", {"(budynek C2 brama T9)": 2, "Budynek C2, wejście T9": 1}),
    ("templates", "twentytwentyfour//wp-custom-template-about-us", {"(Budynek B8)": 1}),
]
STARE = re.compile(r"(?i)budyn\w*\s*(?:C2|B8)|brama\s*T9|wej[sś]cie\s*(?:T9|1A)")
MAPA = dict(ZAMIANY)


def przerob(tresc, oczekiwane):
    nowa = tresc
    for stary, ile in oczekiwane.items():
        n = nowa.count(stary)
        if n != ile:
            sys.exit(f"PRZERYWAM: „{stary}” występuje {n} razy zamiast {ile}")
        nowa = nowa.replace(stary, MAPA[stary])
    reszta = [m.group(0) for m in STARE.finditer(nowa)]
    if reszta:
        sys.exit(f"PRZERYWAM: po zamianie zostało: {reszta}")
    # kontrola bilansu: roznica dlugosci = suma roznic podmienionych fragmentow
    oczek_roznica = sum(ile * (len(MAPA[s]) - len(s)) for s, ile in oczekiwane.items())
    if len(nowa) - len(tresc) != oczek_roznica:
        sys.exit("PRZERYWAM: zmienilo sie cos poza adresem")
    if nowa.count(NOWY) != tresc.count(NOWY) + sum(oczekiwane.values()):
        sys.exit("PRZERYWAM: liczba nowych adresow sie nie zgadza")
    return nowa


def main():
    wdroz = "--wdroz" in sys.argv
    for typ, ident, oczek in CELE:
        st, p = call("GET", f"/wp/v2/{typ}/{ident}?context=edit")
        if st != 200:
            sys.exit(f"nie pobrano {typ} {ident}: {st}")
        stara = p["content"]["raw"]
        nowa = przerob(stara, oczek)
        print(f"{typ} {ident} [{p.get('status')}]: {sum(oczek.values())} zamian")
        if wdroz:
            st2, r = call("POST", f"/wp/v2/{typ}/{ident}", body={"content": nowa})
            if st2 != 200:
                sys.exit(f"  zapis nieudany: {st2} {json.dumps(r, ensure_ascii=False)[:300]}")
            if r.get("status") != p.get("status"):
                sys.exit(f"  ALARM: status zmienił się z {p.get('status')} na {r.get('status')}")
            print(f"  zapisano, status {r.get('status')}")
    if not wdroz:
        print("\n(PRÓBA NA SUCHO)")


if __name__ == "__main__":
    main()
