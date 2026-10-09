# Grawerowanie laserowe: plan linkowania wewnętrznego i analiza kanibalizacji

Strona: szkic „Grawerowanie laserowe”, który zastąpi stronę 456 `/grawerowanie-laserowe/` (ten sam adres po akceptacji).
Podstawa: `zrodla/SPIS.json`, `zrodla/pages-*.raw.html` i `.txt`, `zrodla/posts-*.raw.html` i `.txt`, szablon
`zrodla/szablon-wp-custom-template-grawerowanie-laserowe.*`, wzorzec `praca/wzorzec.md`.
Tytuły SEO i opisy meta obecnych stron nie są w `zrodla/`. Odczytałem je 2026-10-09 z publicznych stron serwisu
(tylko odczyt, zwykłe pobranie strony). Stamtąd też pochodzi treść strony głównej, której nie ma w `SPIS.json`.
Żadnych liczb wyszukiwań: wszystko poniżej wynika z tego, jak serwis już pisze i linkuje.

---

## 1. Główna intencja i frazy

### Intencja strony

Handlowa, usługowa i lokalna: ktoś szuka pracowni, która wykona grawer laserowy (w Warszawie), i chce szybko
sprawdzić, co da się zrobić, na czym, dla kogo, jak wygląda zamówienie i jak się skontaktować. Strona jest
**przeglądem usługi i rozdzielnikiem** do stron segmentowych (przemysł, HoReCa, prezenty, noże). Wiedza
poradnikowa (jak działa laser, CO2 i fiber, przygotowanie pliku, porównania metod) zostaje na blogu.

Tak samo ustawiona jest siostrzana `/wycinanie-laserowe/` (1019): h1 z nazwą usługi, krótkie sekcje, galeria,
proces, park maszyn, FAQ, formularz. Jej meta: „Wycinanie laserowe plexi, sklejki, drewna, filcu i tworzyw.
Czysta krawędź i powtarzalność przy krótkich seriach. Wycena na podstawie pliku.”

### Pod jakie frazy serwis już ustawia stronę 456

| gdzie | brzmienie |
|---|---|
| tytuł SEO (strona publiczna) | „Grawerowanie Laserowe [półpauza] Precyzyjne znakowanie powierzchni” (półpauza do usunięcia) |
| meta description (strona publiczna) | „Grawerowanie laserowe na szkle, stali, plexi, drewnie i skórze. Trwały znak bez farby i naklejek, od pojedynczej sztuki po serie produkcyjne.” |
| h1 (szablon `wp-custom-template-grawerowanie-laserowe`) | „Grawerowanie Laserowe”, pod nim „Nadaj przedmiotom indywidualny charakter” |
| h2 treści 456 | „Na czym polega grawerowanie laserowe?”, „Dlaczego warto wybrać Padir?”, „Nowoczesna technologia”, „Sprawdzone i uniwersalne rozwiązanie”, „Grawerowanie laserowe - najczęściej zadawane pytania”, „Materiały w których grawerujemy”, „Grawerujemy dla przemysłu i dla gastronomii.”, „Grawerowanie laserowe - co warto wygrawerować”, „Grawerowane prezenty”, „Planujesz prezent na inną okazję?” |
| h3/h4 treści 456 | „Grawerowanie w drewnie”, „Grawerowanie w metalu”, „Grawerowanie na szkle”, „Grawerowana biżuteria”, „Grawerowane breloczki i klucze”, „Grawerowane długopisy i pióra wieczne”, „Grawerowane tabliczki znamionowe i identyfikacyjne”, „Grawerowane prezenty na komunię / na Ślub / na walentynki” |

Anchory, którymi inne strony serwisu linkują dziś do `/grawerowanie-laserowe/` (z plików `zrodla/`):

| anchor | skąd |
|---|---|
| „grawerowanie laserowe” | wpisy 1584, 1673, 1757, 1770, 1771, 968; „Grawerowanie laserowe” we wpisie 1868 |
| „Grawerowanie laserowe Warszawa” | wpis 1851 (grawer-jako-prezent) |
| „grawerowania laserowego” | wpis 1631 (jak przygotować projekt) |
| „Czym jest Grawerowanie Laserowe” | strony potomne 1812 (prezenty) i 2228 (nóż) |
| „Zobacz usługę →” | `/produkty/` (8) i `/uslugi-dla-przemyslu/` (2264) |
| „grawerowanie”, „trwałym grawerem”, „laser usuwa mikrowarstwę materiału” | wpisy 2030, 2063, 2550 |
| „Zobacz więcej” | strona główna (odczyt publiczny) |

