# Usługi dla marketingu: notatki składacza (13.10.2026)

Plik: `praca/marketing/strona.html` (277 linii, 31 077 znaków, 1147 słów widocznego tekstu, 21 zdjęć, 1 × h1).
Źródła: `tresc.md` (treść), `wzorzec-pdl.md` (komponenty, dopisek), markup i arkusz z `zrodla/pages-2283-uslugi-dla-horeca.raw.html`
(arkusz identyczny z 2264), JSON-LD wg 2264.

## Kontrola

| co | wynik |
|---|---|
| `python3 -I sprawdz_szkic.py praca/marketing/strona.html --pdl` | kod 0, błędy 0, ostrzeżenia 0 (także `--styl-tekstu`) |
| to samo z `--pdl --szkic` (tak wywołuje `szkic_wdroz.py marketing`) | kod 0 |
| linie 1-148 vs 2283 (opakowanie + arkusz) | `diff` pusty: arkusz skopiowany znak w znak, dopisek `wzorzec-pdl-dopisek.css` doklejony przed `</style>` |
| widoczny tekst vs `tresc.md` | 105 z 105 wierszy `> ` występuje dosłownie; alt 21/21 zgodne; kolejność zdjęć zgodna; każde zdjęcie raz |
| linki | 10 adresów wewnętrznych, wszystkie `publish` w `SPIS.json`; kotwice `#zakres`, `#nagrody`, `#event`, `#upominki` mają swoje `id`; `id="galeria"` jest na 1397 |
| klasy | każda klasa z treści zdefiniowana w arkuszu |
| JSON-LD | `json.loads` przechodzi, `Service` z 5 pozycjami katalogu, bez `&&` |
| render 1440 i 390 (`wzorzec-podglad.py`, rama `marketing/zywa-horeca.html`) | przewijanie w bok 0 / 0, niewczytanych zdjęć 0, par poniżej progu kontrastu 0; wysokość 7964 / 13 949 px |

Zrzuty: `sklad-1440.png`, `sklad-390.png`, sekcje `sklad-1440-s00…s08.png`, `sklad-390-s00…s08.png`; pomiar `sklad-pomiar.json`;
złożona strona w ramie `sklad.html`. Obejrzałem wszystkie zrzuty sekcji w obu szerokościach.

## Meta (nie ma ich w `strona.html`, wpisuje człowiek prowadzący)

| pole | wartość |
|---|---|
| tytuł w WordPressie i nazwa w menu „Produkty” | `Usługi dla marketingu` (za „Usługi dla HoReCa”; `szkic_wdroz.py` daje roboczo „Usługi dla marketingu (szkic do akceptacji)”) |
| slug | `uslugi-dla-marketingu` |
| szablon | `page-no-title` |
| title SEO (53 zn., ręcznie w polu SEO) | `Statuetki, puchary i upominki z logo dla firm \| Padir` |
| meta description (144 zn.) | `Statuetki i nagrody z plexi, puchary, upominki z logo, napisy przestrzenne i dekoracje na event dla marek i agencji. Od 1 sztuki, wycena w 24 h.` |

## Komponenty per sekcja

Naprzemienność teł jak u sióstr: hero bez tła, potem wash / białe na przemian, 7 sekcji między hero a pasem (nieparzyście),
pierwsza i przedostatnia wash, pas w białej. Zmierzone w przeglądarce: tła sekcji `rgb(245,245,245)` i przezroczyste na zmianę.

| s | znacznik | tło | komponent | wzorzec u sióstr | wys. 1440 |
|---|---|---|---|---|---|
| s00 | `section.pdl-hero` | białe | K1: eyebrow, h1 z `<br>`, lead, tekst, 2 przyciski (`/kontakt/`, `#zakres`), 3 × `li.pdl-stat`, 2 zdjęcia 3:4 eager | s00 obu sióstr | 640 |
| s01 | `section.pdl-sec.pdl-sec--wash` | wash | K2 + K3: 3 × `article.pdl-card`, linki `#upominki`, `#event`, `#nagrody` | s01 obu | 897 |
| s02 | `section.pdl-sec#zakres` | białe | K2 + K4: 5 × `article.pdl-p` + `pdl-p--cta` do `/kontakt/` | s02 obu | 1047 |
| s03 | `section.pdl-sec.pdl-sec--wash#nagrody` | wash | K7 `pdl-detail--rev` (zdjęcie z lewej), 3 × ptaszek, przycisk `/kontakt/` | s05 obu | 620 |
| s04 | `section.pdl-sec#event` | białe | K7 zwykły (zdjęcie z prawej), 3 × ptaszek (jeden z linkiem do case study), przycisk `/kontakt/` | s04 obu | 669 |
| s05 | `section.pdl-sec.pdl-sec--wash#upominki` | wash | K2 + K8: 6 × `article.pdl-mat` (rząd 4 + 2 jak u sióstr) | s06 obu | 1213 |
| s06 | `section.pdl-sec` | białe | K2 + K9: 8 zdjęć 1:1 (5 + 3; na telefonie 2 kolumny) + ghost „Zobacz wszystkie realizacje” | s07 obu | 935 |
| s07 | `section.pdl-sec.pdl-sec--wash` | wash | K2 + K11: 7 × `details.pdl-q`, domyślnie zamknięte | s09 obu | 889 |
| s08 | `section.pdl-sec` + `div.pdl-band` | białe | K12: h2, tekst, przyciski `/kontakt/` (biały) i `/przykladkowe-realizacje/` (ghost) | s10 obu | 398 |
| po grupie | drugi `wp:html` | - | K14 JSON-LD `Service` (wartości z `tresc.md`, K14) | tylko 2264 | - |

