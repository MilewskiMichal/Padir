#!/usr/bin/env python3
"""Skraca formularz kontaktowy w nowym stylu (.pdw .pdw-form).

Formularz Contact Form 7 (id 480) wstawia po kazdej etykiecie i kazdym polu
<br>. W akapicie z wysokoscia linii 37 px kazdy taki <br> to pusta linia,
a jest ich osiem. Do tego pole wiadomosci ma 10 wierszy, a motyw dokleja
pod nim margines. W efekcie karta formularza miala 1306 px przy 573 px
kolumny obok (na starych stronach formularz mial 790 px).

Zmieniamy TYLKO reguly .pdw-form w arkuszu strony:
  - <br> w formularzu ukryte,
  - mniejsze odstepy etykiet i zgody, pole wiadomosci 120 px (da sie
    je powiekszyc, resize: vertical),
  - e-mail i telefon obok siebie, gdy sama karta ma co najmniej 440 px
    (zapytanie @container, nie szerokosc ekranu: przy 768-1100 px ekran
    jest szeroki, a karta waska).

Szablonu formularza 480 nie ruszamy, bo korzysta z niego tez strona Kontakt.

    python3 formularz_krotszy.py --plik praca/grawerowanie/strona.html
    python3 formularz_krotszy.py --strona 1019            # próba na sucho
    python3 formularz_krotszy.py --strona 1019 --wdroz
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

ZAMIANY = [
    (".pdw .pdw-form .wpcf7-form>p{margin:0}",
     ".pdw .pdw-form{container-type:inline-size}\n"
     ".pdw .pdw-form .wpcf7-form>p{margin:0}\n"
     ".pdw .pdw-form .wpcf7-form br{display:none}"),
    ("color:#9FB3E0;margin:24px 0 9px}",
     "color:#9FB3E0;margin:20px 0 4px}"),
    ("font:300 15px Poppins,sans-serif;outline:none;border-radius:0}",
     "font:300 15px Poppins,sans-serif;outline:none;border-radius:0;margin:0}"),
    (".pdw .pdw-form .form-textarea{min-height:96px;line-height:1.5;resize:vertical}",
     ".pdw .pdw-form .form-textarea{min-height:96px;height:120px;line-height:1.5;resize:vertical}"),
    (".pdw .pdw-form .form-policy{display:block;margin:28px 0 26px}",
     ".pdw .pdw-form .form-policy{display:block;margin:22px 0 20px}"),
    (".pdw .pdw-form .wpcf7-spinner{filter:invert(1)}",
     ".pdw .pdw-form .wpcf7-spinner{filter:invert(1)}\n"
     "@container (min-width:440px){\n"
     ".pdw .pdw-form .wpcf7-form>p:first-of-type{display:grid;grid-template-columns:1fr 1fr;column-gap:24px}\n"
     ".pdw .pdw-form .wpcf7-form>p:first-of-type>*{grid-column:1/-1}\n"
     ".pdw .pdw-form .wpcf7-form>p:first-of-type>label:nth-of-type(2){grid-column:1;grid-row:3}\n"
     ".pdw .pdw-form .wpcf7-form>p:first-of-type>span:nth-of-type(2){grid-column:1;grid-row:4}\n"
     ".pdw .pdw-form .wpcf7-form>p:first-of-type>label:nth-of-type(3){grid-column:2;grid-row:3}\n"
     ".pdw .pdw-form .wpcf7-form>p:first-of-type>span:nth-of-type(3){grid-column:2;grid-row:4}\n"
     "}"),
]
ZNACZNIK = ".pdw .pdw-form .wpcf7-form br{display:none}"


def przerob(tresc):
    """Zwraca (nowa_tresc, uwagi). Zmienia wylacznie arkusz z regulami .pdw-form."""
    if ZNACZNIK in tresc:
        return tresc, ["już poprawione wcześniej, nic do zrobienia"]
    arkusze = [m for m in re.finditer(r"<style\b[^>]*>.*?</style>", tresc, re.S) if ".pdw-form" in m.group(0)]
    if len(arkusze) != 1:
        sys.exit(f"PRZERYWAM: arkuszy z .pdw-form jest {len(arkusze)}, a miał być dokładnie jeden")
    m = arkusze[0]
    if 'data-no-optimize="1"' not in m.group(0)[:120]:
        sys.exit("PRZERYWAM: arkusz bez data-no-optimize, LiteSpeed by go wyciął")
    arkusz = m.group(0)
    for stare, nowe in ZAMIANY:
        n = arkusz.count(stare)
        if n != 1:
            sys.exit(f"PRZERYWAM: reguła występuje {n} razy zamiast 1: {stare[:70]}")
        arkusz = arkusz.replace(stare, nowe)
    nowa = tresc[:m.start()] + arkusz + tresc[m.end():]
    assert nowa[:m.start()] == tresc[:m.start()]
    assert nowa[m.start() + len(arkusz):] == tresc[m.end():]
    return nowa, [f"arkusz: {len(m.group(0))} -> {len(arkusz)} znaków, zmienionych reguł: {len(ZAMIANY)}"]


def sprawdzarka(tresc, szkic):
    plik = os.path.join(HERE, "_tmp-formularz.html")
    open(plik, "w", encoding="utf-8").write(tresc)
    arg = [sys.executable, "-I", os.path.join(HERE, "sprawdz_szkic.py"), plik, "--json"] + (["--szkic"] if szkic else [])
    w = subprocess.run(arg, capture_output=True, text=True)
    os.remove(plik)
    return [b["opis"] for b in json.loads(w.stdout)["bledy"]]


def main():
    if "--plik" in sys.argv:
        sciezka = sys.argv[sys.argv.index("--plik") + 1]
        stara = open(sciezka, encoding="utf-8").read()
        nowa, uwagi = przerob(stara)
        print(sciezka, *uwagi)
        nowe_bledy = [b for b in sprawdzarka(nowa, True) if b not in sprawdzarka(stara, True)]
        if nowe_bledy:
            sys.exit("PRZERYWAM, nowe błędy sprawdzarki: " + "; ".join(nowe_bledy))
        if nowa != stara:
            open(sciezka, "w", encoding="utf-8").write(nowa)
            print("  zapisano")
        return

    if "--strona" not in sys.argv:
        print(__doc__)
        sys.exit(2)
    from wp import call
    ident = int(sys.argv[sys.argv.index("--strona") + 1])
    st, p = call("GET", f"/wp/v2/pages/{ident}?context=edit&_fields=id,status,link,content")
    if st != 200:
        sys.exit(f"nie pobrano strony {ident}: HTTP {st}")
    stara = p["content"]["raw"]
    nowa, uwagi = przerob(stara)
    print(f"strona {ident} [{p['status']}] {p['link']}")
    for u in uwagi:
        print("  " + u)
    if nowa == stara:
        return
    przed, po = sprawdzarka(stara, False), sprawdzarka(nowa, False)
    nowe_bledy = [b for b in po if b not in przed]
    print(f"  sprawdzarka: błędów przed {len(przed)}, po {len(po)}, nowych {len(nowe_bledy)}")
    if nowe_bledy:
        sys.exit("PRZERYWAM: " + "; ".join(nowe_bledy))
    if "--wdroz" not in sys.argv:
        print("\n(PRÓBA NA SUCHO, nic nie zapisano)")
        return
    kopia = os.path.join(HERE, f"backup-{ident}-przed-skroceniem-formularza.json")
    if not os.path.exists(kopia):
        json.dump({"id": ident, "content": stara}, open(kopia, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"  kopia: {os.path.basename(kopia)}")
    st2, r = call("POST", f"/wp/v2/pages/{ident}", body={"content": nowa})
    print(f"  zapis: HTTP {st2}, status {r.get('status') if isinstance(r, dict) else '?'}")
    if st2 != 200:
        sys.exit(json.dumps(r, ensure_ascii=False)[:300])
    if r.get("status") != p["status"]:
        sys.exit(f"ALARM: status zmienił się z {p['status']} na {r.get('status')}")


if __name__ == "__main__":
    main()
