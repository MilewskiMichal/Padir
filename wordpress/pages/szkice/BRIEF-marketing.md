# Brief: szkic strony branżowej „Usługi dla marketingu”

Czytaj RAZEM z `S/BRIEF.md` (reguły techniczne, treściowe, językowe i konwencja
szkicu obowiązują w całości). Ten plik mówi, co jest INNE przy tej stronie.

## Zadanie

Zleceniodawca (13.10.2026): „Przygotuj szkic zakładki »działania w branży
marketingowej« jako kolejną Branżę, dla której pracujemy. W tym marketingu
puchary, statuetki etc. i co tam jeszcze można, np. upominki grawerowane.”

To NOWA strona branżowa, rodzeństwo dwóch opublikowanych:
- `/uslugi-dla-przemyslu/` (2264), `S/zrodla/pages-2264-uslugi-dla-przemyslu.raw.html`
- `/uslugi-dla-horeca/` (2283), `S/zrodla/pages-2283-uslugi-dla-horeca.raw.html`

Obie stoją w menu „Produkty” jako „Usługi dla przemysłu” i „Usługi dla HoReCa”.
Nowa strona: tytuł roboczy „Usługi dla marketingu”, slug `uslugi-dla-marketingu`,
szablon `page-no-title`. Zostanie zapisana jako NIEOPUBLIKOWANA (robi to
człowiek prowadzący, nie agenci). Zleceniodawca zaakceptuje ją z klientem (Padir).

Odbiorca strony: działy marketingu firm, agencje reklamowe i eventowe, organizatorzy
konkursów, gal i firmowych wydarzeń. Intencja: zamówienie (wycena), nie poradnik.

## Szablon: komponenty `.pdl`, NIE `.pdw`

Strony branżowe mają własny zestaw komponentów i własny arkusz:
- opakowanie: `<!-- wp:group {"align":"full",...} -->` → `<div class="wp-block-group alignfull" ...>` →
  `<!-- wp:html -->` → `<div class="pdl">` z arkuszem `<style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">` W ŚRODKU kontenera,
  sekcje `<section class="pdl-hero">`, `<section class="pdl-sec">` i `<section class="pdl-sec pdl-sec--wash">` na przemian;
- na końcu niebieski pas `.pdl-band` z przyciskami do `/kontakt/` i `/przykladkowe-realizacje/` (strony branżowe NIE mają formularza CF7);
- FAQ na `<details class="pdl-q">`.
Kopiuj arkusz i markup z 2283/2264, podmieniając teksty, zdjęcia i linki.

Znane usterki szablonu branżowego, których NIE kopiujemy (sprawdzone):
1. Zdjęcia w hero mają `loading="lazy"`. W nowej stronie hero: `loading="eager" fetchpriority="high" data-no-lazy="1"`.
2. Martwe kotwice: na HoReCa `href="#produkty"`, na Przemyśle `href="#uslugi"`, a takich id nie ma. W nowej stronie każde `href="#x"` ma `id="x"`.
3. Kontrast: `--pdl-grey:#9a9aa6` na białym tle to 2,78:1 (podpisy liczb w hero), biały tekst na rdzawej plakietce `#DE6B24` to 3,37:1. W nowej stronie szarość tekstu min. 4,5:1 (np. `#6b6b76` na białym, policz), a plakietki z tekstem 11-13 px muszą mieć min. 4,5:1.
4. Wszystko, co zgłasza `python3 -I sprawdz_szkic.py <plik> --pdl` na 2283/2264.

Sprawdzarka dla tej strony: `cd S && python3 -I sprawdz_szkic.py praca/marketing/strona.html --pdl` (kod 0 = czysto, BEZ --szkic).
Podgląd w prawdziwym motywie da się zrobić dopiero po zapisie szkicu (robi to człowiek prowadzący).
Do własnych zrzutów: Playwright, `chromium.launch(executable_path="/opt/pw-browsers/chromium")`, plik lokalny
`S/marketing/zywa-horeca.html` (kopia żywej strony HoReCa z arkuszami i fontami na dysku) jako rama: podmień w niej
`<div class="pdl">…</div>` na swój kontener (zdjęcia z sieci mogą się nie wczytać).

## Bez żółtych ramek (decyzja zleceniodawcy, 13.10.2026)

Na tej stronie NIE MA ramek „Do potwierdzenia z klientem” ani ramki „Wersja robocza do akceptacji”.
Konwencja szkicu z BRIEF.md w tej części NIE obowiązuje. Twierdzenie bez źródła nie trafia do tekstu.
Pytania do klienta zapisujemy wyłącznie w `S/praca/marketing/pytania.md`.

## Fakty specjalne (mają pierwszeństwo przed starszymi źródłami)

Informacje od zleceniodawcy, wolno ich używać jako faktów (źródło: „zleceniodawca, 13.10.2026”):
- W branży marketingowej Padir robi: puchary, statuetki, upominki grawerowane. Szczegółów (z czego są puchary,
  czy Padir robi całe puchary, czy grawer/tabliczki na gotowych, nakłady, terminy) NIE podał: to pytania do klienta.
- Napisy przestrzenne „Tea” i „Team” z galerii realizacji były CIĘTE LASEREM: lustrzana plexi na sklejce.
  W galerii mają dziś plakietkę „Frezowanie”, to błąd. Na tej stronie: wycinanie laserowe.
- Ceny i terminy obowiązujące: najniższa cena za realizację to 100 zł; grawer w ciągu 2 dni albo od ręki
  za dodatkową opłatą. NIE pisać o progu 12 sztuk dla szkła (to dotyczyło HoReCa i jest w trakcie wyjaśniania).

„Co jeszcze można” dla marketingu: wolno proponować tylko rzeczy, które Padir już robi według źródeł
(`S/zrodla/`), np. napisy i logo przestrzenne, ścianki i dekoracje na event, ekspozytory z plexi, gadżety
i upominki z logo, opakowania, tabliczki. Pomysł bez pokrycia w źródłach = pytanie „Czy robicie X?” w pytania.md, a nie twierdzenie na stronie.

## Kanibalizacja

Serwis ma już: `/grawerowanie-laserowe/prezenty/` (1812, prezenty), wpis `/blog/firmowe-prezenty-z-grawerem/`
(2177, prezenty firmowe), wpis o 5 branżach (2009), szkic wpisu o długopisach (1841, NIEopublikowany: nie linkować).
Strona marketingowa = segment klienta (marketing, agencje, eventy) i zamówienie. Prezenty firmowe tylko jako
jedna z usług z linkiem do istniejących treści, bez powielania ich zdań.

## Pliki wynikowe

Wszystko w `S/praca/marketing/` (katalog już istnieje albo go załóż). Każdy agent pisze tylko do swoich plików.