Pominięte komponenty sióstr (decyzja autora treści, `tresc.md` p. 0): K5 przed/po (brak pary zdjęć, W01), K6 kroki
(dublowałyby szkic grawerowania), K10 branże z chipami (trzy grupy odbiorców niesie K3).

## Odstępstwa od sióstr i powód

1. **Hero ładuje się od razu** (U1): oba zdjęcia `loading="eager" fetchpriority="high" decoding="async" data-no-lazy="1"`; u sióstr `lazy`.
2. **Kotwice mają cele** (U2, U12): `id` na sekcjach `zakres`, `nagrody`, `event`, `upominki`; każda karta K3 prowadzi gdzie indziej. U sióstr martwe `#produkty` / `#uslugi`.
3. **Dopisek do arkusza** (U4-U9), arkusz sióstr bez zmian, dopisek na końcu, zawężony do `.pdl`:
   część A `--pdl-grey:#6b6b76`, `--pdl-rust:#B55119` (kontrast: podpisy liczb w hero 5,26:1 zamiast 2,78:1);
   część B1 odstępy w hero i K7, B2 rozmiar linku w karcie CTA (15,5 px zamiast 24 px), B3 galeria 2 kolumny na telefonie.
4. **Przycisk pod galerią** (U10): ghost „Zobacz wszystkie realizacje” do `/przykladkowe-realizacje/#galeria`, `style="margin-top:32px"` jak pod krokami u sióstr.
5. **`<h3 class="pdl-h4">` zamiast `<h4>`** w kartach K8 (U11): bez przeskoku h2 → h4, wygląd bez zmian.
6. **Kolejność K7 odwrócona względem sióstr**: najpierw `--rev` na wash (s03), potem zwykły na białym (s04), bo tak wypada
   z mapy teł w `tresc.md` (nagrody przed eventem). Na desktopie zygzak zdjęć zostaje (lewo, prawo).
7. **Miniatury `-768x…`** w K3, K8, K9 i w drugim zdjęciu hero (U17); pełne pliki tylko tam, gdzie `tresc.md` tak każe
   (INSOFT 2340 i plakieta 2354, bo `url_medium` ma 225-226 px szerokości; 2332 i 2516 w K7).
8. **Linki w środku tekstu** (`<a>` w `.pdl-txt`, `.pdl-txt-sm`, `li`): siostry ich nie mają (poza kartą CTA), tu są z planu linkowania (`linki.md`, 9 kontekstowych). Kolor i podkreślenie z `.pdl a` i motywu, kontrast granatu 10,66:1 / 9,78:1.
9. **Twarde spacje między liczbą a jednostką**: `100&nbsp;zł` (podpis w hero), `2&nbsp;dni` (FAQ), `24&nbsp;godzin` (pas).
   Na pierwszym renderze „24” zostawało na końcu wiersza, a „godzin” spadało do następnego (1440 i 390). Tekst bez zmian.
10. **JSON-LD bez `availableChannel`, `mainEntityOfPage` i `image`** (2264 je ma): zostałem przy propozycji z `tresc.md`;
    `image` wskazuje na `#primaryimage` z Yoasta, którego nowa strona może nie mieć, dopóki nie dostanie obrazka wyróżniającego.
11. **Martwe reguły w arkuszu**: K5 (`.pdl-ba`, `.pdl-tag`), K6 (`.pdl-steps`) i K10 (`.pdl-branze`, `.pdl-chip`) nie mają tu znaczników.
    Zostawione celowo: arkusz ma być znak w znak jak u sióstr, żeby dało się go porównać `diff`em i podmienić hurtem.

Świadomie NIE zmieniałem (jak u sióstr):
- U15: na telefonie w K7 `--rev` zdjęcie stoi nad tekstem, w zwykłym pod tekstem (s03 i s04 sąsiadują, więc widać to od razu).
  Poprawka z wzorca (`@media (max-width:779px){.pdl-detail .pdl-detail-media{order:-1;}}`) jest opcjonalna; do decyzji, czy wprowadzić ją na wszystkich trzech stronach naraz.
- U16: karta K3 unosi się na hover; U19: ramka ghost 1,41:1.
- Na 390 px trzy kafelki liczb w hero układają się 1 + 1 + 1 (u sióstr 1 + 2), bo podpis „minimum 100 zł za zlecenie” jest szerszy. Nic się nie ucina; hero ma 1215 px wysokości.

## Do wiadomości prowadzącego (bez zmian w treści, pytania już są w `pytania.md`)

- s03, zdjęcie 2332: na tabliczce czytelne imiona i nazwisko osób prywatnych (P31). To samo zdjęcie stoi już na `/wycinanie-laserowe/`.
- s01, karta 3, zdjęcie 2322: rozpoznawalna osoba na ściance Bondi Sands (P32).
- s04, zdjęcie 2516 w kadrze 4:3 ze środka: obejrzany pełny plik, u dołu tylko krawędź ceglanego muru, cudzej instalacji z dzianiny nie widać.
- Nowych twierdzeń nie dodawałem i żadnego nie usuwałem, więc nowych pytań do `pytania.md` nie dopisałem.
- Linki do `/uslugi-dla-marketingu/` z innych stron (np. trzecia branża w „Branże, w których grawerujemy” na grawerowaniu) dopiero po publikacji tej strony (`wzorzec-pdl.md`, p. 5.10).
