#!/usr/bin/env python3
"""Buduje pliki artykułu nr 1 z jednego źródła (tresc.html + dane poniżej).

    python3 zbuduj.py

Wynik w katalogu nadrzędnym:
  podglad.html                    artykuł ze zdjęciami, do obejrzenia w przeglądarce
  DO-WKLEJENIA.md                 tytuł, lead, treść HTML i tekst, linki, zdjęcia, uwagi dla wydawcy
  artykul.docx                    ta sama treść w Wordzie (A4), ze zdjęciami, altami i aktywnymi linkami
  INSTRUKCJA-CLAUDE-W-CHROME.md   instrukcja.md + wszystkie materiały do wklejenia
  whitepress-artykul-01.zip       paczka dla właściciela (poza gitem, zob. .gitignore)

Na końcu kontrola: zakazane myślniki, liczba linków i znaków, komplet plików.
"""
import html
import os
import re
import sys
import zipfile
from html.parser import HTMLParser

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

TU = os.path.dirname(os.path.abspath(__file__))
KAT = os.path.dirname(TU)
PACZKA = "whitepress-artykul-01"

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


class Czytnik(HTMLParser):
    """Zamienia tresc.html na listę bloków: h2, p, ul, obraz."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.bloki, self.biezacy, self.link, self.lista = [], None, None, None

    def handle_comment(self, data):
        m = re.match(r"\s*OBRAZ:(\w+)\s*$", data)
        if m:
            self.bloki.append(("obraz", m.group(1)))

    def handle_starttag(self, tag, attrs):
        if tag in ("h2", "p"):
            self.biezacy = (tag, [])
        elif tag == "ul":
            self.lista = []
        elif tag == "li":
            self.biezacy = ("li", [])
        elif tag == "a":
            self.link = dict(attrs)["href"]

    def handle_endtag(self, tag):
        if tag in ("h2", "p") and self.biezacy:
            self.bloki.append(self.biezacy)
            self.biezacy = None
        elif tag == "li":
            self.lista.append(self.biezacy[1])
            self.biezacy = None
        elif tag == "ul":
            self.bloki.append(("ul", self.lista))
            self.lista = None
        elif tag == "a":
            self.link = None

    def handle_data(self, data):
        if self.biezacy is not None:
            tekst = re.sub(r"\s+", " ", data)
            if tekst:
                self.biezacy[1].append((tekst, self.link))


def wczytaj():
    c = Czytnik()
    with open(os.path.join(TU, "tresc.html"), encoding="utf-8") as f:
        c.feed(f.read())
    return c.bloki


def fragmenty_html(fr):
    return "".join(f'<a href="{html.escape(h)}">{html.escape(t)}</a>' if h else html.escape(t)
                   for t, h in fr).strip()


def fragmenty_tekst(fr):
    return "".join(t for t, _ in fr).strip()


def naglowki(bloki):
    return [fragmenty_tekst(d) for t, d in bloki if t == "h2"]


def tresc_html(bloki, z_obrazami, wzgledne=""):
    wyj = []
    for typ, dane in bloki:
        if typ == "obraz":
            if z_obrazami:
                o = OBRAZY[dane]
                wyj.append(f'<figure><img src="{wzgledne}{o["plik"]}" alt="{html.escape(o["alt"])}">'
                           f'<figcaption>{html.escape(o["podpis"])}</figcaption></figure>')
        elif typ == "ul":
            wyj.append("<ul>\n" + "\n".join(f"<li>{fragmenty_html(li)}</li>" for li in dane) + "\n</ul>")
        else:
            wyj.append(f"<{typ}>{fragmenty_html(dane)}</{typ}>")
    return "\n\n".join(wyj)


def tresc_tekst(bloki):
    """Wersja do edytora bez trybu HTML: [H2] przed śródtytułem, „- ” przed punktem listy."""
    wyj = []
    for typ, dane in bloki:
        if typ == "obraz":
            continue
        if typ == "ul":
            wyj.append("\n".join(f"- {fragmenty_tekst(li)}" for li in dane))
        elif typ == "h2":
            wyj.append("[H2] " + fragmenty_tekst(dane))
        else:
            wyj.append(fragmenty_tekst(dane))
    return "\n\n".join(wyj)


def miejsca_obrazow(bloki):
    """Opis miejsca każdego obrazu słowami, dla wydawcy."""
    opisy, poprzedni_h2 = {}, None
    for i, (typ, dane) in enumerate(bloki):
        if typ == "h2":
            poprzedni_h2 = fragmenty_tekst(dane)
        if typ != "obraz":
            continue
        nastepny = next((fragmenty_tekst(d) for t, d in bloki[i + 1:] if t == "h2"), None)
        przed = next(((t, d) for t, d in reversed(bloki[:i]) if t != "obraz"), None)
        if poprzedni_h2 is None:
            opisy[dane] = f"pod leadem, przed pierwszym śródtytułem „{nastepny}”"
        elif przed and przed[0] == "ul":
            opisy[dane] = f"w sekcji „{poprzedni_h2}”, zaraz pod listą punktowaną"
        else:
            opisy[dane] = (f"na końcu sekcji „{poprzedni_h2}”"
                           + (f", przed śródtytułem „{nastepny}”" if nastepny else ""))
    return opisy


def uwagi_dla_wydawcy(bloki):
    miejsca = miejsca_obrazow(bloki)
    pelne = ("Dzień dobry, prosimy o publikację tekstu bez zmian w treści i w linkach. "
             f"W artykule są {len(LINKI)} linki dofollow, prosimy zostawić je w podanym brzmieniu: "
             + "; ".join(f"„{a}” {u}" for a, u, _ in LINKI) + ". "
             "Zdjęcie główne: zdjecie-glowne-kieliszek-grawer-padir.jpg. "
             "W załącznikach są 3 infografiki i 1 zdjęcie do wstawienia w tekst: "
             + "; ".join(f"{os.path.basename(o['plik'])} {miejsca[k]}" for k, o in OBRAZY.items())
             + ". W pliku artykul.docx pod każdym obrazem jest podpis (kursywą), a pod nim osobno "
             "tekst alternatywny (ALT), który nie jest częścią podpisu. Jeśli to możliwe, prosimy "
             "o powiększanie infografik po kliknięciu, bo na telefonie ich tekst jest drobny. "
             "Wszystkie zdjęcia i grafiki należą do zamawiającego (Padir). Dziękujemy.")
    krotkie = ("Dzień dobry, prosimy o publikację bez zmian w treści i w linkach "
               f"({len(LINKI)} linki dofollow, anchory i adresy jak w tekście). "
               "Zdjęcie główne: zdjecie-glowne-kieliszek-grawer-padir.jpg. Pozostałe 4 obrazy "
               "z załączników prosimy wstawić w miejscach pokazanych w artykul.docx, tam są też "
               "teksty alternatywne i podpisy. Wszystkie zdjęcia i grafiki należą do Padir. Dziękujemy.")
    return pelne, krotkie


def podglad(bloki):
    tresc = tresc_html(bloki, True)
    g = ZDJECIE_GLOWNE
    strona = f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TYTUL)}</title>
<style>
body{{margin:0;background:#f4f5f8;font:18px/1.7 Georgia,'Times New Roman',serif;color:#1b1b1f}}
main{{max-width:760px;margin:0 auto;background:#fff;padding:40px 48px 64px}}
h1{{font:700 34px/1.25 system-ui,sans-serif;margin:0 0 18px}}
h2{{font:700 25px/1.3 system-ui,sans-serif;margin:40px 0 12px}}
.lead{{font-weight:700;font-size:19px}}
figure{{margin:28px 0}} img{{max-width:100%;height:auto;display:block}}
figcaption{{font:14px/1.5 system-ui,sans-serif;color:#5A5A60;margin-top:8px}}
a{{color:#12388C}}
.znacznik{{font:12px system-ui,sans-serif;color:#888;margin-bottom:20px}}
@media (max-width:600px){{main{{padding:24px 16px 48px}}h1{{font-size:27px}}}}
</style></head><body><main>
<div class="znacznik">Podgląd artykułu sponsorowanego. Wydawca doda własne oznaczenie i układ.</div>
<h1>{html.escape(TYTUL)}</h1>
<p class="lead">{html.escape(LEAD)}</p>
<figure><img src="{g['plik']}" alt="{html.escape(g['alt'])}"><figcaption>{html.escape(g['podpis'])}</figcaption></figure>
{tresc}
</main></body></html>
"""
    with open(os.path.join(KAT, "podglad.html"), "w", encoding="utf-8") as f:
        f.write(strona)


