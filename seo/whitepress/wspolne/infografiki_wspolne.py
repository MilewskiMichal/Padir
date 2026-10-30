"""Wspólne elementy infografik WhitePress: styl, stopka, ikony i render HTML -> PNG.

Płótno ma 760 px CSS i jest renderowane do 2160 px szerokości, żeby na telefonie
(obraz ok. 360 px) tekst miał ok. 11 px, a nie 7 px.
Kolory z arkusza strony: granat #12388C, tło #eef1f7, tekst #141414, szary #5A5A60,
akcent #DE6B24 tylko na dużych elementach (kontrast z bielą 3,4:1).
Fonty Poppins leżą w wspolne/fonty/; HTML infografik powstaje w NN-slug/zrodla/.
"""
import asyncio
import os
import re

from PIL import Image
from playwright.async_api import async_playwright

SZER_CSS, SZER_PNG = 760, 2160
FONTY = "../../wspolne/fonty"

CSS = f"""
@font-face{{font-family:Poppins;font-weight:400;src:url({FONTY}/Poppins-Regular.ttf)}}
@font-face{{font-family:Poppins;font-weight:500;src:url({FONTY}/Poppins-Medium.ttf)}}
@font-face{{font-family:Poppins;font-weight:600;src:url({FONTY}/Poppins-SemiBold.ttf)}}
@font-face{{font-family:Poppins;font-weight:700;src:url({FONTY}/Poppins-Bold.ttf)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#fff;font-family:Poppins,sans-serif;color:#141414}}
.ig{{width:{SZER_CSS}px;padding:48px 40px 36px;background:#fff}}
.nad{{font-size:18px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#12388C;margin-bottom:12px}}
h1{{font-size:44px;line-height:1.12;font-weight:700;color:#141414;margin-bottom:14px}}
.pod{{font-size:23px;line-height:1.45;color:#5A5A60;margin-bottom:32px}}
.stopka{{display:flex;justify-content:space-between;align-items:center;margin-top:32px;padding-top:18px;border-top:2px solid #eef1f7;font-size:19px;color:#5A5A60}}
.stopka b{{color:#12388C;font-weight:600}}
sub{{font-size:.62em;vertical-align:-.25em;line-height:0}}
"""

STOPKA = '<div class="stopka"><span>Pracownia Padir, Warszawa</span><b>grawerowanie-laserowe.pl</b></div>'

TAK_SVG = '<svg viewBox="0 0 40 40" width="36" height="36"><circle cx="20" cy="20" r="20" fill="#12388C"/><path d="M11 20.5l6 6 12-13" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
NIE_SVG = '<svg viewBox="0 0 40 40" width="36" height="36"><circle cx="20" cy="20" r="18" fill="#fff" stroke="#DE6B24" stroke-width="4"/><path d="M13.5 13.5l13 13M26.5 13.5l-13 13" stroke="#DE6B24" stroke-width="4" stroke-linecap="round"/></svg>'


def nbsp(t):
    """Jednoliterowe spójniki i przyimki nie zostają na końcu wiersza."""
    return re.sub(r"(?<![\w<])([aiouwzAIOUWZ]) ", r"\1&nbsp;", t)


def strona(css_dodatkowy, srodek):
    return (f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>{CSS}\n{css_dodatkowy}'
            f'</style></head><body><div class="ig">{srodek}{STOPKA}</div></body></html>')


def renderuj(pliki, zrodla):
    """pliki: {nazwa: funkcja zwracająca HTML}, w kolejności z artykułu. zrodla: katalog zrodla/ artykułu."""
    wyj = os.path.join(os.path.dirname(zrodla), "infografiki")
    os.makedirs(wyj, exist_ok=True)

    async def main():
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
            pg = await b.new_page(viewport={"width": SZER_CSS, "height": 800},
                                  device_scale_factor=SZER_PNG / SZER_CSS)
            for nazwa, f in pliki.items():
                html = os.path.join(zrodla, nazwa + ".html")
                with open(html, "w", encoding="utf-8") as h:
                    h.write(f())
                await pg.goto("file://" + html)
                await pg.evaluate("document.fonts.ready")
                fonty = await pg.evaluate("[...document.fonts].filter(f => f.status === 'loaded').length")
                png = os.path.join(wyj, nazwa + ".png")
                await pg.locator(".ig").screenshot(path=png)
                # płaskie kolory: paleta 128 barw zmniejsza plik o ok. 60% bez widocznej straty
                Image.open(png).quantize(colors=128, method=Image.Quantize.MEDIANCUT,
                                         dither=Image.Dither.NONE).save(png, optimize=True)
                im = Image.open(png)
                print(f"{nazwa}.png  {im.size[0]}x{im.size[1]}  {os.path.getsize(png) // 1024} KB  fontów: {fonty}")
                if fonty < 2:
                    raise SystemExit("fonty Poppins się nie wczytały, sprawdź ścieżkę " + FONTY)
            await b.close()

    asyncio.run(main())