Wniosek: serwis traktuje 456 jako stronę główną frazy **„grawerowanie laserowe”** i jej wersji lokalnej
**„grawerowanie laserowe Warszawa”**. Nowa strona powinna tę rolę utrzymać: h1 „Grawerowanie Laserowe”
(jak h1 „Wycinanie Laserowe” na 1019), fraza i miasto w tytule SEO, reszta nagłówków opisowa, bez upychania frazy.

### Frazy rozproszone dziś po innych stronach i wpisach

| temat / fraza | gdzie już jest |
|---|---|
| „grawerowanie laserowe” (fraza główna) | strona główna: tytuł „Padir - Grawerowanie Laserowe”, meta „Grawerowanie Laserowe”, h4 „Grawerowanie laserowe w Warszawie” i „Grawerowanie w Warszawie”; domena dokładnie tej frazy |
| „na czym polega / czym jest / jak działa grawerowanie laserowe” | wpis 2208 (tytuł „Jak działa grawerowanie laserowe?”), wpis 1584 (h2 „Na czym polega grawerowanie laserowe?”, identyczny jak h2 na 456), wpisy 1673 i 1771 (h2 „Czym jest Grawerowanie Laserowe?”), szkic 1832 |
| „materiały do grawerowania”, „grawerowanie w drewnie / w metalu / na szkle” | `/materialy-do-grawerowania/` (h1 „Materiały do grawerowania laserowego”), wpis 762 (h2 „Grawerowanie laserowe w drewnie / w metalu / na szkle i krysztale…”), wpis 2195 (h2 „Grawerowanie w Drewnie”, „Grawerowanie w Metalu”…), wpis 1865 („grawerowanie w metalu”, „Grawerowanie metalu”), strona główna (h2 „Materiały w których grawerujemy” z tymi samymi h3 co na 456), `/produkty/` (h2 „Nie wiesz, czy Twój materiał się nadaje?”) |
| „grawerowanie laserowe, kiedy warto / dla kogo / najczęściej grawerowane przedmioty” | wpis 1868 (tytuł „Grawerowanie laserowe - kiedy warto zdecydować się na usługę?”), szkice 1731 i 1786 |
| zalety grawerowania laserowego | wpisy 1770, 1673, 1771; FAQ na 456 |
| grawer laserowy a mechaniczny / a CNC | wpis 1584, sekcja we wpisie 2208 |
| tabliczki znamionowe, DMC, QR, numery seryjne, znakowanie przemysłowe | `/uslugi-dla-przemyslu/`, wpis 1673, wpis 2184 |
| grawer na szkle i zastawie, hotele, restauracje | `/uslugi-dla-horeca/`, wpis 2550 |
| grawerowane prezenty, grawer na prezent | `/grawerowanie-laserowe/prezenty/` (tytuł „Grawerowanie na prezent”), wpisy 1851, 1546, 2177 (firmowe), 2009, sekcja w 2208 |
| grawer na nożu | `/grawerowanie-laserowe/grawerowanie-na-nozu/`, `/produkty/` („Noże z grawerem”), `/uslugi-dla-horeca/`, wpis 2550 |
| grawer w biznesie, promocja marki | wpisy 1757, 2009, 968 |
| biżuteria, jubilerstwo | wpis 1771, sekcja w 2009 |
| przygotowanie pliku | wpis 1631, wpis FAQ 1660, FAQ `/produkty/` |
| statuetki i nagrody | `/wycinanie-laserowe/#nagrody`, `/produkty/`, wpis 2177 |
| park laserów Trotec | `/wycinanie-laserowe/#technologia`, `/produkty/` („Czym to robimy i jak duże to może być.”) |

---

## 2. Ryzyka kanibalizacji i jak nowa strona ma się odróżnić

