# Notatki składu: Grawerowanie laserowe (szkic)

Plik: `praca/grawerowanie/strona.html`
Źródła składu: `praca/wzorzec.md` (K01-K17, arkusz dodatków z sekcji 6), `praca/grawerowanie/tresc.md`,
kod sekcji wzorca z `zrodla/1019-sekcje/*.html`.

Wynik kontroli: `python3 -I sprawdz_szkic.py praca/grawerowanie/strona.html --szkic`
kod 0, 0 błędów, 0 ostrzeżeń (po rundzie 2 poprawek: 80 499 zn., 1567 słów razem z ramkami, 32 zdjęcia, h1 = 1,
ramek `pdw-uwaga` = 7).

## Złożenie pliku

| kolejność | co | stan |
|---|---|---|
| 1 | `zrodla/1019-sekcje/00-poczatek.html` | bajt w bajt (sprawdzone porównaniem bajtów) |
| 2 | drugi `<style>` z dodatkami (wzorzec.md, sekcja 6) | 1:1 z katalogu |
| 3 | K01 ramka „Wersja robocza do akceptacji…” | pierwsza rzecz po arkuszach, przed `<header>` |
| 4 | `<header>` + 11 sekcji | patrz tabela niżej |
| 5 | `zrodla/1019-sekcje/98-koniec.html` | bajt w bajt, w nim warstwa `.pdw-lb` i skrypt lightboxa (jedna kopia, bez doklejania `99-skrypt-lightbox.js.html`) |

Całość w jednym bloku `wp:html` w grupie `alignfull`, jeden kontener `<div class="pdw">`, formularz `[contact-form-7 id="480"]`.

## Komponenty per sekcja

| # | sekcja | `id` | tło | padding | komponenty |
|---|---|---|---|---|---|
| 00 | ramka robocza | - | - | - | K01 (ramka górna) |
| 01 | hero | `<header>` | białe | `56px 0px 72px` | K02 (siatka 2x2, nawias L), K03 A (`#kontakt`), K03 B (`#proces`), K04 (`#portfolio`) |
| 02 | dlaczego | - | białe | `82px 0px` | K05 wyśrodkowany, K06 (czarna ◆ + szara ✓ + szara ★) |
| 03 | materiały | `materialy` | `#F5F5F5` | `82px 0px` | K05 do lewej, K07 (6 kart białych), K01 w karcie 6, akapit pod kartami |
| 04 | portfolio | `portfolio` | białe | `82px 0px` | K05, K09 (9 kart `#F5F5F5`, plakietka „Grawerowanie” `#12388C`), K03 A-mały do `/przykladkowe-realizacje/#galeria` |
| 05 | na czym polega | - | białe | `36px 0px 78px` | K10 |
| 06 | proces | `proces` | `#F5F5F5` | `78px 0px` | K05 do lewej, K11 (4 kroki, SVG 01-04 z `06-proces.html`) |
| 07 | realizacje | `realizacje` | `#F5F5F5` | `82px 0px` | K05 do lewej, K12 karta A, K03 A-mały do `/case-study-wosp/`, K12 ciemny pas CTA z K03 A-ciemny |
| 08 | zastosowania | - | białe | `82px 0px` | K05 do lewej, K07 w wariancie na białym (4 karty `#F5F5F5`) z linkiem tekstowym |
| 09 | technologia | `technologia` | białe | `82px 0px` | K14 (blok ciemny + 3 liczby + 5 kart maszyn), K01 w karcie „Laser fiber”, K01 pod siatką |
| 10 | zaufali | - | białe | `20px 0px 82px` | K15 (logotypy bez zmian), K01 pod leadem |
| 11 | faq | `faq` | `#F5F5F5` | `82px 0px` | K16 (5 pytań), 2 × K01 pod pudełkiem |
| 12 | kontakt | `kontakt` | białe | `82px 0px 92px` | K17 |

Kotwice: `#kontakt`, `#proces`, `#portfolio` mają swoje sekcje. Żadnego `href="#"`.
Linki wewnętrzne (10, wszystkie `publish` w `zrodla/SPIS.json`): dokładnie lista z `tresc.md`.

## Odstępstwa od wzorca 1019 i powody

### Cała strona

1. **Drugi arkusz (dodatki z wzorzec.md, sekcja 6).** Na 1019 go nie ma. Naprawia zepsute `@keyframes chevBounce`
   (usterka 5, strzałka w hero ruszy), daje efekt najechania kart K09 jak `.pdr-card:hover` na 1397 i wyłącza ruch przy
   `prefers-reduced-motion`. Arkusz 1019 nietknięty.
2. **Ramka K01 na górze i 6 ramek „Do potwierdzenia”.** Konwencja szkicu z BRIEF. Ramki stoją dokładnie tam, gdzie
   wskazuje `tresc.md` (tabela „Ramki do potwierdzenia”).
