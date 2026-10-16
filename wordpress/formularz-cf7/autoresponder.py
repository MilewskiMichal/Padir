#!/usr/bin/env python3
"""Automatyczna odpowiedz formularza kontaktowego (Contact Form 7, id 480, „Mail (2)”).

Do osoby, ktora wyslala formularz, idzie potwierdzenie. Celowo bez
powtorzenia tresci formularza i bez imienia: inaczej kazdy moglby wpisac
cudzy adres i rozsylac przez nasz serwer dowolny tekst.

    python3 autoresponder.py           # pokazuje, co zostanie ustawione
    python3 autoresponder.py --wdroz
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from wp import call

FORM = 480
TRESC = """Dzień dobry,

dziękujemy za wiadomość wysłaną przez formularz na stronie grawerowanie-laserowe.pl. Dotarła do nas. Odpowiemy najszybciej, jak to możliwe, zwykle w ciągu 24 godzin w dni robocze.

Jeśli chcesz coś dopisać, na przykład plik z logo albo zdjęcie przedmiotu, po prostu odpowiedz na tego maila.

W pilnej sprawie zadzwoń: +48 22 741 36 55 (poniedziałek-piątek, 8:30-16:00).

Pozdrawiamy
Zespół Padir
Grawerowanie i wycinanie laserowe, frezowanie CNC
ul. Matuszewska 14, 03-876 Warszawa
laser@padir.pl | grawerowanie-laserowe.pl

Ta wiadomość została wysłana automatycznie, bo ten adres e-mail podano w formularzu kontaktowym na stronie grawerowanie-laserowe.pl."""

MAIL_2 = {
    "active": True,
    "subject": "Dziękujemy za wiadomość | Padir",
    "sender": "Padir <form@grawerowanie-laserowe.pl>",
    "recipient": "[your-email]",
    "body": TRESC,
    "additional_headers": "Reply-To: laser@padir.pl",
    "attachments": "",
    "use_html": False,
    "exclude_blank": False,
}


def main():
    assert not any(c in TRESC + MAIL_2["subject"] for c in "–—−"), "pauza w treści"
    st, przed = call("GET", f"/contact-form-7/v1/contact-forms/{FORM}")
    if st != 200:
        sys.exit(f"nie pobrano formularza: {st}")
    if "--wdroz" not in sys.argv:
        print(json.dumps(MAIL_2, ensure_ascii=False, indent=1))
        print("\n(PRÓBA NA SUCHO)")
        return
    kopia = os.path.join(HERE, f"backup-cf7-{FORM}-przed-autoresponderem.json")
    if not os.path.exists(kopia):
        json.dump(przed, open(kopia, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    st2, r = call("POST", f"/contact-form-7/v1/contact-forms/{FORM}", body={"mail_2": MAIL_2, "context": "save"})  # bez context=save CF7 tylko waliduje
    print("zapis:", st2)
    st3, po = call("GET", f"/contact-form-7/v1/contact-forms/{FORM}")
    pp, pr = po["properties"], przed["properties"]
    for k in ("form", "mail", "messages", "additional_settings"):
        print(f"  {k} bez zmian:", pp.get(k) == pr.get(k))
    m2 = pp.get("mail_2", {})
    print("  mail_2 zgodny z zamierzonym:", all(m2.get(k) == v for k, v in MAIL_2.items()))
    print("  błędy konfiguracji:", json.dumps(po.get("config_errors"), ensure_ascii=False))


if __name__ == "__main__":
    main()