Zasada podziału ról:
- **456 (nowa)**: intencja handlowa, przegląd usługi, „co, na czym, dla kogo, jak zamówić”, odsyła dalej;
- **strony segmentowe** (przemysł, HoReCa, prezenty, noże): konkretny klient i jego szczegóły;
- **`/materialy-do-grawerowania/`**: katalog materiałów;
- **wpisy**: poradniki i wyjaśnienia;
- **strona główna i `/produkty/`**: rozdzielniki trzech technologii.

### R1. Strona główna a 456 (największe ryzyko)
Strona główna ma tytuł „Padir - Grawerowanie Laserowe”, meta „Grawerowanie Laserowe”, h4 „Grawerowanie laserowe
w Warszawie” i blok „Materiały w których grawerujemy” z tymi samymi h3 co obecna 456 („Grawerowanie w drewnie /
w metalu / na szkle”) i niemal tym samym tekstem. Domena to dokładnie fraza główna.
- Nowa 456 NIE powtarza bloku materiałów ze strony głównej (ani nagłówków, ani zdań).
- 456 przejmuje frazę usługową z miastem („w Warszawie”) w tytule SEO. Strona główna ma już h1 „Cięcie laserowe,
  grawerowanie i frezowanie CNC”, czyli rolę rozdzielnika trzech technologii.
- Do decyzji klienta (poza szkicem): tytuł i meta strony głównej w duchu trzech technologii, a w akapicie
  „Grawerowanie laserowe w Warszawie” na stronie głównej link do `/grawerowanie-laserowe/`.

### R2. Wpis 1868 „Grawerowanie laserowe - kiedy warto zdecydować się na usługę?”
Najbliższy 456 wpis pod względem intencji (słowo „usługa”, sekcje „dla kogo” i „najczęściej grawerowane
przedmioty”). Obecna 456 ma podobne sekcje: „Sprawdzone i uniwersalne rozwiązanie” (dla kogo) i „co warto
wygrawerować” (biżuteria, breloczki, długopisy, tabliczki).
- Nowa 456 nie ma listy „co warto wygrawerować” ani akapitu „dla kogo” pisanego ogólnie. Zamiast tego karty
  segmentów z linkami do stron segmentowych (sekcja „Dla kogo grawerujemy”, punkt 3).
- Nie linkujemy z 456 do 1868 (nie przekazujemy wpisowi sygnału na frazę usługową). Wpis 1868 już linkuje do 456.

### R3. Wpisy poradnikowe: 2208 (jak działa), 1584 (laser czy mechaniczny), 1673 i 1771 (h2 „Czym jest…”)
- Nie używać h2 „Na czym polega grawerowanie laserowe?” (identyczne h2 ma wpis 1584) ani „Czym jest grawerowanie
  laserowe?” (1673, 1771, szkic 1832). Sekcja w slocie 05 wzorca („Na czym to polega”, K10) ma własny,
  opisowy nagłówek, tak jak „Skoncentrowane światło zamiast noża” na 1019.
- Nie powielać wykładu o CO2 i fiber, długości fal (10,6 µm i 1,06 µm), głębokości 0,2 i 0,5 mm, trwałości
  „zależy od materiału”, porównania laser kontra CNC. Na 456 wystarczą dwa, trzy zdania faktów i link do 2208.
- Sekcje „Zalety grawerowania laserowego” (1770) i hasła o zaletach z FAQ 456 nie wracają.

### R4. Klaster materiałów: `/materialy-do-grawerowania/`, wpisy 762, 2195, 1865, `/produkty/`, strona główna
Pięć miejsc celuje dziś w „grawerowanie w drewnie / metalu / na szkle”.
- Sekcja materiałów na 456 (slot 03, K07) w stylu 1019: nagłówek typu „Na czym grawerujemy” (1019 ma
  „W czym tniemy laserowo”), tytuły kart to nazwy materiałów („Drewno i sklejka”, „Metal”, „Szkło i kryształ”,
  „Skóra”, „Plexi i tworzywa”), a nie „Grawerowanie w metalu”. Na karcie jedno, dwa zdania: jaki efekt i co
  z tego robimy. Pod kartami link do pełnej listy (`/materialy-do-grawerowania/`).
- Nie używać nagłówka „Materiały do grawerowania laserowego” (h1 strony 1212) ani „Materiały w których
  grawerujemy” (h2 strony głównej i obecnej 456).