def dodaj_link(akapit, tekst, url):
    rid = akapit.part.relate_to(url, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink")
    h.set(qn("r:id"), rid)
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    kolor = OxmlElement("w:color")
    kolor.set(qn("w:val"), "12388C")
    pod = OxmlElement("w:u")
    pod.set(qn("w:val"), "single")
    rpr.append(kolor)
    rpr.append(pod)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = tekst
    t.set(qn("xml:space"), "preserve")
    r.append(t)
    h.append(r)
    akapit._p.append(h)


def wypelnij(akapit, fr):
    for t, h in fr:
        if h:
            dodaj_link(akapit, t, h)
        else:
            akapit.add_run(t)


def word(bloki):
    d = docx.Document()
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.5)
    d.core_properties.author = "Padir"
    d.core_properties.title = TYTUL
    d.core_properties.comments = ""
    styl = d.styles["Normal"]
    styl.font.name = "Calibri"
    styl.font.size = Pt(11.5)
    d.add_heading(TYTUL, level=1)
    p = d.add_paragraph()
    p.add_run(LEAD).bold = True

    def obraz(o, szer=Cm(15.5)):
        d.add_picture(os.path.join(KAT, o["plik"]), width=szer)
        akap = d.paragraphs[-1]
        akap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        akap.paragraph_format.keep_with_next = True
        d.inline_shapes[-1]._inline.docPr.set("descr", o["alt"])
        pp = d.add_paragraph()
        pp.paragraph_format.keep_with_next = True
        r = pp.add_run(o["podpis"])
        r.italic = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0x5A, 0x5A, 0x60)
        ra = d.add_paragraph().add_run("Tekst alternatywny (ALT, nie publikować jako podpis): " + o["alt"])
        ra.font.size = Pt(8.5)
        ra.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    obraz(ZDJECIE_GLOWNE)
    for typ, dane in bloki:
        if typ == "obraz":
            # infografiki są wysokie, w docx wystarczy węższy podgląd
            obraz(OBRAZY[dane], Cm(11) if dane.startswith("ig") else Cm(12))
        elif typ == "h2":
            d.add_heading(fragmenty_tekst(dane), level=2)
        elif typ == "p":
            wypelnij(d.add_paragraph(), dane)
        elif typ == "ul":
            for li in dane:
                wypelnij(d.add_paragraph(style="List Bullet"), li)
    d.save(os.path.join(KAT, "artykul.docx"))


