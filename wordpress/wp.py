#!/usr/bin/env python3
"""Cienka warstwa na REST API WordPressa.

Poswiadczenia siedza w `wp.creds.json` obok tego pliku, z uprawnieniami 600.
Nigdy nie trafiaja do argumentow polecenia ani na wyjscie, bo historia powloki
i logi to miejsca, z ktorych haslo sie juz nie da wycofac.

Kazde wywolanie ma ponawianie z rosnacym odstepem: proxy w tym srodowisku
potrafi zerwac polaczenie w polowie i pojedyncza proba klamie.
"""
import base64
import json
import os
import ssl
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PLIK = os.path.join(HERE, "wp.creds.json")
BAZA = "https://grawerowanie-laserowe.pl/wp-json"

with open(PLIK, encoding="utf-8") as f:
    _k = json.load(f)

_naglowek = "Basic " + base64.b64encode(
    f"{_k['user']}:{_k['app_password']}".encode()).decode()

_proxy = os.environ.get("HTTPS_PROXY")
_kontekst = ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt") \
    if os.path.exists("/root/.ccr/ca-bundle.crt") else None
_otwieracz = urllib.request.build_opener(
    urllib.request.ProxyHandler({"https": _proxy} if _proxy else {}),
    *( [urllib.request.HTTPSHandler(context=_kontekst)] if _kontekst else [] ))


def call(metoda, sciezka, body=None, prob=4):
    """Zwraca (kod_http, odpowiedz_jako_python)."""
    adres = BAZA + sciezka
    dane = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
    for p in range(prob):
        zapytanie = urllib.request.Request(adres, data=dane, method=metoda)
        zapytanie.add_header("Authorization", _naglowek)
        zapytanie.add_header("User-Agent", "Mozilla/5.0")
        if dane is not None:
            zapytanie.add_header("Content-Type", "application/json")
        try:
            with _otwieracz.open(zapytanie, timeout=90) as r:
                return r.status, json.loads(r.read().decode("utf-8", "replace") or "null")
        except urllib.error.HTTPError as e:
            tresc = e.read().decode("utf-8", "replace")
            if e.code in (429, 502, 503, 504) and p < prob - 1:
                time.sleep(2 ** p)
                continue
            try:
                return e.code, json.loads(tresc)
            except Exception:
                return e.code, tresc[:400]
        except Exception as e:
            if p < prob - 1:
                time.sleep(2 ** p)
                continue
            raise
    raise RuntimeError("nie udało się po " + str(prob) + " próbach")
