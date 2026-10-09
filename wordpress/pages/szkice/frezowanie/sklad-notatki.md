# Frezowanie CNC: notatki ze składu

Plik wynikowy: `praca/frezowanie/strona.html` (zapis bloków WordPressa, jeden blok `wp:html` w grupie `alignfull`).
Treść: 1:1 z `praca/frezowanie/tresc.md`, bez zmian merytorycznych i bez nowych faktów. Literówek do poprawy nie znalazłem.

## Kontrola

- `python3 -I sprawdz_szkic.py praca/frezowanie/strona.html --szkic`: **kod 0**, 0 błędów, 0 ostrzeżeń
  (58,8 tys. znaków, 1 `<h1>`, 20 obrazków, 10 ramek `pdw-uwaga`).
- Opakowanie: początek pliku jest bajt w bajt `zrodla/1019-sekcje/00-poczatek.html`, koniec bajt w bajt
  `98-koniec.html` (warstwa `.pdw-lb` + skrypt lightboxa bez zmian). Skrypt występuje raz, nie doklejałem `99-skrypt-lightbox.js.html`.
- Kotwice: `#kontakt` (2×: hero, ciemny pas), `#proces`, `#portfolio`; wszystkie mają sekcje z `id`. Żadnego `href="#"`.
  Każde `id` występuje raz (`materialy`, `portfolio`, `proces`, `technologia`, `faq`, `kontakt`).
- Linki wewnętrzne (8, wszystkie `publish` w `SPIS.json`): `/wycinanie-laserowe/`, `/grawerowanie-laserowe/`,
  `/blog/obrobka-tworzyw-sztucznych/`, `/przykladkowe-realizacje/#galeria`, `/blog/ciecie-przemyslowe/`, `/produkty/`,
  `/uslugi-dla-przemyslu/`, `/wycinanie-laserowe/#technologia`.
- `data-pdw-zoom`: 15 zdjęć z treścią (4 hero, 3 materiały, 6 portfolio, 1 „Na czym to polega”, 1 park). Bez niego: 3 logotypy
  klientów i logo Padir w kontakcie.
- Podgląd lokalny w Chromium (bez motywu, zdjęcia zdalne zablokowane), 1280 px i 360 px: brak przewijania w bok, żaden element
  nie wychodzi poza ekran; `@keyframes chevBounce` ma klatki `0%, 100%|50%` (działa poprawka z arkusza dodatków).
  Kadrów zdjęć w tym podglądzie nie widać; dobór i kadry zdjęć sprawdzał autor treści (`kont-1.png`, `kont-7-kwadraty.png`).
  Pliki podglądu usunąłem po sprawdzeniu.

## Komponenty per sekcja

| # | sekcja | tło / padding | komponenty | źródło kodu |
|---|---|---|---|---|
| - | arkusze | - | arkusz 1019 (z `00-poczatek.html`) + arkusz dodatków | `00-poczatek.html`, `wzorzec.md` rozdz. 6 (1:1) |
| 0 | ramka-robocza | - | K01 ramka górna | `wzorzec.md` K01 |
| 1 | hero `<header>` | białe, `56px 0px 72px` | K02 (siatka 2x2 + nawias L), K03 A + B, K04 | `01-wycinanie-laserowe.html` |
| 2 | dlaczego-padir | białe, `82px 0px` | K05 wyśrodkowany, K06 (◆ czarna, ✓ szara, ★ szara) | `02-tw-j-pomys-nasza-realizacja.html` |
| 3 | materialy `#materialy` | `#F5F5F5`, `82px 0px` | K05, K07 (3 białe karty), 2× K01 (M1, M2) | `03-materialy.html` |
| 4 | portfolio `#portfolio` | białe, `82px 0px` | K05, K09 (6 kart, wariant na białym), K01 (P1), K03 A-mały | `wzorzec.md` rozdz. 5 + dane z `realizacje-karty.json` |
| 5 | na-czym-to-polega | białe, `36px 0px 78px` | K10 (zdjęcie z granatowym nawiasem + tekst), K01 (N1) | `05-skoncentrowane-wiat-o-zamias.html` |
| 6 | proces `#proces` | `#F5F5F5`, `78px 0px 26px` | K05, K11 (4 karty, ilustracje SVG) | `06-proces.html` |
| 7 | laser-i-frez | `#F5F5F5`, `0px 0px 78px` | K01 (L1), K12 ciemny pas CTA z K03 A-ciemny, K01 (L2) w pasie | `07-realizacje.html` (pas pod kartami) |
| 8 | technologia `#technologia` | białe, `82px 0px` | K14 (blok ciemny + 3 liczby + 2 karty maszyn), K01 (T1) w karcie | `09-technologia.html` |
| 9 | zaufali-nam | białe, `20px 0px 82px` | K15, K01 (Z1) | `10-wsp-pracujemy-z-najwi-kszymi.html` |
| 10 | faq `#faq` | `#F5F5F5`, `82px 0px` | K16 (5 pytań), K01 (F1) | `11-faq.html` |
| 11 | kontakt `#kontakt` | białe, `82px 0px 92px` | K17 (CF7 `[contact-form-7 id="480"]`) | `12-kontakt.html` |

