#!/usr/bin/env python3
"""Sklada kontaktowke z miniatur, zeby zobaczyc, co naprawde jest na zdjeciu.

Opisu zdjecia nie wolno zgadywac z nazwy pliku. `img_8312` nie mowi nic
o tym, czy to kubek, swieczka czy skrzynka, a jedno zdjecie z tej
biblioteki (zamek w Bielsku-Bialej) pokazuje tez instalacje, ktora NIE jest
praca Padiru. Dlatego najpierw kontaktowka, potem podpis.

    python3 -I kontaktowka.py WYNIK.png ID [ID ...]
    python3 -I kontaktowka.py WYNIK.png https://.../plik.jpg [...]

Argumenty to identyfikatory z `zrodla/media.json` albo pelne adresy URL.
Pod kazdym kafelkiem jest numer (id albo kolejny numer) i nazwa pliku.
Najwyzej 16 kafli na arkusz, zeby dalo sie je przeczytac.
"""
import io
import json
import os
import sys
import time
import urllib.request

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
KOLUMNY, KAFEL, PODPIS = 4, 320, 30
OP = urllib.request.build_opener(urllib.request.ProxyHandler(
    {"https": os.environ.get("HTTPS_PROXY")} if os.environ.get("HTTPS_PROXY") else {}))
POD = os.path.join(HERE, "pamiec-zdjec")
os.makedirs(POD, exist_ok=True)


def pobierz(u):
    nazwa = os.path.join(POD, str(abs(hash(u))) + os.path.splitext(u)[1][:5])
    if os.path.exists(nazwa):
        return open(nazwa, "rb").read()
    for p in range(4):
        try:
            d = OP.open(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}),
                        timeout=70).read()
            open(nazwa, "wb").write(d)
            return d
        except Exception:
            time.sleep(2 ** p)
    return None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    wynik, pozycje = sys.argv[1], sys.argv[2:18]
    baza = {}
    try:
        for x in json.load(open(os.path.join(HERE, "zrodla", "media.json"), encoding="utf-8")):
            baza[str(x["id"])] = x
    except Exception:
        pass
    wiersze = (len(pozycje) + KOLUMNY - 1) // KOLUMNY
    plansza = Image.new("RGB", (KOLUMNY * KAFEL, wiersze * (KAFEL + PODPIS)), "white")
    rys = ImageDraw.Draw(plansza)
    for i, poz in enumerate(pozycje):
        x0, y0 = (i % KOLUMNY) * KAFEL, (i // KOLUMNY) * (KAFEL + PODPIS)
        if poz in baza:
            m = baza[poz]
            u = m.get("url_medium") or m["url"]
            etykieta = f"{poz}  {m['slug'][:30]}"
        else:
            u = poz
            etykieta = f"#{i + 1}  {os.path.basename(poz)[:30]}"
        d = pobierz(u)
        if not d:
            rys.text((x0 + 6, y0 + 6), "nie pobrano", fill="red")
        else:
            try:
                im = Image.open(io.BytesIO(d)).convert("RGB")
                im.thumbnail((KAFEL - 8, KAFEL - 8))
                plansza.paste(im, (x0 + (KAFEL - im.width) // 2, y0 + (KAFEL - im.height) // 2))
            except Exception as e:
                rys.text((x0 + 6, y0 + 6), f"błąd: {e}"[:40], fill="red")
        rys.rectangle([x0, y0, x0 + KAFEL - 1, y0 + KAFEL + PODPIS - 1], outline="#cccccc")
        rys.text((x0 + 6, y0 + KAFEL + 8), etykieta, fill="black")
    plansza.save(wynik)
    print(wynik, plansza.size, len(pozycje), "kafli")


if __name__ == "__main__":
    main()
