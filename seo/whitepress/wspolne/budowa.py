"""Wspólna budowa artykułów WhitePress.

Artykuł ma katalog NN-slug/ z podkatalogiem zrodla/:
  zrodla/tresc.html    treść (h2, p, ul, linki <a>, znaczniki <!-- OBRAZ:klucz -->)
  zrodla/zbuduj.py     dane artykułu (TYTUL, LEAD, ZDJECIE_GLOWNE, OBRAZY, LINKI, ...) i wywołanie zbuduj()
  zrodla/infografiki.py  infografiki, renderowane funkcją renderuj() z infografiki_wspolne.py

zbuduj(A) tworzy w katalogu artykułu: podglad.html, DO-WKLEJENIA.md, artykul.docx,
INSTRUKCJA-CLAUDE-W-CHROME.md (szablon wspolne/instrukcja.md + materiały) i paczkę .zip
(poza gitem). Na końcu kontrola: zakazane myślniki, linki, kolejność obrazów, komplet plików.
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
from PIL import Image

WSPOLNE = os.path.dirname(os.path.abspath(__file__))


def odmiana(n, jeden, kilka, wiele):
    """3 linki, 5 linków, 1 link."""
    if n == 1:
        slowo = jeden
    elif n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        slowo = kilka
    else:
        slowo = wiele
    return f"{n} {slowo}"


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


def fragmenty_html(fr):
    return "".join(f'<a href="{html.escape(h)}">{html.escape(t)}</a>' if h else html.escape(t)
                   for t, h in fr).strip()


def fragmenty_tekst(fr):
    return "".join(t for t, _ in fr).strip()


class Artykul:
    def __init__(self, A):
        self.A = A
        self.TU = os.path.dirname(os.path.abspath(A.__file__))
        self.KAT = os.path.dirname(self.TU)
        c = Czytnik()
        with open(os.path.join(self.TU, "tresc.html"), encoding="utf-8") as f:
            c.feed(f.read())
        self.bloki = c.bloki

    # --- pomocnicze ---------------------------------------------------------

    def naglowki(self):
        return [fragmenty_tekst(d) for t, d in self.bloki if t == "h2"]

    def surowy(self):
        """Sam tekst treści, akapity i punkty list rozdzielone końcem wiersza."""
        return "\n".join(fragmenty_tekst(d) if t != "ul" else "\n".join(fragmenty_tekst(li) for li in d)
                         for t, d in self.bloki if t != "obraz")

    def znaki(self):
        s = len(self.surowy())
        return {"tresc": s, "calosc": len(self.A.TYTUL) + len(self.A.LEAD) + s}

    def tresc_html(self, z_obrazami):
        wyj = []
        for typ, dane in self.bloki:
            if typ == "obraz":
                if z_obrazami:
                    o = self.A.OBRAZY[dane]
                    wyj.append(f'<figure><img src="{o["plik"]}" alt="{html.escape(o["alt"])}">'
                               f'<figcaption>{html.escape(o["podpis"])}</figcaption></figure>')
            elif typ == "ul":
                wyj.append("<ul>\n" + "\n".join(f"<li>{fragmenty_html(li)}</li>" for li in dane) + "\n</ul>")
            else:
                wyj.append(f"<{typ}>{fragmenty_html(dane)}</{typ}>")
        return "\n\n".join(wyj)

    def tresc_tekst(self):
        """Wersja do edytora bez trybu HTML: [H2] przed śródtytułem, „- ” przed punktem listy."""
        wyj = []
        for typ, dane in self.bloki:
            if typ == "obraz":
                continue
            if typ == "ul":
                wyj.append("\n".join(f"- {fragmenty_tekst(li)}" for li in dane))
            elif typ == "h2":
                wyj.append("[H2] " + fragmenty_tekst(dane))
            else:
                wyj.append(fragmenty_tekst(dane))
        return "\n\n".join(wyj)

    def miejsca_obrazow(self):
        """Opis miejsca każdego obrazu słowami, dla wydawcy."""
        opisy, poprzedni_h2, b = {}, None, self.bloki
        for i, (typ, dane) in enumerate(b):
            if typ == "h2":
                poprzedni_h2 = fragmenty_tekst(dane)
            if typ != "obraz":
                continue
            nastepny = next((fragmenty_tekst(d) for t, d in b[i + 1:] if t == "h2"), None)
            przed = next(((t, d) for t, d in reversed(b[:i]) if t != "obraz"), None)
            if poprzedni_h2 is None:
                opisy[dane] = f"pod leadem, przed pierwszym śródtytułem „{nastepny}”"
            elif przed and przed[0] == "ul":
                opisy[dane] = f"w sekcji „{poprzedni_h2}”, zaraz pod listą punktowaną"
            else:
                opisy[dane] = (f"na końcu sekcji „{poprzedni_h2}”"
                               + (f", przed śródtytułem „{nastepny}”" if nastepny else ""))
        return opisy

    def uwagi(self):
        A, miejsca = self.A, self.miejsca_obrazow()
        n_ig = sum(1 for k in A.OBRAZY if k.startswith("ig"))
        n_zdj = len(A.OBRAZY) - n_ig
        glowne = os.path.basename(A.ZDJECIE_GLOWNE["plik"])
        pelne = ("Dzień dobry, prosimy o publikację tekstu bez zmian w treści i w linkach. "
                 f"W artykule są {odmiana(len(A.LINKI), 'link', 'linki', 'linków')} dofollow, "
                 "prosimy zostawić je w podanym brzmieniu: "
                 + "; ".join(f"„{a}” {u}" for a, u, _ in A.LINKI) + ". "
                 f"Zdjęcie główne: {glowne}. "
                 f"W załącznikach są {odmiana(n_ig, 'infografika', 'infografiki', 'infografik')} i "
                 f"{odmiana(n_zdj, 'zdjęcie', 'zdjęcia', 'zdjęć')} do wstawienia w tekst: "
                 + "; ".join(f"{os.path.basename(o['plik'])} {miejsca[k]}" for k, o in A.OBRAZY.items())
                 + ". W pliku artykul.docx pod każdym obrazem jest podpis (kursywą), a pod nim osobno "
                 "tekst alternatywny (ALT), który nie jest częścią podpisu. Jeśli to możliwe, prosimy "
                 "o powiększanie infografik po kliknięciu, bo na telefonie ich tekst jest drobny. "
                 "Wszystkie zdjęcia i grafiki należą do zamawiającego (Padir). Dziękujemy.")
        krotkie = ("Dzień dobry, prosimy o publikację bez zmian w treści i w linkach "
                   f"({odmiana(len(A.LINKI), 'link', 'linki', 'linków')} dofollow, anchory i adresy jak w tekście). "
                   f"Zdjęcie główne: {glowne}. Obrazy z załączników prosimy wstawić w miejscach "
                   "pokazanych w artykul.docx, tam są też teksty alternatywne i podpisy. "
                   "Wszystkie zdjęcia i grafiki należą do Padir. Dziękujemy.")
        return pelne, krotkie

    def dlugosci(self):
        z, (pelne, krotkie) = self.znaki(), self.uwagi()
        return (f"treść {z['tresc']} znaków ze spacjami (sama treść, bez tytułu i leadu), "
                f"z tytułem i leadem {z['calosc']}; tytuł {len(self.A.TYTUL)} znaków; "
                f"lead {len(self.A.LEAD)} znaków; uwagi dla wydawcy {len(pelne)} znaków "
                f"(wersja krótka {len(krotkie)})")

    def rozmiary(self):
        def wym(p):
            w, h = Image.open(os.path.join(self.KAT, p)).size
            return f"{w} × {h} px"
        A = self.A
        zdj = [o for k, o in A.OBRAZY.items() if not k.startswith("ig")]
        ig = [o for k, o in A.OBRAZY.items() if k.startswith("ig")]
        czesci = [f"zdjęcie główne {wym(A.ZDJECIE_GLOWNE['plik'])}"]
        if zdj:
            czesci.append("zdjęcia w tekście " + ", ".join(wym(o["plik"]) for o in zdj))
        if ig:
            szer = sorted({Image.open(os.path.join(self.KAT, o["plik"])).size[0] for o in ig})
            czesci.append("infografiki " + "/".join(map(str, szer)) + " px szerokości")
        return ", ".join(czesci)

    # --- wyjścia ------------------------------------------------------------

    def podglad(self):
        A, g = self.A, self.A.ZDJECIE_GLOWNE
        strona = f"""<!doctype html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(A.TYTUL)}</title>
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
<h1>{html.escape(A.TYTUL)}</h1>
<p class="lead">{html.escape(A.LEAD)}</p>
<figure><img src="{g['plik']}" alt="{html.escape(g['alt'])}"><figcaption>{html.escape(g['podpis'])}</figcaption></figure>
{self.tresc_html(True)}
</main></body></html>
"""
        with open(os.path.join(self.KAT, "podglad.html"), "w", encoding="utf-8") as f:
            f.write(strona)

    def word(self):
        A = self.A
        d = docx.Document()
        s = d.sections[0]
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Cm(2.5)
        d.core_properties.author = "Padir"
        d.core_properties.title = A.TYTUL
        d.core_properties.comments = ""
        styl = d.styles["Normal"]
        styl.font.name = "Calibri"
        styl.font.size = Pt(11.5)
        d.add_heading(A.TYTUL, level=1)
        d.add_paragraph().add_run(A.LEAD).bold = True

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

        def obraz(o, szer=Cm(15.5)):
            d.add_picture(os.path.join(self.KAT, o["plik"]), width=szer)
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

        obraz(A.ZDJECIE_GLOWNE)
        for typ, dane in self.bloki:
            if typ == "obraz":
                # infografiki są wysokie, w docx wystarczy węższy podgląd
                obraz(A.OBRAZY[dane], Cm(11) if dane.startswith("ig") else Cm(12))
            elif typ == "h2":
                d.add_heading(fragmenty_tekst(dane), level=2)
            elif typ == "p":
                wypelnij(d.add_paragraph(), dane)
            elif typ == "ul":
                for li in dane:
                    wypelnij(d.add_paragraph(style="List Bullet"), li)
        d.save(os.path.join(self.KAT, "artykul.docx"))

    def do_wklejenia(self):
        A, miejsca = self.A, self.miejsca_obrazow()
        pelne, krotkie = self.uwagi()
        linki = "\n".join(f"| {i} | „{a}” | {u} | {r} |" for i, (a, u, r) in enumerate(A.LINKI, 1))
        obrazy = "\n".join(f"| {k} | `{o['plik']}` | {miejsca[k]} | {o['alt']} | {o['podpis']} |"
                           for k, o in A.OBRAZY.items())
        g = A.ZDJECIE_GLOWNE
        md = f"""# Artykuł nr {A.NR} do WhitePress: dane do wklejenia