Naprzemienność teł jak na 1019: białe (hero, dlaczego) / szare (materiały) / białe (portfolio + na czym, jeden blok) /
szare (proces + laser-i-frez, jeden blok jak 06 + 07 na 1019) / białe (park + logotypy) / szare (FAQ) / białe (kontakt).

## Odstępstwa od wzorca 1019 i powody

### Poprawki z katalogu `wzorzec.md` (świadomie inne niż 1019)

1. Wszystkie siatki `auto-fit`/`auto-fill`: `minmax(min(100%, N), 1fr)` zamiast `minmax(N, 1fr)` (usterka 8, treść wychodziła
   poza karty na 360 px). Na desktopie wygląd bez zmian.
2. `aria-hidden="true"` na strzałce SVG w hero, ikonach ◆ ✓ ★ i ilustracjach kroków (usterka 18).
3. Drugi `<style>` (arkusz dodatków z `wzorzec.md` rozdz. 6, 1:1): poprawny `@keyframes chevBounce` (usterka 5), efekt najechania
   `.pdw-karta` jak `.pdr-card:hover` na 1397, `prefers-reduced-motion`. Innych własnych reguł CSS nie dodawałem.
4. Kroki procesu bez napisu „szkic” w rogu ilustracji (usterka 6).
5. Ostatnie pytanie FAQ ma tylko `border-bottom:none;` (usterka 17).
6. h1 zapisem zdaniowym `Frezowanie<br>CNC` (usterka 14); szary początek podtytułu kończy się kropką (usterka 15).

### Nawias L w hero

Skopiowany z produkcyjnego 1019 razem z `border-top: 0; border-right: 0;` przed skrótami
`border-left: 11px solid …; border-bottom: 11px solid …;` (tak każe zadanie i tak jest dziś na 1019). Katalog `wzorzec.md` te dwa
zera pomija jako niepotrzebne; są nieszkodliwe, a kontrola `border-wp` przechodzi. Żadnego `border-width` ani `border-*-color`
w stylach inline. Zdjęcia hero: `loading="eager" fetchpriority="high" data-no-lazy="1"`, kolejność atrybutów jak na 1019.

### Układ sekcji (wg `tresc.md`)

7. **Slot 07 (case study K12, karty A i B) i slot 08 (nagrody K13) pominięte.** W ich miejscu sekcja „laser-i-frez”: ramka L1
   i sam ciemny pas K12. Powód z `tresc.md`: realizacje CNC mają po jednym zdjęciu i nie mają opisu, karta case study byłaby
   zmyślona; nagrody to temat lasera. Pas otwiera sekcję, więc ma `margin-top: 0px` zamiast `26px`; sekcja procesu ma padding
   dolny `26px` zamiast `78px`, żeby odstęp karty kroków → pas był taki jak karty case study → pas na 1019. Sekcja pasa nie ma `id`.
8. **Materiały: 3 karty zamiast 6** (9 kadrów z frezarki w serwisie, reszta materiałów bez potwierdzenia trafia do ramek M1, M2).
   Siatka 280 px daje na desktopie 1 rząd po 3.
9. **Portfolio: K09 (hybryda `.pdr-card`) zamiast kafli K08** (rekomendacja `wzorzec.md` rozdz. 5, spójność z
   `/przykladkowe-realizacje/`). 6 kart z `plakietka == "Frezowanie"`, tytuł, materiał, alt i pełny plik 1:1 z
   `realizacje-karty.json`. Plakietka `#DE6B24` z tekstem `rgb(20, 20, 20)` zamiast białego z 1397 (kontrast 5,47 zamiast 3,37).
   Bez arkusza i skryptu `.pdr-*`; lightbox ten sam co na 1019.