- Meta description nowej 456 nie zaczyna się od listy materiałów: meta `/materialy-do-grawerowania/` to
  „Sprawdź, na czym grawerujemy: szkło, stal, plexi, drewno, skóra, sklejka i tworzywa…”, a obecna meta 456 ma
  prawie tę samą listę.

### R5. `/uslugi-dla-przemyslu/` i wpisy 1673, 2184
Strona przemysłowa ma pełny zakres: tabliczki znamionowe, kody DMC i QR, oznaczenia CE, znakowanie narzędzi,
ratowanie serii (2344 tłoki, 2339 odratowane), normy, FAQ o dyrektywie maszynowej.
- Na 456 jedna karta segmentu i ewentualnie jedna realizacja (np. tabliczka znamionowa z galerii) plus link.
- NIE powielać: list z kartami usług, norm (GS1, ISO/IEC 16022, 765/2008/WE), historii z tłokami, czasów serii
  „24 do 48 godzin”, zdania „Oznaczenia, które przechodzą audyt” (bez pokrycia, fakty.md N11).

### R6. `/uslugi-dla-horeca/` i wpis 2550
- Na 456 jedna karta segmentu plus link. Fakt „szkło od 12 sztuk” może wrócić krótko w FAQ 456, bo dotyczy
  całej usługi (jest też w FAQ `/produkty/`), ale innymi słowami.
- NIE powielać: 50 i 2000 cykli zmywarki, case 480 kieliszków i 120 karafek, listy „Do Not Disturb”, kart menu,
  sześciu typów lokali.

### R7. `/grawerowanie-laserowe/prezenty/` i wpisy 1851, 1546, 2177, 2009
Obecna 456 ma całą sekcję „Grawerowane prezenty” z h3 „na komunię / na Ślub / na walentynki”. To kopia
nagłówków strony potomnej, a wszystkie trzy linki prowadzą pod ten sam adres.
- Na 456 jedna karta „Prezenty z grawerem” z linkiem do strony potomnej. Bez podsekcji okazji.
- NIE przenosić „+20% wartości” i „klienci zapłacą o 20% więcej” (BRIEF, fakty.md 12b).

### R8. `/grawerowanie-laserowe/grawerowanie-na-nozu/`, `/produkty/` (Noże z grawerem), HoReCa
- Na 456 jedna karta „Noże z grawerem” z linkiem do strony potomnej. Realizacja z nożami może być w galerii
  (karta z 1397), z nazwą klienta tylko tak jak w galerii.

### R9. Siostra `/wycinanie-laserowe/` (1019): bloki, które łatwo skopiować ze wzorca razem z treścią
- **„Dlaczego Padir”** (slot 02, K06): na 1019 h2 „Twój pomysł, nasza realizacja” i karty „Nowoczesne
  technologie / Gwarancja udanego produktu / Doświadczenie i profesjonalizm”. To przeróbka bloku z obecnej 456
  (te same h4) i ogólniki bez pokrycia (fakty.md N05). Nowa 456 bierze komponent, ale pisze własne karty
  z konkretem graweru (np. próbka przed serią, plik ze zdjęcia, jedna pracownia z cięciem i frezowaniem).
- **Park maszynowy** (slot 09, K14, `#technologia` na 1019): pięć kart Trotec. Na 456 tylko maszyny i parametry
  ważne dla graweru (np. Speedy 300 i 360, Q500, laser fiber, a co nie ma źródła, w żółtej ramce). O laserach
  do cięcia jedno zdanie z linkiem do `/wycinanie-laserowe/#technologia` zamiast kopii pięciu kart.
- **Nagrody** (slot 08, K13, `#nagrody` na 1019, h2 „Tworzenie nagród i statuetek”): nie powtarzać tego bloku.
  Slot 08 na 456 lepiej wykorzystać na sekcję segmentów (punkt 3). Jeśli statuetki mają się pojawić, to jako
  realizacja w galerii albo zdanie z linkiem do `/wycinanie-laserowe/#nagrody`.
- **FAQ**: 1019 ma pytania o cięcie. Na 456 pytania o grawer, bez kopiowania zdań 1019.
- **Logotypy**: ten sam pas logo może być, ale bez nagłówka „Współpracujemy z największymi” (fakty.md N04).

