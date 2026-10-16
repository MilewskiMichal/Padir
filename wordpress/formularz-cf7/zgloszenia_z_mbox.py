#!/usr/bin/env python3
"""Zgloszenia z formularza kontaktowego wyciagniete z eksportu Gmaila (.mbox).

Eksport: Google Takeout -> Poczta -> tylko etykieta z tymi wiadomosciami
(albo cala poczta). Plik .mbox z Takeout ma naglowek X-Gmail-Labels,
wiec widac, czy wiadomosc byla w Odebranych, w Archiwum czy w Koszu.

    python3 -I zgloszenia_z_mbox.py EKSPORT.mbox WYNIK      # WYNIK.csv i WYNIK.xlsx

Bierzemy wiadomosci z tematem zawierajacym „FORMULARZ KONTAKTOWY” (dzisiejszy
temat to „FORMULARZ KONTAKTOWY | Ze strony www”). Ta sama wiadomosc moze
wystapic dwa razy (np. kopia w Koszu i w Archiwum), wiec duplikaty usuwamy
po Message-ID, a gdy go brak, po dacie i tresci.
"""
import csv
import mailbox
import re
import sys
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo

WARSZAWA = ZoneInfo("Europe/Warsaw")

TEMAT = re.compile(r"formularz\s+kontaktowy", re.I)


def naglowek(m, nazwa):
    w = m.get(nazwa)
    if w is None:
        return ""
    try:
        return str(make_header(decode_header(w)))
    except Exception:
        return str(w)


def tekst(m):
    if m.is_multipart():
        for czesc in m.walk():
            if czesc.get_content_type() == "text/plain":
                ladunek = czesc.get_payload(decode=True) or b""
                return ladunek.decode(czesc.get_content_charset() or "utf-8", "replace")
        for czesc in m.walk():
            if czesc.get_content_type() == "text/html":
                ladunek = czesc.get_payload(decode=True) or b""
                h = ladunek.decode(czesc.get_content_charset() or "utf-8", "replace")
                return re.sub(r"<[^>]+>", "\n", h)
        return ""
    ladunek = m.get_payload(decode=True) or b""
    return ladunek.decode(m.get_content_charset() or "utf-8", "replace")


def rozbierz(tresc):
    """Pola z szablonu maila CF7. Toleruje starsze wersje szablonu."""
    t = tresc.replace("\r\n", "\n")
    imie = re.search(r"^\s*(.+?)\s+uzupełnił/a formularz", t, re.M)
    email = re.search(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", t.split("Treść zapytania", 1)[0])
    tel = re.search(r"Dane kontaktowe to:\s*\n[^\n]*\n\s*([+0-9][0-9 ()+-]{5,})", t)
    zapyt = re.search(r"Treść zapytania:\s*\n(.*?)(?:\n\s*--\s*\n|\Z)", t, re.S)
    return {
        "imie_nazwisko": imie.group(1).strip() if imie else "",
        "email": email.group(0) if email else "",
        "telefon": tel.group(1).strip() if tel else "",
        "tresc": (zapyt.group(1).strip() if zapyt else t.strip())[:5000],
    }


def gdzie(etykiety):
    e = [x.strip() for x in etykiety.split(",") if x.strip()]
    if any(x.lower() in ("trash", "kosz") for x in e):
        return "Kosz"
    if any(x.lower() in ("spam",) for x in e):
        return "Spam"
    if any(x.lower() in ("inbox", "odebrane") for x in e):
        return "Odebrane"
    return "Archiwum" if e else ""


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    mb = mailbox.mbox(sys.argv[1])
    wiersze, widziane = [], {}
    for m in mb:
        temat = naglowek(m, "Subject")
        if not TEMAT.search(temat):
            continue
        tresc = tekst(m)
        klucz = naglowek(m, "Message-ID") or (naglowek(m, "Date") + tresc[:200])
        etykiety = naglowek(m, "X-Gmail-Labels")
        if klucz in widziane:
            # ta sama wiadomosc w drugim miejscu (np. Kosz i Archiwum): dopisz etykiety
            w = widziane[klucz]
            w["etykiety_gmail"] = ",".join(dict.fromkeys((w["etykiety_gmail"] + "," + etykiety).split(","))).strip(",")
            w["gdzie_w_gmailu"] = gdzie(w["etykiety_gmail"])
            continue
        try:
            data = parsedate_to_datetime(naglowek(m, "Date")).astimezone(WARSZAWA).strftime("%Y-%m-%d %H:%M")
        except Exception:
            data = naglowek(m, "Date")
        w = {"data": data, **rozbierz(tresc), "gdzie_w_gmailu": gdzie(etykiety),
             "etykiety_gmail": etykiety, "temat": temat}
        widziane[klucz] = w
        wiersze.append(w)
    wiersze.sort(key=lambda w: w["data"])
    pola = ["data", "imie_nazwisko", "email", "telefon", "tresc", "gdzie_w_gmailu", "etykiety_gmail", "temat"]
    with open(sys.argv[2] + ".csv", "w", encoding="utf-8-sig", newline="") as f:
        z = csv.DictWriter(f, fieldnames=pola, delimiter=";")
        z.writeheader()
        z.writerows(wiersze)
    try:
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Zgłoszenia"
        ws.append(pola)
        for w in wiersze:
            ws.append([w[p] for p in pola])
        ws.freeze_panes = "A2"
        for kol, szer in zip("ABCDEFGH", (17, 26, 30, 16, 80, 14, 30, 36)):
            ws.column_dimensions[kol].width = szer
        wb.save(sys.argv[2] + ".xlsx")
        pliki = f"{sys.argv[2]}.csv i {sys.argv[2]}.xlsx"
    except ImportError:
        pliki = f"{sys.argv[2]}.csv (bez .xlsx: brak modułu openpyxl)"
    print(f"zgłoszeń: {len(wiersze)}  ->  {pliki}")
    for g in ("Odebrane", "Archiwum", "Kosz", "Spam"):
        print(f"  {g}: {sum(1 for w in wiersze if w['gdzie_w_gmailu'] == g)}")


if __name__ == "__main__":
    main()