Plik generowany przez `zrodla/zbuduj.py`. Nie edytuj go ręcznie, popraw `zrodla/tresc.html` i uruchom skrypt ponownie.

Długości: {self.dlugosci()}.

## Tytuł

```
{A.TYTUL}
```

## Lead

```
{A.LEAD}
```

## Treść (HTML, do trybu źródła / HTML w edytorze)

Bez obrazów: obrazy wstawia wydawca według tabeli niżej.

```html
{self.tresc_html(False)}
```

## Treść (czysty tekst, gdy edytor nie ma trybu HTML)

Wiersz zaczynający się od `[H2] ` to śródtytuł: usuń znacznik `[H2] ` i ustaw wiersz jako nagłówek H2, bez zmiany liter. Wiersze zaczynające się od `- ` zamień na listę punktowaną. Linki ustaw ręcznie według tabeli „Linki”.

```
{self.tresc_tekst()}
```

## Linki ({len(A.LINKI)}, wszystkie dofollow, w kolejności ważności)

| # | Anchor (dokładnie) | Adres | Rodzaj |
|---|---|---|---|
{linki}

## Zdjęcie główne

`{g['plik']}`, alt: {g['alt']}, podpis: {g['podpis']}

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
        with open(os.path.join(self.KAT, "DO-WKLEJENIA.md"), "w", encoding="utf-8") as f:
            f.write(md)
        self.instrukcja(md)

    def instrukcja(self, md):
        """Szablon wspolne/instrukcja.md + materiały: agent w przeglądarce nie czyta plików z dysku."""
        A = self.A
        with open(os.path.join(WSPOLNE, "instrukcja.md"), encoding="utf-8") as f:
            instr = f.read().rstrip()
        h2 = self.naglowki()
        zamiany = {
            "{{NR}}": str(A.NR),
            "{{PACZKA}}": A.PACZKA,
            "{{TEMAT}}": A.TEMAT,
            "{{TEMATYKA}}": A.TEMATYKA,
            "{{H2_LICZBA}}": str(len(h2)),
            "{{H2_LISTA}}": ", ".join(f"„{t}”" for t in h2),
            "{{DLUGOSCI}}": self.dlugosci(),
            "{{TYTUL_KONIEC}}": " ".join(A.TYTUL.split()[-3:]),
            "{{LEAD_KONIEC}}": " ".join(A.LEAD.split()[-3:]),
            "{{LINKI_LICZBA}}": str(len(A.LINKI)),
            "{{LINKI}}": odmiana(len(A.LINKI), "link", "linki", "linków"),
            "{{LISTY_LICZBA}}": str(sum(1 for t, _ in self.bloki if t == "ul")),
            "{{OBRAZY}}": odmiana(len(A.OBRAZY), "obraz", "obrazy", "obrazów"),
            "{{ROZMIARY}}": self.rozmiary(),
            "{{ZDJECIE_GLOWNE}}": A.ZDJECIE_GLOWNE["plik"],
            "{{PODPIS_GLOWNE}}": A.ZDJECIE_GLOWNE["podpis"],
            "{{ZALACZNIKI}}": "\n".join(f"  - `{o['plik']}`" for o in A.OBRAZY.values()),
        }
        for k, v in zamiany.items():
            instr = instr.replace(k, v)
        if "{{" in instr:
            raise SystemExit("instrukcja.md: niepodstawiony znacznik " + re.search(r"\{\{\w+\}\}", instr).group(0))
        materialy = md[md.index("## Tytuł"):].replace("\n## ", "\n### ").replace("## Tytuł", "### Tytuł", 1)
        with open(os.path.join(self.KAT, "INSTRUKCJA-CLAUDE-W-CHROME.md"), "w", encoding="utf-8") as f:
            f.write(instr + "\n\n---\n\n## Materiały do wklejenia\n\n"
                    + f"Długości: {self.dlugosci()}.\n\n" + materialy)

    def paczka(self):
        """Zip dla właściciela: po rozpakowaniu w Pobranych powstaje Pobrane/<PACZKA>/."""
        A = self.A
        pliki = (["INSTRUKCJA-CLAUDE-W-CHROME.md", "DO-WKLEJENIA.md", "artykul.docx", "podglad.html",
                  A.ZDJECIE_GLOWNE["plik"]] + [o["plik"] for o in A.OBRAZY.values()])
        sciezka = os.path.join(self.KAT, A.PACZKA + ".zip")
        with zipfile.ZipFile(sciezka, "w", zipfile.ZIP_DEFLATED) as z:
            for p in pliki:
                z.write(os.path.join(self.KAT, p), f"{A.PACZKA}/{p}")
        return sciezka, len(pliki)

    def kontrola(self):
        A = self.A
        pelne, krotkie = self.uwagi()
        calosc = "\n".join([A.TYTUL, A.LEAD, self.surowy(), pelne, krotkie]
                           + [o["alt"] + o["podpis"] for o in list(A.OBRAZY.values()) + [A.ZDJECIE_GLOWNE]])
        with open(os.path.join(WSPOLNE, "instrukcja.md"), encoding="utf-8") as f:
            calosc += f.read()
        bledy = []
        for znak, nazwa in (("—", "pauza"), ("–", "półpauza"), ("−", "minus")):
            if znak in calosc:
                bledy.append(f"{nazwa}: {calosc.count(znak)}x")
        if re.search(r"[^\n] - ", self.surowy() + A.TYTUL + A.LEAD):
            bledy.append("dywiz ze spacjami (WordPress zamieni go na półpauzę)")
        linki = [(t, h) for typ, dane in self.bloki if typ in ("p", "h2") for t, h in dane if h]
        linki += [(t, h) for typ, dane in self.bloki if typ == "ul" for li in dane for t, h in li if h]
        if sorted(linki) != sorted((a, u) for a, u, _ in A.LINKI):
            bledy.append(f"linki niezgodne z listą: {linki}")
        if [k for t, k in self.bloki if t == "obraz"] != list(A.OBRAZY):
            bledy.append("kolejność obrazów w tresc.html różni się od OBRAZY (numery plików mają iść po kolei)")
        for o in list(A.OBRAZY.values()) + [A.ZDJECIE_GLOWNE]:
            if not os.path.exists(os.path.join(self.KAT, o["plik"])):
                bledy.append(f"brak pliku {o['plik']}")
        return bledy, len(linki)


def zbuduj(A):
    a = Artykul(A)
    bledy, n = a.kontrola()
    if any(b.startswith("brak pliku") for b in bledy):
        print("BŁĘDY:", *bledy, sep="\n  ")
        sys.exit(1)
    a.podglad()
    a.word()
    a.do_wklejenia()
    zip_sciezka, zip_n = a.paczka()
    print(f"{a.dlugosci()}; linków: {n}; śródtytułów: {len(a.naglowki())}")
    print(f"paczka: {zip_sciezka} ({zip_n} plików, {os.path.getsize(zip_sciezka) // 1024} KB)")
    print("BŁĘDY:" if bledy else "kontrola: czysto", *bledy, sep="\n  ")
    sys.exit(1 if bledy else 0)