### R10. `/produkty/` (rozdzielnik trzech technologii, rodzic w menu)
- FAQ `/produkty/` ma już „Czy grawer się zetrze?”, „Jakie pliki przyjmujecie?”, „Realizujecie pojedyncze
  sztuki?”, „Ile trwa realizacja?”, a sekcja „Jak to działa” ma pięć kroków. FAQ i proces na 456 mają być
  o grawerze i pisane od nowa. Fakty tak (np. szkło od 12 sztuk, plik odtworzony ze zdjęcia), zdania nie.
- Sekcja „Trzy grupy klientów” na `/produkty/` linkuje do tych samych segmentów anchorami „Zobacz zakres →”.
  Na 456 anchory opisowe (punkt 3), inne niż na `/produkty/`.

### R11. Wpis FAQ 1660: nie linkować, dopóki nie zostanie poprawiony
Podaje „2500 × 1650 mm” jako pole największego lasera (znany błąd, poprawnie 2510 × 1680 mm) i „Minimalny koszt
usługi wynosi 100 zł” (brak potwierdzenia gdzie indziej). Link z 456 prowadziłby z poprawnych danych do
sprzecznych. Zdań z tego wpisu nie przenosimy.

### R12. Szkice i adresy spoza listy
Szkice 1731 („Najczęściej grawerowane przedmioty”, rodzic 456), 1786, 1832, 2530, 14 (sklep) nie mogą dostać
linku. Po publikacji 1731 lub 1786 konkurowałyby z wpisem 1868 i z 456 o te same frazy.
`/torebki/` i `/realizacje/` są linkowane na `/produkty/` i stronie głównej, ale nie ma ich w `SPIS.json`, więc
na 456 ich nie używamy (galeria: `/przykladkowe-realizacje/`).

### Treści, których nowa 456 NIE powiela (skrót)
- blok materiałów ze strony głównej i obecnej 456 („Grawerowanie w drewnie / w metalu / na szkle”);
- listę „co warto wygrawerować” (biżuteria, breloczki, długopisy, tabliczki) i podsekcje prezentów na okazje;
- wykład o CO2 i fiber, długości fal, głębokości i trwałości (wpis 2208);
- normy, case z tłokami i liczby z `/uslugi-dla-przemyslu/`; cykle zmywarki i case z kieliszkami z `/uslugi-dla-horeca/`;
- karty „Dlaczego Padir” i blok nagród z 1019; pięć kart parku maszyn z 1019;
- FAQ z `/produkty/` i z wpisu 1660;
- twierdzenia bez pokrycia z obecnej 456 (fakty.md, sekcja 12: case manufaktury biżuterii z „30%”, „20W do 500W”
  jako moc parku, OptiMotion i InPack, „największe marki”, „sztuka, która trwa”, „dla wszystkich”, „miękkie stopy”).

---

## 3. Linki wewnętrzne do wstawienia (10)

Wszystkie adresy mają status `publish` w `SPIS.json`. Kotwice `#galeria` (1397) oraz `#technologia` i `#nagrody`
(1019) sprawdziłem w kodzie tych stron. Zapis względny (`/adres/`), jak na 1397, 2264 i `/produkty/`.
Nie używać wersji z `www.`, bo `sprawdz_szkic.py` jej nie sprawdza. Wygląd: zwykły link w tekście
(kolor linku z arkusza `.pdw`) albo przycisk K03 A-mały tam, gdzie wzorzec ma przycisk.

Numery slotów jak w kolejności 1019 (`praca/wzorzec.md`, 2.3).

