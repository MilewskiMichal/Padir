# Katalog komponentów nowej stylistyki Padir

Źródła: `/wycinanie-laserowe/` (strona 1019, `zrodla/1019-sekcje/*`) jako główny wzorzec,
`/przykladkowe-realizacje/` (1397) jako wzorzec galerii, `pages-2530-…-szkic` jako wzorzec ramek szkicu.
Dotyczy dwóch szkiców: **Grawerowanie laserowe** (`praca/grawerowanie/`) i **Frezowanie CNC** (`praca/frezowanie/`).
Oba składacze biorą kod WYŁĄCZNIE z tego pliku i z plików `zrodla/1019-sekcje/00-poczatek.html` oraz `98-koniec.html`.

Zrzuty, na których oparty jest katalog (do obejrzenia narzędziem Read):

| plik | co pokazuje |
|---|---|
| `praca/wzorzec-d-01-hero.png` … `wzorzec-d-12-kontakt.png` | każda sekcja wzorca 1019 na desktopie (1280 px) |
| `praca/wzorzec-m-01-hero.png`, `-m-04-portfolio`, `-m-07-case`, `-m-09-park`, `-m-12-kontakt` | te same sekcje na telefonie (390 px), widać usterki 8 i 9 |
| `praca/wzorzec-hybryda-na-bialym.png` | rekomendowana karta realizacji (K09) na białej sekcji |
| `praca/wzorzec-hybryda-na-szarym.png` | wariant K09 na sekcji #F5F5F5 |
| `praca/wzorzec-hybryda-360.png` | K09 na telefonie 360 px |
| `praca/wzorzec-kontrola-azur.png` | dowód usterki 11 (zdjęcie „ażurowy panel” to wnętrze kawiarni BOKO) |
| `praca/wzorzec-poprawka-case-360.png` | karta case study K12 z poprawką `min(100%, …)` na 360 px (porównaj z `wzorzec-m-07-case.png`) |

Sprawdzenie katalogu: strona testowa złożona ze wszystkich bloków K01 do K17 (z `00-poczatek.html`,
arkuszem dodatków i `98-koniec.html`, znaczniki `[[…]]` zastąpione tekstem) przechodzi
`sprawdz_szkic.py --szkic` z kodem 0, bez ostrzeżeń. Na 360 px i 1280 px nic nie wychodzi poza ekran ani
poza karty, lightbox otwiera i zamyka zdjęcie z karty K09 (także klawiszem Escape), strzałka w hero ma 3 klatki animacji.

## 0. Jak używać tego katalogu

- Fragmenty kodu są skrócone do jednego powtórzenia. Style inline są skopiowane ze źródła (zapis `rgb(…)` jest
  oryginalny, tak zapisuje je wzorzec). Miejsca, w których kod RÓŻNI się od 1019, są opisane jako **POPRAWKA**.
- Wszystko, co trzeba podmienić, jest w podwójnych nawiasach kwadratowych: `[[…]]`. Skrypt
  `sprawdz_szkic.py` traktuje `[[` i `]]` jako błąd, więc zapomniany znacznik nie przejdzie kontroli.
- Wszystko poza `[[…]]` zostaje bez zmian: kolory, promienie, odstępy, rozmiary, kolejność atrybutów obrazka.
- Akcent marki na OBU stronach to granat `#12388C`. Wzorzec 1019 (wycinanie) nie używa nigdzie swojego zielonego
  koloru kategorii, więc grawer i frezowanie też nie przemalowują stron na swoje kolory. Kolory kategorii
  występują tylko na plakietkach usług w kartach realizacji (K09).

---

## 1. Opakowanie strony

### Co jest w `00-poczatek.html`

```html
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"0","bottom":"0","left":"0","right":"0"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding:0">
<!-- wp:html -->
<div class="pdw">
<style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">
… arkusz 1019: klasy pomocnicze .pdw .fx/.col/.grid/…, baza .pdw (Poppins 300, #141414, tło #fff),
  linki #12388C (hover #0A2456), zaznaczenie #c3d2ee, @keyframes chevBounce (zepsute, patrz usterka 5),
  FAQ (.pdw-faq), overflow-x:clip na section/header, cały wygląd formularza CF7 (.pdw-form …)
</style>
```

- Grupa WordPressa `alignfull` z zerowym marginesem i paddingiem. Szablon strony `page-no-title` ma treść
  w układzie „constrained”, a `alignfull` pozwala sekcjom iść na całą szerokość ekranu.
- W środku JEDEN blok `wp:html`. Cała strona jest w tym jednym bloku, bez innych bloków WordPressa.
- `<div class="pdw">` otwiera kontener. Wszystkie reguły arkusza są zawężone do `.pdw`.
- Arkusz jest na samym początku `.pdw`, z trzema atrybutami `data-no-*` (bez nich LiteSpeed go wytnie).

### Co jest w `98-koniec.html`

```html
<div class="pdw-lb" style="display:none;position:fixed;inset:0;z-index:9999; …">   ← warstwa lightboxa
  <img class="pdw-lb-img" alt="" style="…">                                       ← pusty obrazek, src wstawia skrypt
  <button type="button" aria-label="Zamknij" style="…">&times;</button>
</div>
<script data-no-optimize="1" data-no-defer="1"> … skrypt lightboxa … </script>
</div>              ← zamyka .pdw
<!-- /wp:html -->
</div>              ← zamyka grupę
<!-- /wp:group -->
```

- Skrypt lightboxa jest JUŻ w `98-koniec.html`. Plik `99-skrypt-lightbox.js.html` to ten sam skrypt
  wyjęty do podglądu. **Nie doklejamy go drugi raz** (każdy kafel dostałby dwa nasłuchy kliknięcia).
- Skrypt musi być na końcu, po wszystkich zdjęciach, bo uruchamia się od razu i szuka obrazków, które już są w DOM.

### Jak działa lightbox (dla K02, K07, K08, K09, K10, K12, K13, K14)

1. Skrypt bierze PIERWSZY element `.pdw` na stronie (na stronie ma być tylko jeden).
2. Każdemu `<img data-pdw-zoom>` wewnątrz `.pdw` ustawia kursor `zoom-in` i nasłuch kliknięcia.
3. Kliknięcie otwiera warstwę `.pdw-lb` z obrazkiem `currentSrc` albo `src` klikniętego zdjęcia i jego `alt`.
4. Zamyka kliknięcie gdziekolwiek na warstwie oraz klawisz Escape. Nie ma strzałek ani podpisu (to robi tylko 1397).

Wynikają z tego trzy zasady:
- atrybut `data-pdw-zoom` stoi na samym `<img>`, nie na opakowaniu;
- w powiększeniu pokazuje się dokładnie plik z `src`, więc do galerii dajemy pełny plik (w bibliotece pełne
  zdjęcia realizacji mają najwyżej 1000 px, ciężar jest taki sam jak na 1019), bez `srcset`;
- napisy położone na zdjęciu dostają `pointer-events: none`, żeby kliknięcie w napis też otwierało zdjęcie
  (we wzorcu 1019 tego brakuje na kaflach galerii, w K09 jest dodane).
- `data-pdw-zoom` dostaje każde zdjęcie z treścią. NIE dostają go logotypy (K15) i logo w kontakcie (K17).

### Składanie nowej strony

```
1. zrodla/1019-sekcje/00-poczatek.html      bez zmian, bajt w bajt
2. arkusz dodatków z sekcji 6 tego pliku    drugi <style>, identyczny na obu stronach
3. K01 ramka „Wersja robocza”               pierwsza rzecz po arkuszach
4. <header> (K02)                           dokładnie jeden <h1> na stronie
5. <section> … </section>                   kolejne sekcje z katalogu
6. zrodla/1019-sekcje/98-koniec.html        bez zmian, bajt w bajt
```

- Szablon strony w WordPressie: `page-no-title`, jak 1019, 1397 i 2530. Strony 456 i 1011 mają dziś własne
  szablony (`wp-custom-template-grawerowanie-laserowe`, `frezowanie-cnc`), które dokładają stary hero z drugim
  `<h1>`. Przy przenoszeniu treści na 456 i 1011 trzeba przełączyć szablon (informacja dla prowadzącego).
- Formularz tylko `[contact-form-7 id="480"]` (K17). Stare strony 456 i 1011 mają blok
  `[contact-form-7 id="a8bd5e2" title="Kontakt" html_id="contact"]`. Tego nie kopiujemy.
- Każdy `id` na stronie występuje raz. Każde `href="#x"` ma `id="x"`. Sekcje z `id` mają `scroll-margin-top: 56px`.

---

## 2. Tokeny

### 2.1 Kolory i role

| token | wartość | rola i miejsce we wzorcu |
|---|---|---|
| granat (akcent marki) | `#12388C` = `rgb(18, 56, 140)` | etykiety sekcji, numery kroków, nawiasy na zdjęciach, przycisk B, ikona w ciemnej karcie, linki, `accent-color` w formularzu |
| granat ciemny | `#0A2456` | `.pdw a:hover` |
| granat kontaktu | `#16264D` = `rgb(22, 38, 77)` | tło karty z formularzem (K17) |
| czerń | `#141414` = `rgb(20, 20, 20)` | tekst główny, h2/h3, przycisk A, nawias w hero, tło ciemnej karty i bloku parku |
| czerń h1 | `#111111` = `rgb(17, 17, 17)` | tylko `<h1>` |
| czerń kart maszyn | `#1C1C1C` = `rgb(28, 28, 28)` | tło kart maszyn (K14) |
| linia na ciemnym | `#2E2E2E` = `rgb(46, 46, 46)` | `border-top` wierszy parametrów |
| szarość tła | `#F5F5F5` = `rgb(245, 245, 245)` | tło sekcji szarej i karty jasne na białej sekcji |
| błękit chipów | `#E6ECF7` = `rgb(230, 236, 247)` | tło ikon w jasnych kartach, chip kategorii w case study |
| błękit szkicu | `#EEF1F7` = `rgb(238, 241, 247)` | tło ilustracji w krokach procesu, tło pod zdjęciem karty K09 |
| błękit na ciemnym | `#7FB0F5` = `rgb(127, 176, 245)` | etykiety sekcji i chipy na czarnym tle |
| błękit liczb | `#4D94F7` = `rgb(77, 148, 247)` | duże liczby w bloku parku |
| linia FAQ | `#eee` | `border-bottom` pytań |
| ramka szkicu | tło `#FFF4CC`, ramka `#E8CE72`, tekst `#5A4708` | tylko `p.pdw-uwaga` (K01) |
| **kategoria: grawerowanie** | `#12388C` | plakietka „Grawerowanie” (1397: `--pdr-navy`, zakładka `data-cat="eng"`) |
| **kategoria: wycinanie** | `#175C43` | plakietka „Wycinanie” (1397: `--pdr-green`, `data-cat="cut"`) |
| **kategoria: frezowanie CNC** | `#DE6B24` | plakietka „Frezowanie” (1397: `--pdr-orange`, `data-cat="cnc"`) |

Kolory kategorii sprawdzone w źródle 1397: zmienne `.pdr-real{--pdr-navy:#12388C;--pdr-green:#175C43;--pdr-orange:#DE6B24}`,
atrybuty `data-color` zakładek filtra, tła `.pdr-pill` (21× `#12388C` Grawerowanie, 17× `#175C43` Wycinanie,
6× `#DE6B24` Frezowanie) i podpisy w hero 1397. Kolor kategorii grawerowania jest tym samym granatem co akcent marki.