3. **Siatki `minmax(min(100%, N), 1fr)` zamiast `minmax(N, 1fr)`** we wszystkich siatkach `auto-fit` (hero 340, K06 260,
   K07 280, K10 300, K11 230, K12 340, K14 320 i 220, K17 320). POPRAWKA z katalogu (usterka 8: na 360 px treść wychodziła
   poza karty). Na desktopie wygląd bez zmian.
4. **`aria-hidden="true"`** na strzałce w hero, ikonach ◆ ✓ ★ i ilustracjach SVG kroków (usterka 18).
5. **Zakresy mocy z dywizem** (`25-120 W`, `60-120 W`, `180-500 W`). Wzorzec ma tu półpauzy (usterka 1).
6. **Rozmiary plików zdjęć.** Pliki do 1000 px (`padir-realizacja-*`) idą w pełnej wersji, jak na 1019. Dla zdjęć,
   których oryginał ma 2000-2560 px, `tresc.md` podaje wersję „lżejszą” 768 px:
   - w małych kartach (K07: 1009, 1614, 1622; K07 zastosowań: 2262, 1891, 1450) wstawiona jest wersja 768 px
     (karta ma ok. 380 px szerokości, 768 px to zapas na ekrany 2x; oryginały ważyłyby kilka razy więcej niż zdjęcia 1019);
   - w dużych slotach (K10: 1808, blok K14: 2279) i w case study (1738, 1737, 1740, `tresc.md` podaje tylko pełne pliki)
     stoi pełny plik, żeby lightbox pokazał ostre zdjęcie.
   Skutek: w lightboxie zdjęcia z małych kart mają 768 px (na 1019 ok. 1000 px). Jeśli klient woli ostrzejsze
   powiększenie, wystarczy podmienić `src` na adres z `tresc.md`.

### Sekcje

- **01 hero.** Struktura i style 1:1 z `01-wycinanie-laserowe.html`. Nawias L przeniesiony w wersji z produkcji 1019:
  `border-top: 0; border-right: 0; border-left: 11px solid …; border-bottom: 11px solid …;` (same skróty, bez
  `border-width` i `border-*-color`; katalog pomija `border-top: 0; border-right: 0`, ale zostawiłem je zgodnie
  z zadaniem i ze źródłem, są nieszkodliwe). h1 zapisem zdaniowym `Grawerowanie<br>laserowe` (usterka 14), szary
  początek podtytułu kończy się kropką (usterka 15). Zdjęcia `loading="eager" fetchpriority="high" data-no-lazy="1"`,
  wszystkie z `data-pdw-zoom`. Pod nawiasem kafel 3 (ściana), jak każe `tresc.md`.
- **02 dlaczego.** Dwa zwykłe linki w tekście karty 3 (`/wycinanie-laserowe/`, `/frezowanie-cnc/`), kolor z arkusza
  `.pdw a` (`#12388C` na `#F5F5F5`, 9,78:1). Na 1019 karty nie mają linków.
- **03 materiały.** Ramka K01 w karcie 6 ma `margin:0` zamiast `margin:0 0 26px`, bo jest ostatnim elementem
  w karcie z paddingiem 26 px (inaczej dół karty miałby 52 px pustego miejsca); odstęp od akapitu daje jego
  `margin-bottom: 14px`. Akapit pod kartami to nowy element (na 1019 go nie ma): styl podpisu z K14
  (`300 15px / 1.7`, `#6B6B6B`, na `#F5F5F5` 4,89:1), `margin: 34px 0px 0px` wg `tresc.md`, wyrównany do lewej jak nagłówek
  sekcji; dodane `max-width: 720px` z podpisu K14, żeby wiersz nie szedł na 1172 px.
- **04 portfolio.** Zamiast kafli K08 z 1019 karty K09 (hybryda `.pdr-card`, rekomendacja wzorzec.md, sekcja 5):
  tytuł h3, materiał, plakietka kategorii, `data-pdw-zoom`, `pointer-events: none` na plakietce. Bez arkusza `.pdr-*`
  i bez skryptu filtrów 1397. Dane 9 kart 1:1 z `zrodla/realizacje-karty.json` (`pelne`, `alt`, `tytul`, `material`,
  `plakietka`, sprawdzone skryptem). Lead bez sklejonych przecinkiem zdań (usterka 15).
- **05 na czym polega.** Bez zmian w kodzie K10 poza podmianą treści. Link do poradnika w akapicie 2.
- **06 proces.** Usunięte napisy `szkic` z rogów ilustracji (usterka 6) i lead o „zdjęciach, które opowiadają historię”.
  SVG 01-04 bez zmian (ikona 03 to wiązka lasera, pasuje do graweru).
