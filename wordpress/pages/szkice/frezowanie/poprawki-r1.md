# Frezowanie CNC: poprawki po rundzie 1 weryfikacji

Plik: `praca/frezowanie/strona.html`. Wszystkie 27 uwag okazały się zasadne co do problemu i wszystkie są wprowadzone.
Żadnej nie odrzuciłem w całości. W kilku odrzuciłem pojedyncze elementy proponowanej poprawki, każdy z powodem
przy uwadze: „dysze chłodziwa” (25), „płyta z tworzywa” (3), miejsce bloku i osobna ramka (5), anchor „Wycinanie laserowe”
(9d), wyliczenie „plexi, sklejki i MDF” (8/9b), „nie zaczynamy od zera” (20), 30% (26), „nie wiadomo, czy grubość
wystarczy” (18), „białej płycie” (24), „grubych” (7), tekst FAQ 1 (13). Na uwagę 10 nie poszło skrócenie FAQ 3.
Zmiany treści przeniesione 1:1 do `tresc.md`, źródła w `ksiega.json` (192 wpisy, `narzedzia-fz/sprawdz_ksiege.py`: 0 błędów).

Kontrola końcowa:
- `python3 -I sprawdz_szkic.py praca/frezowanie/strona.html --szkic`: **kod 0**, 0 błędów, 0 ostrzeżeń, 20 zdjęć, 1 h1, 10 ramek.
- Podgląd w Chromium z motywem (`r1-frezowanie-kontrola/render.py`, zrzuty `r1-*.png`): 1440, 390 i 360 px bez przewijania
  w bok, 0 elementów ze złym kontrastem, bez zdublowanych `id`. Konspekt nagłówków: pas „Laser i frez razem” ma
  teraz własne h2, a nie piąte h3 pod „Cztery kroki”.
- Tekst `tresc.md` porównany maszynowo z widocznym tekstem strony: wszystkie pola i ramki zgodne.
- Nakładanie 5 słów z innymi stronami (`narzedzia-fz/licz_tresc.py`, NG=5): zostały tylko etykiety przycisków wzorca, dane kart
  galerii, „iges stl i pdf z”, „przyjmujemy już od jednej sztuki” i „większe elementy dzielimy na moduły” (zdanie z faktem, bez zmian).

## Oględziny zdjęć (do uwag 3, 24, 25, 26, 27)

Pliki pobrane w pełnej rozdzielczości do `r1-frezowanie-kontrola/`, kadry `object-fit: cover` policzone i obejrzane na
`kadry.png` i `tea-kwadrat.png`, potem sprawdzone w podglądzie (`r1-1440-s00.png`, `-s02`, `-s03`, `-s04`, `-s07`).

Oględziny 2148 (pełny plik 2560x1916 i zbliżenia): frez CNC wycina kontury w jasnoszarej, nieprzezroczystej płycie; wokół białe, skręcone wióry; przy wrzecionie dwie dysze na giętkich niebieskich wężach, z kadru nie wynika, czy podają chłodziwo, czy powietrze.

- 1739 w kadrze 16:10 (karta plexi): wrzeciono, cienki frez, otwór i fragment napisu ALTUGLAS na folii. Biały kolor to
  najpewniej folia ochronna, dlatego w alcie nie piszę „białej płycie”.
- „Tea” w kwadracie: przy 50% ucięte lewe ramię „T”, przy 30% końcówka szeryfu na krawędzi, przy 20% cała litera „T”,
  a „a” lekko przycięte z prawej. Wybrane 20%.
- „Team” 4:3: przy 0% całe „T”; „m” i tak wychodzi poza oryginalny kadr. „Duka” 4:3: przy 25% całe „DUKA”.

## Uwagi

