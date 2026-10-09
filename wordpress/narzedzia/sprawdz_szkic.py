#!/usr/bin/env python3
"""Mechaniczna kontrola tresci strony przed zapisem do WordPressa.

Kazda regula tutaj to blad, ktory juz raz poszedl na produkcje albo prawie
poszedl. Skrypt nie ocenia jakosci tekstu ani wygladu, tylko rzeczy,
ktore da sie sprawdzic maszynowo i ktorych czlowiek nie zauwazy w podgladzie.

    python3 -I sprawdz_szkic.py plik.html [--szkic] [--json]

  --szkic   tryb wersji do akceptacji: zolte ramki `pdw-uwaga` sa dozwolone
            (i liczone), bo tak oznaczamy rzeczy do potwierdzenia z klientem.
            Bez tej flagi ich obecnosc to blad, bo nie moga trafic na produkcje.
  --json    wynik jako JSON (dla agentow).

Kod wyjscia 0 = brak bledow, 1 = sa bledy. Ostrzezenia nie zmieniaja kodu.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
ZRODLA = os.path.join(HERE, "zrodla")

bledy, ostrzezenia, info = [], [], {}


def blad(regula, opis):
    bledy.append({"regula": regula, "opis": opis})


def ostrz(regula, opis):
    ostrzezenia.append({"regula": regula, "opis": opis})


def okolica(t, i, szer=70):
    return re.sub(r"\s+", " ", t[max(0, i - szer):i + szer])


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    szkic = "--szkic" in sys.argv
    jako_json = "--json" in sys.argv
    if not argv:
        print(__doc__)
        sys.exit(2)
    t = open(argv[0], encoding="utf-8").read()
    info["plik"] = argv[0]
    info["znakow"] = len(t)

    # 1. Pauzy. Regula domu: wylacznie dywiz.
    for znak, nazwa in (("—", "myślnik"), ("–", "półpauza"), ("−", "minus")):
        for m in re.finditer(znak, t):
            blad("pauza", f"{nazwa} zamiast dywizu: …{okolica(t, m.start())}…")
    #    WordPress (wptexturize) sam zamienia w widocznym tekscie „ - ” ze
    #    spacjami na polpauze, a „--” na pauze. Zrodlo wyglada czysto, strona
    #    juz nie. Zakresy piszemy bez spacji: „8:30-16:00”.
    widoczny = re.sub(r"<(style|script)\b.*?</\1>|<!--.*?-->|<[^>]+>", " ", t, flags=re.S | re.I)
    for m in re.finditer(r"(?<=\S) - (?=\S)|(?<!-)--(?!-)", widoczny):
        blad("pauza", f"WordPress zamieni „{m.group(0).strip() or '-'}” na pauzę: "
                      f"…{okolica(widoczny, m.start())}…")

    # 2. Podwojny ampersand: WordPress zamienia go w tresci na encje
    #    i psuje skladnie skryptu oraz tekst.
    for m in re.finditer(r"&&", t):
        blad("ampersand", f"„&&” w treści: …{okolica(t, m.start())}…")

    # 3. Regula zgodnosci z block-library WordPressa:
    #    html :where([style*="; border-width"]){border-style:solid} i podobne.
    #    Skrot `border-width` albo dlugie `border-*-color`/`border-*-width`
    #    w atrybucie style sprawiaja, ze WordPress domalowuje WSZYSTKIE boki.
    #    Tak nawias w hero na /wycinanie-laserowe/ zamienil sie w kwadrat.
    ryzykowne = ["border-color", "border-width", "border-top-color", "border-right-color",
                 "border-bottom-color", "border-left-color", "border-top-width",
                 "border-right-width", "border-bottom-width", "border-left-width"]
    for m in re.finditer(r'style="([^"]*)"', t):
        s = m.group(1)
        for w in ryzykowne:
            if re.search(r"(^|;\s*)" + re.escape(w) + r"\s*:", s):
                blad("border-wp", f"inline `{w}:` - WordPress narzuci border-style:solid "
                                  f"na wszystkie boki: …{s[:110]}…")
                break

    # 4. Arkusze musza byc nietykalne dla LiteSpeeda, inaczej UCSS je wycina.
    for m in re.finditer(r"<style([^>]*)>", t):
        if 'data-no-optimize="1"' not in m.group(1):
            blad("arkusz", f"<style{m.group(1)}> bez data-no-optimize=\"1\" - LiteSpeed go wytnie")
    info["arkuszy"] = len(re.findall(r"<style", t))

    # 5. Naglowki h3: motyw ma `div div div h3{color:...base!important}`,
    #    ktory maluje je na bialo. Tylko inline z !important to przebija.
    for m in re.finditer(r"<h3\b([^>]*)>", t):
        a = m.group(1)
        st = re.search(r'style="([^"]*)"', a)
        if not st or "color" not in st.group(1) or "!important" not in st.group(1):
            blad("h3-kolor", f"<h3> bez inline color z !important (motyw pomaluje go na biało): "
                             f"{m.group(0)[:120]}")

    # 6. Dokladnie jeden h1.
    h1 = len(re.findall(r"<h1\b", t))
    info["h1"] = h1
    if h1 != 1:
        blad("h1", f"liczba <h1>: {h1}, ma być dokładnie 1")

    # 7. Obrazki: alt, ladowanie, zrodla.
    media_urls = set()
    try:
        for x in json.load(open(os.path.join(ZRODLA, "media.json"), encoding="utf-8")):
            media_urls.add(x["url"])
            if x.get("url_medium"):
                media_urls.add(x["url_medium"])
    except Exception:
        pass
    imgs = list(re.finditer(r"<img\b[^>]*>", t))
    info["zdjec"] = len(imgs)
    hero = re.search(r"<header\b.*?</header>", t, re.S)
    hero_rng = (hero.start(), hero.end()) if hero else (-1, -1)
    for m in imgs:
        tag = m.group(0)
        # Pusty obrazek lightboxa: src i alt wstawia skrypt po kliknieciu
        # w kafel. Na wzorcu /wycinanie-laserowe/ wyglada tak samo.
        if 'class="pdw-lb-img"' in tag:
            continue
        alt = re.search(r'\balt="([^"]*)"', tag)
        if not alt or not alt.group(1).strip():
            blad("alt", f"obrazek bez opisu alternatywnego: {tag[:120]}")
        src = re.search(r'\bsrc="([^"]+)"', tag)
        if not src:
            blad("src", f"obrazek bez src: {tag[:100]}")
            continue
        u = src.group(1)
        if u.startswith("blob:") or u.startswith("data:"):
            blad("src", f"tymczasowy adres obrazka ({u[:30]}…)")
        elif "grawerowanie-laserowe.pl/wp-content/uploads/" not in u:
            blad("src", f"obrazek spoza biblioteki serwisu: {u[:100]}")
        elif media_urls:
            # dopuszczamy wszystkie rozmiary posrednie tego samego pliku
            rdzen = re.sub(r"-\d+x\d+(?=\.\w+$)", "", u)
            rdzen = re.sub(r"-scaled(?=\.\w+$)", "", rdzen)
            if not any(re.sub(r"-scaled(?=\.\w+$)", "", x).startswith(rdzen.rsplit(".", 1)[0])
                       for x in media_urls):
                ostrz("src", f"nie znalazłem pliku w media.json: {u}")
        w_hero = hero_rng[0] <= m.start() < hero_rng[1]
        if w_hero:
            for wym in ('loading="eager"', 'fetchpriority="high"', 'data-no-lazy="1"'):
                if wym not in tag:
                    blad("hero-ladowanie", f"zdjęcie w hero bez {wym} - LiteSpeed i leniwe "
                                           f"ładowanie zostawią puste kafle: {tag[:100]}")
        elif 'loading="lazy"' not in tag:
            ostrz("ladowanie", f"zdjęcie poza hero bez loading=\"lazy\": {tag[:100]}")

    # 8. Rownowaga blokow i znacznikow.
    for otw, zam in (("<!-- wp:html -->", "<!-- /wp:html -->"),
                     ("<!-- wp:group", "<!-- /wp:group -->")):
        a, b = t.count(otw), t.count(zam)
        if a != b:
            blad("bloki", f"{otw!r}: {a} otwarć, {b} zamknięć")

    class Licznik(HTMLParser):
        PUSTE = {"br", "hr", "img", "input", "meta", "link", "source", "area", "col", "wbr", "path",
                 "circle", "rect", "line", "polyline", "polygon", "ellipse", "use", "stop"}

        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stos, self.problemy = [], []

        def handle_starttag(self, tag, attrs):
            if tag not in self.PUSTE:
                self.stos.append((tag, self.getpos()))

        def handle_startendtag(self, tag, attrs):
            pass

        def handle_endtag(self, tag):
            if tag in self.PUSTE:
                return
            if not self.stos:
                self.problemy.append(f"</{tag}> bez otwarcia (linia {self.getpos()[0]})")
                return
            if self.stos[-1][0] == tag:
                self.stos.pop()
                return
            # szukamy glebiej; jesli jest, to po drodze cos nie zostalo zamkniete
            for i in range(len(self.stos) - 1, -1, -1):
                if self.stos[i][0] == tag:
                    for niezamk, poz in self.stos[i + 1:]:
                        if niezamk not in ("p", "li", "option", "dt", "dd", "td", "tr", "th"):
                            self.problemy.append(f"<{niezamk}> z linii {poz[0]} niezamknięte przed </{tag}>")
                    del self.stos[i:]
                    return
            self.problemy.append(f"</{tag}> bez otwarcia (linia {self.getpos()[0]})")

    bez_skryptow = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", t, flags=re.S)
    lp = Licznik()
    lp.feed(bez_skryptow)
    for tag, poz in lp.stos:
        if tag not in ("p", "li"):
            lp.problemy.append(f"<{tag}> z linii {poz[0]} nigdy niezamknięte")
    for p in lp.problemy[:12]:
        blad("html", p)
    if len(lp.problemy) > 12:
        blad("html", f"…i jeszcze {len(lp.problemy) - 12} problemów ze znacznikami")

    # 9. Kontener i formularz.
    if not re.search(r'<div class="pdw"', t):
        blad("kontener", "brak kontenera <div class=\"pdw\">, arkusz jest zawężony do .pdw")
    if '[contact-form-7 id="480"]' not in t:
        blad("formularz", 'brak formularza [contact-form-7 id="480"]')

    # 10. Kotwice: kazde href="#x" musi miec id="x" na stronie.
    idy = set(re.findall(r'\bid="([^"]+)"', t))
    for k in sorted(set(re.findall(r'href="#([^"]+)"', t))):
        if k not in idy:
            blad("kotwica", f"link do #{k}, a na stronie nie ma id=\"{k}\"")

    # 11. Linki wewnetrzne musza prowadzic do istniejacych, OPUBLIKOWANYCH adresow.
    znane = {}
    try:
        for x in json.load(open(os.path.join(ZRODLA, "SPIS.json"), encoding="utf-8")):
            sciezka = x["link"].replace("https://grawerowanie-laserowe.pl", "")
            znane[sciezka] = x["status"]
    except Exception:
        pass
    for m in re.finditer(r'href="((?:https://grawerowanie-laserowe\.pl)?/[^"#?]*)', t):
        sciezka = m.group(1).replace("https://grawerowanie-laserowe.pl", "") or "/"
        if sciezka.startswith("/wp-content/"):
            continue
        if not sciezka.endswith("/"):
            sciezka += "/"
        if znane and sciezka != "/" and sciezka not in znane:
            blad("link", f"link wewnętrzny do nieznanego adresu: {sciezka}")
        elif znane.get(sciezka) and znane[sciezka] != "publish":
            blad("link", f"link do strony, która nie jest opublikowana ({znane[sciezka]}): {sciezka}")
    info["linkow_wewnetrznych"] = len(set(re.findall(
        r'href="(?:https://grawerowanie-laserowe\.pl)?(/[^"#?]+)', t)))

    # 12. Znane bledne parametry, raz juz poprawione na /wycinanie-laserowe/.
    for zle, dlaczego in (("do 400 W", "moc sprzeczna z resztą serwisu (park to 20-500 W, SP2000 180-500 W)"),
                          ("1650 × 2510", "pole robocze SP2000 to 2510 × 1680 mm"),
                          ("1650x2510", "pole robocze SP2000 to 2510 × 1680 mm")):
        if zle in t:
            blad("parametry", f"„{zle}”: {dlaczego}")

    # 13. Znaczniki wersji roboczej.
    uwagi = len(re.findall(r'class="pdw-uwaga"', t))
    info["ramek_pdw_uwaga"] = uwagi
    for slad in ("blob:", "SZKIC", "Lorem", "lorem ipsum", "TODO", "XXX", "[[", "]]"):
        if slad in t:
            blad("slad", f"pozostałość w treści: „{slad}”")
    if not szkic and uwagi:
        blad("szkic", f"{uwagi} ramek pdw-uwaga - na produkcję nie mogą trafić")
    if not szkic and "Wersja robocza" in t:
        blad("szkic", "napis „Wersja robocza” - na produkcję nie może trafić")

    # 14. Typowe slady tekstu z modelu jezykowego (ostrzezenia, nie bledy).
    tekst = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", t, flags=re.S)
    tekst = re.sub(r"<[^>]+>", " ", tekst)
    for zwrot in ("W dzisiejszych czasach", "W dzisiejszym", "Warto zauważyć", "Warto podkreślić",
                  "Należy pamiętać", "Nie da się ukryć", "Bez wątpienia", "Podsumowując",
                  "Reasumując", "kluczową rolę", "W świecie, w którym", "to nie tylko",
                  "kompleksow", "innowacyjn", "szeroki wachlarz", "od A do Z",
                  "najwyższej jakości", "Nasz zespół", "pasja", "dynamicznie"):
        if zwrot.lower() in tekst.lower():
            ostrz("styl-tekstu", f"zwrot typowy dla tekstu generowanego: „{zwrot}”")
    info["slow"] = len(tekst.split())

    wynik = {"bledy": bledy, "ostrzezenia": ostrzezenia, "info": info,
             "ok": not bledy}
    if jako_json:
        print(json.dumps(wynik, ensure_ascii=False, indent=1))
    else:
        print(f"{argv[0]}  ({info.get('znakow')} zn., {info.get('slow')} słów, "
              f"{info.get('zdjec')} zdjęć, h1={info.get('h1')}, ramek pdw-uwaga={uwagi})")
        print(f"  BŁĘDY: {len(bledy)}")
        for b in bledy:
            print(f"    ✗ [{b['regula']}] {b['opis']}")
        print(f"  ostrzeżenia: {len(ostrzezenia)}")
        for o in ostrzezenia:
            print(f"    ! [{o['regula']}] {o['opis']}")
    sys.exit(0 if not bledy else 1)


if __name__ == "__main__":
    main()
