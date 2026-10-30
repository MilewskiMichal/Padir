#!/usr/bin/env python3
"""Infografiki do artykułu nr 1 (WhitePress): treść. Styl i render w wspolne/infografiki_wspolne.py.

    python3 infografiki.py

Numery plików idą w kolejności, w jakiej grafiki stoją w artykule.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "wspolne"))
from infografiki_wspolne import CSS, NIE_SVG, STOPKA, TAK_SVG, nbsp, renderuj  # noqa: E402


KROKI = [
    ("Materiał", "Z czego jest przedmiot? To decyduje o efekcie i o wyborze lasera."),
    ("Plik", "Wektor: AI, EPS, SVG, CDR, PDF. Bitmapa co najmniej 300 dpi."),
    ("Laser", "CO<sub>2</sub> do drewna, szkła, skóry i plexi. Fiber do gołego metalu."),
    ("Próba", "Przy serii najpierw jedna sztuka do zatwierdzenia."),
    ("Grawer", "Na drewnie zwykle ok. 0,2 mm, na metalu płycej. Głębiej to kilka przejść."),
    ("Odbiór", "Czyszczenie i kontrola. Znak jest tak trwały jak materiał."),
]


def ig1():
    karty = "".join(
        f'<div class="k"><div class="n">{i}</div><h2>{t}</h2><p>{nbsp(o)}</p></div>'
        for i, (t, o) in enumerate(KROKI, 1))
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>{CSS}
.siatka{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}}
.k{{background:#eef1f7;border-radius:20px;padding:26px 24px 28px}}
.n{{width:56px;height:56px;border-radius:50%;background:#12388C;color:#fff;font-weight:700;font-size:27px;display:flex;align-items:center;justify-content:center;margin-bottom:16px}}
.k h2{{font-size:28px;font-weight:700;margin-bottom:8px}}
.k p{{font-size:23px;line-height:1.42;color:#3d3d44}}
</style></head><body><div class="ig">
<div class="nad">Poradnik</div>
<h1>Grawerowanie laserowe w&nbsp;6&nbsp;krokach</h1>
<p class="pod">{nbsp("Ta sama droga dla jednego prezentu i dla serii tabliczek. Najwięcej czasu oszczędzają kroki 1 i 2.")}</p>
<div class="siatka">{karty}</div>{STOPKA}</div></body></html>"""


OK = [
    "Logo i napisy w wektorze: AI, EPS, SVG, CDR albo PDF z programu wektorowego",
    "Zdjęcia i inne bitmapy (JPG, PNG, TIFF) w co najmniej 300 dpi w docelowym rozmiarze",
    "Teksty zamienione na krzywe",
    "Wymiary 1:1 w milimetrach",
    "Linie nie cieńsze niż ok. 0,1 mm",
]
NIE = [
    "Logo skopiowane ze stopki maila albo zrzut ekranu",
    "Skan zapisany jako PDF zamiast pliku wektorowego",
]