| # | soczewka, waga | uwaga (skrót) | decyzja |
|---|---|---|---|
| 1 | fakty, drobny | ramka L1 pomija case study WOŚP ze zdjęciem 1739 | wprowadzona |
| 2 | fakty, drobny | ramka T1 pyta o wszystkie zbliżenia, a niepewne jest tylko 2148 | wprowadzona |
| 3 | fakty, drobny | alt 2148: „chłodziwo” i „kieszeń” bez pokrycia | wprowadzona (połączona z 25, bez „płyty z tworzywa”) |
| 4 | wzorzec, drobny | dolny padding pasa 78 zamiast 82 px | wprowadzona |
| 5 | technika, ważny | szkic gubi dane strukturalne Service z 1011 | wprowadzona (blok w innym miejscu) |
| 6 | technika, drobny | h3 pasa wpada w konspekcie pod „Cztery kroki” | wprowadzona |
| 7 | język, ważny | lead materiałów: „tych trzech grup” wskazuje złą rzecz | wprowadzona (z poprawką) |
| 8 | język, ważny | zdanie o narożniku wewnętrznym, „mikrodetal”, „akrylu” | wprowadzona |
| 9 | język, ważny | pięć zdań z linkami według jednego szablonu | wprowadzona (z poprawkami) |
| 10 | język, ważny | za dużo trójek | wprowadzona (z poprawkami, jeden wyjątek) |
| 11 | język, drobny | hero: „Tam, gdzie liczy się głębokość” | wprowadzona |
| 12 | język, drobny | h2 „Frezowanie to często tylko część projektu” | wprowadzona (plus zmiana h3 karty 2) |
| 13 | język, drobny | FAQ 1 powtarza kartę „Duży format” | wprowadzona (z poprawką) |
| 14 | język, drobny | „pracownia” 4 razy w parku maszynowym | wprowadzona |
| 15 | język, drobny | „pomyłka” bez wskazania, czyja | wprowadzona |
| 16 | język, drobny | „prowadzi je”, „który zostawia laser” | wprowadzona |
| 17 | język, drobny | FAQ 2 miesza kategorie | wprowadzona (z poprawką) |
| 18 | język, drobny | kroki 01-03 | wprowadzona (krok 02 z poprawką) |
| 19 | język, drobny | „Zaufali nam”: h2, lead, „Lead” w ramce | wprowadzona |
| 20 | język, drobny | FAQ 5 parafrazuje stronę HoReCa | wprowadzona (z poprawką) |
| 21 | język, drobny | „ścianka foto” | wprowadzona |
| 22 | język, drobny | niespójne nazwy w altach (Duka, Tea, Team) | wprowadzona |
| 23 | język, drobny | godziny z dywizami ze spacjami | wprowadzona |
| 24 | zdjęcia, ważny | Team i Duka dwa razy (materiały i galeria) | wprowadzona |
| 25 | zdjęcia, ważny | alt 2148 opisuje kieszeń w przezroczystej płycie | wprowadzona (bez „dysz chłodziwa”) |
| 26 | zdjęcia, drobny | hero: kwadrat ucina „T” w „Tea” | wprowadzona (20% zamiast 30%) |
| 27 | zdjęcia, drobny | galeria: kadr 4:3 ucina „T” w „Team” i „D” w „Duka” | wprowadzona |

### 1. Ramka L1 a case study WOŚP: wprowadzona
Sprawdzone: `zrodla/pages-12-case-study-wosp.raw.html` ma 4 zdjęcia, w tym `IMG_20250116_082620_HDR-766x1024.jpg` (1739),
`SPIS.json`: id 12, `case-study-wosp`, `publish`. Na `wer-fakty-wosp.png` widać przezroczyste panele z otworami w narożnikach
i kadr 1739 z frezem w płycie z folią ALTUGLAS. Zdanie „każda realizacja CNC ma jedno zdjęcie” było nieprecyzyjne.
Zmiana: nowa treść L1 z kandydatem („grawerowane ramki dla WOŚP ze strony /case-study-wosp/”), pytaniem, czy formatki
i otwory szły przez frezarkę i czy można pokazać nazwę WOŚP i Fundacji Ronalda McDonalda, oraz dopiskiem, że to samo zdjęcie
stoi wyżej w karcie plexi. Zamiast „ramki z plexi” piszę „grawerowane ramki” (tak nazywa je strona; materiał ramek nie pada
w tekście case study). Nazwy WOŚP i Fundacji są tylko w ramce, nie w treści strony (reguła treści 4).