10. **Park maszynowy: 2 karty zamiast 5.** Karta frezarki ma jeden wiersz parametru (pole robocze) i w miejscu pozostałych
    wierszy ramkę T1 (zasada K14). Karta laserów zbiorcza z trzema wierszami. Zakresy i wymiary: dywiz / `×` ze spacjami,
    bez półpauz z 1019 (usterka 1). Akapit pod kartami linkuje do parku na 1019 zamiast opisu „wiele innych maszyn”.
11. **Pas logotypów:** te same pliki i alty co na 1019, zmienione h2 i lead (powtarzałyby się z 1019, 1011 i główną, R2 w `linki.md`).
12. **FAQ: 5 pytań zamiast 4** (wg `tresc.md`).
13. **Kontakt:** zmienione tylko h2 i lead nad kartami; karta formularza, dane firmy, godziny i logo bez zmian.

### Nowy element

14. **Ilustracja kroku 03** narysowana od nowa (wzorzec ma tu wiązkę lasera): belka, wrzeciono, oprawka, frez palcowy ze spiralą,
    strzałka obrotu, płyta w rzucie izometrycznym z wyfrezowaną kieszenią (widać ścianki i dno), 4 wióry. Ten sam styl co reszta:
    `viewBox="0 0 200 240"`, `stroke="#12388C"`, `stroke-width="2.4"`, zaokrąglone końce, wypełnienia tylko `#12388C` i `#eef1f7`.
    Ilustracje 01, 02 i 04 skopiowane z `06-proces.html` bez zmian rysunku (dodane tylko `aria-hidden`).

### Ramki szkicu (10 × `p.pdw-uwaga`)

Styl dokładnie z BRIEF; zmieniałem tylko `margin` (i tam, gdzie trzeba, szerokość), zgodnie z miejscami z `tresc.md`:

| ramka | miejsce | margines / uwagi |
|---|---|---|
| ramka górna | zaraz po arkuszach, przed `<header>` | wariant K01 `margin:24px auto 0;width:calc(100% - 48px);max-width:1172px` |
| M1, M2 | materiały, pod siatką (nie w siatce) | `26px 0 0`, `12px 0 0` |
| P1 | portfolio, pod siatką, przed przyciskiem | `26px 0 0` |
| N1 | „Na czym to polega”, kolumna tekstu pod akapitem 2 | `18px 0 0` |
| L1 | nad ciemnym pasem | `0 0 18px` |
| L2 | w pasie, pod akapitem, w kolumnie tekstu | `14px 0 0` |
| T1 | karta frezarki, pod wierszem „Pole robocze” | `margin:0` (**decyzja składu**: `tresc.md` nie podaje marginesu; ramka stoi w kolumnie flex z `gap: 9px`, a domyślne `0 0 26px` zostawiłoby pusty pas na dole karty) |
| Z1 | pod logotypami | `30px auto 0`, `max-width:920px`; dodane `text-align:left` (**decyzja składu**: sekcja ma `text-align: center`, a pozostałe ramki są wyrównane do lewej) |
| F1 | pod białym pudełkiem FAQ, poza `<details>` | `22px 0 0` |

Ramki nie stoją w `<p>`, `<a>`, `<h*>` ani `<summary>` i nie są bezpośrednim dzieckiem żadnej siatki.

### Czego nie przeniosłem z 1019

Półpauz w parametrach, „400 W” w nagłówku parku, „od A do Z”, „najwyższej jakości”, martwych `href="#"`, zapowiedzi
„wkrótce”, zdjęć ani case’ów z wycinania (Bondi Sands, BOKO), komentarzy HTML z nazwami komponentów (1019 ich nie ma).
Style skopiowane z 1019 z `font: … Poppins` bez rodziny zapasowej zostawiłem bez zmian (usterka 16: nie ruszamy skopiowanych).

## Dla prowadzącego

- Przy przenoszeniu na 1011 przełączyć szablon z `frezowanie-cnc` na `page-no-title` (inaczej będą dwa `<h1>`).
- W WordPressie formularz `[contact-form-7 id="480"]` rozwinie się sam; w lokalnym podglądzie widać sam skrót.
