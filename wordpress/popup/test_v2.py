import os, re, sys, hashlib, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from podglad_szkicu import pobierz, lokalizuj, MEDIA, wytnij_div
import popup_hala
from playwright.sync_api import sync_playwright
ZRODLO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "kontakt-surowy.html")
h = open(ZRODLO, encoding="utf-8").read()
blok = popup_hala.blok(2606)
render = re.sub(r"<!--\s*/?wp:[^>]*-->\n?", "", blok)          # do_blocks zostawia sam HTML
i = h.find('<div class="wp-block-uagb-popup-builder')
if i >= 0:
    a, b = wytnij_div(h, i); h = h[:a] + render + h[b:]
else:
    j = h.find(">", h.find("<body")) + 1; h = h[:j] + render + h[j:]
for u in sorted(set(re.findall(r'(?:src|data-src)=["\']((?:https:)?//grawerowanie-laserowe\.pl/[^"\']+\.js[^"\']*)', h))):
    pelny = "https:" + u if u.startswith("//") else u
    js = pobierz(pelny)
    if js is None: continue
    plik = os.path.join(MEDIA, hashlib.md5(pelny.encode()).hexdigest()[:12] + ".js")
    open(plik, "w", encoding="utf-8").write(js); h = h.replace(u, "file://" + plik)
h, _ = lokalizuj(h)
P = os.path.join(HERE, "test-v2.html"); open(P, "w", encoding="utf-8").write(h)
STAN = """() => { const p = document.querySelector('.pdw-popup'); if (!p) return {jest:false, blokada: document.body.classList.contains('pdw-popup-blokada')};
  const s = getComputedStyle(p), w = p.querySelector('.uagb-popup-builder__wrapper').getBoundingClientRect(), c = p.querySelector('.uagb-popup-builder__container');
  return {jest:true, display:s.display, opacity:s.opacity, pozycja:s.position, karta:[Math.round(w.left),Math.round(w.top),Math.round(w.width),Math.round(w.height)],
     tlo_karty:getComputedStyle(c).backgroundColor, w_bok: document.documentElement.scrollWidth - innerWidth, blokada: document.body.classList.contains('pdw-popup-blokada'),
     klasa_spectry: p.classList.contains('uagb-block-a7c3e591'), fokus: document.activeElement && document.activeElement.textContent.trim()}; }"""
wyn = {}
with sync_playwright() as pw:
    br = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    def nowa(w=1440, czas=None):
        ctx = br.new_context(viewport={"width": w, "height": 900})
        if czas: ctx.add_init_script(f"(() => {{ const t = {czas}; Date.now = () => t; }})();")
        s = ctx.new_page(); bledy = []
        s.on("pageerror", lambda e: bledy.append(str(e)[:150]))
        s.goto("file://" + P, wait_until="load", timeout=180000); s.wait_for_timeout(900)
        return ctx, s, bledy
    for w in (1440, 390, 360):
        ctx, s, bledy = nowa(w)
        wyn[f"{w} bez ruchu myszy"] = s.evaluate(STAN)
        s.screenshot(path=os.path.join(HERE, f"v2-{w}.png"))
        s.mouse.move(200, 200); s.mouse.move(400, 300); s.wait_for_timeout(2500)   # LiteSpeed odpala opoznione skrypty
        wyn[f"{w} po ruchu myszy (skrypty LiteSpeeda)"] = s.evaluate(STAN)
        s.click("[data-pdw-zamknij=glowny]"); s.wait_for_timeout(300)
        wyn[f"{w} po Rozumiem"] = s.evaluate(STAN)
        s.reload(wait_until="load"); s.wait_for_timeout(900)
        wyn[f"{w} po odświeżeniu"] = s.evaluate(STAN)
        wyn[f"{w} błędy JS"] = bledy; ctx.close()
    for nazwa, akcja in (("tło", lambda s: s.mouse.click(30, 450)), ("Esc", lambda s: s.keyboard.press("Escape")), ("krzyżyk", lambda s: s.click("[data-pdw-zamknij=x]"))):
        ctx, s, bledy = nowa(); akcja(s); s.wait_for_timeout(300); wyn["zamknięcie: " + nazwa] = s.evaluate(STAN); ctx.close()
    ctx, s, b_ = nowa(czas="Date.UTC(2026,9,16,21,59,30)"); wyn["16.10 23:59:30"] = s.evaluate(STAN)["jest"]; ctx.close()
    ctx, s, b_ = nowa(czas="Date.UTC(2026,9,16,22,0,1)"); wyn["17.10 00:00:01"] = s.evaluate(STAN); ctx.close()
    br.close()
for k, v in wyn.items(): print(k, "->", v)