### 2.2 Szarości tekstu na każdym tle, z kontrastem WCAG 2.x

Wyliczone wzorem WCAG (luminancja względna sRGB). Próg: 4,5:1 dla zwykłego tekstu, 3:1 dla elementów
interfejsu. Kolumna „użycie” mówi, gdzie wzorzec ma ten kolor. Wolno używać WYŁĄCZNIE par z tej tabeli.

**Tło białe `#FFFFFF`**

| tekst | kontrast | użycie |
|---|---|---|
| `#111111` / `#141414` | 18,88 / 18,42 | h1 / h2, h3, tekst główny |
| `#12388C` | 10,66 | etykiety sekcji, numery, linki |
| `#4E4B66` = `rgb(78, 75, 102)` | 8,33 | akapity Wyzwanie/Rozwiązanie/Efekt w case study |
| `#5A5A60` | 6,85 | odpowiedzi w FAQ (na białym pudełku) |
| `#5F5F5F` = `rgb(95, 95, 95)` | 6,39 | akapit hero, akapity w sekcjach dzielonych (K10, K13) |
| `#6B6B6B` = `rgb(107, 107, 107)` | 5,33 | lead pod h2, tekst kart, podpis pod parkiem |
| `#6F6F7C` = `rgb(111, 111, 124)` | 4,95 | szary początek podtytułu w hero (najjaśniejsza szarość na białym, jaśniej nie wolno) |

**Tło szare `#F5F5F5`**