def dlugosci(bloki, znaki):
    pelne, krotkie = uwagi_dla_wydawcy(bloki)
    return (f"treść {znaki['tresc']} znaków ze spacjami (sama treść, bez tytułu i leadu), "
            f"z tytułem i leadem {znaki['calosc']}; tytuł {len(TYTUL)} znaków; lead {len(LEAD)} znaków; "
            f"uwagi dla wydawcy {len(pelne)} znaków (wersja krótka {len(krotkie)})")


def do_wklejenia(bloki, znaki):
    miejsca = miejsca_obrazow(bloki)
    pelne, krotkie = uwagi_dla_wydawcy(bloki)
    linki = "\n".join(f"| {i} | „{a}” | {u} | {r} |" for i, (a, u, r) in enumerate(LINKI, 1))
    obrazy = "\n".join(
        f"| {k} | `{o['plik']}` | {miejsca[k]} | {o['alt']} | {o['podpis']} |" for k, o in OBRAZY.items())
    md = f"""# Artykuł nr 1 do WhitePress: dane do wklejenia

Plik generowany przez `zrodla/zbuduj.py`. Nie edytuj go ręcznie, popraw `zrodla/tresc.html` i uruchom skrypt ponownie.

Długości: {dlugosci(bloki, znaki)}.

## Tytuł

```
{TYTUL}
```

## Lead

```
{LEAD}
```

## Treść (HTML, do trybu źródła / HTML w edytorze)

Bez obrazów: obrazy wstawia wydawca według tabeli niżej.

```html
{tresc_html(bloki, False)}
```

## Treść (czysty tekst, gdy edytor nie ma trybu HTML)

Wiersz zaczynający się od `[H2] ` to śródtytuł: usuń znacznik `[H2] ` i ustaw wiersz jako nagłówek H2, bez zmiany liter. Wiersze zaczynające się od `- ` zamień na listę punktowaną. Linki ustaw ręcznie według tabeli „Linki”.

```
{tresc_tekst(bloki)}
```

## Linki ({len(LINKI)}, wszystkie dofollow, w kolejności ważności)

| # | Anchor (dokładnie) | Adres | Rodzaj |
|---|---|---|---|
{linki}

## Zdjęcie główne

`{ZDJECIE_GLOWNE['plik']}`, alt: {ZDJECIE_GLOWNE['alt']}, podpis: {ZDJECIE_GLOWNE['podpis']}

## Obrazy w treści (jako załączniki)

| Klucz | Plik | Gdzie w tekście | Alt | Podpis |
|---|---|---|---|---|
{obrazy}

## Uwagi dla wydawcy (pole „Uwagi” / „Komentarz do zamówienia”)

```
{pelne}
```

## Uwagi dla wydawcy, wersja krótka (gdy pole ma limit znaków)

```
{krotkie}
```
"""
    with open(os.path.join(KAT, "DO-WKLEJENIA.md"), "w", encoding="utf-8") as f:
        f.write(md)

    # Instrukcja dla Claude w Chrome niesie całą treść w sobie: agent w przeglądarce
    # nie musi czytać plików z dysku, wgrywa tylko obrazy (robi to właściciel).
    with open(os.path.join(TU, "instrukcja.md"), encoding="utf-8") as f:
        instr = f.read().rstrip()
    h2 = naglowki(bloki)
    zamiany = {
        "{{H2_LICZBA}}": str(len(h2)),
        "{{H2_LISTA}}": ", ".join(f"„{t}”" for t in h2),
        "{{DLUGOSCI}}": dlugosci(bloki, znaki),
        "{{TYTUL_KONIEC}}": " ".join(TYTUL.split()[-3:]),
        "{{LEAD_KONIEC}}": " ".join(LEAD.split()[-3:]),
        "{{LINKI_LICZBA}}": str(len(LINKI)),
    }
    for k, v in zamiany.items():
        instr = instr.replace(k, v)
    if "{{" in instr:
        raise SystemExit("instrukcja.md: niepodstawiony znacznik " + re.search(r"\{\{\w+\}\}", instr).group(0))
    materialy = md[md.index("## Tytuł"):].replace("\n## ", "\n### ")
    with open(os.path.join(KAT, "INSTRUKCJA-CLAUDE-W-CHROME.md"), "w", encoding="utf-8") as f:
        f.write(instr + "\n\n---\n\n## Materiały do wklejenia\n\n"
                + f"Długości: {dlugosci(bloki, znaki)}.\n\n" + materialy.replace("## Tytuł", "### Tytuł", 1))


