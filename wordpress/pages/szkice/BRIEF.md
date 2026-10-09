# Brief: szkice zakładek „Grawerowanie laserowe” i „Frezowanie CNC”

Katalog roboczy (dalej `S/`):
`/tmp/claude-0/-home-user-Padir/0b1fd493-c242-587c-b117-75001e9171f1/scratchpad/`

## Zadanie

Klient (Padir, pracownia obróbki laserowej i CNC w Warszawie, serwis
grawerowanie-laserowe.pl) przebudował zakładkę „Wycinanie laserowe”
(strona 1019, `/wycinanie-laserowe/`) według zatwierdzonego projektu.
Robimy w TYM SAMYM stylu dwie nowe zakładki:

- **grawerowanie**: „Grawerowanie laserowe”, zastąpi dziś stronę 456 `/grawerowanie-laserowe/`
- **frezowanie**: „Frezowanie CNC”, zastąpi dziś stronę 1011 `/frezowanie-cnc/`

To SZKICE do akceptacji z klientem. Trafią do WordPressa jako nieopublikowane
(robi to człowiek prowadzący, nie agenci). Po akceptacji treść zostanie
przeniesiona na istniejące strony, więc adresy URL się nie zmienią.

Spójność stylistyczna z dwiema stronami:
1. `/wycinanie-laserowe/` (1019): główny wzorzec, cały układ sekcji i komponentów.
2. `/przykladkowe-realizacje/` (1397): galeria realizacji, karty `.pdr-card`.

**Agenci NIE zapisują niczego do WordPressa.** Pracują tylko na plikach.

## Materiały źródłowe (tylko do odczytu)

| ścieżka | co to |
|---|---|
| `S/zrodla/1019-sekcje/` | wzorzec rozcięty na sekcje: `00-poczatek.html`, `00-arkusz.css.html`, `01-…html` do `12-kontakt.html`, `98-koniec.html`, `99-skrypt-lightbox.js.html`, `SPIS.json` |
| `S/zrodla/pages-1019-wycinanie-laserowe.raw.html` | wzorzec w całości (zapis bloków WordPressa) |
| `S/zrodla/pages-1397-przykladkowe-realizacje.raw.html` | strona realizacji (galeria `.pdr-*`) |
| `S/zrodla/pages-2530-wycinanie-laserowe-szkic.raw.html` | dawny szkic wycinania, wzór konwencji „wersja robocza” |
| `S/zrodla/pages-<id>-<slug>.raw.html` i `.txt` | WSZYSTKIE strony i wpisy serwisu: zapis bloków i czysty tekst |
| `S/zrodla/szablon-*.raw.html` / `.txt` | szablony, które niosą część treści obecnych stron 456 i 1011 |
| `S/zrodla/SPIS.json` | indeks stron i wpisów: id, slug, status, link, liczba słów |
| `S/zrodla/realizacje-karty.json` | 44 zatwierdzone realizacje z galerii: tytuł, materiał, kategoria (`eng` grawer, `cut` wycinanie, `cnc` frezowanie), zdjęcie, alt |
| `S/zrodla/media.json` | 289 obrazków z biblioteki mediów: id, slug, tytuł, alt, url, wymiary |

Narzędzia (uruchamiaj zawsze z `python3 -I`, z katalogu `S/`):

- `python3 -I kontaktowka.py WYNIK.png ID_LUB_URL [...]`, do 16 kafli na arkusz.
  Potem obejrzyj arkusz narzędziem Read. **Nie wolno podpisać zdjęcia, którego
  się nie widziało.** Nazwa pliku nie mówi, co jest na kadrze.
- `python3 -I sprawdz_szkic.py PLIK.html --szkic [--json]`: mechaniczna kontrola
  wszystkich pułapek z listy niżej. Kod 0 = czysto.

## Twarde reguły techniczne

Każda z nich już raz zepsuła produkcję albo prawie zepsuła.

1. **Tylko dywiz `-`.** Nigdy `—`, `–`, `−`. Także w zakresach: `60-200 W`.
   (Wzorzec 1019 ma 4 półpauzy w parku maszynowym, „60–200 W”. To błąd
   wzorca, NIE kopiować go.)
2. **Nigdy `&&`** w treści. WordPress zamienia to na encję i psuje skrypt.
3. **Inline style bez `border-width`, `border-color`, `border-*-color`,
   `border-*-width`** (na początku atrybutu albo po średniku). WordPress ma regułę
   zgodności, która wtedy maluje `solid` na WSZYSTKICH bokach. Tak nawias
   w hero wzorca zamienił się kiedyś w kwadrat. Zamiast tego skróty:
   `border-left: 7px solid #141414; border-bottom: 7px solid #141414;`
   (dopuszczalny jest też skrót `border: 1px solid #E8CE72`).
4. **Każdy `<h3>` ma inline `style` z `color: … !important`.** Motyw ma regułę
   `div div div h3{color:…base!important}`, która maluje je na biało.
5. **Każdy `<style>` ma `data-no-optimize="1" data-no-minify="1" data-no-ucss="1"`.**
   Bez tego LiteSpeed wciąga arkusz do pliku zbiorczego i UCSS wycina reguły.
