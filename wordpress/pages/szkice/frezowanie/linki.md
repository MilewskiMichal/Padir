# Frezowanie CNC: plan linkowania wewnętrznego i analiza kanibalizacji

Strona: szkic „Frezowanie CNC”, który zastąpi stronę 1011 `/frezowanie-cnc/` (ten sam adres po akceptacji).
Podstawa: `zrodla/SPIS.json`, `zrodla/pages-*.raw.html` i `.txt`, `zrodla/posts-*.raw.html` i `.txt`, szablon
`zrodla/szablon-frezowanie-cnc.*`, arkusz faktów `praca/frezowanie/fakty.md` (numery F, S, P), wzorzec `praca/wzorzec.md`,
plan siostrzany `praca/grawerowanie/linki.md` (żeby obie nowe strony linkowały się symetrycznie).
Tytuły SEO, opisy meta i treść strony głównej (jej nie ma w `SPIS.json`) odczytałem 2026-10-09 z publicznych stron
serwisu, zwykłym pobraniem strony, bez logowania i bez zapisu. Kopie: `pobrane-fz-meta/`.
Żadnych liczb wyszukiwań: wszystko poniżej wynika z tego, co serwis już pisze, jak nagłówkuje i jak linkuje.
W cytatach tytułów pauzy i półpauzy ze źródła zastąpiłem znacznikiem [pauza], a w zakresach liczb dywizem.

---

## 1. Główna intencja i frazy

### Intencja strony

Handlowa, usługowa i lokalna: ktoś szuka pracowni, która wyfrezuje mu konkretną rzecz (litery i napisy przestrzenne,
relief, nośnik, detal z grubszej płyty albo z tworzywa) i chce szybko sprawdzić: w czym frezujecie, jak duże, co już
zrobiliście, kiedy frez, a kiedy laser, jak zamówić i jak się skontaktować. Strona jest **przeglądem usługi i rozdzielnikiem**:
do galerii, do stron siostrzanych (laser, grawer), do strony przemysłowej i do dwóch poradników, które już dobrze opisują
wybór metody i tworzywa. Wiedza ogólna (czym jest frezowanie, rodzaje frezów, zalety i wady, frezowanie w meblarstwie)
zostaje na blogu.

Tak jest ustawiona siostrzana `/wycinanie-laserowe/` (1019): h1 z nazwą usługi, krótkie sekcje, galeria, „Na czym to
polega”, proces, case, park maszyn, FAQ, formularz. Jej meta: „Wycinanie laserowe plexi, sklejki, drewna, filcu
i tworzyw. Czysta krawędź i powtarzalność przy krótkich seriach. Wycena na podstawie pliku.”

Obecna 1011 jest w połowie poradnikiem: h2 „Na czym polega frezowanie CNC?”, „Nowoczesna technologia”, „Sprawdzone
i uniwersalne rozwiązanie”, pytanie „Jakie są zalety frezowania CNC?”. Te bloki konkurują z wpisami (punkt 2), a nie
pomagają w zamówieniu. Nowa wersja przesuwa stronę w stronę „co, w czym, jak duże, jak zamówić”.

### Pod jakie frazy serwis już ustawia stronę 1011

| gdzie | brzmienie |
|---|---|
| tytuł SEO (strona publiczna) | „Frezowanie CNC - Padir” |
| meta description (strona publiczna) | „Frezowanie CNC w MDF, konglomeracie, drewnie i tworzywach technicznych. Litery przestrzenne, reliefy i detale z zachowaniem tolerancji.” |
| adres | `/frezowanie-cnc/` |
| h1 (szablon `frezowanie-cnc`) | „Frezowanie CNC”, pod nim „Twórz wyjątkowe formy z precyzją CNC” |
| h2 treści 1011 | „Na czym polega frezowanie CNC?”, „Dlaczego warto wybrać Padir?”, „Nowoczesna technologia”, „Sprawdzone i uniwersalne rozwiązanie”, „Frezowanie CNC [pauza] najczęściej zadawane pytania”, „Dokładność, która robi różnicę [pauza] Frezowanie CNC. Twórz z nami stawiając na precyzję i niezawodność.”, „Współpracujemy z największymi”, „Materiały w których frezujemy”, „Frezujemy dla przemysłu i dla gastronomii.” |
| h3/h4 treści 1011 | „Frezowanie w drewnie”, „Frezowanie w metalu”, „Grawerowanie w tworzywach sztucznych” (błąd: grawer w sekcji o frezie); h4 „Nowoczesne technologie”, „Gwarancja udanego produktu”, „Doświadczenie i profesjonalizm” |
| pytania FAQ 1011 | „Jakiej wielkości produkty mogę frezować”, „Jakie są zalety frezowania CNC?”, „Czy oferujemy wsparcie projektowe”, „Czy mogę zamówić frezowanie prototypu?” |

Anchory, którymi serwis linkuje dziś do `/frezowanie-cnc/`:

| anchor | skąd |
|---|---|
| „Frezowanie CNC” | menu „Produkty”, stopka i karta usługi na stronie głównej (odczyt publiczny) |
| „Zobacz więcej” | karta „Frezowanie CNC” na stronie głównej |
| „Zobacz usługę →” | `/produkty/` (8) i `/uslugi-dla-przemyslu/` (2264), karta „Frezowanie CNC” |
| „Poznaj frezowanie CNC” | `/uslugi-dla-przemyslu/`, pod sekcją „Obróbka skrawaniem 3- i 5-osiowa.” |
| „frezowanie CNC” | wpisy 1578 (laser vs frez) i 967 (meble) |
| „Frezowanie w drewnie,” i „Frezowanie drewna” | wpis 1873 (frezowanie drewna; pierwszy anchor ma przecinek w środku linku) |

Wniosek: serwis traktuje 1011 jako stronę główną frazy **„frezowanie CNC”**. Wersji z miastem strona dziś nie ma
(„Warszawa” jest tylko w stopce kontaktowej), choć reszta serwisu konsekwentnie łączy usługi z Warszawą: `/produkty/`
«Grawerowanie laserowe, wycinanie laserowe i frezowanie CNC pod jednym dachem w Warszawie.», meta `/uslugi-dla-horeca/`
«Pracownia w Warszawie.», wpis 2293 h2 «Wycinanie laserowe w Warszawie», strona główna «Od 2002 roku w pracowni na
warszawskim Targówku». Nowa strona: h1 „Frezowanie CNC” (jak h1 „Wycinanie Laserowe” na 1019), fraza i miasto
w tytule SEO, pozostałe nagłówki opisowe, bez powtarzania frazy w każdym h2.

Fraza poboczna, którą 1011 już ma w meta i którą potwierdza galeria: **litery i napisy przestrzenne, reliefy**
(`zrodla/pages-1397-przykladkowe-realizacje.txt` «napisy przestrzenne oraz detale frezujemy na maszynach CNC w MDF,
konglomeracie i tworzywach technicznych»; `zrodla/pages-8-produkty.txt` «grubsze materiały, przestrzenne kształty,
reliefy i litery 3D»). To naturalny wyróżnik strony CNC wobec 1019, pod warunkiem rozgraniczenia z laserem (R2).

### Frazy rozproszone dziś po innych stronach i wpisach

| temat / fraza | gdzie już jest |
|---|---|
| „frezowanie CNC” w tytule | wpis 1578 (tytuł SEO „Wycinanie Laserowe vs. Frezowanie CNC [pauza] Porównanie Technologii”), wpis 967 („Frezowanie CNC w nowoczesnym designie mebli: Od koncepcji do realizacji”), wpis 1660 (h2 „1. Jak przygotować plik do grawerowania laserowego lub frezowania CNC?”), strona główna (h1 „Cięcie laserowe, grawerowanie i frezowanie CNC”), `/blog/` („Poznaj bliżej świat grawerowania laserowego i frezowania CNC”) |
| „czym jest / na czym polega frezowanie (CNC)” | 1011 h2 „Na czym polega frezowanie CNC?”, wpis 1578 h2 „Czym jest Frezowanie CNC?”, wpis 1873 h2 „Czym jest frezowanie?”, wpis 967 h2 „Wprowadzenie do frezowania CNC…”, szkic 1829 „Czym jest frezowanie oraz co warto o nim wiedzieć?” |
| zalety i wady frezowania CNC | 1011 FAQ „Jakie są zalety frezowania CNC?”, wpis 1578 h2 „Zalety Frezowania CNC” i „Wady Frezowania CNC” |
| laser czy frez, CNC vs laser | wpis 2078 (tytuł „Cięcie przemysłowe: CNC vs laser [pauza] jak świadomie wybrać metodę do akrylu, sklejki i MDF”, meta „Akryl, sklejka, MDF: kiedy laser, a kiedy frez.”), wpis 1578 (całość), wpis 2147 h2 „CNC czy laser: praktyczne wskazówki wyboru”, wpis 2208 h2 „Laser a CNC i ręczne znakowanie [pauza] czym to się różni?”, wpis 2293 h2 „Wycinanie laserowe a inne metody” |
| frezowanie drewna / w drewnie / sklejki | 1011 h3 „Frezowanie w drewnie”, wpis 1873 (tytuł „Frezowanie drewna [pauza] na czym polega i jakie efekty można uzyskać?”), szkic 1823 (frezowanie sklejki), `/produkty/` karta „Drewno i sklejka: Grawer, cięcie i frezowanie.” |
| frezowanie metalu, aluminium, mosiądzu, obróbka 3- i 5-osiowa | 1011 h3 „Frezowanie w metalu” i karta „Usługi dla przemysłu”, `/uslugi-dla-przemyslu/` (h2 „Obróbka skrawaniem 3- i 5-osiowa.”, h4 „Aluminium i stopy Al”, „Mosiądz i miedź”), szkic 1797 (frezowanie aluminium) |
| frezowanie / obróbka tworzyw sztucznych | 1011 h3 „Grawerowanie w tworzywach sztucznych”, wpis 2147 (tytuł „Obróbka tworzyw sztucznych: od projektu do powtarzalnej produkcji”, h2 „Obróbka CNC: kiedy i za co płacimy”), `/uslugi-dla-przemyslu/` h4 „Tworzywa techniczne”, szkic 1845 |
| frezowanie w meblarstwie, panele 3D, panele akustyczne | wpis 967 (całość), 1011 h2 „Sprawdzone i uniwersalne rozwiązanie” |
| litery i napisy przestrzenne, litery 3D, reliefy | meta 1011, `/produkty/` karta „Frezowanie CNC”, galeria 1397 (6 kart „Frezowanie”), wpis 2078 («duże litery 3D z akrylu 15-20 mm»); te same litery pokazuje laser: 1019 karta „Drewno i sklejka” («Litery, panele ścienne»), 1397 karty „Podświetlana litera „R””, „Logo przestrzenne „BOKO”” z plakietką „Wycinanie” |
| pole robocze frezarki 2000 × 3000 mm | 1011 (treść i FAQ), wpis 1660 h3 „4. Jak duże jest pole robocze laserów i frezarki?”, wpis 2078 (FAQ) |
| plik do frezowania (STEP) | `/produkty/` FAQ „Jakie pliki przyjmujecie?”, `/uslugi-dla-przemyslu/` FAQ „Jakie pliki przyjmujecie do cięcia i frezowania?”, wpis 1660 h2 nr 1 |
| cięcie, frezowanie i grawer w jednym zleceniu | `/produkty/` (h2 „Od czego zacząć? Od tego, co ma powstać.” i FAQ „Można zamówić cięcie, frezowanie i grawerowanie w jednym zleceniu?”), `/uslugi-dla-przemyslu/` (lead i FAQ „Czy mogę zlecić w jednym zamówieniu cięcie, frezowanie i grawerowanie?”) |
| ekspozytory, POS, nośniki pod fronty | wpis 2078 (mini-case ścianki na barce), wpis 2043 (h2 „Technologie produkcji: laser, frezarka, gięcie, grawerowanie”) |
| park maszyn CNC | nigdzie jako sekcja; tylko wpis 2078 h2 „Parametry maszyn a praktyka” (ploter Kimla, dane katalogowe, F21 i F22) |