### 2. Ramka T1: wprowadzona
Sprawdzone: 2256 (`cnc-drewno.jpg`) na 2264 z altem „Frezowanie CNC detalu w pracowni Padir”; 1739 w case study WOŚP;
2148 nie występuje na żadnej stronie, w `media.json` bez altu. Zmiana: T1 pyta tylko o 2148, opisane słowami
(„zdjęcie frezu w szarej płycie”, plik IMG_20250909_084928, „tu i w sekcji „Na czym to polega””), a o dwóch pozostałych
mówi, że serwis już je pokazuje jako prace pracowni. Numerów mediów nie wstawiałem, klient ich nie zna.

### 3 i 25. Alt zdjęcia 2148: wprowadzone razem, z jednym elementem odrzuconym
Obejrzane pełne zdjęcie i zbliżenia (zapis oględzin wyżej). Obie uwagi mają rację co do „kieszeni” i „przezroczystej
płyty”: płyta jest jasnoszara i nieprzezroczysta, frez idzie wąskim rowkiem po konturze. Uwaga 25 proponuje jednak
„z dwiema dyszami chłodziwa”, a uwaga 3 słusznie zauważa, że żadne źródło nie mówi o chłodzeniu cieczą, a z kadru nie da się
odróżnić chłodziwa od powietrza (wpis 2078 podaje tylko „Odciąg: szczotka przy wrzecionie + odsys”). Odrzucam więc
„dysze chłodziwa” z uwagi 25, a z uwagi 3 nie biorę „płyty z tworzywa” (materiał to domysł), tylko „jasnoszarą płytę”
z uwagi 25. Nowy alt w obu miejscach (K10 i park): „Frez CNC wycina kontury w jasnoszarej płycie, dookoła wióry”.
W księdze usunięte źródło „kieszenie (widoczne na zdjęciu 2148)”, a opis maszyny już nie mówi o kieszeniach.

### 4. Padding pasa: wprowadzona
Sprawdzone: `07-realizacje.html` `padding: 82px 0px`, `06-proces.html` `78px 0px`; szary blok 06+07 kończy się
dolnym odstępem 82 px. Zmiana: `<section style="padding: 0px 0px 82px; …">`. W `tresc.md` poprawione obie wzmianki.
`sklad-notatki.md` (tabela komponentów, wiersz 7) nadal podaje `0px 0px 78px`; nie jest na mojej liście plików,
do poprawienia przez składacza.

### 5. Dane strukturalne: wprowadzona, blok w innym miejscu niż w propozycji
Sprawdzone: 1011 ma na końcu osobny blok `wp:html` z `ld+json` Service (5 osi, aluminium, mosiądz, protokół pomiarowy,
oferta „Frezowanie aluminium i mosiądzu”); tak samo 456, 2264 i 20; wzorzec 1019 bloku nie ma. Szkic nie miał żadnego.
Zmiana: na końcu pliku, za `<!-- /wp:group -->`, osobny blok `<!-- wp:html -->` z `<script type="application/ld+json"
data-no-optimize="1">`, czyli dokładnie tak, jak na 1011, 456 i 2264 (propozycja stawiała go w `.pdw`; osobny blok zostawia
opakowanie `98-koniec.html` bez zmian). Treść według propozycji z dwiema korektami: w `description` są „nośniki pod fronty
z lasera” zamiast samego „detale”, a pozycja katalogu to „Frezowanie tworzyw technicznych i konglomeratu kwarcowego”.
Bez `image` (`#primaryimage`). Każde twierdzenie ma wpis w księdze (sekcja `dane-strukturalne`). Ramki nie dodawałem
osobno: informacja dla klienta jest dopisana na końcu M1, która i tak pyta o metale i 5 osi. W `tresc.md` nowa sekcja 12
i uwaga dla prowadzącego: przy przenoszeniu usunąć stary blok `ld+json` z 1011.

### 6. h3 w ciemnym pasie: wprowadzona
Sprawdzone: na 1019 pas stoi w `#realizacje` pod h2 „Projekt od A do Z”; w szkicu sekcja nie miała h2. Zmiana:
`<h2 style="font: 700 22px / 1.3 Poppins, sans-serif; margin: 0px 0px 8px; color: rgb(255, 255, 255);">`. W podglądzie
z motywem kolor biały, wygląd bez zmian, konspekt poprawny.