| # | adres | anchor (propozycja) | sekcja na 456 |
|---|---|---|---|
| 1 | `/uslugi-dla-przemyslu/` | „Oznaczenia dla przemysłu” (tytuł karty), link „Tabliczki, kody i numery seryjne” | „Dla kogo grawerujemy”, karta 1 (slot 08 zamiast bloku nagród, karty K07 albo K06) |
| 2 | `/uslugi-dla-horeca/` | „Grawer dla hoteli i restauracji” | „Dla kogo grawerujemy”, karta 2 |
| 3 | `/grawerowanie-laserowe/prezenty/` | „Pomysły na prezent z grawerem” | „Dla kogo grawerujemy”, karta 3 |
| 4 | `/grawerowanie-laserowe/grawerowanie-na-nozu/` | „Noże z grawerem” | „Dla kogo grawerujemy”, karta 4 |
| 5 | `/materialy-do-grawerowania/` | „pełna lista materiałów” (w zdaniu pod kartami: „Nie ma tu Twojego materiału? Zajrzyj na pełną listę materiałów albo napisz do nas.”) | Materiały, slot 03 (K07), pod kartami |
| 6 | `/przykladkowe-realizacje/#galeria` | „Zobacz wszystkie realizacje” (przycisk jak w kodzie portfolio z `wzorzec.md`, sekcja 5) | Portfolio, slot 04 (K09), pod siatką |
| 7 | `/case-study-wosp/` | „Cała historia ramek dla WOŚP” (przycisk K03 A-mały w miejscu „Zobacz pełny case”) | Case study, slot 07 (K12), jedyny opublikowany case z grawerem |
| 8 | `/blog/jak-dziala-grawerowanie-laserowe/` | „poradnik o tym, jak działa grawer laserowy” (w zdaniu: „Więcej o laserach CO2 i fiber piszemy w poradniku o tym, jak działa grawer laserowy.”) | „Na czym to polega”, slot 05 (K10), ostatnie zdanie tekstu |
| 9 | `/wycinanie-laserowe/` | „wycinanie laserowe” (w zdaniu: „W tej samej pracowni detal wytniemy i sfrezujemy: zobacz wycinanie laserowe i frezowanie CNC.”) | „Dlaczego Padir”, slot 02 (K06), karta o jednej pracowni |
| 10 | `/frezowanie-cnc/` | „frezowanie CNC” (to samo zdanie co #9) | „Dlaczego Padir”, slot 02 (K06), ta sama karta |

Zasady anchorów: opisują cel, nie powtarzają frazy „grawerowanie laserowe” (to fraza samej 456), nie zawierają
nazw klientów, nie są to „kliknij tutaj” ani gołe „Zobacz zakres →” (te ma już `/produkty/`).

### Rezerwa (jeśli składacz ma miejsce, nie ponad 10 łącznie w treści)
- `/wycinanie-laserowe/#technologia`, anchor „lasery Trotec do cięcia”, w parku maszyn (slot 09), zamiast
  kopiowania kart maszyn tnących. Może zastąpić link #9, jeśli karta „jedna pracownia” nie powstanie.
- `/blog/jak-przygotowac-projekt-do-grawerowania-laserowego/`, anchor „jak przygotować plik do graweru”,
  w procesie (slot 06, K11), krok „Projekt i plik”.
- `/blog/co-mozna-wygrawerowac-laserem-w-konkretnych-materialach/`, anchor „co najlepiej wychodzi w drewnie,
  metalu, skórze i szkle”, zamiennie z linkiem #5 albo w FAQ.
- `/wycinanie-laserowe/#nagrody`, anchor „statuetki i nagrody na zamówienie”, tylko jeśli na 456 pojawi się
  wzmianka o statuetkach.
- `/produkty/`, anchor „trzy technologie w jednym zleceniu”, zamiennie z #9 i #10.

### Nie linkować z 456
Wpis 1660 (R11), wpis 1868 (R2), wpis 1865 (cienki, z listą metali bez pokrycia), szkice z R12, `/torebki/`,
`/realizacje/`, `/sklep/`.

---

## 4. Strony potomne i siostrzane

Strony potomne (rodzic 456 w `SPIS.json`, obie opublikowane):
- `/grawerowanie-laserowe/prezenty/` (1812, tytuł „Grawerowanie na prezent”, h1 „Grawerowane Prezenty na Każdą Okazję”);
- `/grawerowanie-laserowe/grawerowanie-na-nozu/` (2228, tytuł „Grawerowanie na nożu”, h1 „Grawerowanie laserowe na nożach”).

Obie trzeba podpiąć w treści 456, nie tylko w menu: karty 3 i 4 w sekcji „Dla kogo grawerujemy”.
Obecnie 456 linkuje do prezentów czterema linkami w jednym bloku, a do noży wcale. Nowa wersja: po jednym
wyraźnym linku do każdej. Trzecie dziecko, 1731, to szkic: bez linku.

Strony siostrzane:
- `/wycinanie-laserowe/` (1019) i `/frezowanie-cnc/` (1011): rodzeństwo w menu „Produkty”; linki #9 i #10 plus
  ewentualnie głęboki link do `#technologia` w parku.
- `/produkty/` (8): rozdzielnik trzech usług. Prowadzi do 456 („Zobacz usługę →”), 456 wraca do niego przez menu
  (opcjonalnie link z rezerwy).
- `/uslugi-dla-przemyslu/` (2264) i `/uslugi-dla-horeca/` (2283): strony segmentowe, linki #1 i #2.
- `/przykladkowe-realizacje/` (1397): galeria, link #6. Galeria nie ma kotwicy filtra „Grawerowanie”
  (filtr działa tylko po kliknięciu, `data-cat="eng"`), więc link prowadzi do `#galeria`.

### Linki przychodzące do poprawy po publikacji (poza szkicem, do decyzji klienta)
- 1812 i 2228 linkują do 456 anchorem „Czym jest Grawerowanie Laserowe”, który obiecuje poradnik. Po zmianie 456
  w stronę usługową lepiej „Grawerowanie laserowe w Padir” albo „O usłudze grawerowania”.
- Wpis 1865 linkuje anchorem „laserowe znakowanie produktów” do `/grawerowanie-laserowe/prezenty/`. Cel nie pasuje
  do anchora: lepiej `/grawerowanie-laserowe/` albo `/uslugi-dla-przemyslu/`.
- Wpis 2208 (najobszerniejszy poradnik o grawerze) nie linkuje do 456 wcale. Naturalne miejsce: sekcja „Jak to
  wygląda u nas w praktyce?”. Ten wpis ma też resztki szablonu w h3 („Strategic ulting”, „Digital Marketing”,
  „Technology Solutions”), do usunięcia.
- Wpisy 762, 2195, 2177, 2009 nie linkują do 456; wpis 2184 (tabliczki) lepiej podpiąć do `/uslugi-dla-przemyslu/`.
- Strona główna: akapit „Grawerowanie laserowe w Warszawie” bez linku do 456 (R1).

---

## 5. Title i meta description

Konwencja serwisu: tytuły SEO podstron to „Nazwa - Padir” (np. „Wycinanie Laserowe - Padir”), a 456 ma dziś
własny tytuł bez nazwy serwisu i z półpauzą. Proponowany tytuł jest pełny (wpisany w pole SEO, jak dziś),
bez myślników i półpauz.

**Title (51 znaków):**
`Grawerowanie laserowe w Warszawie | Pracownia Padir`

Wariant (57 znaków): `Grawerowanie laserowe w Warszawie, sztuki i serie | Padir`

**Meta description (154 znaki):**
`Grawerujemy laserem logo, numery seryjne i dedykacje. Trwały znak bez farby, od pojedynczej sztuki po serie z próbką do akceptacji. Pracownia w Warszawie.`

Źródła treści meta (fakty, nie zdania):
- logo, numery seryjne: `pages-8-produkty.txt` «Tabliczki znamionowe, numery seryjne, logo, personalizacja.»;
- dedykacje: `pages-2228-grawerowanie-na-nozu.txt` «Imię, data lub krótka dedykacja»;
- bez farby: `pages-8-produkty.txt` «Trwałe znakowanie bez farby i naklejek»;
- pojedyncze sztuki: `pages-8-produkty.txt` «Realizujecie pojedyncze sztuki? Tak.» (wyjątek: szkło od 12 sztuk, to do FAQ, nie do meta);
- próbka: `pages-8-produkty.txt` «Przy seriach i przy nowych materiałach najpierw powstaje wzorzec do akceptacji.»;
- Warszawa: `pages-8-produkty.txt` «Osobiście przy ulicy Matuszewskiej 14 w Warszawie».

Tytuł i meta celowo nie zaczynają się od listy materiałów (R4) i nie powtarzają meta strony głównej ani `/produkty/`.

h1 strony: „Grawerowanie Laserowe”, w tym samym zapisie co h1 „Wycinanie Laserowe” na 1019. Przy przenoszeniu
na 456 trzeba przełączyć szablon na `page-no-title`, bo obecny szablon dokłada drugi h1 (`wzorzec.md`, sekcja 1).
