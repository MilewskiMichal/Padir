#!/usr/bin/env python3
"""Dodaje jedną kartę na początek galerii realizacji na stronie 1397.

Karta: dzbanek do mleka ze stali nierdzewnej i szklanka do latte z logo LOT.
Zgoda zleceniodawcy na pokazywanie zdjęć: 25.11.2026. Zdjęcie: media 2641
(to samo, które otwiera szkic wpisu 2644).

Galeria jest wpisana w treść strony na sztywno, więc dodanie karty to
wstawienie bloku `<article class="pdr-card">` przed pierwszą kartą. Przy okazji:
  - opóźnienia animacji liczone od nowa, jak w obecnej galerii:
    co 35 ms, najwyżej 385 ms,
  - licznik `.pdr-count` w tej samej odmianie co funkcja `plural()` galerii,
  - filtry nie mają wpisanych liczb, liczą przez `data-cats`, więc ich nie ruszamy.

    python3 realizacja_dodaj.py            # próba na sucho
    python3 realizacja_dodaj.py --wdroz
    python3 realizacja_dodaj.py --tylko-filtry [--wdroz]   # karta już jest, popraw liczby przy filtrach
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORDPRESS = os.path.dirname(os.path.dirname(HERE))  # tu leży wp.py
sys.path.insert(0, WORDPRESS)
sys.path.insert(0, HERE)
from wp import call  # noqa: E402
from realizacja_usun import karty, odmien  # noqa: E402

STRONA = 1397
TYTUL = "Dzbanek i szklanka „LOT”"
MATERIAL = "Stal nierdzewna + szkło"
PELNE = "https://grawerowanie-laserowe.pl/wp-content/uploads/2026/11/padir-grawer-dzbanek-do-mleka-i-szklanka-latte.jpg"
MINIATURA = "https://grawerowanie-laserowe.pl/wp-content/uploads/2026/11/padir-grawer-dzbanek-do-mleka-i-szklanka-latte-768x576.jpg"
KARTA = (f'<article class="pdr-card" data-cats="eng" style="animation-delay:0ms">'
         f'<button type="button" class="pdr-shotbtn" data-full="{PELNE}" data-title="{TYTUL}" '
         f'data-mat="{MATERIAL}" aria-label="Powiększ zdjęcie: {TYTUL}">'
         f'<img src="{MINIATURA}" alt="{TYTUL} - {MATERIAL}" loading="lazy" decoding="async">'
         f'<span class="pdr-pill" style="background:#12388C">Grawerowanie</span></button>'
         f'<div class="pdr-body"><h3 class="pdr-h3">{TYTUL}</h3><div class="pdr-mat">{MATERIAL}</div></div></article>')
KOPIA = os.path.join(HERE, "backup-1397-przed-dodaniem-karty-lot.json")


def dodaj(c):
    wszystkie = karty(c)
    if TYTUL in c:
        if "--tylko-filtry" in sys.argv:
            return przelicz_filtry(c), len(wszystkie), len(wszystkie)
        raise SystemExit(f"karta „{TYTUL}” już jest w galerii (liczniki filtrów: --tylko-filtry)")
    a = wszystkie[0][0]
    nowa = c[:a] + KARTA + "\n" + c[a:]
    # opoznienia od nowa: co 35 ms, najwyzej 385 ms
    licz = iter(range(10 ** 6))
    nowa = re.sub(r'(<article class="pdr-card"[^>]*style="animation-delay:)\d+ms',
                  lambda m: f"{m.group(1)}{min(next(licz) * 35, 385)}ms", nowa)
    bylo, ile = len(wszystkie), len(wszystkie) + 1
    if nowa.count(odmien(bylo)) != 1:
        raise SystemExit(f"licznik „{odmien(bylo)}” występuje {nowa.count(odmien(bylo))} razy")
    return przelicz_filtry(nowa.replace(odmien(bylo), odmien(ile))), bylo, ile


def przelicz_filtry(c):
    """Liczby przy filtrach (`.pdr-n`) sa wpisane na sztywno i skrypt galerii ich nie
    przelicza. Przeliczamy je z `data-cats` kart; po usunieciu karty w pazdzierniku
    zostaly nieaktualne („Wszystkie 45” przy 44 kartach, „Wycinanie 20” przy 19)."""
    cats = [m.group(1).split() for m in re.finditer(r'<article class="pdr-card" data-cats="([^"]+)"', c)]
    liczby = {"all": len(cats)}
    for k in ("eng", "cut", "cnc"):
        liczby[k] = sum(k in x for x in cats)
    for k, n in liczby.items():
        wz = re.compile(r'(<button type="button" class="pdr-tab" data-cat="' + k + r'"[^>]*>.*?<span class="pdr-n">)\d+(</span>)', re.S)
        c, ile = wz.subn(lambda m: f"{m.group(1)}{n}{m.group(2)}", c)
        if ile != 1:
            raise SystemExit(f"nie znalazłem licznika filtra {k}")
    return c


def sprawdz(t, bylo, ma_byc):
    zarzuty = []
    if t.count(f'<h3 class="pdr-h3">{TYTUL}</h3>') != 1:
        zarzuty.append("nowa karta nie występuje dokładnie raz")
    if len(re.findall(r'<article class="pdr-card"', t)) != ma_byc:
        zarzuty.append(f"kart po zmianie: {len(re.findall(r'<article class=.pdr-card.', t))}, spodziewam się {ma_byc}")
    for otw, zam in (("<article", "</article>"), ("<div", "</div>"), ("<button", "</button>")):
        if t.count(otw) != t.count(zam):
            zarzuty.append(f"{otw}: {t.count(otw)} otwarć, {t.count(zam)} zamknięć")
    if odmien(ma_byc) not in t or (bylo != ma_byc and odmien(bylo) in t):
        zarzuty.append(f"licznik nie pokazuje „{odmien(ma_byc)}”")
    if "&&" in t:
        zarzuty.append("podwójny ampersand, WordPress zepsuje skrypt galerii")
    for znak in ("—", "–", "−"):
        if znak in t:
            zarzuty.append(f"pauza {znak!r} zamiast dywizu")
    for kat in ("eng", "cut", "cnc"):
        if f'data-cat="{kat}"' not in t:
            zarzuty.append(f"zniknął filtr {kat}")
    return zarzuty


def main(na_sucho=True):
    st, p = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=id,link,content")
    stara = p["content"]["raw"]
    nowa, bylo, ma_byc = dodaj(stara)
    przed = re.findall(r'data-cat="(\w+)"[^>]*>.*?<span class="pdr-n">(\d+)</span>', stara, re.S)
    po = re.findall(r'data-cat="(\w+)"[^>]*>.*?<span class="pdr-n">(\d+)</span>', nowa, re.S)
    print(f"  liczby przy filtrach: {dict(przed)} -> {dict(po)}")
    if nowa == stara:
        print("  nic do zmiany")
        return
    print(f"strona {STRONA}: {p['link']}")
    print(f"  treść: {len(stara)} -> {len(nowa)} znaków, karty: {bylo} -> {ma_byc}")
    print(f"  licznik: „{odmien(bylo)}” -> „{odmien(ma_byc)}”")
    print(f"  nowa karta: {TYTUL} | {MATERIAL} | Grawerowanie | pierwsza w galerii")
    zarzuty = sprawdz(nowa, bylo, ma_byc)
    if zarzuty:
        for z in zarzuty:
            print("  ✗", z)
        sys.exit("PRZERYWAM.")
    print("  kontrola: znaczniki domknięte, licznik zgodny, filtry na miejscu")
    if na_sucho:
        print("\n(PRÓBA NA SUCHO, nic nie zapisano)")
        return
    kopia = KOPIA if "--tylko-filtry" not in sys.argv else KOPIA.replace(".json", "-filtry.json")
    json.dump({"id": STRONA, "content": stara}, open(kopia, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  kopia: {os.path.basename(kopia)}")
    st2, r = call("POST", f"/wp/v2/pages/{STRONA}", body={"content": nowa})
    print(f"\nzapis: HTTP {st2}")
    if st2 != 200:
        print(json.dumps(r, ensure_ascii=False)[:400])
        sys.exit(1)
    st3, po = call("GET", f"/wp/v2/pages/{STRONA}?context=edit&_fields=content,status")
    print(f"  status: {po['status']}, treść zgodna z wysłaną: {po['content']['raw'] == nowa}")


if __name__ == "__main__":
    main(na_sucho="--wdroz" not in sys.argv)