---

## 2. Ryzyka kanibalizacji i jak nowa strona ma się odróżnić

Zasada podziału ról (ta sama co w planie grawerowania):
- **1011 (nowa)**: intencja handlowa, przegląd usługi: w czym frezujemy, jak duże, co zrobiliśmy, kiedy frez, a kiedy laser, jak zamówić;
- **strony segmentowe** (`/uslugi-dla-przemyslu/`, `/uslugi-dla-horeca/`): konkretny klient i jego szczegóły;
- **strony siostrzane** (`/wycinanie-laserowe/`, `/grawerowanie-laserowe/`): inne technologie tej samej pracowni;
- **`/produkty/`**: rozdzielnik trzech technologii (rodzic w menu);
- **wpisy**: poradniki, porównania i wiedza ogólna.

### R1. `/uslugi-dla-przemyslu/` (2264): frezowanie metali, 3 i 5 osi (największe ryzyko)
Strona przemysłowa ma własną sekcję CNC z h2 „Obróbka skrawaniem 3- i 5-osiowa.”, listą metali, protokołem
pomiarowym, kartą „Frezowanie CNC” i FAQ o plikach. Obecna 1011 kopiuje zdanie z tej strony prawie dosłownie (karta
„Usługi dla przemysłu”, fakty F23) i ma h3 „Frezowanie w metalu” z branżami „motoryzacja, lotnictwo i inżynieria”.
- Nowa 1011 NIE ma sekcji ani h2/h3 o metalu, obróbce 3- i 5-osiowej ani branżach przemysłowych. Metale i 5 osi tylko
  w żółtej ramce „Do potwierdzenia z klientem” (fakty S1, S2, pytania P03, P04).
- NIE kopiować: karty z 2264 i z 1011, listy norm (IATF, AS9100, ISO 13485), zdania „Wysoka gładkość powierzchni, bez
  śladów mocowania” (F34), statystyki „±0,01 mm dokładność pozycjonowania” (F33), terminów „24 do 48 godzin” i „24-72 h”
  (dotyczą serii znakowanych, S7).
