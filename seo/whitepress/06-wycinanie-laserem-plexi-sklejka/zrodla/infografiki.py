#!/usr/bin/env python3
"""Infografiki do artykułu nr 6 (WhitePress): treść. Styl i render w wspolne/infografiki_wspolne.py.

    python3 infografiki.py

Numery plików idą w kolejności, w jakiej grafiki stoją w artykule.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "wspolne"))
from infografiki_wspolne import NIE_SVG, TAK_SVG, nbsp, renderuj, strona  # noqa: E402

KOSZTY = [
    ("Długie linie cięcia", "Każdy ażur, ząbek i ozdobnik to dłuższa droga głowicy."),
    ("Dużo otworów", "Przy każdym kształcie laser zaczyna cięcie od nowa."),
    ("Gruba płyta", "Grubszy materiał to wolniejsze cięcie, czasem w dwóch przejściach."),
    ("Duży grawer", "Wypełnienie pola trwa dłużej niż cięcie samego konturu."),
    ("Zdublowane linie", "Laser tnie to samo miejsce dwa razy i mocniej je przypala."),
    ("Luźny rozkrój", "Mniej elementów na arkuszu to więcej zużytego materiału."),
]


def ig1():
    karty = "".join(
        f'<div class="k"><div class="n">{i}</div><h2>{t}</h2><p>{nbsp(o)}</p></div>'
        for i, (t, o) in enumerate(KOSZTY, 1))
    return strona("""