### 7. Lead materiałów: wprowadzona z poprawką
Nowy: „Frez wybieramy do grubszych płyt i do obróbki w głąb materiału. Daje też pionową krawędź. Niżej trzy grupy
materiałów, a przy każdej przykłady z naszej frezarki.” Zostawiłem „grubszych” zamiast „grubych” z propozycji, bo tak
mówi źródło (wpis 2293: „ma sens przy grubszych materiałach”).

### 8. Akapit 2 „Na czym to polega”: wprowadzona
Sprawdzone: wpis 2078 „Minimalne promienie wewnętrzne = promień narzędzia. Do mikro-detalu i puzzli lepszy będzie laser.”
Zmiana: „Ograniczeniem jest średnica narzędzia. W narożniku wewnętrznym zawsze zostaje zaokrąglenie o promieniu co najmniej
takim jak promień frezu, dlatego drobny ażur i bardzo małe detale lepiej wychodzą laserem.” Ostatnie zdanie z linkiem
patrz uwaga 9.

### 9. Zdania z linkami: wprowadzona z poprawkami
Każde zdanie przepisane, żadne nie ma już schematu „[temat] opisujemy w [miejsce]”, nazwy zakładek w cudzysłowie.
- (a) karta tworzyw: „Nie wiesz, które tworzywo wybrać? Pomoże poradnik o obróbce tworzyw.” (anchor „poradnik o obróbce
  tworzyw”). Zamiast „Zajrzyj do” z propozycji, bo „zajrzyj” stoi już w (c).
- (b) K10: „Oba narzędzia porównujemy we wpisie o tym, kiedy wybrać laser, a kiedy frez.” Uwaga 9 zostawiała tu wersję
  z uwagi 8 („pokazujemy na przykładzie plexi, sklejki i MDF”), ale uwaga 10 liczy to wyliczenie jako trójkę, więc wybrałem
  zdanie bez wyliczenia. Anchor jak w `linki.md`.
- (c) lead procesu: „Jeśli w projekcie frez spotyka się z laserem, zajrzyj do przeglądu trzech technologii w zakładce
  „Produkty”.”
- (d) park: „Moc i pole robocze każdego z pięciu laserów znajdziesz w opisie parku laserów Trotec na stronie o wycinaniu.”
  Anchor „opisie parku laserów Trotec” zamiast proponowanego „Wycinanie laserowe”, bo ten anchor ma już link #1
  do `/wycinanie-laserowe/`, a zasada z `linki.md` każe anchorowi opisywać cel (tu: park maszyn).
- (e) FAQ 5: „Jeśli zamawiasz dla produkcji albo jako firma OEM, zobacz zakładkę „Usługi dla przemysłu”.”

### 10. Trójki: wprowadzona z poprawkami
- Zostaje jedyna trójka retoryczna „Frez, cięcie i grawer wyceniamy razem”.
- Karta laserów: „Tniemy fronty z połyskiem na krawędzi i grawerujemy oznaczenia.” (jak w propozycji).
- Karta tworzyw: „Z tworzyw technicznych frezujemy bryły z kieszeniami i gniazdami pod montaż.” (jak w propozycji).
- Lead kontaktu: „Wyślij plik STEP albo choćby zdjęcie detalu. Dopisz materiał i wymiary, a przy serii także liczbę sztuk.
  Odeślemy wycenę z terminem.” Zamiast „materiał, wymiar i liczbę sztuk” z propozycji, bo to byłaby kolejna trójka.
- Park: „fronty i oznaczenia” (uwaga 14). Hero i lead materiałów: uwagi 11 i 7. K10: uwaga 9 (b).
- Dodatkowo skrócone dłuższe listy: opis frezarki „Od liter i reliefów po nośniki pod fronty z lasera.” (było „Litery,
  reliefy, kieszenie i nośniki z płyt i bloków.”), lead galerii „Sześć realizacji z frezarki, od napisów z lustrzanej plexi
  po medalion z MDF.”, FAQ 2 (uwaga 17).