def paczka():
    """Zip dla właściciela: po rozpakowaniu w Pobranych powstaje Pobrane/whitepress-artykul-01/."""
    pliki = (["INSTRUKCJA-CLAUDE-W-CHROME.md", "DO-WKLEJENIA.md", "artykul.docx", "podglad.html",
              ZDJECIE_GLOWNE["plik"]] + [o["plik"] for o in OBRAZY.values()])
    sciezka = os.path.join(KAT, PACZKA + ".zip")
    with zipfile.ZipFile(sciezka, "w", zipfile.ZIP_DEFLATED) as z:
        for p in pliki:
            z.write(os.path.join(KAT, p), f"{PACZKA}/{p}")
    return sciezka, len(pliki)


def kontrola(bloki):
    # sam tekst, bez znaczników [H2] i „- ” z tresc_tekst
    surowy = "\n".join(fragmenty_tekst(d) if t != "ul" else "\n".join(fragmenty_tekst(li) for li in d)
                       for t, d in bloki if t != "obraz")
    pelne, krotkie = uwagi_dla_wydawcy(bloki)
    calosc = "\n".join([TYTUL, LEAD, surowy, pelne, krotkie]
                       + [o["alt"] + o["podpis"] for o in list(OBRAZY.values()) + [ZDJECIE_GLOWNE]])
    with open(os.path.join(TU, "instrukcja.md"), encoding="utf-8") as f:
        calosc += f.read()
    bledy = []
    for znak, nazwa in (("—", "pauza"), ("–", "półpauza"), ("−", "minus")):
        if znak in calosc:
            bledy.append(f"{nazwa}: {calosc.count(znak)}x")
    if re.search(r"[^\n] - ", surowy + TYTUL + LEAD):
        bledy.append("dywiz ze spacjami (WordPress zamieni go na półpauzę)")
    linki = [(t, h) for typ, dane in bloki if typ in ("p", "h2") for t, h in dane if h]
    linki += [(t, h) for typ, dane in bloki if typ == "ul" for li in dane for t, h in li if h]
    if sorted(linki) != sorted((a, u) for a, u, _ in LINKI):
        bledy.append(f"linki niezgodne z listą: {linki}")
    if [k for t, k in bloki if t == "obraz"] != list(OBRAZY):
        bledy.append("kolejność obrazów w tresc.html różni się od OBRAZY (numery plików mają iść po kolei)")
    for o in list(OBRAZY.values()) + [ZDJECIE_GLOWNE]:
        if not os.path.exists(os.path.join(KAT, o["plik"])):
            bledy.append(f"brak pliku {o['plik']}")
    # znaki liczone z samego tekstu (bez [H2] i „- ” z wersji tekstowej), akapity rozdziela jeden znak końca wiersza
    znaki = {"tresc": len(surowy), "calosc": len(TYTUL) + len(LEAD) + len(surowy)}
    return bledy, znaki, len(linki)


def main():
    bloki = wczytaj()
    bledy, znaki, n = kontrola(bloki)
    podglad(bloki)
    word(bloki)
    do_wklejenia(bloki, znaki)
    zip_sciezka, zip_n = paczka()
    print(f"{dlugosci(bloki, znaki)}; linków: {n}; śródtytułów: {len(naglowki(bloki))}")
    print(f"paczka: {zip_sciezka} ({zip_n} plików, {os.path.getsize(zip_sciezka) // 1024} KB)")
    print("BŁĘDY:" if bledy else "kontrola: czysto", *bledy, sep="\n  ")
    sys.exit(1 if bledy else 0)


if __name__ == "__main__":
    main()
