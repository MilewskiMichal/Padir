#!/usr/bin/env python3
"""Popup „Zmieniamy halę!” w Popup Builderze Spectry (spectra-popup).

Widoczny do 16.10.2026 23:59 (Warszawa). Dwa zabezpieczenia konca:
  1. w tresci popupu skrypt, ktory od 17.10 00:00 (= 16.10 22:00 UTC)
     usuwa popup jeszcze przed skryptem Spectry, wiec znika tez ze stron
     zapamietanych w cache LiteSpeeda,
  2. po terminie popup wylaczamy w WordPressie (--wylacz).

Blok uagb/popup-builder zapisany dokladnie jak save() Spectry 2.20.5,
bez wbudowanej ikony zamkniecia (zamykaja przyciski w tresci z klasa
spectra-popup-close-<ID>, ktora obsluguje skrypt Spectry).

    python3 popup_hala.py              # proba na sucho: pokazuje tresc
    python3 popup_hala.py --wdroz      # zaklada albo aktualizuje i wlacza
    python3 popup_hala.py --wylacz     # wylacza (spectra-popup-enabled=false)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from wp import call

TYTUL = "Zmieniamy halę (do 16.10)"
BLOCK_ID = "a7c3e591"
STAN = os.path.join(HERE, "popup-id.json")
KONIEC_UTC = (2026, 9, 16, 22, 0, 0)  # Date.UTC: miesiac od zera -> 17.10 00:00 w Warszawie (CEST)

ATRYBUTY = {
    "block_id": BLOCK_ID, "className": "pdw-popup", "variationSelected": True, "variantType": "popup",
    "popupPositionH": "center", "popupPositionV": "center",
    "popupWidth": 540, "popupWidthMobile": 92, "popupWidthUnitMobile": "%",
    "popupHeight": 90, "popupHeightUnit": "vh", "hasFixedHeight": False,
    "closeIcon": "",
    "backgroundType": "color", "backgroundColor": "#ffffff",
    "popupOverlayColor": "rgba(20,20,20,0.6)",
    "popupPaddingTop": 40, "popupPaddingRight": 40, "popupPaddingBottom": 36, "popupPaddingLeft": 40,
    "popupPaddingTopMobile": 30, "popupPaddingRightMobile": 24, "popupPaddingBottomMobile": 28, "popupPaddingLeftMobile": 24,
    "contentBorderStyle": "none",
    "contentBorderTopLeftRadius": 30, "contentBorderTopRightRadius": 8,
    "contentBorderBottomLeftRadius": 30, "contentBorderBottomRightRadius": 30,
}


def tresc_html(popup_id):
    # Wlasny arkusz i skrypt: LiteSpeed serwuje tu tylko wczesniej policzony
    # UCSS (bez stylow popupu) i opoznia skrypty do pierwszej interakcji,
    # wiec popup Spectry pokazalby sie jako goly tekst nad naglowkiem.
    # Skrypt zdejmuje klase uagb-block-<id>, zeby opozniony skrypt Spectry
    # nie znalazl popupu i nie dublowal obslugi.
    return f'''<style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">
.pdw-popup.uagb-popup-builder{{display:none!important}}
.pdw-popup.uagb-popup-builder.pdw-popup--otwarty{{display:flex!important;opacity:1!important;position:fixed!important;top:0;left:0;width:100vw;height:100vh;max-width:100vw;max-height:100vh;z-index:999999999;align-items:center;justify-content:center;padding:16px;box-sizing:border-box;background:rgba(20,20,20,.6);overflow:hidden;animation:pdwPopupWejscie .25s ease}}
.pdw-popup .uagb-popup-builder__wrapper{{position:relative;box-sizing:border-box;width:540px;max-width:100%;max-height:calc(100vh - 32px);display:flex}}
.pdw-popup .uagb-popup-builder__container{{display:flex;flex-direction:column;box-sizing:border-box;width:100%;overflow-y:auto;background:#ffffff;border-radius:30px 8px 30px 30px;padding:40px 40px 36px;box-shadow:0 30px 60px -30px rgba(0,0,0,.45)}}
.pdw-popup .pdw-popup-x:hover,.pdw-popup .pdw-popup-x:focus-visible{{color:#12388C}}
.pdw-popup .pdw-popup-ok:hover,.pdw-popup .pdw-popup-ok:focus-visible{{background:#0d2a6b}}
@media (max-width:600px){{.pdw-popup .uagb-popup-builder__container{{padding:30px 24px 28px}}}}
@keyframes pdwPopupWejscie{{from{{opacity:0}}to{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.pdw-popup.uagb-popup-builder.pdw-popup--otwarty{{animation:none}}}}
.pdw-popup.uagb-popup-builder:focus{{outline:none}}
body.pdw-popup-blokada{{overflow:hidden}}
</style>
<div style="position:relative;font-family:Poppins,sans-serif;color:#141414;text-align:left">
<button type="button" class="pdw-popup-x" data-pdw-zamknij="x" aria-label="Zamknij komunikat" style="position:absolute;top:-20px;right:-16px;width:44px;height:44px;padding:0;border:0;background:transparent;font:300 32px/1 Poppins,sans-serif;color:#5f5f5f;cursor:pointer">×</button>
<span style="display:inline-block;font:600 12px/1 Poppins,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#12388C;margin:0 0 14px">Komunikat</span>
<h2 id="pdw-popup-tytul" style="font:800 30px/1.15 Poppins,sans-serif;letter-spacing:-.01em;margin:0 0 14px;color:#141414 !important">Zmieniamy halę!</h2>
<p style="font:300 16px/1.65 Poppins,sans-serif;color:#4e4b66;margin:0 0 18px">W dniach 15-16.10 przenosimy się do nowej hali pod tym samym adresem. Kontakt z nami może być w tych dniach utrudniony.</p>
<p style="font:600 16px/1.5 Poppins,sans-serif;color:#12388C;margin:0 0 26px;padding:14px 18px;border-radius:16px 4px 16px 16px;background:#EEF2FA">Od 19.10 zapraszamy do Hali D (wjazd T1)!</p>
<button type="button" class="pdw-popup-ok" data-pdw-zamknij="glowny" style="display:inline-block;align-self:flex-start;padding:15px 28px;border:0;border-radius:12px 4px 12px 12px;background:#12388C;color:#ffffff;font:700 15px/1 Poppins,sans-serif;cursor:pointer">Rozumiem</button>
</div>
<script data-no-optimize="1" data-no-defer="1" data-cfasync="false">(function(){{
var s=document.currentScript;if(!s){{return;}}
var p=s.closest(".uagb-popup-builder");if(!p){{return;}}
var KLUCZ="padirHala2026",zamkniety=false;
try{{zamkniety=localStorage.getItem(KLUCZ)==="1";}}catch(e){{}}
if(Date.now()>=Date.UTC({",".join(map(str, KONIEC_UTC))})||zamkniety){{p.remove();return;}}
p.classList.remove("uagb-block-{BLOCK_ID}");
p.setAttribute("role","dialog");p.setAttribute("aria-modal","true");p.setAttribute("aria-labelledby","pdw-popup-tytul");
function klawisz(e){{if(e.key==="Escape"){{zamknij();}}}}
function zamknij(){{try{{localStorage.setItem(KLUCZ,"1");}}catch(e){{}}p.remove();document.body.classList.remove("pdw-popup-blokada");document.removeEventListener("keydown",klawisz);}}
p.addEventListener("click",function(e){{if(e.target===p||e.target.closest("[data-pdw-zamknij]")){{zamknij();}}}});
document.addEventListener("keydown",klawisz);
p.classList.add("pdw-popup--otwarty");document.body.classList.add("pdw-popup-blokada");
p.setAttribute("tabindex","-1");try{{p.focus({{preventScroll:true}});}}catch(e){{}}
}})();</script>'''


def blok(popup_id):
    wnetrze = "<!-- wp:html -->\n" + tresc_html(popup_id) + "\n<!-- /wp:html -->"
    return (f"<!-- wp:uagb/popup-builder {json.dumps(ATRYBUTY, ensure_ascii=False, separators=(',', ':'))} -->\n"
            f'<div class="wp-block-uagb-popup-builder pdw-popup uagb-block-{BLOCK_ID} uagb-popup-builder">'
            f'<div class="uagb-popup-builder__wrapper uagb-popup-builder__wrapper--popup">'
            f'<div class="uagb-popup-builder__container uagb-popup-builder__container--popup">'
            f"{wnetrze}</div></div></div>\n<!-- /wp:uagb/popup-builder -->")


def main():
    if "--wylacz" in sys.argv:
        pid = json.load(open(STAN))["id"]
        st, r = call("POST", f"/wp/v2/spectra-popup/{pid}", body={"meta": {"spectra-popup-enabled": False}})
        print("wyłączenie:", st, r.get("meta") if isinstance(r, dict) else r)
        return
    if "--wdroz" not in sys.argv:
        print(blok("ID"))
        print("\n(PRÓBA NA SUCHO)")
        return
    if os.path.exists(STAN):
        pid = json.load(open(STAN))["id"]
    else:
        st, r = call("POST", "/wp/v2/spectra-popup", body={"title": TYTUL, "status": "draft", "content": blok("ID")})
        if st not in (200, 201):
            sys.exit(f"nie założono popupu: {st} {json.dumps(r, ensure_ascii=False)[:300]}")
        pid = r["id"]
        json.dump({"id": pid}, open(STAN, "w"))
        print("założono szkic popupu:", pid)
    st, r = call("POST", f"/wp/v2/spectra-popup/{pid}", body={
        "title": TYTUL, "status": "publish", "content": blok(pid),
        "meta": {"spectra-popup-type": "popup", "spectra-popup-enabled": True, "spectra-popup-repetition": 1}})
    print("publikacja:", st, r.get("status") if isinstance(r, dict) else r, r.get("meta") if isinstance(r, dict) else "")
    if st != 200:
        sys.exit(json.dumps(r, ensure_ascii=False)[:400])


if __name__ == "__main__":
    main()