| tekst | kontrast | użycie |
|---|---|---|
| `#141414` | 16,90 | nagłówki |
| `#12388C` | 9,78 | etykiety sekcji |
| `#4E4B66` | 7,64 | godziny otwarcia (K17) |
| `#5F5F5F` | 5,86 | akapit w bloku nagród (K13) |
| `#6B6B6B` | 4,89 | lead i tekst kart na szarym (najjaśniejsza szarość na #F5F5F5) |

**Tła błękitne**: `#12388C` na `#E6ECF7` 8,99; `#12388C` na `#EEF1F7` 9,42; `#6B6B6B` na `#EEF1F7` 4,71.

**Tło czarne `#141414`** (ciemna karta „Dlaczego”, blok parku, ciemny pas CTA)

| tekst | kontrast | użycie |
|---|---|---|
| `#FFFFFF` | 18,42 | h2, h3, przycisk na ciemnym |
| `#C9C9D2` = `rgb(201, 201, 210)` | 11,20 | akapity |
| `#7FB0F5` | 8,27 | etykieta sekcji |
| `#9A9AA6` = `rgb(154, 154, 166)` | 6,62 | podpisy liczb |
| `#4D94F7` | 6,05 | duże liczby (30 px, 800) |

**Tło kart maszyn `#1C1C1C`**

| tekst | kontrast | użycie |
|---|---|---|
| `#FFFFFF` | 17,04 | nazwa maszyny (h3) |
| `#E8E8EE` = `rgb(232, 232, 238)` | 13,97 | wartość parametru |
| `#9A9AA6` | 6,12 | opis maszyny |
| `#7FB0F5` na tle chipa `rgba(127,176,245,.12)` (wynik `#282E36`) | 6,15 | chip „Wielki format” |
| `#8A8A94` = `rgb(138, 138, 148)` | 4,99 | nazwa parametru (najjaśniejsza szarość na ciemnym) |

**Tło granatowe `#16264D`** (karta formularza)

| tekst | kontrast | użycie |
|---|---|---|
| `#FFFFFF` | 14,80 | h2, tekst pól, przycisk |
| `#FFC9C9` | 10,19 | komunikat błędu pola |
| `#C3CCDF` | 9,18 | „Chętnie pomożemy”, treść zgody |
| `#9FB3E0` | 7,05 | etykiety pól |
| placeholder `rgba(255,255,255,.45)` (wynik `#7F889D`) | 4,17 | podpowiedź w polu, poniżej 4,5 (znana słabość wzorca, arkusza nie ruszamy) |
| linia pola `rgba(255,255,255,.32)` (wynik `#616B86`) | 2,79 | element interfejsu, poniżej 3:1 (jw.) |

**Napis na zdjęciu**: pigułka `rgba(20, 20, 20, 0.72)` z białym tekstem. Najgorszy przypadek (białe zdjęcie
pod spodem) daje tło `#565656` i kontrast 7,34. Bezpieczne na każdym zdjęciu.

**Plakietki kategorii (K09)**

| plakietka | kontrast | decyzja |
|---|---|---|
| biały na `#12388C` | 10,66 | jak na 1397 |
| biały na `#175C43` | 7,93 | jak na 1397 |
| biały na `#DE6B24` | **3,37, za mało** dla 12,5 px | NIE kopiujemy z 1397 |
| `#141414` na `#DE6B24` | 5,47 | tak robimy plakietkę „Frezowanie” |

**Ramka szkicu**: `#5A4708` na `#FFF4CC` 8,15.

**Szarość z 1397, której NIE używamy na jasnym tle**: `#9A9AA6` (`--pdr-grey`) ma 2,78 na białym i 2,55 na
`#F5F5F5`. Na 1397 jest w szarym początku podtytułu hero, etykiecie filtra, podpowiedzi pod filtrem.
Na naszych stronach w tym miejscu stoi `#6F6F7C` (hero) albo `#6B6B6B` (reszta).

### 2.3 Tła sekcji i naprzemienność (kolejność 1019)

| # | sekcja | tło sekcji | karty w środku |
|---|---|---|---|
| 01 | hero `<header>` | białe | zdjęcia |
| 02 | Dlaczego Padir | białe | 1 czarna + 2 szare `#F5F5F5` |
| 03 | Materiały | `#F5F5F5` | białe |
| 04 | Portfolio | białe | kafle zdjęć (u nas K09 z kartą `#F5F5F5`) |
| 05 | Na czym to polega | białe (padding górny tylko 36 px, czyta się jako ciąg dalszy 04) | zdjęcie |
| 06 | Proces | `#F5F5F5` | białe |
| 07 | Case study | `#F5F5F5` (06 i 07 tworzą jeden szary blok) | białe + czarny pas |
| 08 | Nagrody | białe (padding górny 20 px) | duży blok `#F5F5F5` |
| 09 | Park maszynowy | białe | duży blok `#141414` + karty `#1C1C1C` |
| 10 | Logotypy | białe (padding górny 20 px) | brak |
| 11 | FAQ | `#F5F5F5` | białe pudełko |
| 12 | Kontakt | białe | granatowa karta + szare pudełko godzin |

Zasada, którą da się zastosować do każdej nowej sekcji: **karta ma kolor przeciwny do tła sekcji**
(białe karty na `#F5F5F5`, karty `#F5F5F5` albo czarne na białym). Dwie sąsiednie sekcje szare łączą się
w jeden blok (jak 06 i 07), dwie białe też (04 i 05, 08 do 10). Sekcja, która zaczyna się zaraz po sekcji
o tym samym tle, ma zmniejszony padding górny (36 px albo 20 px), jak 05, 08 i 10.

### 2.4 Promienie (asymetryczne narożniki)

Zapis CSS: `a b c d` = lewy górny, prawy górny, prawy dolny, lewy dolny; `a b c` = LG, PG i LD, PD.
Podpis stylu: trzy narożniki duże, jeden (prawy górny) mały.

| element | `border-radius` |
|---|---|
| karta „Dlaczego” | `44px 12px 44px 44px` |
| pudełko FAQ, kafel galerii 2 w rzędzie | `40px 12px 40px 40px` |
| karta materiału | `36px 10px 36px 36px` |
| kafel galerii 3 w rzędzie, karta kroku, karta realizacji K09 (= `.pdr-card`) | `34px 10px 34px 34px` |
| karta case study | `48px 14px 48px 48px`, lustrzana `14px 48px 48px` |
| ciemny pas CTA | `48px 14px 48px 48px` |
| karta maszyny | `30px 8px 30px 30px` |
| pudełko godzin otwarcia | `28px 8px 28px 28px` |
| duży blok nagród i parku | `52px 52px 14px` (mały jest prawy dolny) |
| karta formularza | `30px 30px 130px` (duży łuk w prawym dolnym) |
| ikona w karcie, ramka szkicu | `14px 4px 14px 14px` |
| chip kategorii w case study | `16px 4px 16px 16px` |
| chip w karcie maszyny | `12px 3px 12px 12px` |
| pigułka na zdjęciu | `20px` (mała: `18px`) |
| ramka zdjęcia z nawiasem L | `28px 28px 28px 120px` (hero), `24px 24px 24px 120px` (K10), `18px 18px 18px 90px` (case), lustrzana `18px 18px 90px` |
| kafle hero 2x2 | `24px 8px 8px`, `8px 24px 8px 8px`, `8px 8px 8px 90px`, `8px 8px 24px` |
| miniatury w case study | `18px 6px 18px 18px` |

Nawias L ma `border-bottom-left-radius` równy dolnemu lewemu promieniowi ramki, którą obejmuje
(hero: 90 px kafla pod nim; K10: 120 px; case: 90 px).

### 2.5 Typografia (Poppins, wagi 300 do 800)

| rola | styl |
|---|---|
| h1 | `font: 800 clamp(38px, 5.4vw, 62px) / 1.03`, `letter-spacing: -0.025em`, `#111` |
| podtytuł hero | `font: 700 clamp(20px, 2.6vw, 26px) / 1.3`, szary początek w `<span>` `#6F6F7C` |
| akapit hero | `font: 300 16.5px / 1.7`, `#5F5F5F`, `max-width: 470px` |
| etykieta sekcji | `font: 600 13px / 1`, `letter-spacing: 0.14em`, wersaliki, `#12388C` (na ciemnym `#7FB0F5`) |
| h2 sekcji | `font: 700 clamp(26px, 3.8vw, 38px) / 1.12`, `letter-spacing: -0.01em` |
| h2 w sekcji dzielonej (K10, K13) | `700 clamp(26px, 3.6vw, 36px) / 1.14` (K13: `3.4vw`) |
| h2 na ciemnym (park) | `700 clamp(24px, 3vw, 32px) / 1.15`, biały |
| h2 logotypów | `700 clamp(24px, 3.4vw, 34px) / 1.15` |
| h2 kontaktu | `800 clamp(28px, 4vw, 42px) / 1.12`; w karcie formularza `800 clamp(24px, 3vw, 30px) / 1.15` |
| lead pod h2 | `font: 300 17px / 1.65`, `#6B6B6B` |
| akapit w sekcji dzielonej | `300 16.5px / 1.7`, `#5F5F5F`, `max-width: 560px` |
| h3 | 23 px (case), 22 px (pas CTA), 20 px (maszyna), 19 px („Dlaczego”), 18 px (materiał, krok), 17,5 px (K09); zawsze 700 |
| tekst kart | 15 px / 1.65 („Dlaczego”), 14,5 px / 1.65 (case), 14 px / 1.6 (materiał, krok), 13 px / 1.5 (maszyna) |
| mikroetykiety | 11,5 px 700 `0.06em` (Wyzwanie), 11 px 600 `0.1em` (Telefon), 11 px 600 `0.08em` (materiał w K09), 10,5 px 600 `0.1em` (chip maszyny) |
| przyciski | 800, 17 px (hero), 16 px (na ciemnym), 15 px (w treści) |
| pigułka na zdjęciu | 500 13 px (mała 12,5 px); plakietka K09 600 12,5 px |
| FAQ | pytanie `600 16.5px/1.4`, odpowiedź `300 15px/1.7` `#5A5A60`, znak „+” `400 28px` |

### 2.6 Odstępy

- Kontener: `max-width: 1220px; margin: 0px auto; padding: 0px 24px;` (FAQ: `max-width: 860px`).
- Sekcja standardowa: `padding: 82px 0px` (proces `78px 0px`). Hero: `56px 0px 72px`. Kontakt: `82px 0px 92px`.
  Sekcja po sekcji o tym samym tle: `36px 0px 78px` (K10) albo `20px 0px 78px` / `20px 0px 82px` (K13, K15).
- Nagłówek sekcji do siatki: `margin-top: 44px` (materiały, portfolio, proces) albo `46px` („Dlaczego”, case).
- Odstępy w siatkach: 22 px (karty), 24 px („Dlaczego”), 18 px (maszyny), 14 px (hero 2x2), 12 px (zdjęcia w case).
- Odstęp między kartami case study: `margin-top: 26px`.
- Kotwice: `scroll-margin-top: 56px` na każdej sekcji z `id`.

---

## 3. Komponenty

Wspólne opakowanie sekcji (do każdego komponentu typu „sekcja”):

```html
<section id="[[id-sekcji]]" style="padding: 82px 0px; scroll-margin-top: 56px;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px;">
    … nagłówek K05 i treść …
  </div></section>
```
Sekcja szara: `style="padding: 82px 0px; background: rgb(245, 245, 245); scroll-margin-top: 56px;"`.
`id` dajemy tylko tam, gdzie prowadzi kotwica (wzorzec: `materialy`, `portfolio`, `proces`, `realizacje`,
`nagrody`, `technologia`, `faq`, `kontakt`).

**POPRAWKA dla wszystkich siatek `auto-fit`:** wzorzec ma `minmax(340px, 1fr)`, `minmax(300px, 1fr)` itd.
Na telefonie 360 px kolumna 340 px nie mieści się w karcie z paddingiem i treść wychodzi poza kartę
(usterka 8). W całym katalogu stoi `minmax(min(100%, 340px), 1fr)`, tak jak na 1397. Na desktopie wygląd
się nie zmienia.

### K01. Ramki szkicu: „Wersja robocza” i „Do potwierdzenia”

Źródło: konwencja z BRIEF i `pages-2530-…-szkic` (tam ramka nad formularzem).

Ramka na samej górze, wstawiana zaraz po arkuszach, przed `<header>` (szerokość dopasowana do kontenera 1220 px):

```html
<!-- K01 ramka gorna -->
<p class="pdw-uwaga" style="margin:24px auto 0;width:calc(100% - 48px);max-width:1172px;padding:13px 16px;border-radius:14px 4px 14px 14px;background:#FFF4CC;border:1px solid #E8CE72;font:600 13px/1.5 Poppins,sans-serif;color:#5A4708">Wersja robocza do akceptacji. Żółte ramki oznaczają miejsca do potwierdzenia przed publikacją.</p>
```

Ramka przy konkretnej informacji (dokładnie styl z BRIEF):

```html
<!-- K01 ramka w tresci -->
<p class="pdw-uwaga" style="margin:0 0 26px;padding:13px 16px;border-radius:14px 4px 14px 14px;background:#FFF4CC;border:1px solid #E8CE72;font:600 13px/1.5 Poppins,sans-serif;color:#5A4708">Do potwierdzenia z klientem: [[konkretne pytanie, np. jakie modele frezarek i jakie pole robocze podać]]</p>
```

- Tekst do podmiany: tylko pytanie po dwukropku. Reszta bez zmian.
- Ramka to `<p>`, więc nie wolno jej wkładać do innego `<p>`, `<a>`, `<h*>`, `<summary>`. Stawiamy ją między
  blokami: w kolumnie tekstu, w karcie (np. karta maszyny), pod akapitem.
- Nie stawiamy ramki jako bezpośredniego dziecka siatki (zajęłaby komórkę). Jeśli musi tam być: dopisz na
  początku stylu `grid-column:1/-1;`.
- Ramka ma własne tło, więc działa też na czarnych i granatowych sekcjach.
- NIE używamy żółtego znacznika „DO POTWIERDZENIA” wpisanego w tekst ze szkicu 2530 (`<span … background:#FFE08A …>`).
  Nie ma klasy `pdw-uwaga`, więc skrypt kontroli go nie liczy, a skrypt wdrożeniowy go nie usunie.

### K02. Hero z siatką 2x2 i nawiasem L (wersja poprawiona)

Źródło: 1019, sekcja 01 (`01-wycinanie-laserowe.html`), zrzut `wzorzec-d-01-hero.png`.

```html
<!-- K02 hero -->
<header style="padding: 56px 0px 72px; overflow: hidden;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 56px; align-items: center;">
    <div>
      <h1 style="font: 800 clamp(38px, 5.4vw, 62px) / 1.03 Poppins, sans-serif; letter-spacing: -0.025em; margin: 0px 0px 24px; color: rgb(17, 17, 17);">[[Grawerowanie]]<br>[[laserowe]]</h1>
      <p style="font: 700 clamp(20px, 2.6vw, 26px) / 1.3 Poppins, sans-serif; margin: 0px 0px 20px; color: rgb(20, 20, 20); max-width: 480px;"><span style="color: rgb(111, 111, 124);">[[Szary początek.]]</span> [[Czarna reszta podtytułu]]</p>
      <p style="font: 300 16.5px / 1.7 Poppins, sans-serif; color: rgb(95, 95, 95); max-width: 470px; margin: 0px 0px 34px;">[[Akapit: 1-2 zdania z faktami ze źródeł]]</p>
      <div style="display: flex; flex-wrap: wrap; gap: 36px; align-items: center; margin-bottom: 38px;">
        <a href="#kontakt" style="position: relative; display: inline-block; padding: 17px 44px 19px 22px; font: 800 17px / 1 Poppins, sans-serif; color: rgb(20, 20, 20); text-decoration: none; border-left: 7px solid rgb(20, 20, 20); border-bottom: 7px solid rgb(20, 20, 20); border-bottom-left-radius: 24px;">Skorzystaj z oferty</a>
        <a href="#proces" style="position: relative; display: inline-block; padding: 17px 22px 19px 44px; font: 800 17px / 1 Poppins, sans-serif; color: rgb(18, 56, 140); text-decoration: none; border-right: 7px solid rgb(18, 56, 140); border-bottom: 7px solid rgb(18, 56, 140); border-bottom-right-radius: 24px;">Czytaj więcej</a>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 20px;">
      <div style="position: relative; border-radius: 28px 28px 28px 120px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 14px;">
          <div style="border-radius: 24px 8px 8px; overflow: hidden; aspect-ratio: 1 / 1;"><img src="[[URL zdjęcia 1]]" alt="[[ALT 1]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="eager" fetchpriority="high" data-no-lazy="1" decoding="async" data-pdw-zoom></div>
          <div style="border-radius: 8px 24px 8px 8px; overflow: hidden; aspect-ratio: 1 / 1;"><img src="[[URL zdjęcia 2]]" alt="[[ALT 2]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="eager" fetchpriority="high" data-no-lazy="1" decoding="async" data-pdw-zoom></div>
          <div style="border-radius: 8px 8px 8px 90px; overflow: hidden; aspect-ratio: 1 / 1;"><img src="[[URL zdjęcia 3]]" alt="[[ALT 3]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="eager" fetchpriority="high" data-no-lazy="1" decoding="async" data-pdw-zoom></div>
          <div style="border-radius: 8px 8px 24px; overflow: hidden; aspect-ratio: 1 / 1;"><img src="[[URL zdjęcia 4]]" alt="[[ALT 4]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="eager" fetchpriority="high" data-no-lazy="1" decoding="async" data-pdw-zoom></div>
        </div>
        <div style="position: absolute; left: -5px; bottom: -5px; width: 150px; height: 150px; border-left: 11px solid rgb(20, 20, 20); border-bottom: 11px solid rgb(20, 20, 20); border-bottom-left-radius: 90px; pointer-events: none; z-index: 3;"></div>
      </div>
      <a href="#portfolio" style="align-self: center; display: inline-flex; flex-direction: column; align-items: center; gap: 8px; padding: 6px 12px; font: 800 15px / 1 Poppins, sans-serif; color: rgb(18, 56, 140); text-decoration: none;">Zobacz więcej realizacji<svg viewBox="0 0 40 34" width="30" height="26" fill="none" stroke="#12388C" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="animation: 1.4s ease-in-out 0s infinite normal none running chevBounce;"><polyline points="6,6 20,18 34,6"></polyline><polyline points="6,17 20,29 34,17"></polyline></svg></a>
    </div>
  </div></header>
```

- Do podmiany: dwie linie h1, podtytuł (szary początek kończy się kropką, jak „Laser i frez.” na 1397),
  akapit, 4 zdjęcia z `alt`. Teksty przycisków mogą zostać jak we wzorcu.
- Bez zmian: cała reszta. Kotwice `#kontakt`, `#proces`, `#portfolio` wymagają sekcji z tymi `id`.
- Zdjęcia w hero: `loading="eager" fetchpriority="high" data-no-lazy="1"`, w tej kolejności co we wzorcu.
  Pod nawiasem jest kafel 3 (lewy dolny, promień 90 px), tam dajemy kadr, któremu nawias nie zasłoni sedna.
- **Nawias L**: wyłącznie skróty `border-left: 11px solid …; border-bottom: 11px solid …;`. Nigdy
  `border-width`, `border-color`, `border-*-width`, `border-*-color`, `border-*-style` w stylu inline.
  WordPress ma regułę zgodności `html :where([style*="border-width"]){border-style:solid}` (i podobne dla
  `border-*-color`), która wtedy maluje WSZYSTKIE boki i nawias robi się kwadratem. Tak było na szkicu 2530:
  `border-width: 11px; border-left-style: solid; border-left-color: …`. We wzorcu 1019 przed skrótami stoją
  jeszcze `border-top: 0; border-right: 0;`. Są nieszkodliwe, ale niepotrzebne, w katalogu ich nie ma.
- **POPRAWKA**: `minmax(min(100%, 340px), 1fr)` zamiast `minmax(340px, 1fr)`, `aria-hidden="true"` na strzałce.
- h1: zapis zdaniowy (`Grawerowanie<br>laserowe`, `Frezowanie<br>CNC`), patrz usterka 14.

### K03. Przyciski-nawiasy CTA

Źródło: 1019, sekcje 01, 07, 08. Zawsze `<a>` z tekstem 800, bez tła, z „nawiasem” z dwóch krawędzi.

```html
<!-- K03 A: nawias lewy, czarny (glowny), duzy w hero -->
<a href="#kontakt" style="position: relative; display: inline-block; padding: 17px 44px 19px 22px; font: 800 17px / 1 Poppins, sans-serif; color: rgb(20, 20, 20); text-decoration: none; border-left: 7px solid rgb(20, 20, 20); border-bottom: 7px solid rgb(20, 20, 20); border-bottom-left-radius: 24px;">[[Skorzystaj z oferty]]</a>

<!-- K03 B: nawias prawy, granatowy (drugi) -->
<a href="#proces" style="position: relative; display: inline-block; padding: 17px 22px 19px 44px; font: 800 17px / 1 Poppins, sans-serif; color: rgb(18, 56, 140); text-decoration: none; border-right: 7px solid rgb(18, 56, 140); border-bottom: 7px solid rgb(18, 56, 140); border-bottom-right-radius: 24px;">[[Czytaj więcej]]</a>

<!-- K03 A-maly: w tresci karty (case study, pod galeria) -->
<a href="[[#kotwica albo /opublikowany-adres/]]" style="position: relative; display: inline-block; padding: 15px 40px 17px 20px; font: 800 15px / 1 Poppins; color: rgb(20, 20, 20); text-decoration: none; border-left: 6px solid rgb(20, 20, 20); border-bottom: 6px solid rgb(20, 20, 20); border-bottom-left-radius: 20px;">[[Zobacz pełny case]]</a>

<!-- K03 A-ciemny: na tle #141414 -->
<a href="#kontakt" style="position: relative; flex: 0 0 auto; display: inline-block; padding: 16px 40px 18px 20px; font: 800 16px / 1 Poppins; color: rgb(255, 255, 255); text-decoration: none; border-left: 6px solid rgb(255, 255, 255); border-bottom: 6px solid rgb(255, 255, 255); border-bottom-left-radius: 20px;">[[Zapytaj o realizację]]</a>

<!-- K03 C: kreska, granatowa (w bloku nagrod) -->
<a href="#kontakt" style="position: relative; display: inline-block; padding: 15px 24px 17px 20px; font: 800 15px / 1 Poppins, sans-serif; color: rgb(18, 56, 140); text-decoration: none; border-left: 6px solid rgb(18, 56, 140);">[[Zapytaj o nagrodę na zamówienie]]</a>
```

- Do podmiany: tekst i `href`. Wszystko inne bez zmian.
- Para w hero: zawsze A po lewej, B po prawej, `gap: 36px`.
- `href` tylko do `#id` istniejącego na stronie albo do OPUBLIKOWANEGO adresu z `SPIS.json`. Nigdy `href="#"`
  (usterka 7; kontrola tego nie łapie).
- Te same skróty krawędzi co w nawiasie L. Przycisk formularza (`.form-btn`) ma ten sam kształt co C, ale
  jest w arkuszu i go nie dotykamy.

### K04. Link ze strzałką w dół

Część K02 („Zobacz więcej realizacji”). Podwójna strzałka SVG z animacją `chevBounce`. Animacja działa
dopiero z poprawką z sekcji 6 (usterka 5). Tekst do podmiany: napis linku. Cel: `#portfolio`.

### K05. Etykieta sekcji + h2 + lead

Źródło: 1019, sekcje 02, 03, 04, 06, 07, 11.

```html
<!-- K05 do lewej (materialy, portfolio, proces, case) -->
<div style="max-width: 680px;">
  <span style="display: inline-block; font: 600 13px / 1 Poppins, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(18, 56, 140); margin: 0px 0px 14px;">[[Etykieta]]</span>
  <h2 style="font: 700 clamp(26px, 3.8vw, 38px) / 1.12 Poppins, sans-serif; letter-spacing: -0.01em; margin: 0px 0px 14px; color: rgb(20, 20, 20);">[[Nagłówek sekcji]]</h2>
  <p style="font: 300 17px / 1.65 Poppins, sans-serif; color: rgb(107, 107, 107); margin: 0px;">[[Lead: jedno, dwa zdania]]</p>
</div>
```

- Wariant wyśrodkowany („Dlaczego Padir”): zewnętrzny `<div style="text-align: center; max-width: 680px; margin: 0px auto;">`.
- Wariant bez leadu (FAQ): etykieta z `margin: 0px 0px 12px;`, h2 z `margin: 0px;`, całość w
  `<div style="text-align: center; margin-bottom: 38px;">`.
- Wariant na ciemnym tle: etykieta `color: rgb(127, 176, 245)`, h2 `color: rgb(255, 255, 255)` (patrz K14).
- Do podmiany: etykieta (1-3 słowa), h2, lead. Etykiety we wzorcu: Dlaczego Padir, Materiały, Portfolio,
  Na czym to polega, Jak pracujemy, Case studies, Nowość, Nowoczesna technologia, Zaufali nam, FAQ.

### K06. Karty cech „Dlaczego Padir”

Źródło: 1019, sekcja 02, zrzut `wzorzec-d-02-dlaczego.png`. Sekcja biała, nagłówek K05 wyśrodkowany.
Zawsze 3 karty: pierwsza czarna, dwie szare.

```html
<!-- K06 karty cech -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 24px; margin-top: 46px;">
  <div style="background: rgb(20, 20, 20); color: rgb(255, 255, 255); border-radius: 44px 12px 44px 44px; padding: 38px 34px;">
    <div aria-hidden="true" style="width: 48px; height: 48px; border-radius: 14px 4px 14px 14px; background: rgb(18, 56, 140); display: flex; align-items: center; justify-content: center; font: 800 20px / 1 Poppins; color: rgb(255, 255, 255); margin-bottom: 20px;">◆</div>
    <h3 style="font: 700 19px / 1.3 Poppins, sans-serif; margin: 0px 0px 8px; color: rgb(255, 255, 255) !important;">[[Cecha 1]]</h3>
    <p style="font: 300 15px / 1.65 Poppins; color: rgb(201, 201, 210); margin: 0px;">[[Opis cechy 1]]</p>
  </div>
  <div style="background: rgb(245, 245, 245); border-radius: 44px 12px 44px 44px; padding: 38px 34px;">
    <div aria-hidden="true" style="width: 48px; height: 48px; border-radius: 14px 4px 14px 14px; background: rgb(230, 236, 247); display: flex; align-items: center; justify-content: center; font: 800 20px / 1 Poppins; color: rgb(18, 56, 140); margin-bottom: 20px;">✓</div>
    <h3 style="font: 700 19px / 1.3 Poppins, sans-serif; margin: 0px 0px 8px; color: rgb(20, 20, 20) !important;">[[Cecha 2]]</h3>
    <p style="font: 300 15px / 1.65 Poppins; color: rgb(107, 107, 107); margin: 0px;">[[Opis cechy 2]]</p>
  </div>
  <!-- trzecia karta: jak druga, znak ★ -->
</div>
```

- Znaki w ikonach bez zmian i w tej kolejności: ◆ (czarna), ✓, ★.
- Do podmiany: h3 i opis. Teksty 1019 („Nowoczesne technologie”, „Gwarancja udanego produktu”,
  „Doświadczenie i profesjonalizm”) to te same hasła co na starych 456 i 1011, a zdania są już na 1019.
  Fakty wolno zostawić, zdania piszemy od nowa (zasada treści 5). Bez „najwyższej jakości” (usterka 3).
- **POPRAWKA**: `min(100%, 260px)` i `aria-hidden="true"` na ikonie.

### K07. Karty materiałów

Źródło: 1019, sekcja 03 (`id="materialy"`), zrzut `wzorzec-d-03-materialy.png`. Sekcja `#F5F5F5`, karty białe.

```html
<!-- K07 karty materialow -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 22px; margin-top: 44px;">
  <div style="background: rgb(255, 255, 255); border-radius: 36px 10px 36px 36px; overflow: hidden;">
    <div style="aspect-ratio: 16 / 10; overflow: hidden;"><img src="[[URL zdjęcia materiału]]" alt="[[ALT]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom></div>
    <div style="padding: 24px 26px 26px;">
      <h3 style="font: 700 18px / 1.3 Poppins, sans-serif; margin: 0px 0px 6px; color: rgb(20, 20, 20) !important;">[[Materiał]]</h3>
      <p style="font: 300 14px / 1.6 Poppins; color: rgb(107, 107, 107); margin: 0px 0px 14px;">[[Co z niego robimy: 1-2 zdania]]</p>
    </div>
  </div>
</div>
```

- Liczba kart: wielokrotność 3 (wzorzec ma 6). Do podmiany: zdjęcie, alt, nazwa, opis.
- Zdjęcie ma pokazywać materiał w realnej pracy Padiru i nie powtarzać się z galerią na tej samej stronie (usterka 10).
- Jeśli sekcja materiałów wypada na białym tle, karta dostaje `background: rgb(245, 245, 245)` (zasada z 2.3).

### K08. Kafle galerii z lightboxem (galeria 1019)

Źródło: 1019, sekcja 04 (`id="portfolio"`), zrzuty `wzorzec-d-04-portfolio.png` i `wzorzec-m-04-portfolio.png`.
Na nowych stronach portfolio robimy z K09 (sekcja 5). K08 zostaje do małych zestawów zdjęć bez tytułów
(np. dodatkowe ujęcia w opisie usługi).

```html
<!-- K08 kafle galerii -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 22px; margin-top: 22px;">
  <div style="position: relative; border-radius: 40px 12px 40px 40px; overflow: hidden; aspect-ratio: 4 / 3;"><img src="[[URL]]" alt="[[ALT]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom><span style="position: absolute; left: 16px; bottom: 16px; background: rgba(20, 20, 20, 0.72); color: rgb(255, 255, 255); font: 500 13px / 1 Poppins; padding: 8px 15px; border-radius: 20px; pointer-events: none;">[[Branża / materiał]]</span></div>
</div>
```

- Rząd 3 kafli: kafel `border-radius: 34px 10px 34px 34px; … aspect-ratio: 3 / 4;` (albo `4 / 3`),
  pigułka `left: 14px; bottom: 14px; … font: 500 12.5px / 1 Poppins; padding: 7px 13px; border-radius: 18px;`.
- Rytm wzorca: rzędy po 2 i po 3 kafle, każdy rząd to osobna siatka, kolejne mają `margin-top: 22px`.
- **POPRAWKA**: wzorzec ma `repeat(2, minmax(0px, 1fr))` i `repeat(3, minmax(0px, 1fr))` bez wersji na telefon
  (na 390 px trzy kafle mają po ok. 100 px, a pigułki się ucinają). `repeat(auto-fit, minmax(min(100%, 260px), 1fr))`
  daje 2 albo 3 kolumny na desktopie (zależnie od liczby kafli w rzędzie) i jedną na telefonie.
- **POPRAWKA**: `pointer-events: none` na pigułce, żeby klik w napis też powiększał.
- Do podmiany: zdjęcie, alt, pigułka „Branża / materiał”.

### K09. Karta realizacji (hybryda `.pdr-card`): REKOMENDOWANA do portfolio

Pełny opis, uzasadnienie i kod w sekcji 5.

### K10. „Na czym to polega”: zdjęcie z nawiasem + tekst

Źródło: 1019, sekcja 05, zrzut `wzorzec-d-05-na-czym.png`.

```html
<!-- K10 na czym to polega -->
<section style="padding: 36px 0px 78px;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 52px; align-items: center;">
    <div style="position: relative; border-radius: 24px 24px 24px 120px;">
      <div style="border-radius: 24px 24px 24px 120px; overflow: hidden; aspect-ratio: 5 / 4;">
        <img src="[[URL zdjęcia z pracowni]]" alt="[[ALT]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom>
      </div>
      <div style="position: absolute; left: -5px; bottom: -5px; width: 155px; height: 155px; border-left: 10px solid rgb(18, 56, 140); border-bottom: 10px solid rgb(18, 56, 140); border-bottom-left-radius: 120px; pointer-events: none; z-index: 3;"></div>
    </div>
    <div>
      <span style="display: inline-block; font: 600 13px / 1 Poppins, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(18, 56, 140); margin: 0px 0px 14px;">Na czym to polega</span>
      <h2 style="font: 700 clamp(26px, 3.6vw, 36px) / 1.14 Poppins, sans-serif; letter-spacing: -0.01em; margin: 0px 0px 16px; color: rgb(20, 20, 20);">[[Nagłówek: obrazowo, czym jest technologia]]</h2>
      <p style="font: 300 16.5px / 1.7 Poppins, sans-serif; color: rgb(95, 95, 95); margin: 0px 0px 14px; max-width: 560px;">[[Akapit 1]]</p>
      <p style="font: 300 16.5px / 1.7 Poppins, sans-serif; color: rgb(95, 95, 95); margin: 0px; max-width: 560px;">[[Akapit 2]]</p>
    </div>
  </div></section>
```

- Nawias granatowy, 10 px, promień 120 px = lewy dolny promień ramki zdjęcia.
- Padding górny 36 px, bo we wzorcu sekcja idzie po białym portfolio. Jeśli poprzednia sekcja jest szara,
  daj `padding: 82px 0px 78px;`.
- Do podmiany: zdjęcie, alt, h2, dwa akapity. Etykieta może zostać.
- Zdjęcie: prawdziwy kadr z pracowni. Zdjęcie prasowe producenta tylko jako zdjęcie maszyny, z takim alt.

### K11. Kroki procesu

Źródło: 1019, sekcja 06 (`id="proces"`), zrzut `wzorzec-d-06-proces.png`. Sekcja `#F5F5F5`
(`padding: 78px 0px`), nagłówek K05 do lewej, 4 karty.

```html
<!-- K11 kroki procesu -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr)); gap: 22px; margin-top: 44px;">
  <div style="background: rgb(255, 255, 255); border-radius: 34px 10px 34px 34px; overflow: hidden; display: flex; flex-direction: column;">
    <div style="position: relative; aspect-ratio: 4 / 5;">
      <div style="position: absolute; inset: 0px; background: rgb(238, 241, 247); display: flex; align-items: center; justify-content: center;">
        <svg viewBox="0 0 200 240" fill="none" stroke="#12388C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width: 76%; height: auto;">
          <rect x="34" y="54" width="132" height="94" rx="8"></rect>
          <line x1="100" y1="148" x2="100" y2="168"></line><line x1="74" y1="168" x2="126" y2="168"></line>
          <path d="M56 124 C 78 80, 120 80, 144 116"></path>
          <rect x="50" y="118" width="12" height="12" rx="2" fill="#eef1f7"></rect>
          <rect x="138" y="110" width="12" height="12" rx="2" fill="#eef1f7"></rect>
          <circle cx="100" cy="76" r="5" fill="#12388C" stroke="none"></circle><line x1="82" y1="84" x2="118" y2="84"></line>
          <path d="M104 126 l30 12 l-13 4 l-4 13 z" fill="#12388C" stroke="none"></path>
        </svg>
      </div>
    </div>
    <div style="padding: 20px 24px 26px;">
      <div style="font: 800 15px / 1 Poppins, sans-serif; color: rgb(18, 56, 140); margin-bottom: 8px;">01</div>
      <h3 style="font: 700 18px / 1.3 Poppins, sans-serif; margin: 0px 0px 6px; color: rgb(20, 20, 20) !important;">[[Nazwa kroku]]</h3>
      <p style="font: 300 14px / 1.6 Poppins; color: rgb(107, 107, 107); margin: 0px;">[[Opis kroku]]</p>
    </div>
  </div>
</div>
```

- 4 kroki, numery `01` do `04`. Do podmiany: nazwa, opis, ilustracja.
- Ilustracje: liniowe SVG w stylu wzorca (`viewBox="0 0 200 240"`, `stroke="#12388C"`, `stroke-width="2.4"`,
  zaokrąglone końce, wypełnienia tylko `#12388C` i `#eef1f7`). Ikony 01 (plik na ekranie), 02 (warstwy
  materiału i suwaki) i 04 (gotowy element z ptaszkiem) pasują do obu usług i można je wziąć z
  `06-proces.html` bez zmian. Ikona 03 to wiązka lasera: pasuje do grawerowania, do frezowania trzeba
  narysować wrzeciono z frezem w tym samym stylu.
- Zamiast ilustracji można dać zdjęcie: w miejsce wewnętrznego `<div … background: rgb(238, 241, 247) …>`
  wstaw `<img src alt style="position: absolute; inset: 0px; width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom>`.
  Na jednej stronie wszystkie 4 kroki w jednej technice (same SVG albo same zdjęcia).
- **NIE kopiujemy** napisu `<span …>szkic</span>` z prawego dolnego rogu ilustracji (usterka 6) ani leadu
  o „zdjęciach, które opowiadają historię”, jeśli zdjęć nie ma.

### K12. Case study

Źródło: 1019, sekcja 07 (`id="realizacje"`), zrzut `wzorzec-d-07-case.png`. Sekcja `#F5F5F5`, nagłówek K05.

Karta A (zdjęcia z lewej):

```html
<!-- K12 case study karta A -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 38px; align-items: center; margin-top: 46px; background: rgb(255, 255, 255); border-radius: 48px 14px 48px 48px; padding: 28px;">
  <div style="display: flex; flex-direction: column; gap: 12px;">
    <div style="position: relative; border-radius: 18px 18px 18px 90px;">
      <div style="border-radius: 18px 18px 18px 90px; overflow: hidden; aspect-ratio: 4 / 3;"><img src="[[URL zdjęcia głównego]]" alt="[[ALT]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom></div>
      <div style="position: absolute; left: -4px; bottom: -4px; width: 118px; height: 118px; border-left: 8px solid rgb(18, 56, 140); border-bottom: 8px solid rgb(18, 56, 140); border-bottom-left-radius: 90px; pointer-events: none; z-index: 3;"></div>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
      <div style="position: relative; border-radius: 18px 6px 18px 18px; overflow: hidden; aspect-ratio: 1 / 1;"><img src="[[URL miniatury]]" alt="[[ALT]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom></div>
      <!-- druga miniatura tak samo -->
    </div>
  </div>
  <div>
    <span style="display: inline-block; font: 600 12px / 1 Poppins; letter-spacing: 0.04em; color: rgb(18, 56, 140); background: rgb(230, 236, 247); padding: 6px 14px; border-radius: 16px 4px 16px 16px; margin-bottom: 14px;">[[Branża / typ]]</span>
    <h3 style="font: 700 23px / 1.25 Poppins, sans-serif; margin: 0px 0px 16px; color: rgb(20, 20, 20) !important;">[[Tytuł realizacji]]</h3>
    <div style="margin: 0px 0px 14px;"><b style="display: block; font: 700 11.5px / 1 Poppins; letter-spacing: 0.06em; text-transform: uppercase; color: rgb(18, 56, 140); margin-bottom: 4px;">Wyzwanie</b><p style="margin: 0px; font: 300 14.5px / 1.65 Poppins; color: rgb(78, 75, 102);">[[Wyzwanie]]</p></div>
    <div style="margin: 0px 0px 14px;"><b style="display: block; font: 700 11.5px / 1 Poppins; letter-spacing: 0.06em; text-transform: uppercase; color: rgb(18, 56, 140); margin-bottom: 4px;">Rozwiązanie</b><p style="margin: 0px; font: 300 14.5px / 1.65 Poppins; color: rgb(78, 75, 102);">[[Rozwiązanie]]</p></div>
    <div style="margin: 0px 0px 22px;"><b style="display: block; font: 700 11.5px / 1 Poppins; letter-spacing: 0.06em; text-transform: uppercase; color: rgb(18, 56, 140); margin-bottom: 4px;">Efekt</b><p style="margin: 0px; font: 300 14.5px / 1.65 Poppins; color: rgb(78, 75, 102);">[[Efekt]]</p></div>
    <!-- opcjonalnie K03 A-maly z href do OPUBLIKOWANEJ strony case study -->
  </div>
</div>
```

Karta B (lustrzana, tekst z lewej, druga i kolejne parzyste): kontener
`… margin-top: 26px; background: rgb(255, 255, 255); border-radius: 14px 48px 48px; padding: 28px;`,
najpierw kolumna tekstu, potem zdjęć; ramka zdjęcia głównego `border-radius: 18px 18px 90px;` i nawias z prawej:

```html
<!-- K12 nawias prawy (karta B) -->
<div style="position: absolute; right: -4px; bottom: -4px; width: 118px; height: 118px; border-right: 8px solid rgb(18, 56, 140); border-bottom: 8px solid rgb(18, 56, 140); border-bottom-right-radius: 90px; pointer-events: none; z-index: 3;"></div>
```

Ciemny pas CTA pod kartami:

```html
<!-- K12 ciemny pas CTA -->
<div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 24px; margin-top: 26px; background: rgb(20, 20, 20); color: rgb(255, 255, 255); border-radius: 48px 14px 48px 48px; padding: 36px 40px;">
  <div style="max-width: 640px;">
    <span style="display: inline-block; font: 600 12px / 1 Poppins; letter-spacing: 0.06em; text-transform: uppercase; color: rgb(127, 176, 245); margin-bottom: 10px;">[[Etykieta]]</span>
    <h3 style="font: 700 22px / 1.3 Poppins, sans-serif; margin: 0px 0px 8px; color: rgb(255, 255, 255) !important;">[[Nagłówek]]</h3>
    <p style="font: 300 14.5px / 1.65 Poppins; color: rgb(201, 201, 210); margin: 0px;">[[Tekst]]</p>
  </div>
  <a href="#kontakt" style="position: relative; flex: 0 0 auto; display: inline-block; padding: 16px 40px 18px 20px; font: 800 16px / 1 Poppins; color: rgb(255, 255, 255); text-decoration: none; border-left: 6px solid rgb(255, 255, 255); border-bottom: 6px solid rgb(255, 255, 255); border-bottom-left-radius: 20px;">[[Zapytaj o realizację]]</a>
</div>
```

- Każde zdjęcie w case study z `data-pdw-zoom` (we wzorcu dwóch brakuje, usterka 12).
- Klienci z nazwy tylko tacy, którzy już są pokazani na stronach serwisu, w tym samym kontekście.
  Opublikowane strony case study: `/case-study/`, `/case-study/zamek-sulkowskich/`, `/case-study-wosp/`.
- Pas CTA nie zapowiada „wkrótce” rzeczy, których nie ma (usterka 13). Treść pasa to zaproszenie do kontaktu.
- **POPRAWKA**: `min(100%, 340px)`.

### K13. Sekcja nagród (blok wyróżniony z dużym zdjęciem)

Źródło: 1019, sekcja 08 (`id="nagrody"`), zrzut `wzorzec-d-08-nagrody.png`.

```html
<!-- K13 blok nagrod -->
<section id="nagrody" style="padding: 20px 0px 78px; scroll-margin-top: 56px;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px;">
    <div style="background: rgb(245, 245, 245); border-radius: 52px 52px 14px; overflow: hidden; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); align-items: center;">
      <div style="padding: 52px 48px;">
        <span style="display: inline-block; font: 600 13px / 1 Poppins, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(18, 56, 140); margin: 0px 0px 14px;">[[Etykieta]]</span>
        <h2 style="font: 700 clamp(26px, 3.4vw, 36px) / 1.14 Poppins, sans-serif; letter-spacing: -0.01em; margin: 0px 0px 16px; color: rgb(20, 20, 20);">[[Nagłówek]]</h2>
        <p style="font: 300 16.5px / 1.7 Poppins, sans-serif; color: rgb(95, 95, 95); margin: 0px 0px 16px; max-width: 520px;">[[Akapit główny]]</p>
        <p style="font: 300 15px / 1.65 Poppins, sans-serif; color: rgb(107, 107, 107); margin: 0px 0px 26px; max-width: 520px;">[[Akapit dodatkowy]]</p>
        <a href="#kontakt" style="position: relative; display: inline-block; padding: 15px 24px 17px 20px; font: 800 15px / 1 Poppins, sans-serif; color: rgb(18, 56, 140); text-decoration: none; border-left: 6px solid rgb(18, 56, 140);">[[Zapytaj o …]]</a>
      </div>
      <div style="position: relative; min-height: 340px; align-self: stretch;">
        <img src="[[URL]]" alt="[[ALT]]" style="position: absolute; inset: 0px; width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom>
        <span style="position: absolute; left: 18px; bottom: 18px; background: rgba(20, 20, 20, 0.72); color: rgb(255, 255, 255); font: 500 13px / 1 Poppins; padding: 8px 15px; border-radius: 20px; pointer-events: none;">[[Branża / materiał]]</span>
      </div>
    </div>
  </div></section>
```

- Padding górny 20 px, bo we wzorcu blok stoi zaraz po szarym case study. Po białej sekcji daj `82px 0px 78px`.
- Do podmiany: etykieta, h2, dwa akapity, tekst przycisku, zdjęcie, pigułka.
- Ten sam blok nadaje się na każdą wyróżnioną usługę (nagrody na stronie grawerowania, inny wyróżnik
  na frezowaniu). Bez obietnic „osobna strona powstaje” (usterka 13).
- **POPRAWKA**: `min(100%, 300px)` i `pointer-events: none` na pigułce.

### K14. Park maszynowy: blok ciemny z liczbami + karty maszyn

Źródło: 1019, sekcja 09 (`id="technologia"`), zrzuty `wzorzec-d-09-park.png`, `wzorzec-m-09-park.png`. Sekcja biała.

```html
<!-- K14 park maszynowy -->
<section id="technologia" style="padding: 82px 0px; scroll-margin-top: 56px;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px;">
    <div style="background: rgb(20, 20, 20); border-radius: 52px 52px 14px; overflow: hidden; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));">
      <div style="position: relative; min-height: 360px;">
        <img src="[[URL zdjęcia maszyny]]" alt="[[ALT: co to za maszyna]]" style="position: absolute; inset: 0px; width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom>
      </div>
      <div style="padding: 50px 48px; color: rgb(255, 255, 255);">
        <span style="display: inline-block; font: 600 13px / 1 Poppins; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(127, 176, 245); margin: 0px 0px 14px;">[[Etykieta]]</span>
        <h2 style="font: 700 clamp(24px, 3vw, 32px) / 1.15 Poppins, sans-serif; margin: 0px 0px 14px; color: rgb(255, 255, 255);">[[Park maszynowy …]]</h2>
        <p style="font: 300 15.5px / 1.7 Poppins; color: rgb(201, 201, 210); margin: 0px 0px 30px; max-width: 520px;">[[Akapit]]</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 26px;">
          <div><div style="font: 800 30px / 1 Poppins; color: rgb(77, 148, 247);">[[liczba]]</div><p style="font: 300 13px / 1.4 Poppins; color: rgb(154, 154, 166); margin: 8px 0px 0px;">[[podpis liczby]]</p></div>
          <!-- zwykle 3 liczby -->
        </div>
      </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 18px; margin-top: 18px;">
      <div style="background: rgb(28, 28, 28); border-radius: 30px 8px 30px 30px; padding: 28px 26px; color: rgb(255, 255, 255); display: flex; flex-direction: column;">
        <span style="align-self: flex-start; font: 600 10.5px / 1 Poppins; letter-spacing: 0.1em; text-transform: uppercase; color: rgb(127, 176, 245); background: rgba(127, 176, 245, 0.12); padding: 6px 11px; border-radius: 12px 3px 12px 12px; margin-bottom: 18px;">[[Przeznaczenie]]</span>
        <h3 style="font: 700 20px / 1.2 Poppins, sans-serif; margin: 0px 0px 4px; color: rgb(255, 255, 255) !important;">[[Marka i model]]</h3>
        <p style="font: 300 13px / 1.5 Poppins; color: rgb(154, 154, 166); margin: 0px 0px 18px;">[[Jedno zdanie o maszynie]]</p>
        <div style="margin-top: auto; display: flex; flex-direction: column; gap: 9px;">
          <div style="display: flex; justify-content: space-between; gap: 12px; border-top: 1px solid rgb(46, 46, 46); padding-top: 9px;"><span style="font: 300 12.5px / 1.3 Poppins; color: rgb(138, 138, 148);">[[Pole robocze]]</span><span style="font: 600 12.5px / 1.3 Poppins; color: rgb(232, 232, 238);">[[2510 × 1680 mm]]</span></div>
          <!-- 3 wiersze parametrów na kartę -->
        </div>
      </div>
    </div>

    <p style="font: 300 15px / 1.7 Poppins, sans-serif; color: rgb(107, 107, 107); text-align: center; max-width: 720px; margin: 34px auto 0px;">[[Podsumowanie pod kartami]]</p>
  </div></section>
```

- Do podmiany: wszystkie `[[…]]`. Bez zmian: kolory, promienie, wiersz parametru (`border-top: 1px solid rgb(46, 46, 46)`
  to skrót, jest bezpieczny).
- Każda liczba i każdy parametr musi mieć źródło. Zakresy zapisujemy dywizem bez spacji: `180-500 W`, `60-120 W`
  (wzorzec ma tu 4 półpauzy, usterka 1). Wymiary ze znakiem `×` ze spacjami: `2510 × 1680 mm`.
- Gdy modeli albo parametrów nie ma w źródłach (np. frezarki CNC), karta zostaje, a w miejscu wierszy
  parametrów stoi ramka K01 z pytaniem do klienta. Nie zgadujemy parametrów.
- Liczby w nagłówku nie mogą przeczyć kartom ani akapitowi (usterka 4: „400 W” obok „do 500 W” i „180-500 W”).
- Zdjęcie producenta (np. `wyc-trotec.jpg`) wolno pokazać tylko jako zdjęcie maszyny, z alt mówiącym o maszynie.
- **POPRAWKA**: `min(100%, 320px)` i `min(100%, 220px)`.

### K15. Pas logotypów

Źródło: 1019, sekcja 10, zrzut `wzorzec-d-10-logotypy.png`. Biała sekcja po białej, padding górny 20 px.

```html
<!-- K15 pas logotypow -->
<section style="padding: 20px 0px 82px;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px; text-align: center;">
    <span style="display: inline-block; font: 600 13px / 1 Poppins; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(18, 56, 140); margin: 0px 0px 12px;">Zaufali nam</span>
    <h2 style="font: 700 clamp(24px, 3.4vw, 34px) / 1.15 Poppins, sans-serif; margin: 0px 0px 10px; color: rgb(20, 20, 20);">Współpracujemy z największymi</h2>
    <p style="font: 300 16px / 1.6 Poppins; color: rgb(107, 107, 107); max-width: 600px; margin: 0px auto 40px;">Tworzyliśmy produkty dla wielu rozpoznawalnych marek.</p>
    <img src="https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-klienci.png" alt="Logotypy klientów: Time Trend, Sokołów, PKP, Dajar, Centrum Nauki Kopernik, iGF" style="width: 100%; max-width: 920px; height: auto; display: block; margin: 8px auto 0px;" loading="lazy" decoding="async">
    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 48px; max-width: 920px; margin: 36px auto 0px;">
      <img src="https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-willson-brown.png" alt="Willson &amp; Brown" style="height: 34px; width: auto; display: block;" loading="lazy" decoding="async">
      <img src="https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-uniwersytet.jpg" alt="Uniwersytet Warszawski" style="height: 84px; width: auto; display: block;" loading="lazy" decoding="async">
    </div>
  </div></section>
```

- Cały blok bez zmian, te same pliki logotypów co na 1019. Nie dopisujemy nowych marek.
- Logotypy bez `data-pdw-zoom`. W `alt` pojedynczy `&amp;` jest w porządku (zakazany jest tylko podwójny).

### K16. FAQ na `<details>`

Źródło: 1019, sekcja 11 (`id="faq"`), zrzut `wzorzec-d-11-faq.png`. Sekcja `#F5F5F5`, kontener 860 px.

```html
<!-- K16 FAQ -->
<section id="faq" style="padding: 82px 0px; background: rgb(245, 245, 245); scroll-margin-top: 56px;">
  <div style="max-width: 860px; margin: 0px auto; padding: 0px 24px;">
    <div style="text-align: center; margin-bottom: 38px;">
      <span style="display: inline-block; font: 600 13px / 1 Poppins; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(18, 56, 140); margin: 0px 0px 12px;">FAQ</span>
      <h2 style="font: 700 clamp(26px, 3.8vw, 38px) / 1.12 Poppins, sans-serif; margin: 0px; color: rgb(20, 20, 20);">Najczęstsze pytania</h2>
    </div>
    <div style="background: rgb(255, 255, 255); border-radius: 40px 12px 40px 40px; padding: 10px 28px;"><details class="pdw-faq" style="border-bottom:1px solid #eee;"><summary style="display:flex;justify-content:space-between;align-items:center;gap:18px;cursor:pointer;list-style:none;padding:22px 2px;font:600 16.5px/1.4 Poppins,sans-serif;color:#141414"><span>[[Pytanie?]]</span><span class="pdw-faq-znak" style="flex:0 0 auto;font:400 28px/1 Poppins;color:#12388C">+</span></summary><p style="margin:0;padding:0 2px 24px;font:300 15px/1.7 Poppins,sans-serif;color:#5A5A60">[[Odpowiedź]]</p></details><details class="pdw-faq" style="border-bottom:none;"><summary style="display:flex;justify-content:space-between;align-items:center;gap:18px;cursor:pointer;list-style:none;padding:22px 2px;font:600 16.5px/1.4 Poppins,sans-serif;color:#141414"><span>[[Ostatnie pytanie?]]</span><span class="pdw-faq-znak" style="flex:0 0 auto;font:400 28px/1 Poppins;color:#12388C">+</span></summary><p style="margin:0;padding:0 2px 24px;font:300 15px/1.7 Poppins,sans-serif;color:#5A5A60">[[Odpowiedź]]</p></details></div>
  </div></section>
```

- Klasy `pdw-faq` i `pdw-faq-znak` są potrzebne (arkusz chowa systemowy trójkąt i powiększa „+” po otwarciu).
- Ostatnie pytanie ma `style="border-bottom:none;"` (wzorzec ma tam dwa sprzeczne `border-bottom`, usterka 17).
- Znak zostaje „+”. Nie zamieniamy go na znak minus (U+2212 jest zakazany regułą 1 i łapie go kontrola).
- Wzorzec ma 4 pytania. Do podmiany: pytania i odpowiedzi; etykieta i h2 mogą zostać.

### K17. Kontakt z formularzem CF7

Źródło: 1019, sekcja 12 (`id="kontakt"`), zrzut `wzorzec-d-12-kontakt.png`.

```html
<!-- K17 kontakt -->
<section id="kontakt" style="padding: 82px 0px 92px; scroll-margin-top: 56px;">
  <div style="max-width: 1220px; margin: 0px auto 40px; padding: 0px 24px; text-align: center;">
    <h2 style="font: 800 clamp(28px, 4vw, 42px) / 1.12 Poppins, sans-serif; margin: 0px 0px 14px; color: rgb(20, 20, 20); letter-spacing: -0.01em;">[[Masz projekt do …?]]</h2>
    <p style="font: 300 17.5px / 1.65 Poppins; color: rgb(107, 107, 107); max-width: 600px; margin: 0px auto;">[[Prześlij pomysł lub plik. …]]</p>
  </div>
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap: 56px; align-items: start;">
    <div style="background: rgb(22, 38, 77); color: rgb(255, 255, 255); border-radius: 30px 30px 130px; padding: 46px 44px;">
      <h2 style="font: 800 clamp(24px, 3vw, 30px) / 1.15 Poppins, sans-serif; margin: 0px 0px 16px; color: rgb(255, 255, 255); letter-spacing: -0.01em;">Skontaktuj się z nami</h2>
      <p style="font: 700 16px / 1.45 Poppins; margin: 0px 0px 32px; color: rgb(255, 255, 255);">Masz pytania?<br><span style="font-weight: 600; color: rgb(195, 204, 223);">Chętnie pomożemy</span></p>
      <div class="pdw-form">[contact-form-7 id="480"]</div>
    </div>
    <div style="padding-top: 6px;">
      <img src="https://grawerowanie-laserowe.pl/wp-content/uploads/2024/02/padir-logo.png" alt="Padir" style="height: 66px; display: block; margin-bottom: 36px;" loading="lazy" decoding="async">
      <div style="display: flex; flex-direction: column; gap: 22px; margin-bottom: 36px;">
        <div><div style="font: 600 11px / 1 Poppins; letter-spacing: 0.1em; text-transform: uppercase; color: rgb(18, 56, 140); margin-bottom: 6px;">Telefon</div><a href="tel:+48227413655" style="font: 700 18px / 1 Poppins; color: rgb(20, 20, 20); text-decoration: none;">+48 22 741 36 55</a></div>
        <div><div style="font: 600 11px / 1 Poppins; letter-spacing: 0.1em; text-transform: uppercase; color: rgb(18, 56, 140); margin-bottom: 6px;">E-mail</div><a href="mailto:laser@padir.pl" style="font: 700 18px / 1 Poppins; color: rgb(20, 20, 20); text-decoration: none;">laser@padir.pl</a></div>
        <div><div style="font: 600 11px / 1 Poppins; letter-spacing: 0.1em; text-transform: uppercase; color: rgb(18, 56, 140); margin-bottom: 6px;">Adres</div><span style="font: 300 16px / 1.4 Poppins; color: rgb(20, 20, 20);">ul. Matuszewska 14, Warszawa</span></div>
      </div>
      <div style="background: rgb(245, 245, 245); border-radius: 28px 8px 28px 28px; padding: 30px 32px;">
        <div style="font: 700 14px / 1 Poppins; letter-spacing: 0.06em; text-transform: uppercase; color: rgb(20, 20, 20); margin-bottom: 14px;">Godziny otwarcia</div>
        <p style="font: 300 14.5px / 1.7 Poppins; color: rgb(78, 75, 102); margin: 0px 0px 16px;">Poniedziałek - Piątek: 8:30 - 16:00<br>Budynek C2, wejście T9</p>
        <p style="font: 300 13.5px / 1.7 Poppins; color: rgb(107, 107, 107); margin: 0px;">PADIR Ewa Salabura<br>Matuszewska 14, 03-876 Warszawa<br>NIP: 536-104-65-17</p>
      </div>
    </div>
  </div></section>
```

- Do podmiany: TYLKO h2 sekcji i lead nad kartami (np. „Masz projekt do grawerowania?”). Dane firmy,
  godziny, logo, karta formularza: bez zmian.
- Formularz: dokładnie `<div class="pdw-form">[contact-form-7 id="480"]</div>`. Kod pól generuje WordPress
  z formularza 480 (pola z klasami `form-label`, `form-input`, `form-textarea`, `form-policy`, `form-btn`).
  Wygląd daje arkusz z `00-poczatek.html` (reguły `.pdw .pdw-form …`): etykiety 11 px wersalikami `#9FB3E0`,
  pola bez ramek z linią dolną `2px solid rgba(255,255,255,.32)` (po kliknięciu biała), zgoda 12 px `#C3CCDF`
  z checkboxem 20 px w kolorze `#12388C`, przycisk „Wyślij” 800 16 px z białą kreską z lewej (hover `#9FB3E0`),
  błędy `#FFC9C9`, komunikat wysyłki w ramce `12px 4px 12px 12px`, spinner odwrócony do bieli.
  Wszystko to działa tylko wewnątrz `.pdw-form` na granatowej karcie. Nie piszemy pól ręcznie (tak zrobił
  szkic 2530 i formularz niczego nie wysyłał).
- W lokalnym podglądzie zamiast pól widać tekst `[contact-form-7 id="480"]`. To normalne: shortcode
  rozwija dopiero WordPress.
- **POPRAWKA**: `min(100%, 320px)`.

---

## 4. Usterki wzorca, których NIE kopiujemy

Wynik `python3 -I sprawdz_szkic.py zrodla/pages-1019-wycinanie-laserowe.raw.html`: kod 1, 4 błędy, 2 ostrzeżenia.

| # | usterka | gdzie | co robimy |
|---|---|---|---|
| 1 | **4 półpauzy** w zakresach mocy: SP500 „60[półpauza]200 W”, Q500 i Speedy 360 „60[półpauza]120 W”, Speedy 300 „25[półpauza]120 W” (błędy `[pauza]` w kontroli) | K14, karty maszyn | tylko dywiz: `60-200 W` |
| 2 | **„od A do Z”** w h2 „Projekt od A do Z” (ostrzeżenie kontroli) | K12 | inny nagłówek |
| 3 | **„najwyższej jakości”** w karcie „Gwarancja udanego produktu” (ostrzeżenie kontroli) | K06 | konkret zamiast wypełniacza |
| 4 | liczba **„400 W” / „maks. moc cięcia”** w nagłówku parku przeczy akapitowi („moc do 500 W”) i karcie SP2000 („180-500 W”). Kontrola łapie tylko frazę „do 400 W”, więc to przechodzi | K14 | liczby tylko ze źródeł, spójne z kartami |
| 5 | **zepsute `@keyframes chevBounce`**: w arkuszu klatki mają przedrostek `.pdw` (`.pdw 0%,.pdw 100%{…}`), przeglądarka odrzuca je i animacja ma zero klatek. Strzałka w hero stoi w miejscu (sprawdzone w Chromium: `chevBounce:` bez klatek) | arkusz | poprawny `@keyframes` w arkuszu dodatków (sekcja 6) |
| 6 | **napis „szkic”** w rogu 4 ilustracji kroków (CSS zamienia go na „SZKIC” na produkcji; kontrola szuka tylko wersalików, więc małe litery przechodzą) + ilustracje zastępcze + lead „właśnie tutaj zdjęcia opowiadają historię najlepiej”, choć zdjęć nie ma | K11 | bez napisu, lead zgodny z tym, co widać |
| 7 | **martwe linki `href="#"`** na dwóch przyciskach „Zobacz pełny case” (kontrola kotwic wymaga co najmniej jednego znaku po `#`, więc ich nie łapie) | K12 | link do opublikowanej strony albo bez przycisku |
| 8 | **siatki `minmax(340px, 1fr)` itp. bez `min(100%, …)`**: na 360 px treść case study wychodzi 36 px poza białą kartę (tekst i zdjęcia ucięte przez `overflow-x: clip`), hero 4 px; na 390 px case study traci prawy margines | K02, K12 i inne | `minmax(min(100%, N), 1fr)` |
| 9 | **galeria na sztywno `repeat(2/3, …)`** bez wersji mobilnej: na 390 px trzy kafle po ok. 100 px, pigułki ucięte („Personaliza…”, „Oznakowan…”) | K08 | `auto-fit` + `min(100%, 260px)`, na portfolio K09 |
| 10 | **to samo zdjęcie dwa razy w galerii** (`padir-realizacja-statuetka-z-plexi.jpg` w rzędzie 2 i 3; jest też w karcie materiału) | K08 | każde zdjęcie raz na stronę, chyba że to hero i galeria |
| 11 | **zdjęcie nie pokazuje tego, co podpis**: `padir-realizacja-azurowy-panel-dekoracyjny.jpg` to wnętrze kawiarni BOKO (kanapa, stoliki, logo na ścianie), a ma pigułkę „Ażur / sklejka” i alt „Ażurowy element dekoracyjny ze sklejki”. Ten sam błędny alt jest w `media.json` (dowód: `wzorzec-kontrola-azur.png`) | K08 | nie używać tego pliku jako ażuru; podpisywać tylko obejrzane zdjęcia |
| 12 | **niespójne `data-pdw-zoom`**: główne zdjęcie BOKO i `wyc-boko-wnetrze.jpg` w case study nie powiększają się | K12 | każde zdjęcie z treścią ma `data-pdw-zoom` |
| 13 | **zapowiedzi rzeczy, których nie ma**: „Osobna strona poświęcona nagrodom powstaje, wkrótce…”; pas „Wkrótce / Elewacja budynku na event… Pełny case z galerią już wkrótce” (tymczasem `/case-study/zamek-sulkowskich/` jest już opublikowane) | K12, K13 | nie zapowiadamy; linkujemy tylko do tego, co jest |
| 14 | **wielkie litery w środku nagłówka**: „Wycinanie Laserowe”, „Precyzja Lasera” (po polsku zapis zdaniowy; 1397 ma poprawnie „Nasze realizacje”) | K02 | `Grawerowanie<br>laserowe`, `Frezowanie<br>CNC` |
| 15 | **zdania sklejone przecinkiem** zamiast kropki lub dwukropka: „jedna precyzja, zobacz z bliska”, „pod każdy projekt, moc, prędkość, ostrość”, „powstaje, wkrótce znajdziesz”, „Precyzja Lasera perfekcja” (brak znaku między częścią szarą i czarną) | K02, K08, K11, K13 | kropka, dwukropek; szary początek podtytułu kończy się kropką |
| 16 | `font: … Poppins` bez rodziny zapasowej w części stylów (np. `font: 300 15px / 1.65 Poppins`) | wiele | w NOWYCH elementach pisz `Poppins, sans-serif`; skopiowane style zostawiamy |
| 17 | ostatnie pytanie FAQ ma `border-bottom:1px solid #eee; border-bottom:none;` | K16 | tylko `border-bottom:none;` |
| 18 | ikony ◆ ✓ ★ i strzałki SVG bez `aria-hidden` (czytnik ekranu czyta „romb”, „gwiazdka”) | K02, K06, K11 | `aria-hidden="true"` (dodane w katalogu) |
| 19 | słabe kontrasty arkusza formularza: placeholder 4,17:1, linia pola 2,79:1 | K17 (arkusz) | znane, arkusza nie zmieniamy (spójność z 1019); nie przenosić tych wartości na inne elementy |

Usterki 1397 (strona realizacji), których też nie przenosimy, jeśli coś z niej bierzemy:
- `<h3 class="pdr-h3">` bez stylu inline z `!important` (44 błędy `h3-kolor` w kontroli; na 1397 ratuje je
  reguła z arkusza `.pdr-real`, na stronie `.pdw` motyw pomalowałby je na biało);
- `style="…;border-color:transparent"` na aktywnej zakładce filtra (błąd `border-wp`);
- szarość `#9A9AA6` na jasnym tle (2,55-2,78:1) i biały tekst na pomarańczowej plakietce (3,37:1);
- liczniki na zakładkach wpisane na sztywno i nieaktualne: „Wszystkie 45” przy 44 kartach, „Wycinanie 20” przy
  19 kartach z `cut` (skrypt przelicza tylko licznik nad siatką).

Usterki szkicu 2530 (wzoru konwencji), których nie przenosimy: nawias z `border-width` i `border-*-color`
(kwadrat zamiast L), zdjęcia hero bez `eager`, formularz wpisany ręcznie zamiast CF7, „do 400 W” i
„1650 × 2510”, żółty znacznik „DO POTWIERDZENIA” w tekście (bierzemy tylko `p.pdw-uwaga`).

Zdjęcia, których nie używamy jako realizacji: grafiki wygenerowane przez AI z biblioteki (np. id 1120 i 1113,
slug zaczyna się od `dall`), zdjęcia prasowe producentów (tylko jako zdjęcie maszyny), zdjęcia zamku
Sułkowskich z łukami z dzianiny (to cudza instalacja).

---

## 5. Rekomendacja dla portfolio: hybryda (anatomia `.pdr-card` w technice 1019)

**Decyzja:** karty w budowie `.pdr-card` z 1397 (zdjęcie 4:3, plakietka usługi w kolorze kategorii, tytuł h3,
materiał wersalikami), złożone stylami inline wewnątrz `.pdw`, z `data-pdw-zoom` i lightboxem 1019.
Bez arkusza `.pdr-*`, bez kontenera `.pdr-real`, bez skryptu filtrów 1397.

Dlaczego tak:
- **Spójność z 1397**: ta sama anatomia karty, ten sam promień `34px 10px 34px 34px`, ta sama typografia
  (h3 700 17,5 px, materiał 600 11 px `0.08em` granatowy), te same plakietki kategorii, te same tytuły, materiały
  i zdjęcia (dane z `zrodla/realizacje-karty.json`, czyli z zatwierdzonej galerii). Klient przechodzący z
  „Realizacji” na stronę usługi widzi te same karty.
- **Spójność z 1019**: jeden kontener `.pdw`, style inline, jeden lightbox (skrypt z 98 bez zmian), tła sekcji
  i zasada „karta przeciwna do tła” bez zmian.
- **Bez dublowania `.pdr-*`**: kafle 1019 (K08) nie mają tytułu ani materiału, a pełne `.pdr-card` wymagałyby
  przeniesienia ponad 100 reguł arkusza `.pdr-real` i drugiego skryptu z drugim lightboxem. Filtrów na stronie
  jednej usługi nie potrzeba.
- **Działa na telefonie** (zrzut `wzorzec-hybryda-360.png`), w przeciwieństwie do galerii 1019 (usterka 9).

### Kod (sekcja portfolio na białym tle, jak slot 04 we wzorcu)

```html
<!-- K09 portfolio -->
<section id="portfolio" style="padding: 82px 0px; scroll-margin-top: 56px;">
  <div style="max-width: 1220px; margin: 0px auto; padding: 0px 24px;">
    <div style="max-width: 700px;">
      <span style="display: inline-block; font: 600 13px / 1 Poppins, sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: rgb(18, 56, 140); margin: 0px 0px 14px;">Portfolio</span>
      <h2 style="font: 700 clamp(26px, 3.8vw, 38px) / 1.12 Poppins, sans-serif; letter-spacing: -0.01em; margin: 0px 0px 14px; color: rgb(20, 20, 20);">Galeria realizacji</h2>
      <p style="font: 300 17px / 1.65 Poppins, sans-serif; color: rgb(107, 107, 107); margin: 0px;">[[Lead galerii]]</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); gap: 22px; margin-top: 44px;">
      <article class="pdw-karta" style="background: rgb(245, 245, 245); border-radius: 34px 10px 34px 34px; overflow: hidden; display: flex; flex-direction: column;">
        <div style="position: relative; aspect-ratio: 4 / 3; overflow: hidden; background: rgb(238, 241, 247);"><img src="[[pelne]]" alt="[[alt]]" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy" decoding="async" data-pdw-zoom><span style="position: absolute; left: 16px; bottom: 16px; background: [[kolor plakietki]]; color: [[kolor tekstu plakietki]]; font: 600 12.5px / 1 Poppins, sans-serif; padding: 8px 15px; border-radius: 20px; pointer-events: none;">[[plakietka]]</span></div>
        <div style="padding: 20px 24px 24px; display: flex; flex-direction: column; gap: 10px;">
          <h3 style="font: 700 17.5px / 1.3 Poppins, sans-serif; margin: 0px; color: rgb(20, 20, 20) !important;">[[tytul]]</h3>
          <div style="font: 600 11px / 1 Poppins, sans-serif; letter-spacing: 0.08em; text-transform: uppercase; color: rgb(18, 56, 140);">[[material]]</div>
        </div>
      </article>
    </div>
    <p style="margin: 34px 0px 0px;"><a href="/przykladkowe-realizacje/#galeria" style="position: relative; display: inline-block; padding: 15px 40px 17px 20px; font: 800 15px / 1 Poppins, sans-serif; color: rgb(20, 20, 20); text-decoration: none; border-left: 6px solid rgb(20, 20, 20); border-bottom: 6px solid rgb(20, 20, 20); border-bottom-left-radius: 20px;">Zobacz wszystkie realizacje</a></p>
  </div></section>
```

Pola z `zrodla/realizacje-karty.json` (bez przepisywania, 1:1):

| w kodzie | pole JSON |
|---|---|
| `[[pelne]]` | `pelne` (pełny plik; NIE `miniatura`, bo lightbox powiększa dokładnie `src`) |
| `[[alt]]` | `alt` |
| `[[tytul]]` | `tytul` |
| `[[material]]` | `material` |
| `[[plakietka]]` | `plakietka` |

Plakietki (kolor tła; kolor tekstu):

| `plakietka` | `[[kolor plakietki]]` | `[[kolor tekstu plakietki]]` |
|---|---|---|
| Grawerowanie | `#12388C` | `rgb(255, 255, 255)` |
| Wycinanie | `#175C43` | `rgb(255, 255, 255)` |
| Frezowanie | `#DE6B24` | `rgb(20, 20, 20)` (POPRAWKA kontrastu względem 1397: 5,47 zamiast 3,37) |

Dobór kart:
- **Grawerowanie**: karty z `plakietka == "Grawerowanie"` (21 w JSON). Pokazujemy 9 albo 12 (pełne rzędy po 3).
  Karty z `kategorie` „cut eng” i plakietką „Wycinanie” pomijamy, żeby na stronie grawerowania nie było zielonych plakietek.
- **Frezowanie**: wszystkie 6 kart z `plakietka == "Frezowanie"` (2 rzędy po 3).
- Kolejność dowolna, ale bez powtórzeń zdjęć z hero i K07 na tej samej stronie. Przed użyciem obejrzyj
  zdjęcia (`kontaktowka.py`), nawet jeśli tytuł jest zatwierdzony.
- Klasa `pdw-karta` jest potrzebna tylko do efektu najechania z sekcji 6 (podniesienie karty i lekki zoom
  zdjęcia, jak `.pdr-card:hover` na 1397).
- Link pod siatką prowadzi do opublikowanej galerii 1397 (`id="galeria"` istnieje na tamtej stronie).

Wariant na szarej sekcji (gdy składacz postawi portfolio na `#F5F5F5`, zrzut `wzorzec-hybryda-na-szarym.png`):
karta dokładnie jak `.pdr-card` na 1397, czyli
`style="background: rgb(255, 255, 255); border: 1px solid #EDEDED; border-radius: 34px 10px 34px 34px; overflow: hidden; display: flex; flex-direction: column;"`.
`border: 1px solid #EDEDED` to dozwolony skrót. Domyślnie obie strony używają wariantu na białym tle,
żeby wyglądały tak samo.

---

## 6. Własne reguły CSS

Zasady:
1. Arkusz `00-poczatek.html` zostaje bajt w bajt. Własne reguły idą w DRUGI `<style>` postawiony zaraz po nim
   (wewnątrz `<div class="pdw">`, przed ramką K01 i `<header>`).
2. Każdy `<style>` ma `data-no-optimize="1" data-no-minify="1" data-no-ucss="1"`.
3. Każdy selektor zaczyna się od `.pdw ` (np. `.pdw .pdw-karta:hover`). Nowe klasy mają przedrostek `pdw-`.
   Wyjątek: nazwa `@keyframes` jest globalna; nowe animacje nazywamy z przedrostkiem `pdw`.
4. W arkuszu (także w komentarzach) obowiązują reguły treści: bez półpauz i myślników, bez podwójnego
   ampersandu, bez znaku minus. Kontrola czyta cały plik, nie tylko tekst.
5. Zakaz `border-width` / `border-*-color` dotyczy atrybutów `style="…"`. W arkuszu wolno ich użyć,
   ale nadal najprościej pisać skróty.
6. Stylesheet nie nadpisze stylu inline bez `!important`. Lepiej poprawić styl inline niż dokładać
   `!important` w arkuszu. Wyjątek: reguły dla `@media`, które mają zmienić układ inline (unikaj ich, siatki
   z `min(100%, …)` tego nie wymagają).
7. Arkusz dodatków jest identyczny na obu stronach. Jeśli jeden składacz potrzebuje nowej reguły, zgłasza ją
   do katalogu, a nie dopisuje sam.

Arkusz dodatków (wklejany 1:1 na obu stronach):

```html
<style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">
/* pdw-dodatki: wspolne dla szkicow grawerowania i frezowania */
@keyframes chevBounce{0%,100%{transform:translateY(0)}50%{transform:translateY(7px)}}
.pdw .pdw-karta{transition:transform .24s cubic-bezier(.2,.7,.2,1),box-shadow .24s}
.pdw .pdw-karta:hover{transform:translateY(-6px);box-shadow:0 26px 50px -30px rgba(20,20,20,.5)}
.pdw .pdw-karta img{transition:transform .4s cubic-bezier(.2,.7,.2,1)}
.pdw .pdw-karta:hover img{transform:scale(1.05)}
@media (prefers-reduced-motion:reduce){.pdw *{animation:none!important;transition:none!important}.pdw .pdw-karta:hover,.pdw .pdw-karta:hover img{transform:none}}
</style>
```

- Druga definicja `@keyframes chevBounce` wygrywa z zepsutą z arkusza 1019 (przy tej samej nazwie obowiązuje
  ostatnia), więc strzałka w hero zaczyna działać bez ruszania arkusza wzorca (sprawdzone w Chromium:
  `chevBounce:0%, 100%|50%`).
- Efekt najechania kopiuje `.pdr-card:hover` i `.pdr-card:hover .pdr-shotbtn img` z 1397.
- `prefers-reduced-motion` wyłącza animacje, jak na 1397.

---

## 7. Kontrola przed oddaniem (każdy składacz)

1. `python3 -I sprawdz_szkic.py praca/<katalog>/<plik>.html --szkic` kończy się kodem 0, bez `[[` i `]]`.
2. Dokładnie jeden `<h1>`; wszystkie `<h3>` z `color: … !important`; zdjęcia hero `eager`, reszta `lazy`.
3. Siatki z `min(100%, …)`; podgląd na 360 px bez treści wystającej poza karty.
4. Każdy zakres liczbowy z dywizem; każdy fakt ze źródłem albo ramka K01.
5. Kotwice `#kontakt`, `#proces`, `#portfolio` mają swoje sekcje; żadnego `href="#"`.
6. Jedna ramka „Wersja robocza” na górze; ramki „Do potwierdzenia” tylko jako `p.pdw-uwaga`.
7. Na końcu dokładnie `98-koniec.html`, bez drugiej kopii skryptu.