.siatka{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.k{background:#eef1f7;border-radius:20px;padding:26px 24px 28px}
.n{width:56px;height:56px;border-radius:50%;background:#12388C;color:#fff;font-weight:700;font-size:27px;display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.k h2{font-size:27px;font-weight:700;line-height:1.2;margin-bottom:8px}
.k p{font-size:23px;line-height:1.42;color:#3d3d44}
""", f"""<div class="nad">Poradnik</div>
<h1>Co podnosi cenę cięcia laserem</h1>
<p class="pod">{nbsp("Za narzędzie nie płacisz, za czas pracy maszyny tak. Na większość tych rzeczy masz wpływ już w pliku.")}</p>
<div class="siatka">{karty}</div>""")


OK = [
    "Wektor: DXF, SVG, AI, CDR albo PDF z programu wektorowego",
    "Skala 1:1, wymiary w milimetrach",
    "Zamknięte kontury i teksty zamienione na krzywe",
    "Cięcie, grawer i nacinanie w osobnych kolorach albo warstwach",
    "Detale nie węższe niż grubość materiału",
]
NIE = [
    "Zdublowane linie, np. po kopiowaniu obiektów",
    "Przerwy w konturach",
    "Zdjęcie albo zrzut ekranu zamiast wektora",
]
SKLEJKA, KRAWEDZ = "#E2C79B", "#8A5A2B"


def litera_o(mostki):
    """Płyta z otworem w kształcie litery O. Bez mostków środek wypada, z mostkami zostaje."""
    plyta = f'<rect x="20" y="10" width="260" height="150" rx="10" fill="{SKLEJKA}" stroke="{KRAWEDZ}" stroke-width="2"/>'
    otwor = '<circle cx="150" cy="85" r="56" fill="#fff" stroke="#E0201B" stroke-width="2"/>'
    if not mostki:
        # w miejscu środka litery zostaje pusta dziura: przerywany okrąg pokazuje, co wypadło
        srodek = '<circle cx="150" cy="85" r="28" fill="none" stroke="#5A5A60" stroke-width="2.5" stroke-dasharray="7 6"/>'
    else:
        srodek = (f'<circle cx="150" cy="85" r="28" fill="{SKLEJKA}" stroke="#E0201B" stroke-width="2"/>'
                  f'<rect x="144" y="27" width="12" height="32" fill="{SKLEJKA}"/>'
                  f'<rect x="144" y="111" width="12" height="32" fill="{SKLEJKA}"/>')
    return f'<svg viewBox="0 0 300 170">{plyta}{otwor}{srodek}</svg>'


def ig2():
    ok = "".join(f"<li>{TAK_SVG}<span>{nbsp(t)}</span></li>" for t in OK)
    nie = "".join(f"<li>{NIE_SVG}<span>{nbsp(t)}</span></li>" for t in NIE)
    return strona("""
ul{list-style:none}
li{display:flex;gap:16px;align-items:flex-start;font-size:23px;line-height:1.4;padding:9px 0}
li svg{flex:none;margin-top:1px}
.blok{background:#eef1f7;border-radius:20px;padding:22px 26px;margin-bottom:18px}
.blok h2{font-size:26px;font-weight:700;margin-bottom:6px}
.wyspy{border:2px solid #dde3ee;border-radius:20px;padding:22px 22px 18px}
.wyspy h2{font-size:26px;font-weight:700;margin-bottom:4px}
.wyspy>p{font-size:21px;line-height:1.45;color:#3d3d44;margin-bottom:14px}
.dwa{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.dwa svg{display:block;width:100%;height:auto}
.dwa b{display:block;font-size:22px;font-weight:700;margin-top:8px}
.dwa span{display:block;font-size:20px;color:#3d3d44;line-height:1.35}
""", f"""<div class="nad">Poradnik</div>
<h1>Plik do cięcia laserem: lista kontrolna</h1>
<p class="pod">{nbsp("Dobry plik to szybsza wycena i niższa cena. Sprawdź go przed wysłaniem.")}</p>
<div class="blok"><h2>Wysyłaj</h2><ul>{ok}</ul></div>
<div class="blok"><h2>Unikaj</h2><ul>{nie}</ul></div>
<div class="wyspy"><h2>Napis jako otwór w płycie</h2>
<p>{nbsp("Środki liter O, A czy R wypadną razem z resztą. Pomogą mostki, podkład albo grawer zamiast cięcia.")}</p>
<div class="dwa">
<div>{litera_o(False)}<b>Bez mostków</b><span>{nbsp("środek litery wypada")}</span></div>
<div>{litera_o(True)}<b>Z mostkami</b><span>{nbsp("środek zostaje na miejscu")}</span></div>
</div></div>""")


MATERIALY = [
    # nazwa, kolor płyty, kolor krawędzi, krawędź, do czego
    ("Plexi (akryl)", "#D7ECF7", "#9CCBE6", "gładka, prawie polerowana, bez szlifowania.",
     "litery, standy, statuetki. Pod grawer lepsza plexi lana."),
    ("Sklejka", SKLEJKA, "#6B4423", "ciemna, lekko przypalona. Im grubsza płyta, tym ciemniejsza.",
     "dekoracje, modele, elementy POS."),
    ("MDF", "#C9A47A", "#3F2814", "ciemna, potrafi się lekko strzępić.",
     "elementy do malowania albo oklejania."),
    ("Laminat grawerski", "#C8CBD2", "#26262B", "równa, w kolorze rdzenia.",
     "tabliczki, cięcie i grawer w jednej operacji."),
]


def przekroj(gora, krawedz):
    return (f'<svg viewBox="0 0 120 90" width="120" height="90">'
            f'<path d="M14 30 L44 10 L110 10 L80 30 Z" fill="{gora}" stroke="#141414" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<path d="M14 30 L80 30 L80 74 L14 74 Z" fill="{krawedz}" stroke="#141414" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<path d="M80 30 L110 10 L110 54 L80 74 Z" fill="{krawedz}" opacity=".8" stroke="#141414" stroke-width="1.5" stroke-linejoin="round"/>'
            '</svg>')


def ig3():
    wiersze = "".join(
        f'<div class="m">{przekroj(g, k)}<div><h2>{n}</h2><p><b>Krawędź:</b> {nbsp(e)}</p><p><b>Do:</b> {nbsp(z)}</p></div></div>'
        for n, g, k, e, z in MATERIALY)
    return strona("""
.m{display:flex;gap:20px;align-items:flex-start;background:#eef1f7;border-radius:20px;padding:20px 22px;margin-bottom:14px}
.m svg{flex:none;margin-top:4px}
.m h2{font-size:26px;font-weight:700;margin-bottom:4px}
.m p{font-size:21px;line-height:1.4;color:#3d3d44;margin-top:4px}
.m p b{color:#141414;font-weight:600}
.uwaga{margin-top:18px;border:3px solid #DE6B24;border-radius:20px;padding:18px 22px;font-size:21px;line-height:1.45}
.uwaga p+p{margin-top:8px}
.uwaga b{font-weight:700}
""", f"""<div class="nad">Poradnik</div>
<h1>Plexi, sklejka, MDF: czego się spodziewać po krawędzi</h1>
<p class="pod">{nbsp("Laser CO<sub>2</sub> tnie bez docisku i bez narzędzia, ale każdy materiał zostawia inną krawędź.")}</p>
{wiersze}
<div class="uwaga">
<p>{nbsp("<b>Laserem się nie tnie PVC:</b> przy cięciu wydziela związki chloru.")}</p>
<p>{nbsp("<b>Bardzo gruba płyta</b> albo obróbka przestrzenna? To zadanie dla frezarki CNC.")}</p>
</div>""")


PLIKI = {  # w kolejności, w jakiej grafiki stoją w artykule
    "ig1-co-podnosi-cene-ciecia-laserem": ig1,
    "ig2-plik-do-ciecia-lista-kontrolna": ig2,
    "ig3-plexi-sklejka-mdf-krawedz": ig3,
}

if __name__ == "__main__":
    renderuj(PLIKI, os.path.dirname(os.path.abspath(__file__)))
