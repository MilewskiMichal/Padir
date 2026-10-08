#!/usr/bin/env python3
"""Usuwa jedną kartę z galerii realizacji na stronie 1397.

Karta „Ażurowy panel dekoracyjny”: kadr z lokalu BOKO, w ktorym polowe
zajmuje lisc rosliny, a sam panel ginie za logo na scianie. Na tle
pozostalych czterdziestu czterech zdjec odstawala.

Galeria jest wpisana w tresc strony na sztywno, wiec usuniecie to wyciecie
jednego bloku `<article class="pdr-card">`. Do tego trzeba poprawic licznik
`45 realizacji`, bo jest renderowany statycznie w `.pdr-count`, a skrypt
przelicza go dopiero przy pierwszym klknieciu w filtr.

Czego NIE trzeba ruszac:
  - opoznien animacji. Trzydziesci cztery karty maja `animation-delay:385ms`,
    bo stagger jest ograniczony z gory. Nic sie nie przesuwa.
  - przyciskow filtrow. Nie maja wpisanych liczb, licza przez `data-cats`.
  - funkcji `plural()` w skrypcie, gdzie `1 realizacja` to forma gramatyczna,
    a nie licznik.

Plik `padir-realizacja-azurowy-panel-dekoracyjny.jpg` zostaje w bibliotece
mediow. Usuniecie go z dysku to osobna decyzja i nieodwracalna, a karta
znika niezaleznie od tego.

    python3 realizacja_usun.py            # próba na sucho
    python3 realizacja_usun.py --wdroz
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call

STRONA = 1397
TYTUL = "Ażurowy panel dekoracyjny"
PLIK_ZDJECIA = "azurowy-panel-dekoracyjny"
KOPIA = os.path.join(HERE, "backup-1397-przed-usunieciem-karty.json")


def karty(c):
    """Wszystkie bloki `<article class="pdr-card">` jako (poczatek, koniec)."""
    out = []
    for m in re.finditer(r'<article class="pdr-card"', c):
        koniec = c.find("</article>", m.start())
        if koniec < 0:
            raise SystemExit("karta bez zamknięcia </article>")
        out.append((m.start(), koniec + len("</article>")))
    return out


def odmien(n):
    """Ta sama odmiana, ktora ma funkcja `plural()` w skrypcie galerii.

    Powtarzamy ja, bo licznik jest renderowany statycznie w tresci strony,
    a skrypt przelicza go dopiero przy pierwszym klknieciu w filtr. Gdyby
    obie formy sie roznily, licznik zmienialby sie sam po kliknieciu
    i z powrotem. Dla 44 poprawna forma to „44 realizacje”, nie
    „44 realizacji”: koncowka 4 daje liczbe mnoga blizsza, a wyjatek
    dla 12-14 tu nie zachodzi.
    """
    if n == 1:
        return "1 realizacja"
    d, s = n % 10, n % 100
    mnoga_blizsza = 2 <= d <= 4
    if 12 <= s <= 14:
        mnoga_blizsza = False
    return f"{n} realizacje" if mnoga_blizsza else f"{n} realizacji"


def usun(c):
    wszystkie = karty(c)
    pasujace = [(a, b) for a, b in wszystkie if TYTUL in c[a:b]]
    if len(pasujace) != 1:
        raise SystemExit(f"spodziewam się dokładnie jednej karty z tytułem "
                         f"„{TYTUL}”, znalazłem {len(pasujace)}")
    a, b = pasujace[0]
    wycieta = c[a:b]
    # zjadamy tez biala linie po karcie, zeby nie zostawala pusta przerwa
    koniec = b
    while koniec < len(c) and c[koniec] in "\r\n":
        koniec += 1
    nowa = c[:a] + c[koniec:]

    ile = len(wszystkie) - 1
    stary_licznik = odmien(len(wszystkie))
    nowy_licznik = odmien(ile)
    if nowa.count(stary_licznik) != 1:
        raise SystemExit(f"licznik „{stary_licznik}” występuje "
                         f"{nowa.count(stary_licznik)} razy, spodziewam się jednego")
    nowa = nowa.replace(stary_licznik, nowy_licznik)
    return nowa, wycieta, len(wszystkie), ile


def sprawdz(t, bylo, ma_byc):
    zarzuty = []
    if TYTUL in t:
        zarzuty.append(f"tytuł „{TYTUL}” nadal jest w treści")
    if PLIK_ZDJECIA in t:
        zarzuty.append(f"odwołanie do pliku {PLIK_ZDJECIA} nadal jest w treści")
    ile = len(re.findall(r'<article class="pdr-card"', t))
    if ile != ma_byc:
        zarzuty.append(f"kart po zmianie: {ile}, spodziewam się {ma_byc}")
    if t.count("<article") != t.count("</article>"):
        zarzuty.append(f"article: {t.count('<article')} otwarć, "
                       f"{t.count('</article>')} zamknięć")
    if t.count("<div") != t.count("</div>"):
        zarzuty.append(f"divy: {t.count('<div')} otwarć, {t.count('</div>')} zamknięć")
    if odmien(ma_byc) not in t:
        zarzuty.append(f"licznik nie pokazuje „{odmien(ma_byc)}”")
    if odmien(bylo) in t:
        zarzuty.append(f"został stary licznik „{odmien(bylo)}”")
    if "&&" in t:
        zarzuty.append("podwójny ampersand, WordPress zamieni go na encję "
                       "i zepsuje skrypt galerii")
    for znak in ("—", "–", "−"):
        if znak in t:
            zarzuty.append(f"pauza {znak!r} zamiast dywizu")
    # filtry musza dalej miec komplet kategorii
    for kat in ("eng", "cut", "cnc"):
        if f'data-cat="{kat}"' not in t:
            zarzuty.append(f"zniknął filtr {kat}")
        if f'data-cats="{kat}"' not in t and f'{kat}"' not in t:
            zarzuty.append(f"żadna karta nie ma już kategorii {kat}")
    return zarzuty


def main(na_sucho=True):
    st, p = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=id,link,content")
    stara = p["content"]["raw"]
    nowa, wycieta, bylo, ma_byc = usun(stara)

    print(f"strona {STRONA}: {p['link']}")
    print(f"  treść: {len(stara)} -> {len(nowa)} znaków")
    print(f"  karty: {bylo} -> {ma_byc}")
    print(f"  licznik: „{odmien(bylo)}” -> „{odmien(ma_byc)}”")
    print(f"\n  wycinany blok ({len(wycieta)} znaków):")
    print(f"     tytuł:     {re.search(r'data-title=.([^.]*?). data-mat', wycieta).group(1) if re.search(chr(100)+'ata-title=', wycieta) else '?'}")
    for etykieta, wzor in (("materiał", r'data-mat="([^"]+)"'),
                           ("kategoria", r'data-cats="([^"]+)"'),
                           ("plakietka", r'pdr-pill"[^>]*>([^<]+)<'),
                           ("zdjęcie", r'data-full="[^"]*/([^/"]+)"')):
        m = re.search(wzor, wycieta)
        print(f"     {etykieta:<10} {m.group(1) if m else '?'}")

    zarzuty = sprawdz(nowa, bylo, ma_byc)
    print("\nkontrola przed zapisem:")
    if zarzuty:
        for z in zarzuty:
            print("  ✗", z)
        print("\nPRZERYWAM.")
        return
    print("  po karcie nie ma śladu: ani tytułu, ani nazwy pliku")
    print("  znaczniki domknięte, filtry i wszystkie trzy kategorie na miejscu")
    print("  licznik zgadza się z liczbą kart")

    if na_sucho:
        open(os.path.join(HERE, "realizacje-nowa-tresc.html"), "w",
             encoding="utf-8").write(nowa)
        print("\npodgląd: realizacje-nowa-tresc.html\n(PRÓBA NA SUCHO, nic nie zapisano)")
        return

    if not os.path.exists(KOPIA):
        json.dump({"id": STRONA, "content": stara}, open(KOPIA, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\nkopia: {os.path.basename(KOPIA)}")

    st2, r = call("POST", f"/wp/v2/pages/{STRONA}", body={"content": nowa})
    print(f"\nzapis: HTTP {st2}")
    if st2 != 200:
        print(json.dumps(r, ensure_ascii=False)[:400])
        return
    c = r["content"]["raw"]
    print(f"  kart: {len(re.findall(chr(60) + 'article class=.pdr-card.', c))}")
    print(f"  ślad po usuniętej karcie: {'JEST, ŹLE' if TYTUL in c else 'brak'}")
    print(f"  adres: {p['link']}")


if __name__ == "__main__":
    main(na_sucho="--wdroz" not in sys.argv)