def ig2():
    ok = "".join(f"<li>{TAK_SVG}<span>{nbsp(t)}</span></li>" for t in OK)
    nie = "".join(f"<li>{NIE_SVG}<span>{nbsp(t)}</span></li>" for t in NIE)
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>{CSS}
ul{{list-style:none}}
li{{display:flex;gap:16px;align-items:flex-start;font-size:23px;line-height:1.4;padding:9px 0}}
li svg{{flex:none;margin-top:1px}}
.blok{{background:#eef1f7;border-radius:20px;padding:22px 26px;margin-bottom:18px}}
.blok h2{{font-size:26px;font-weight:700;margin-bottom:6px}}
.kolory{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}}
.kol{{border:2px solid #dde3ee;border-radius:20px;padding:20px 22px}}
.kol svg{{display:block;width:100%;height:96px;margin-bottom:10px}}
.kol b{{display:block;font-size:24px;font-weight:700}}
.kol span{{display:block;font-size:21px;color:#3d3d44;line-height:1.4;margin-top:4px}}
.dop{{font-size:21px;line-height:1.5;color:#3d3d44}}
.dop b{{color:#141414}}
</style></head><body><div class="ig">
<div class="nad">Poradnik</div>
<h1>Plik do graweru: lista kontrolna</h1>
<p class="pod">{nbsp("Dobry plik to szybsza wycena i mniej poprawek. Sprawdź go przed wysłaniem.")}</p>
<div class="blok"><h2>Wysyłaj</h2><ul>{ok}</ul></div>
<div class="blok"><h2>Unikaj</h2><ul>{nie}</ul></div>
<div class="kolory">
<div class="kol"><svg viewBox="0 0 300 96"><rect x="20" y="10" width="260" height="76" rx="16" fill="none" stroke="#E0201B" stroke-width="2"/></svg><b>Cięcie</b><span>{nbsp("najcieńsza czerwona linia (np. 0,001 mm, tzw. hairline)")}</span></div>
<div class="kol"><svg viewBox="0 0 300 96"><rect x="20" y="10" width="260" height="76" rx="16" fill="#eef1f7" stroke="#c3cfe6" stroke-width="2"/><text x="150" y="61" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="36" fill="#1F4FD8">LOGO</text></svg><b>Grawer</b><span>{nbsp("inny kolor, często niebieski")}</span></div>
</div>
<p class="dop">{nbsp("<b>To częsta umowa, nie norma.</b> Zapytaj pracownię o jej oznaczenia. Masz tylko zdjęcie logo albo szkic? Pracownia może odtworzyć znak w wektorze.")}</p>
{STOPKA}</div></body></html>"""


CO2 = [
    ("Drewno i sklejka", "ciemny, lekko przypalony rysunek"),
    ("Szkło i kryształ", "matowa, mleczna powierzchnia"),
    ("Plexi lana", "mleczna linia, świeci przy podświetleniu"),
    ("Skóra", "ciemniejszy odcisk w materiale"),
    ("Papier i karton", "precyzyjny grawer i wycinanie"),
    ("Laminat grawerski", "odsłania kolor spodniej warstwy"),
]
FIBER = [
    ("Stal nierdzewna", "jasny, matowy albo ciemny znak"),
    ("Aluminium anodowane", "czysty, jasny znak"),
    ("Metal z czarną powłoką", "największy kontrast"),
    ("Mosiądz", "trwały znak na tabliczkach i plakietach"),
    ("Części maszyn", "kody QR, Data Matrix, numery seryjne"),
]


def ig3():
    def kol(nazwa, fala, wiersze, klasa):
        w = "".join(f'<li><b>{m}</b><span>{nbsp(e)}</span></li>' for m, e in wiersze)
        return f'<div class="kol {klasa}"><div class="gl"><h2>{nazwa}</h2><span>fala ok. {fala}</span></div><ul>{w}</ul></div>'
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>{CSS}
.dwie{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.kol{{border-radius:20px;overflow:hidden;background:#eef1f7}}
.gl{{padding:20px 20px 18px;color:#fff}}
.co2 .gl{{background:#12388C}} .fib .gl{{background:#141414}}
.gl h2{{font-size:28px;font-weight:700;line-height:1.15}}
.gl span{{display:block;font-size:19px;opacity:.85;margin-top:4px}}
ul{{list-style:none;padding:4px 20px 12px}}
li{{padding:13px 0;border-bottom:2px solid #dde3ee}}
li:last-child{{border-bottom:0}}
li b{{display:block;font-size:22px;font-weight:600;line-height:1.3}}
li span{{display:block;font-size:20px;line-height:1.38;color:#3d3d44;margin-top:3px}}
.uwaga{{margin-top:18px;border:3px solid #DE6B24;border-radius:20px;padding:18px 22px;font-size:21px;line-height:1.45}}
.uwaga p+p{{margin-top:8px}}
.uwaga b{{font-weight:700}}
</style></head><body><div class="ig">
<div class="nad">Poradnik</div>
<h1>Który laser do jakiego materiału?</h1>
<p class="pod">{nbsp("Laser dobiera pracownia. Tobie wystarczy wiedzieć, czego się spodziewać po materiale.")}</p>
<div class="dwie">{kol("Laser CO<sub>2</sub>", "10,6 µm", CO2, "co2")}{kol("Laser fiber", "1,06 µm", FIBER, "fib")}</div>
<div class="uwaga">
<p>{nbsp("<b>Aluminium anodowane i powłokę proszkową</b> oznaczy też laser CO<sub>2</sub>, bo zdejmuje samą powłokę.")}</p>
<p>{nbsp("<b>Słabo przyjmują grawer:</b> guma i powłoki soft touch. <b>Nietypowy materiał?</b> Najpierw próba na jednej sztuce.")}</p>
</div>
{STOPKA}</div></body></html>"""


PLIKI = {  # w kolejności, w jakiej grafiki stoją w artykule
    "ig1-grawerowanie-laserowe-6-krokow": ig1,
    "ig2-plik-do-graweru-lista-kontrolna": ig2,
    "ig3-laser-co2-czy-fiber": ig3,
}


if __name__ == "__main__":
    renderuj(PLIKI, os.path.dirname(os.path.abspath(__file__)))