- Wyjątek, bez zmian: FAQ 3 („materiału, wielkości, liczby sztuk, stopnia skomplikowania i przygotowania pliku”). To lista
  czynników ceny z wpisu 1660, odpowiedź na pytanie „ile kosztuje”, a nie retoryczna trójka; skrócenie zgubiłoby fakty.
  Akapit 1 K10 („kieszenie, wypukłe litery, fazy i otwory”) też zostaje, bo uwaga 16 go przepisuje i zachowuje.

### 11. Hero: wprowadzona
`<span …>Laser tnie, frez rzeźbi.</span> Napisy przestrzenne i reliefy z grubszych płyt.` Źródła w księdze: cięcie
konturowe laserem (`pages-8`), „przestrzenne kształty, reliefy” i „obróbka przestrzenna” (`pages-8`, wpis 2293).

### 12. h2 „Dlaczego Padir”: wprowadzona, plus zmiana h3 karty 2
h2: „Od frezu po grawer w jednym zleceniu”. Karta 2 miała h3 „Wszystko w jednym zamówieniu”, co obok nowego h2
mówiłoby to samo dwa razy. Nowe h3: „Jedna wycena i jeden termin” (2264: „Jedna oferta, jeden termin, jedna faktura.”).

### 13. FAQ 1: wprowadzona z poprawką
Propozycja („dzielimy na moduły z zamkami i składamy po obróbce”) nadal prawie powtarzała kartę 1 („dzielimy na moduły
i łączymy po obróbce”). Nowa odpowiedź: „W jednym kawałku do 2000 × 3000 mm. Większy napis albo ściankę składamy z modułów
łączonych na zamki. Na drugim końcu skali są detale kilkumilimetrowe.” Źródło zamków: wpis 2078. Karta 1 bez zmian.

### 14. Park maszynowy: wprowadzona
Akapit: „Płyty i bloki frezujemy na polu roboczym 2000 × 3000 mm. Mamy też pięć laserów CO₂ Trotec, więc fronty
i oznaczenia do frezowanych elementów robimy u siebie.” Podpisy: „laserów CO₂ Trotec”, „od tego roku jesteśmy na rynku”
(bliżej źródła: „od 2002 na rynku”).

### 15. Karta „Pojedyncze sztuki i prototypy”: wprowadzona
„Jeśli pomylimy się przy zleceniu, poprawiamy element.” Obietnica jest węższa niż w źródle i nie obejmuje błędu w pliku klienta.

### 16. Akapit 1 „Na czym to polega”: wprowadzona
Tekst dokładnie z propozycji.

### 17. FAQ 2: wprowadzona z poprawką
„Na frezarkę kierujemy zwykle plexi grubszą niż około 10 mm, detale z kieszeniami i reliefami oraz części, które mają
pasować do innych. Laser lepiej sprawdza się przy cienkich płytach i drobnym ażurze.” Wszystkie trzy człony to teraz
przedmioty obróbki. Nie wziąłem „Frezarkę wybieramy”, bo lead materiałów zaczyna się już od „Frez wybieramy”.

### 18. Kroki 01-03: wprowadzona, krok 02 z poprawką
01: „Do frezowania najlepiej przyślij plik STEP.” 03: „Przy serii najpierw frezujemy jedną sztukę wzorcową. Resztę robimy
dopiero wtedy, gdy ją zaakceptujesz.” 02: „Gdy materiał jest nietypowy albo grubość budzi wątpliwości, najpierw robimy
próbę.” Propozycja „nie wiadomo, czy grubość wystarczy” zawężała źródło (wątpliwość może dotyczyć też zbyt grubej płyty),
a wersja „masz wątpliwość co do grubości” dawała 5 słów wprost z wpisu 2078.

### 19. „Zaufali nam”: wprowadzona
h2 „Pracowaliśmy dla tych marek”, lead „Firmy i instytucje z różnych branż, dla których realizowaliśmy zlecenia.”,
w ramce Z1 „Tekst pod nagłówkiem celowo nie łączy tych marek z frezowaniem.”