- Jeden link do 2264 (punkt 3, link #7) z anchorem bez „3- i 5-osiowa” i bez metali, dopóki klient tego nie potwierdzi.
- Po akceptacji: jeśli klient nie potwierdzi metali i 5 osi, trzeba poprawić 2264, bo jej link „Poznaj frezowanie CNC”
  prowadzi wprost z tej obietnicy na nową 1011. Jeśli potwierdzi, 1011 dostaje jedno zdanie i link, a szczegóły zostają na 2264.

### R2. Siostra `/wycinanie-laserowe/` (1019): litery przestrzenne, plexi, sklejka
Obie strony mogą pokazywać litery, plexi i sklejkę. Laser ma na 1019 kartę „Drewno i sklejka” z „Litery, panele ścienne”
i w galerii litery z plakietką „Wycinanie”.
- Granica, którą serwis już opisał (wpis 2078): laser to cienkie plexi do ok. 10 mm, drobny detal, ażur, krawędź
  z połyskiem; frez to grubsze plexi, pion krawędzi, pasowanie, gniazda, fazy, otwory, materiały „no-laser”
  (`zrodla/posts-2078-ciecie-przemyslowe.txt` «Akryl powyżej ~10 mm: CNC dla pełnego pionu i pasowania.», «Dibond/PC:
  praktycznie zawsze CNC.»). Karty materiałów na 1011 piszemy z tej perspektywy, a nie jako listę „to samo co na 1019”.
- Nagłówek sekcji materiałów w stylu 1019 („W czym tniemy laserowo”), np. „W czym frezujemy”. Tytuły kart to materiały
  z akcentem CNC: „Grube plexi i plexi lustrzana”, „MDF, sklejka i drewno”, „Tworzywa techniczne”, „Konglomerat kwarcowy”,
  „Dibond i poliwęglan”, „Pianka PVC” (fakty F40-F46). Nie „Frezowanie w drewnie” (h3 obecnej 1011 i temat wpisu 1873).
- Bloki wzorca, które łatwo skopiować razem z treścią:
  - **„Dlaczego Padir”** (slot 02, K06): 1019, obecna 1011 i obecna 456 mają te same trzy karty „Nowoczesne
    technologie / Gwarancja udanego produktu / Doświadczenie i profesjonalizm”. Nowa 1011 bierze komponent, ale pisze
    własne karty z konkretem frezu (np. jedno zlecenie z laserem i grawerem, pole 2000 × 3000 mm, próbka przy nowym
    materiale; F03, F20, F49, F66). Obietnica poprawki (F73) może zostać, bez „najwyższej jakości”.
  - **Park maszynowy** (slot 09, K14): pięciu kart Trotec nie kopiujemy. Na 1011 park CNC (żółta ramka P01, P02,
    pole 2000 × 3000 mm jako fakt) i jedno zdanie o laserach z linkiem do `/wycinanie-laserowe/#technologia` (link #8).
  - **Nagrody** (slot 08, K13, `#nagrody` na 1019): nie powtarzać. Slot 08 lepiej wykorzystać na blok „laser i frez
    w jednym projekcie” (nośnik frezem, front laserem, F04) albo na krótkie „dla kogo frezujemy” (S11: bez tezy
    „głównie przemysł i gastronomia”).
  - **Case study** (slot 07, K12): case’y 1019 (Bondi Sands, BOKO) to cięcie laserowe. Nie przypisywać ich frezowi (F94).
  - **FAQ**: 1019 ma „Jak duże elementy można wycinać?” i „Jak długo trwa proces wycinania?”. Na 1011 pytania o frez,
    pisane od nowa.
  - **Logotypy**: pas logo może zostać w kontekście ogólnym, bez nagłówka „Współpracujemy z największymi” (ten sam h2
    jest dziś na 1011, 1019 i stronie głównej) i bez sugestii, że te firmy zamawiały frezowanie (F92, P24).

### R3. Wpisy porównawcze: 2078 (CNC vs laser), 1578 (laser vs frez), 2147 (CNC czy laser w tworzywach), sekcja w 2208
Pięć miejsc odpowiada na „laser czy frez”. Najlepszy i najbardziej konkretny jest 2078 (autor z pracowni, grubości,
tolerancje jako wskazówka, mini-case).
- Na 1011 najwyżej krótki akapit w sekcji „Na czym to polega” (slot 05): dwa, trzy fakty (pion krawędzi, ograniczenie
  średnicą frezu, akryl powyżej ok. 10 mm) i link do 2078 (link #5). Bez h2 „Laser czy CNC”, „CNC vs laser”,
  „Wycinanie laserowe vs frezowanie CNC”.
- NIE powielać: listy „Decyzja w 30 sekund”, tolerancji ±0,1-0,2 i ±0,3-0,5 mm jako tabeli (to rada projektowa, F32),
  zdań o „karmelowej” krawędzi sklejki, opisu wrzeciona, ATC i stołu próżniowego (F21, F22: to opis maszyny
  z katalogu, nie potwierdzony stan Padiru), „99% zleceń” i „o połowę” (liczby bez źródła).
- Z 1011 do 1578 nie linkujemy: wpis ma frazę „Frezowanie CNC” w tytule, a link z usługi przekazywałby mu sygnał
  na frazę strony. Do tego ogólniki bez pokrycia („Frezowanie CNC jest szeroko stosowane w przemyśle maszynowym,
  lotniczym, motoryzacyjnym”). Wpis 1578 już linkuje do 1011 anchorem „frezowanie CNC” i tak ma zostać.

### R4. Wpisy poradnikowe z frazą w tytule: 967 (meble), 1873 (frezowanie drewna)
- Nie używać h2 „Na czym polega frezowanie CNC?” (obecna 1011), „Czym jest frezowanie (CNC)?” (1578, 1873, szkic 1829).
  Sekcja w slocie 05 ma własny opisowy nagłówek, tak jak „Skoncentrowane światło zamiast noża” na 1019.
- Nie wracają: pytanie „Jakie są zalety frezowania CNC?” (1578 ma h2 „Zalety” i „Wady”), akapit o meblach, elektronice,
  panelach 3D i akustycznych (1011, wpis 967; bez realizacji Padiru, F54), rodzaje frezów i frezarek (1873, szkice 1797,
  1823), „symulacje CAD/CAM” (P17).
- Wpis 1873 jest poradnikiem dla majsterkowicza (frezarki górno- i dolnowrzecionowe, kierunki posuwu), a nie opisem
  usługi; linkuje do 1011 anchorami „Frezowanie w drewnie,” i „Frezowanie drewna” i to wystarczy. Z 1011 najwyżej
  link z rezerwy.
- Wpis 967 opisuje meblarstwo ogólnie. Link z 1011 sugerowałby, że Padir robi meble i fronty, czego serwis nie pokazuje.
  Bez linku, dopóki klient nie potwierdzi takich zleceń.

### R5. Wpis 2147 „Obróbka tworzyw sztucznych” i h3 obecnej 1011 „Grawerowanie w tworzywach sztucznych”
- Na 1011 jedna karta „Tworzywa techniczne” (POM, PA6, PP, PMMA z 2264; relief „Duka” z galerii) z linkiem do 2147 (link #3).
- NIE powielać: charakterystyk polimerów (POM stabilny, PA higroskopijny, PTFE, PEEK, PVDF), FAI, kondycjonowania,
  mocowań w imadle. To treść 2147.

### R6. `/produkty/` (8): rozdzielnik trzech technologii
- `/produkty/` ma kartę „Frezowanie CNC” («Obróbka skrawaniem tam, gdzie laser nie sięga…»), FAQ «Jakie pliki
  przyjmujecie?», «Można zamówić cięcie, frezowanie i grawerowanie w jednym zleceniu?», proces w pięciu krokach i blok
  „Czym to robimy i jak duże to może być.”
- Pytanie „cięcie, frezowanie i grawer w jednym zleceniu” jest już w FAQ `/produkty/` i `/uslugi-dla-przemyslu/`.
  Na 1011 ten fakt idzie do karty w slocie 02, nie jako trzecie identyczne pytanie FAQ.
- Proces na 1011 (slot 06, K11) w czterech krokach jak na 1019, z konkretem frezu (STEP, próbka, frezowanie,
  wykończenie i łączenie z laserem), słowami innymi niż pięć kroków `/produkty/`.
- Meta 1011 nie zaczyna się od „Grawerowanie laserowe, wycinanie laserowe i frezowanie CNC” (to meta `/produkty/`).
- Anchory do segmentów i sióstr inne niż „Zobacz usługę →” i „Zobacz zakres →” (te ma `/produkty/`).

### R7. `/uslugi-dla-horeca/` (2283) i karta HoReCa na obecnej 1011
Obecna 1011 obiecuje dla HoReCa „Litery przestrzenne, oznaczenia wnętrz, deski do serwisu”, czego strona HoReCa nie
potwierdza (S11). Strona HoReCa raz pisze «Frezujemy kontur i grawerujemy treść w jednej operacji», a w tym samym
bloku «Wycinanie i grawerowanie konturu w jednym przejściu» (S8).
- Na 1011 bez karty HoReCa i bez kart menu jako przykładu frezu. Link do 2283 tylko z rezerwy, po odpowiedzi na P21.

### R8. Wpis FAQ 1660: nie linkować, dopóki nie zostanie poprawiony
Ma dobre dane o frezarce («Nasza frezarka oferuje maksymalne pole pracy wielkości 2000 × 3000 mm»), ale w tym samym
pytaniu błędne pole lasera «2500 × 1650 mm» (poprawnie 2510 × 1680 mm) i «Minimalny koszt usługi wynosi 100 zł»
(bez potwierdzenia, P08). To samo zalecenie co w planie grawerowania (tam R11). Na 1011 FAQ o polu roboczym
i plikach piszemy od nowa; 1011 ma być główną odpowiedzią na „jak duży element wyfrezujecie”.

### R9. Strona główna (poza `SPIS.json`)
h1 „Cięcie laserowe, grawerowanie i frezowanie CNC” i karta „Frezowanie CNC” z obietnicami bez pokrycia («z niezrównaną
dokładnością», «z milimetrową precyzją», «Frezowanie CNC gwarantuje szybkość i jakość wykonania»). Strona główna jest
rozdzielnikiem, ryzyko frazy niskie. Na 1011 tych zdań nie przenosimy. Link do strony głównej: nie (brak w `SPIS.json`).

### R10. Szkice i adresy spoza listy
Szkice 1797 (aluminium), 1823 (sklejka), 1829 (czym jest frezowanie), 1845 (tworzywa) nie mogą dostać linku. Po
publikacji 1829 konkurowałby z 1578 i 1873 o „czym jest frezowanie”, a 1797 i 1845 z R1 i R5; przed publikacją warto
je połączyć z istniejącymi wpisami. `/torebki/` (torebki ze sklejki „cięte laserowo i frezowane CNC”) jest linkowane
z `/produkty/`, ale nie ma go w `SPIS.json`: na 1011 bez linku.

### Treści, których nowa 1011 NIE powiela (skrót)
- sekcji CNC ze `/uslugi-dla-przemyslu/` (3 i 5 osi, metale, protokół, gładkość, ±0,01 mm, normy, terminy serii);
- porównania laser kontra frez z wpisów 2078, 1578, 2147 (poza dwoma, trzema faktami i linkiem do 2078);
- definicji „czym jest frezowanie”, zalet i wad, rodzajów frezów, frezowania w meblarstwie (1578, 1873, 967, szkice);
- charakterystyk tworzyw z 2147; parametrów plotera Kimla i danych katalogowych producenta z 2078;
- FAQ `/produkty/` i `/uslugi-dla-przemyslu/` (pliki, jedno zlecenie) jako identycznych pytań; FAQ z wpisu 1660;
- trzech kart „Dlaczego Padir”, pięciu kart Trotec, bloku nagród i case’ów laserowych z 1019;
- twierdzeń bez pokrycia z obecnej 1011 i szablonu (fakty.md, lista 1-24: „kilkadziesiąt centymetrów”, „ułamki
  milimetra”, „największe marki”, „rygorystyczne normy”, „od elektroniki po medycynę”, „Frezujemy dla przemysłu
  i dla gastronomii”, zdjęcia stockowe jako „nasza praca”).

---

## 3. Linki wewnętrzne do wstawienia (8)

Wszystkie adresy mają status `publish` w `SPIS.json`. Kotwice `#galeria` (1397) i `#technologia` (1019) sprawdziłem
w kodzie tych stron (`id="galeria"`, `id="technologia"`). Strona przemysłowa nie ma żadnych `id`, więc do jej sekcji
CNC nie da się linkować głęboko. Galeria 1397 nie czyta filtra z adresu (filtr działa tylko po kliknięciu,
`data-cat="cnc"`), więc link prowadzi do `#galeria`.
Zapis względny (`/adres/`), jak na 1397, 2264 i `/produkty/`. Bez wersji z `www.`. Wygląd: zwykły link w tekście
(kolor linku z arkusza `.pdw`) albo przycisk K03 A-mały tam, gdzie wzorzec ma przycisk.
Numery slotów jak w kolejności 1019 (`praca/wzorzec.md`, 2.3).

| # | adres | anchor (propozycja) | sekcja na 1011 |
|---|---|---|---|
| 1 | `/wycinanie-laserowe/` | „wycinanie laserowe” (w zdaniu: „Frezowany detal od razu wygrawerujemy albo połączymy z elementami wyciętymi laserem, w jednym zleceniu: zobacz grawerowanie laserowe i wycinanie laserowe.”) | „Dlaczego Padir”, slot 02 (K06), karta o jednej pracowni |
| 2 | `/grawerowanie-laserowe/` | „grawerowanie laserowe” (to samo zdanie co #1) | „Dlaczego Padir”, slot 02 (K06), ta sama karta |
| 3 | `/blog/obrobka-tworzyw-sztucznych/` | „jak dobrać tworzywo do funkcji detalu” (w zdaniu: „Jak dobrać tworzywo do funkcji detalu, piszemy w poradniku o obróbce tworzyw.”) | Materiały, slot 03 (K07), karta „Tworzywa techniczne” |
| 4 | `/przykladkowe-realizacje/#galeria` | „Zobacz wszystkie realizacje” (przycisk z kodu portfolio w `wzorzec.md`, sekcja 5) | Portfolio, slot 04 (K09), pod siatką 6 kart „Frezowanie” |
| 5 | `/blog/ciecie-przemyslowe/` | „kiedy wybrać laser, a kiedy frez” (w zdaniu: „Kiedy wybrać laser, a kiedy frez, rozpisujemy na przykładzie akrylu, sklejki i MDF.”) | „Na czym to polega”, slot 05 (K10), ostatnie zdanie po akapicie o pionie krawędzi i średnicy frezu |
| 6 | `/produkty/` | „przegląd trzech technologii” (w leadzie: „Ta sama droga obowiązuje przy laserze i grawerze; przegląd trzech technologii znajdziesz w zakładce Produkty.”) | Proces, slot 06 (K11), lead nad krokami |
| 7 | `/uslugi-dla-przemyslu/` | „usługi dla przemysłu” (w odpowiedzi FAQ o seriach: „Parametry procesu i plik wzorcowy archiwizujemy, więc dozamówienie wychodzi tak samo. Zlecenia dla producentów i firm OEM opisujemy osobno: usługi dla przemysłu.”) | FAQ, slot 11 (K16), pytanie o serie i dozamówienia (albo blok „dla kogo” w slocie 08, jeśli powstanie) |
| 8 | `/wycinanie-laserowe/#technologia` | „park laserów Trotec” (w zdaniu: „Fronty i drobne detale do tych samych projektów tniemy laserem; maszyny opisujemy w parku laserów Trotec.”) | Park maszynowy, slot 09 (K14), pod kartą frezarki |

Pokrycie faktami zdań z anchorami (z `fakty.md`): #1 i #2 F03, F04; #3 F42; #4 F90; #5 F05, F06, F31; #6 F09 i
`zrodla/pages-8-produkty.txt` «Mówimy, czy to zadanie dla lasera, czy dla frezarki»; #7 F68, F72, F53; #8 F04, F24.

Zasady anchorów: opisują cel, nie powtarzają frazy „frezowanie CNC” (to fraza samej 1011), nie zawierają nazw klientów,
metali ani „3- i 5-osiowa” (R1), nie są „kliknij tutaj” ani gołym „Zobacz usługę →”.

Uwagi dla składacza:
- #1 i #2 są lustrem linków #9 i #10 z planu grawerowania (karta o jednej pracowni w slocie 02 na 456 linkuje do
  wycinania i frezowania). Trzy siostry linkują się w tym samym miejscu i tym samym komponentem.
- #1 i #8 prowadzą na tę samą stronę, ale do różnych miejsc. Jeśli składacz chce jednego linku na adres, zostaje #1,
  a #8 przechodzi do rezerwy.
- Jeśli slot 07 (case) dostanie mini-case ze ścianką foto na barce z wpisu 2078 (nośnik z MDF frezem, front
  z lustrzanego plexi laserem, F04; bez nazwy klienta, F94, P14), link #5 przenosimy tam jako „Zobacz pełny opis
  ścianki na barce” zamiast `#` z wzorca, a w slocie 05 nie ma linku. Jeden link do 2078 na stronę.
- Wewnętrzne kotwice wzorca (`#kontakt`, `#proces`, `#portfolio`, `#faq`) nie liczą się do tej listy; każda musi mieć
  swoje `id` na stronie.

### Rezerwa (tylko gdy spełniony warunek; razem nie więcej niż 10 linków w treści)
- `/uslugi-dla-horeca/`, anchor „drewniane karty menu dla lokali”, w karcie „MDF, sklejka i drewno”, dopiero gdy
  klient potwierdzi, że kontur kart menu frezuje (P21).
- `/blog/frezowanie-drewna-na-czym-polega-i-jakie-efekty-mozna-uzyskac/`, anchor „rodzaje frezów do drewna”,
  w karcie drewna, tylko jeśli karta wspomina kształt krawędzi albo fazy. Najniższy priorytet (R4).
- `/blog/frezowanie-cnc-w-nowoczesnym-designie-mebli/`, anchor „frezowanie frontów i mebli”, tylko jeśli klient
  potwierdzi zlecenia meblowe (F54; do dopisania jako pytanie przy P22).
- `/blog/tworzenie-ekspozycji-dla-marek-kosmetycznych/`, anchor „ekspozytory z frezowanymi gniazdami”, tylko po
  odpowiedzi na P15 (czy ekspozytory z wpisu to realizacje Padiru).
- `/przykladkowe-realizacje/` z innym anchorem w hero zamiast „Czytaj więcej”, jeśli składacz zrezygnuje z #4.

### Nie linkować z 1011
Wpis 1660 (R8), wpis 1578 (R3), wpis 967 i 1873 poza rezerwą (R4), wpisy o laserze i grawerze bez związku z frezem
(2293, 2545, 2208), case study (`/case-study/`, `/case-study/zamek-sulkowskich/`, `/case-study-wosp/`: żadna nie
dotyczy frezu), `/materialy-do-grawerowania/` (tylko grawer), dzieci 456 (`/grawerowanie-laserowe/prezenty/`,
`/grawerowanie-laserowe/grawerowanie-na-nozu/`: nie ten temat), szkice z R10, `/torebki/`, `/sklep/`, strona główna.

---

## 4. Strony potomne i siostrzane

Strony potomne: **brak**. Żadna pozycja w `SPIS.json` nie ma rodzica 1011 (rodzica mają tylko 1812, 2228 i szkic 1731,
wszystkie pod 456, oraz 2470 pod 2487). Nie trzeba więc podpinać dzieci tak jak w przypadku grawerowania (prezenty,
nóż). Jeśli kiedyś powstaną podstrony frezu (np. litery przestrzenne), wtedy z 1011 trzeba będzie do nich prowadzić
kartami jak na 456.

Strony siostrzane, do których 1011 ma prowadzić w treści:
- `/wycinanie-laserowe/` (1019) i `/grawerowanie-laserowe/` (456): rodzeństwo w menu „Produkty”. Linki #1 i #2 w karcie
  „jedna pracownia” plus głęboki link #8 do `#technologia`. Nowa 456 ma linkować do 1011 symetrycznie (plan grawerowania, #10).
- `/produkty/` (8): rozdzielnik trzech technologii i rodzic w menu. Link #6. `/produkty/` prowadzi do 1011 („Zobacz usługę →”).
- `/uslugi-dla-przemyslu/` (2264): strona segmentowa z własną sekcją CNC i dwoma linkami do 1011. Link #7.
- `/przykladkowe-realizacje/` (1397): galeria z filtrem „Frezowanie CNC” (6 realizacji). Link #4.
- `/uslugi-dla-horeca/` (2283): link tylko z rezerwy (R7).

### Linki przychodzące do poprawy po publikacji (poza szkicem, do decyzji klienta)
- Wpis 2078 (najlepszy poradnik o frezie, autor z pracowni) nie linkuje do 1011 wcale. Jego anchor „w retailu, eventach
  i małej produkcji” prowadzi na `/uslugi-dla-przemyslu/`, co nie pasuje do treści. Naturalne miejsce na link do 1011:
  akapit „Kiedy CNC jest lepszą decyzją” albo zakończenie („Wyślij krótki brief”).
- Wpis 2147 nie ma ani jednego linku. Miejsce: sekcja „Obróbka CNC: kiedy i za co płacimy”.
- Galeria 1397 ma filtr „Frezowanie CNC” i zdanie «napisy przestrzenne oraz detale frezujemy na maszynach CNC», ale nie
  linkuje do 1011 (linkuje do HoReCa i przemysłu). Link w tym zdaniu domknie trójkąt usługa, galeria, usługa.
- 1019 nie linkuje do żadnej siostry. Po publikacji 1011: link w „Na czym to polega” albo w FAQ przy grubych materiałach.
- Wpis 2293 (sekcja „Wycinanie laserowe a inne metody”) i 2208 (sekcja „Laser a CNC”) piszą o frezie bez linku do 1011.
- Wpis 1873: anchor „Frezowanie w drewnie,” obejmuje przecinek; do poprawy przy okazji.
- `/uslugi-dla-przemyslu/`: link „Poznaj frezowanie CNC” stoi pod obietnicą 3 i 5 osi i metali (R1). Po odpowiedziach na P03 i P04 jedna z dwóch stron wymaga korekty.
- Wpis 1660: po poprawieniu pola lasera i kwoty minimalnej odpowiedź „4. Jak duże jest pole robocze laserów i frezarki?” powinna linkować do 1011.

---

## 5. Title i meta description

Konwencja serwisu: tytuły podstron to „Nazwa - Padir” (dziś „Frezowanie CNC - Padir”, „Wycinanie Laserowe - Padir”).
Plan grawerowania proponuje dla 456 „Grawerowanie laserowe w Warszawie | Pracownia Padir”; dla spójności nowych
sióstr ten sam wzór. Bez myślników i półpauz.

**Title (44 znaki):**
`Frezowanie CNC w Warszawie | Pracownia Padir`

Wariant (55 znaków, z wyróżnikiem): `Frezowanie CNC w Warszawie, litery 3D i reliefy | Padir`

**Meta description (154 znaki):**
`Frezowanie CNC liter przestrzennych, reliefów i nośników z plexi, MDF, sklejki i tworzyw. Pole robocze 2000 × 3000 mm, od 1 sztuki. Pracownia w Warszawie.`

Źródła treści meta (fakty, nie zdania):
- litery przestrzenne, reliefy: `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowana litera przestrzenna», «Frezowany relief „Duka”»; `zrodla/pages-8-produkty.txt` «reliefy i litery 3D» (F50);
- nośniki: `zrodla/posts-2078-ciecie-przemyslowe.txt` «To także metoda pierwszego wyboru dla nośników pod fronty laserowe» (F04, F51);
- plexi, MDF, tworzywa: `zrodla/pages-1397-przykladkowe-realizacje.txt` «Plexi lustrzana», «MDF», «Tworzywo» (F40-F42); sklejka: `zrodla/posts-2078-ciecie-przemyslowe.txt` «CNC ogarnia: PMMA (…), sklejkę (także WBP), MDF» i `zrodla/pages-8-produkty.txt` «Drewno i sklejka Grawer, cięcie i frezowanie.»;
- pole robocze: `zrodla/pages-1011-frezowanie-cnc.txt` «Maksymalny obszar roboczy to 2000 na 3000mm», `zrodla/posts-1660-…txt` «2000 × 3000 mm» (F20);
- od 1 sztuki: `zrodla/posts-1660-…txt` «Zamówienia przyjmujemy już od 1 sztuki .» (F09);
- Warszawa: `zrodla/pages-8-produkty.txt` «pod jednym dachem w Warszawie» (F01).

Tytuł i meta celowo nie zawierają metali, „3- i 5-osiowa” ani tolerancji (R1, P03-P05), nie zaczynają się od listy
trzech technologii (meta `/produkty/`) ani od „Akryl, sklejka, MDF” (meta wpisu 2078). Jeśli klient potwierdzi
metale, meta można przebudować, ale tylko po aktualizacji `/uslugi-dla-przemyslu/` (R1).

h1 strony: „Frezowanie CNC”, w tym samym zapisie co dziś i analogicznie do h1 „Wycinanie Laserowe” na 1019. Przy
przenoszeniu na 1011 trzeba przełączyć szablon z `frezowanie-cnc` na `page-no-title`, bo obecny szablon dokłada
własny h1 „Frezowanie CNC” i podtytuł (`zrodla/szablon-frezowanie-cnc.raw.html`), co dałoby dwa h1.