- **07 realizacje.** Tylko karta A (brak drugiego opublikowanego case study z grawerem, `tresc.md`, „Pominięte sekcje”,
  punkt 2). Etykieta „Case study” w liczbie pojedynczej, bo jest jedna historia. Przycisk prowadzi do `/case-study-wosp/`
  zamiast martwego `href="#"` (usterka 7), napis „Cała historia ramek” (runda 2: krótszy, żeby przycisk stał w jednym
  wierszu także przy 390 i 360 px, jak „Zobacz pełny case” na 1019). Od rundy 1 dwa pionowe kafle 3:4 (1737 pod
  nawiasem, 1738 obok), oba z `data-pdw-zoom` (usterka 12); duplikat 1740 usunięty. Pas CTA bez „Wkrótce” (usterka 13).
- **08 zastosowania (slot 08 wzorca).** Zastępuje blok nagród K13 (`tresc.md`, „Pominięte sekcje”, punkt 1), dlatego na
  stronie nie ma `id="nagrody"`. Karty K07 w wariancie na białym tle (`background: rgb(245, 245, 245)`, zasada „karta
  przeciwna do tła”). Siatka od rundy 1: zewnętrzna `minmax(min(100%, 542px), 1fr)` z dwiema parami kart
  `minmax(min(100%, 260px), 1fr)` (4 w rzędzie na desktopie, 2 × 2 na tablecie). Nowy element: link tekstowy pod
  opisem karty w stylu K04 (`display: inline-block; font: 800 15px / 1.4 Poppins, sans-serif; color: rgb(18, 56, 140);
  text-decoration: none;`, statyczny podwójny szewron, 9,78:1 na `#F5F5F5`). Runda 2: link przypięty do dołu karty
  sposobem z kart maszyn K14 (kolumna flex i `margin-top: auto`): karta ma `display: flex; flex-direction: column;`,
  blok tekstu `flex: 1 1 auto; display: flex; flex-direction: column;`, link na początku stylu
  `align-self: flex-start; margin-top: auto;`. Wszystkie 4 linki kończą się 26 px nad dołem karty przy każdej
  szerokości od 1440 do 320 px. Arkusz dodatków bez zmian.
- **09 technologia.** Kolejność kart: Speedy 300, Speedy 360, Q500, SP2000, laser fiber (1019: SP2000, SP500, Q500,
  Speedy 360, Speedy 300). SP500 pominięty, w jego miejscu karta lasera fiber (`tresc.md`). Liczby w bloku: „od 2002”,
  „120 µm”, „3,55 m/s” zamiast „5 / 400 W / 0,1 mm” (usterka 4). Q500: wiersz „Grawer / od 4 pt” (na 1019 „Grawer od / 4 pt”),
  tak jak w `tresc.md`. Karta „Laser fiber” ma jeden wiersz parametru i pod nim ramkę K01 wewnątrz kolumny wierszy
  (`margin:0`, odstęp daje `gap: 9px` kolumny; ramka ma własne tło, więc czyta się na `#1C1C1C`). Ramka pod siatką
  kart stoi w kontenerze (nie w siatce) z `margin:26px 0 0`, potem podpis z K14 bez zmian stylu.
- **10 zaufali.** h2 i lead zmienione wg `tresc.md` (nie kopiują 1019). Ramka K01 pod leadem z
  `margin:0 auto 26px; max-width:600px; text-align:left;` (wg `tresc.md`). Logotypy, pliki i alty bez zmian, bez `data-pdw-zoom`.
- **11 faq.** 5 pytań zamiast 4. Ostatnie `<details>` ma tylko `border-bottom:none;` (usterka 17). Dwie ramki pod białym
  pudełkiem: pierwsza `margin:26px 0 14px`, druga `margin:0` (wg `tresc.md`).
- **12 kontakt.** Zmienione tylko h2 i lead nad kartami. Karta formularza, dane firmy, godziny, logo bez zmian.

## Do wiadomości prowadzącego

- Szablon WordPressa: `page-no-title` (jak 1019). Przy przenoszeniu treści na stronę 456 trzeba przełączyć szablon
  z `wp-custom-template-grawerowanie-laserowe`, bo ten dokłada drugi `<h1>`.
- Meta (title, description, slug roboczy) są w `tresc.md`, sekcja „Meta”; nie są częścią `strona.html`.
- Ramki `p.pdw-uwaga` (7) i napis „Wersja robocza” trzeba usunąć przed publikacją (skrypt wdrożeniowy je odrzuca).
- Wizualnego podglądu w przeglądarce w tym kroku nie robiłem (składacz pisze tylko do `strona.html` i tych notatek).
  Wszystkie bloki pochodzą z katalogu, który był sprawdzany na 360 px i 1280 px; nowe są tylko akapit pod kartami
  materiałów, linki tekstowe w kartach zastosowań i położenie ramek.