### 20. FAQ 5: wprowadzona z poprawką
Sprawdzone: 2283 „Archiwizujemy plik wzorcowy i parametry procesu…”, `pages-8` „Parametry procesu i plik wzorcowy trafiają
do archiwum…”. Propozycja „przy dokładce nie zaczynamy od zera” gubiła sedno odpowiedzi (powtórka wychodzi taka sama).
Nowa: „Tak. Plik i ustawienia maszyny z pierwszego zlecenia zachowujemy, więc dokładka wychodzi taka sama jak pierwsza
partia.” plus zdanie (e) z uwagi 9. Kontrola 5 słów nie znajduje już wspólnej frazy z 2283 ani z `pages-8`.

### 21. „ścianka foto”: wprowadzona
„Tak powstała ścianka fotograficzna na barce na Wiśle.”

### 22. Alty: wprowadzona
Hero: „Napis przestrzenny „Tea” ze złotej plexi lustrzanej”. Karta tworzyw: „Frezowany relief „Duka” w bloku z tworzywa,
mierzony suwmiarką”. Alt „Team” w materiałach zniknął razem ze zdjęciem (uwaga 24).

### 23. Godziny otwarcia: wprowadzona
„Poniedziałek-piątek: 8:30-16:00”. Uwaga: na 1019 (`12-kontakt.html` i `raw`) jest dziś „Poniedziałek - Piątek: 8:30 - 16:00”
z dywizami ze spacjami; półpauzy są tylko w starym zapisie `.txt`. Zmiana i tak słuszna wg BRIEF, reguła 1.

### 24. Powtórki zdjęć materiały/galeria: wprowadzona
Sprawdzone: `wzorzec.md` K07 („nie powtarzać się z galerią”, usterka 10); kadry obejrzane. Zmiany: karta plexi dostała
1739 (alt „Cienki frez CNC wycina otwór w płycie z plexi”, bez „białej”, patrz oględziny); K10 dostało 2148 (alt z uwag 3
i 25); „Duka” zostaje w karcie tworzyw; do M2 dopisane pytanie o zdjęcie tworzywa albo grubej plexi. Skutek: galeria
pokazuje „Team” jako nowy kadr. Koszt: 2148 stoi w K10 i w parku maszynowym. Przy 11 miejscach i 9 kadrach dwie powtórki
są nieuniknione; ta jest mniej szkodliwa, bo w parku 2148 jest zastępstwem do czasu zdjęcia frezarki (T1 o nie prosi
i wymienia obie sekcje). Mapa zdjęć w `tresc.md` zaktualizowana.

### 26. Kadr „Tea” w hero: wprowadzona z poprawką
`object-position: 20% 50%` zamiast 30%: przy 30% końcówka lewego szeryfu „T” leży na krawędzi kafla, przy 20% cała litera
jest w kadrze (porównanie na `tea-kwadrat.png`, podgląd `r1-1440-s00.png`).

### 27. Kadry „Team” i „Duka” w galerii: wprowadzona
„Team” `object-position: 0% 50%`, „Duka” `object-position: 25% 50%`; w podglądzie widać całe „T” i całe „DUKA”.

## Pliki

- `praca/frezowanie/strona.html`: wszystkie zmiany wyżej, blok danych strukturalnych na końcu.
- `praca/frezowanie/tresc.md`: treść 1:1 ze stroną, mapa zdjęć, sekcja 12 (dane strukturalne), zestawienia linków
  i ramek, długość (1067 słów, bez stałego bloku kontaktu 995).
- `praca/frezowanie/ksiega.json`: 192 wpisy (było 166): zmienione twierdzenia, usunięte „kieszenie z 2148”, „dysze
  chłodziwa” i „drobny detal laserem”, dodane źródła WOŚP, 2256, danych strukturalnych i oględzin 2148.
- Do poprawy poza moim zakresem: `sklad-notatki.md` (wiersz 7 tabeli: padding `0px 0px 78px`, opis T1 i mapa zdjęć
  sprzed rundy 1), `zdjecia.json` (wpis 2148: „kieszeń w przezroczystej płycie”, „dysze chłodziwa”).
