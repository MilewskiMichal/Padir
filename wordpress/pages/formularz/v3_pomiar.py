import json, os, sys
from playwright.sync_api import sync_playwright
PLIK = os.path.abspath(sys.argv[1])
JS_STAN = r"""(stan) => {
 const f = document.querySelector('.pdw .wpcf7-form');
 const out = f.parentElement.querySelector('.wpcf7-response-output') || f.querySelector('.wpcf7-response-output');
 f.classList.remove('init'); f.classList.add(stan);
 if (stan === 'invalid') {
   for (const n of ['your-name','your-email','tel-394','policy']) {
     const w = f.querySelector(`[data-name="${n}"]`);
     const s = document.createElement('span'); s.className = 'wpcf7-not-valid-tip'; s.setAttribute('aria-hidden','true');
     s.textContent = n === 'your-email' ? 'Wprowadzony adres e-mail jest nieprawidłowy.' : 'Wypełnij to pole.'; w.appendChild(s);
   }
   out.textContent = 'Jedno lub więcej pól zawiera błędy. Sprawdź je i spróbuj ponownie.';
 }
 if (stan === 'sent') out.textContent = 'Dziękujemy za wiadomość. Odpowiemy najszybciej, jak to możliwe.';
 // pulapka WP Armour, dokladnie jak dopisuje ja wtyczka
 f.insertAdjacentHTML('beforeend', "<div id='altEmail_container' class='altEmail_container'><label for='alt_s'>Alternative:</label><input type='text' id='alt_s' name='alt_s' ></div>");
}"""
JS_POMIAR = r"""() => {
 const f = document.querySelector('.pdw .wpcf7');
 let k = f.parentElement; while (k && !/^rgb\(/.test(getComputedStyle(k).backgroundColor)) k = k.parentElement;
 const R = parseFloat(getComputedStyle(k).borderBottomRightRadius);
 const kb = k.getBoundingClientRect();
 const luz = el => { const b = el.getBoundingClientRect(); if (!b.width) return null;
   const cx = kb.right - R, cy = kb.bottom - R;
   if (b.right <= cx || b.bottom <= cy) return Math.round(Math.min(kb.right - b.right, kb.bottom - b.bottom) * 10) / 10;
   return Math.round((R - Math.hypot(b.right - cx, b.bottom - cy)) * 10) / 10; };
 const out = document.querySelector('.pdw .wpcf7-response-output');
 const btn = document.querySelector('.pdw .form-btn');
 const p = f.querySelector('.wpcf7-form>p');
 const e = f.querySelector('input[type=email]'), t = f.querySelector('input[type=tel]');
 const tipZgoda = f.querySelector('[data-name=policy] .wpcf7-not-valid-tip');
 const zgoda = f.querySelector('.form-policy');
 const ta = f.querySelector('textarea'), etTa = [...f.querySelectorAll('.form-label')][3];
 const alt = document.getElementById('alt_s');
 alt && alt.focus();
 return { karta_h: Math.round(kb.height), siatka: getComputedStyle(p).display, email_w: Math.round(e.getBoundingClientRect().width),
   tel_w: Math.round(t.getBoundingClientRect().width), luz_ramki: out ? luz(out) : null, luz_przycisku: luz(btn),
   w_bok: document.documentElement.scrollWidth - innerWidth,
   zgoda_tip: tipZgoda ? {nad_przyciskiem: Math.round(btn.getBoundingClientRect().top - tipZgoda.getBoundingClientRect().bottom),
                          pod_zgoda: Math.round(tipZgoda.getBoundingClientRect().top - zgoda.getBoundingClientRect().bottom),
                          lewo: Math.round(tipZgoda.getBoundingClientRect().left - zgoda.getBoundingClientRect().left)} : null,
   etykieta_tresc_odstep: Math.round(ta.getBoundingClientRect().top - etTa.getBoundingClientRect().bottom),
   pulapka: alt ? {widoczna: getComputedStyle(alt).visibility, fokus_na_niej: document.activeElement === alt, w_danych: new FormData(alt.form).has('alt_s')} : null,
   tip_wys_linii: (f.querySelector('[data-name=your-email] .wpcf7-not-valid-tip') || {}).offsetHeight || null };
}"""
wyn = {}
with sync_playwright() as pw:
    br = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    for w in (320, 360, 390, 414, 480, 576, 768, 1024, 1160, 1440):
        for stan in ("init", "invalid", "sent"):
            s = br.new_page(viewport={"width": w, "height": 900})
            s.goto("file://" + PLIK, wait_until="load", timeout=180000)
            if stan != "init":
                s.evaluate(JS_STAN, stan)
            s.wait_for_timeout(300)
            wyn[f"{w}-{stan}"] = s.evaluate(JS_POMIAR)
            if w in (390, 1440) and stan in ("invalid", "sent"):
                el = s.query_selector('.pdw .wpcf7'); y = s.evaluate("(e)=>e.getBoundingClientRect().top+scrollY", el)
                s.screenshot(path=f"formularz/v3-{os.path.basename(PLIK)[:4]}-{w}-{stan}.png", full_page=True,
                             clip={"x": 0, "y": max(0, y - 200), "width": w, "height": el.bounding_box()["height"] + 320})
            s.close()
    br.close()
json.dump(wyn, open(PLIK.replace(".html", "-v3pomiar.json"), "w"), indent=1, ensure_ascii=False)
for k, v in wyn.items():
    print(k, v)