6. **Zdjęcia w hero (`<header>`):** `loading="eager" fetchpriority="high" data-no-lazy="1"`.
   Pozostałe: `loading="lazy" decoding="async"`.
7. **Dokładnie jeden `<h1>`.** Całość w `<div class="pdw">`, arkusz zawężony do `.pdw`.
   Formularz dokładnie jak we wzorcu: `[contact-form-7 id="480"]`.
8. **Każde `href="#x"` ma `id="x"`** na stronie. Linki wewnętrzne tylko do
   OPUBLIKOWANYCH adresów z `SPIS.json`.
9. **Obrazki tylko z biblioteki serwisu** (`grawerowanie-laserowe.pl/wp-content/uploads/…`).
   Nigdy `blob:` ani `data:`.
10. **Znane błędne parametry, których nie wolno powtórzyć:** „do 400 W”,
    „1650 × 2510”. Trotec SP2000 to 2510 × 1680 mm i 180-500 W.
11. **Lightbox:** kafle galerii z `data-pdw-zoom` jak we wzorcu, skrypt
    `99-skrypt-lightbox.js.html` przeniesiony bez zmian.
12. **Kontrast:** szary tekst na jasnym tle min. 4,5:1. Bierz szarości z jasnych
    sekcji wzorca (są już poprawione), nie wprowadzaj jaśniejszych.

## Twarde reguły treści

1. **Zero zmyślonych faktów.** Każda liczba, maszyna, moc, pole robocze,
   tolerancja, termin, materiał, usługa, nazwa klienta musi mieć źródło
   w `S/zrodla/` (plik + dosłowny cytat). Jeśli źródła nie ma, to albo tego nie
   piszemy, albo stawiamy żółtą ramkę „Do potwierdzenia z klientem: …”
   (patrz konwencja szkicu). Lepiej mniej i prawdziwie.
2. **Nie przenosimy twierdzeń bez pokrycia z obecnych stron**, np. „grawer
   podnosi wartość prezentu nawet o 20%”, „klienci zapłacą o 20% więcej”.
3. **Zdjęcia, które nie są pracą Padiru, nie mogą udawać realizacji:**
   zdjęcia prasowe producentów (Trotec w studiu, Opt Lasers, stockowa frezarka),
   a na zdjęciu zamku Sułkowskich w Bielsku-Białej łuki z dzianiny na murze to
   cudza instalacja. Zdjęcie maszyny producenta wolno pokazać tylko jako
   zdjęcie maszyny, nie jako „nasza realizacja”.
4. **Klientów z nazwy** wymieniamy tylko, jeśli już są pokazani na stronach
   serwisu (realizacje, case study) i w tym samym kontekście.
5. Nie powielamy jeden do jednego tekstu z innych stron serwisu (kanibalizacja,
   duplikat treści). Fakty tak, zdania nie.

## Język (reguły „naturalna mowa”)

- Wyłącznie dywiz `-`. Zanim wstawisz dywiz zamiast pauzy, przebuduj zdanie:
  przecinek, kropka, dwukropek, nawias.
- Bez wypełniaczy: „W dzisiejszych czasach”, „Warto zauważyć”, „Należy pamiętać”,
  „Nie da się ukryć”, „Bez wątpienia”, „Podsumowując”, „kluczowa rola”,
  „kompleksowe”, „innowacyjne”, „najwyższej jakości”, „szeroki wachlarz”,
  „od A do Z”, „to nie tylko X, to Y”, „nie chodzi o X, chodzi o Y”.
- Różna długość zdań. Konkret zamiast ogólnika (materiał, wymiar, termin).
- Nie nadużywaj trójek („szybko, tanio i skutecznie”). Raz na tekst wystarczy.
- Rejestr jak na wzorcu 1019: rzeczowo, krótko, do klienta na „Ty”.
- Poprawna odmiana liczebników (np. „2 realizacje”, „5 realizacji”, „22 realizacje”).

## Konwencja szkicu do akceptacji

Wzór z `pages-2530-wycinanie-laserowe-szkic.raw.html`:

```html
<p class="pdw-uwaga" style="margin:0 0 26px;padding:13px 16px;border-radius:14px 4px 14px 14px;background:#FFF4CC;border:1px solid #E8CE72;font:600 13px/1.5 Poppins,sans-serif;color:#5A4708">Do potwierdzenia z klientem: …</p>
```

- Na samej górze wewnątrz `.pdw` jedna ramka: „Wersja robocza do akceptacji.
  Żółte ramki oznaczają miejsca do potwierdzenia przed publikacją.”
- Przy każdej informacji bez źródła, której nie da się pominąć (np. park maszyn
  CNC, jeśli serwis nie podaje modeli), ramka „Do potwierdzenia z klientem: …”
  z konkretnym pytaniem.
- Ramki NIE trafiają na produkcję; skrypt wdrożeniowy je odrzuci.
- `python3 -I sprawdz_szkic.py PLIK --szkic` musi kończyć się kodem 0.

## Pliki wynikowe

Każda strona ma swój katalog: `S/praca/grawerowanie/` i `S/praca/frezowanie/`.
Każdy agent pisze TYLKO do plików wskazanych w swoim zadaniu.
