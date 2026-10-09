#!/usr/bin/env python3
"""Wierny podglad strony, takze NIEOPUBLIKOWANEJ, z prawdziwym motywem.

    python3 podglad_szkicu.py ID_STRONY PREFIKS [--szer 1440,390]

Szkicu nie da sie obejrzec z zewnatrz: haslo aplikacji uwierzytelnia tylko
REST API, nie przegladarke. Dlatego skladamy podglad sami:

  1. bierzemy `content.rendered` strony przez REST (WordPress juz rozwinal
     bloki i skroty, takze formularz Contact Form 7),
  2. bierzemy SERWOWANA strone /wycinanie-laserowe/ jako rame: naglowek,
     stopka, arkusze motywu i LiteSpeeda, dokladnie te, ktore dostaje gosc,
  3. podmieniamy w ramie kontener `.pdw` na kontener szkicu,
  4. sciagamy arkusze i zdjecia na dysk, bo proxy w tym srodowisku zrywa
     rownolegle polaczenia przegladarki i zdjecia by sie nie wczytaly.

Wynik: PREFIKS.html, PREFIKS-<szer>.png (cala strona) i PREFIKS-pomiar.json
z pomiarami: przewijanie w bok, zdjecia, ktore sie nie wczytaly (po
przewinieciu do konca, bo czesc jest leniwa), oraz kontrast kazdego tekstu
wzgledem pierwszego nieprzezroczystego tla.
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wp import call

RAMA = "https://grawerowanie-laserowe.pl/wycinanie-laserowe/"
OP = urllib.request.build_opener(urllib.request.ProxyHandler(
    {"https": os.environ.get("HTTPS_PROXY")} if os.environ.get("HTTPS_PROXY") else {}))
MEDIA = os.path.join(HERE, "podglad-media")
os.makedirs(MEDIA, exist_ok=True)


def pobierz(u, binarnie=False):
    for p in range(4):
        try:
            d = OP.open(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}),
                        timeout=70).read()
            return d if binarnie else d.decode("utf-8", "replace")
        except Exception:
            time.sleep(2 ** p)
    return None


def wytnij_div(h, poczatek):
    """Zwraca (start, koniec) diva zaczynajacego sie na pozycji `poczatek`."""
    glebokosc = 0
    for m in re.compile(r"<div\b|</div>").finditer(h, poczatek):
        if m.group(0) == "</div>":
            glebokosc -= 1
            if glebokosc == 0:
                return poczatek, m.end()
        else:
            glebokosc += 1
    raise ValueError("niedomknięty div")


def lokalizuj(h):
    # arkusze
    for m in list(re.finditer(r'<link[^>]+rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)', h)):
        u = m.group(1)
        pelny = "https:" + u if u.startswith("//") else (u if u.startswith("http") else
                                                          "https://grawerowanie-laserowe.pl" + u)
        css = pobierz(pelny)
        if css is None:
            continue
        nazwa = os.path.join(MEDIA, hashlib.md5(pelny.encode()).hexdigest()[:12] + ".css")
        open(nazwa, "w", encoding="utf-8").write(css)
        h = h.replace(u, "file://" + nazwa)
    # leniwe ladowanie LiteSpeeda: placeholder w src, prawdziwy adres w data-src
    h = re.sub(r'''src=["']data:image/svg\+xml;base64,[^"']+["']([^>]*?)\sdata-src=["']([^"']+)["']''',
               lambda m: 'src="' + m.group(2) + '"' + m.group(1), h)
    # zdjecia
    adresy = set(re.findall(
        r'https://grawerowanie-laserowe\.pl/wp-content/uploads/[^"\'\s)>]+\.(?:jpe?g|png|webp|gif|svg)', h, re.I))
    for u in sorted(adresy):
        nazwa = os.path.join(MEDIA, hashlib.md5(u.encode()).hexdigest()[:12] + os.path.splitext(u)[1])
        if not os.path.exists(nazwa):
            d = pobierz(u, binarnie=True)
            if d:
                open(nazwa, "wb").write(d)
        if os.path.exists(nazwa):
            h = h.replace(u, "file://" + nazwa)
    return h, len(adresy)


POMIAR_JS = r"""async () => {
  for (let y = 0; y < document.body.scrollHeight; y += 500) {
    window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60));
  }
  window.scrollTo(0, 0);
  await new Promise(r => setTimeout(r, 1200));
  const L = c => { const [r, g, b] = c.map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126*r + 0.7152*g + 0.0722*b; };
  const rgb = s => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(',').map(x => parseFloat(x)); return {c: p.slice(0,3), a: p.length > 3 ? p[3] : 1}; };
  const pdw = document.querySelector('.pdw');
  const zle = [], nadZdjeciem = [];
  if (pdw) pdw.querySelectorAll('*').forEach(el => {
    const tekst = [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
    if (!tekst) return;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || parseFloat(s.opacity) === 0) return;
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) return;
    // Tekst nalozony na zdjecie (podpisy kafli galerii): szukamy <img>
    // w obrebie najblizszego przodka, ktory zdjecie zawiera, i sprawdzamy,
    // czy prostokaty sie nakladaja. Takiego tekstu nie da sie zmierzyc
    // wzgledem koloru tla, wiec trafia na osobna liste do obejrzenia.
    let zdjecie = false;
    for (let a = el.parentElement, krok = 0; a && krok < 6; a = a.parentElement, krok++) {
      const img = [...a.querySelectorAll('img')].find(i => !el.contains(i) && !i.classList.contains('pdw-lb-img'));
      if (img) {
        const q = img.getBoundingClientRect();
        if (r.left < q.right && r.right > q.left && r.top < q.bottom && r.bottom > q.top) zdjecie = true;
        break;
      }
    }
    let e = el, tlo = null;
    while (e) {
      const cs = getComputedStyle(e);
      if (cs.backgroundImage && cs.backgroundImage !== 'none' && !cs.backgroundImage.includes('gradient')) zdjecie = true;
      const b = rgb(cs.backgroundColor);
      if (b && b.a > 0.9) { tlo = b.c; break; }
      e = e.parentElement;
    }
    if (zdjecie) { nadZdjeciem.push(tekst.slice(0, 50)); return; }
    if (!tlo) tlo = [255, 255, 255];
    const k = rgb(s.color); if (!k) return;
    const a = L(k.c), b = L(tlo);
    const wsp = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
    const px = parseFloat(s.fontSize), waga = parseInt(s.fontWeight) || 400;
    const duzy = px >= 24 || (px >= 18.66 && waga >= 700);
    const prog = duzy ? 3.0 : 4.5;
    if (wsp < prog) zle.push({wsp: Math.round(wsp * 100) / 100, prog, kolor: s.color, tlo: 'rgb(' + tlo.join(',') + ')', tekst: tekst.slice(0, 60), px});
  });
  const imgs = [...document.querySelectorAll('.pdw img')].filter(i => !i.classList.contains('pdw-lb-img'));
  return {
    przewijanie_w_bok: document.documentElement.scrollWidth - window.innerWidth,
    zdjec: imgs.length,
    niezaladowane: imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => (i.getAttribute('src') || '').split('/').pop()),
    zly_kontrast: zle,
    tekst_nad_zdjeciem: nadZdjeciem.slice(0, 10),
    h1: [...document.querySelectorAll('.pdw h1')].map(h => h.textContent.trim()),
    wysokosc: document.body.scrollHeight,
  };
}"""


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    ident, prefiks = int(sys.argv[1]), sys.argv[2]
    szer = [1440, 390]
    if "--szer" in sys.argv:
        szer = [int(x) for x in sys.argv[sys.argv.index("--szer") + 1].split(",")]

    st, p = call("GET", f"/wp/v2/pages/{ident}?context=edit&_fields=id,status,content")
    if st != 200:
        sys.exit(f"nie pobrano strony {ident}: HTTP {st}")
    szkic = p["content"]["rendered"]
    i = szkic.find('<div class="pdw"')
    if i < 0:
        sys.exit("w treści szkicu nie ma kontenera .pdw")
    a, b = wytnij_div(szkic, i)
    pdw_szkicu = szkic[a:b]
    # arkusz i skrypt leza obok kontenera, nie w nim: bierzemy cala tresc
    poza = szkic[:a] + szkic[b:]
    arkusze = "".join(re.findall(r"<style\b.*?</style>", poza, re.S))
    skrypty = "".join(re.findall(r"<script\b.*?</script>", poza, re.S))

    rama = pobierz(RAMA + "?odswiez=" + str(int(time.time())))
    j = rama.find('<div class="pdw"')
    if j < 0:
        sys.exit("w ramie nie ma kontenera .pdw")
    c, d = wytnij_div(rama, j)
    # usuwamy z ramy arkusze i skrypty wzorca, zeby nie mieszaly sie ze szkicem
    przed = re.sub(r'<style data-no-optimize="1"[^>]*>.*?</style>', "", rama[:c], flags=re.S)
    po = rama[d:]
    h = przed + arkusze + pdw_szkicu + skrypty + po
    h, ile = lokalizuj(h)
    sciezka = os.path.abspath(prefiks + ".html")
    open(sciezka, "w", encoding="utf-8").write(h)
    print(f"strona {ident} [{p['status']}] -> {sciezka}  ({ile} zdjęć zlokalizowanych)")

    from playwright.sync_api import sync_playwright
    pomiary = {}
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        for w in szer:
            s = br.new_page(viewport={"width": w, "height": 900})
            s.goto("file://" + sciezka, wait_until="load", timeout=180000)
            s.wait_for_timeout(1500)
            m = s.evaluate(POMIAR_JS)
            s.screenshot(path=f"{prefiks}-{w}.png", full_page=True)
            pomiary[w] = m
            print(f"  {w:>4} px: w bok {m['przewijanie_w_bok']}, zdjęć {m['zdjec']}, "
                  f"niewczytanych {len(m['niezaladowane'])}, zły kontrast {len(m['zly_kontrast'])}, "
                  f"wysokość {m['wysokosc']}")
            s.close()
        br.close()
    json.dump(pomiary, open(prefiks + "-pomiar.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
