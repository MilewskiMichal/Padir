# Frezowanie CNC: treść szkicu do akceptacji

Szkic zakładki „Frezowanie CNC”. Po akceptacji klienta treść trafi na stronę 1011 `/frezowanie-cnc/`
(adres się nie zmienia). Układ i komponenty: `praca/wzorzec.md` (K01-K17), rytm strony `/wycinanie-laserowe/` (1019).
Fakty: wyłącznie `praca/frezowanie/fakty.md` (numery F, S, P), zdjęcia: wyłącznie `praca/frezowanie/zdjecia.json`,
linki i kanibalizacja: `praca/frezowanie/linki.md` (numery linków #1-#8, ryzyka R1-R10). Każde twierdzenie
o firmie, liczba i nazwa własna ma wpis w `ksiega.json`.

Zasady zapisu w tym pliku:
- Pola oznaczone etykietą w pogrubieniu to tekst widoczny na stronie, przepisany dokładnie tak, jak ma stanąć.
- Link w tekście zapisuję jako `[anchor](/adres/)`; anchor jest dokładnie tym fragmentem zdania, który ma być linkiem.
- Ramki „Do potwierdzenia z klientem” to `p.pdw-uwaga` z K01 (styl z BRIEF). Na produkcję nie trafiają.
- Wszędzie tylko dywiz. Wymiary ze znakiem `×` i spacjami: `2000 × 3000 mm`.

---

## Meta

- **Title:** Frezowanie CNC w Warszawie | Pracownia Padir
  (44 znaki; wzór jak w planie siostrzanej strony grawerowania; źródło propozycji: linki.md, rozdz. 5)
- **Meta description:** Frezowanie CNC liter przestrzennych, reliefów i nośników z plexi, MDF, sklejki i tworzyw. Pole robocze 2000 × 3000 mm, od 1 sztuki. Pracownia w Warszawie.
  (154 znaki; bez metali, bez „3- i 5-osiowa”, bez tolerancji, nie zaczyna się od listy trzech technologii: R1, R6)
- **Slug roboczy:** frezowanie-cnc-szkic
- **Szablon WordPressa:** `page-no-title` (jak 1019). Przy przenoszeniu na 1011 trzeba przełączyć szablon z `frezowanie-cnc`,
  bo obecny dokłada własny h1 i byłyby dwa.
- **h1:** „Frezowanie CNC” (zapis zdaniowy, `Frezowanie<br>CNC`, usterka 14 wzorca).
- Długość (po rundzie 2, `narzedzia-fz/licz_tresc.py`): 1046 słów widocznego tekstu razem ze stałym blokiem kontaktu i etykietami
  formularza (`pages-1019-wycinanie-laserowe.txt` ma 1066 słów); bez stałego bloku kontaktu 970 słów. Ramki i alty nie są liczone.

---

## Kolejność sekcji

| # | identyfikator | id w HTML | komponent | tło sekcji | slot wzorca 1019 |
|---|---|---|---|---|---|
| 0 | ramka-robocza | brak | K01 (ramka górna) | - | - |
| 1 | hero | brak (`<header>`) | K02 + K03 + K04 | białe, `56px 0px 72px` | 01 |
| 2 | dlaczego-padir | brak | K05 wyśrodkowany + K06 | białe | 02 |
| 3 | materialy | `materialy` | K05 + K07 (3 karty) | `#F5F5F5` | 03 |
| 4 | portfolio | `portfolio` | K09 (6 kart „Frezowanie”) | białe | 04 |
| 5 | na-czym-to-polega | brak | K10 | białe, `36px 0px 78px` | 05 |
| 6 | proces | `proces` | K05 + K11 | `#F5F5F5`, `78px 0px` | 06 |
| 7 | laser-i-frez | brak | K01 + K12 ciemny pas CTA | `#F5F5F5`, `0px 0px 82px` (łączy się z procesem w jeden szary blok, jak 06 i 07 na 1019; dolny odstęp jak sekcja 07 wzorca) | 07 + 08 (zamiast case study i nagród) |
| 8 | technologia | `technologia` | K14 (blok ciemny + 2 karty) | białe | 09 |
| 9 | zaufali-nam | brak | K15 | białe, `20px 0px 82px` | 10 |
| 10 | faq | `faq` | K16 (5 pytań) | `#F5F5F5` | 11 |
| 11 | kontakt | `kontakt` | K17 | białe, `82px 0px 92px` | 12 |

Kotwice użyte na stronie: `#kontakt`, `#proces`, `#portfolio` (wszystkie mają swoje sekcje). Żadnego `href="#"`.

### Pominięte albo zastąpione sekcje wzorca

1. **Slot 07, case study (K12, karty A i B): pominięty.** Każda realizacja CNC z galerii ma w serwisie jedno zdjęcie i tylko tytuł
   z materiałem (zdjecia.json: `"case_study": null`; fakty F90: serwis nie podaje wymiarów, grubości, klienta ani czasu;
   pytanie P12). Karta K12 wymaga trzech zdjęć i opisu „Wyzwanie / Rozwiązanie / Efekt”, więc musiałaby być zmyślona.
   Case’ów z 1019 (Bondi Sands, BOKO) nie przenosimy, bo to cięcie laserowe (R2, F94). W tym miejscu stoi ramka z prośbą
   o materiał na case study (z kandydatem: ramki dla WOŚP z opublikowanego `/case-study-wosp/`, gdzie jedno ze zdjęć, 1739,
   pokazuje frez w płycie Altuglas; to, czy ramki szły przez frezarkę, jest pytaniem w ramce) i ciemny pas K12 z jedynym opisanym w serwisie projektem, w którym pracowała frezarka
   (ścianka fotograficzna na barce, wpis 2078, F04, bez nazwy klienta).
2. **Slot 08, nagrody (K13): pominięty.** Nagrody i statuetki to temat lasera (1019) i grawerowania. Wyróżnik frezowania,
   czyli łączenie nośnika z frezarki z frontem z lasera, jest już w pasie K12 ze slotu 07. Do bloku K13 nie zostało
   żadne zdjęcie frezowania, które nie stałoby już dwa razy na stronie (patrz mapa zdjęć).
3. **Slot 09, park maszynowy: zmniejszony.** Zamiast pięciu kart Trotec (R2) są dwie: frezarka (jeden potwierdzony
   parametr i ramka z pytaniami o model) oraz zbiorcza karta laserów z odesłaniem do `/wycinanie-laserowe/#technologia`.
4. **Slot 03, materiały: 3 karty zamiast 6.** W serwisie jest 9 różnych kadrów z frezarki (6 realizacji, 3 zdjęcia procesu).
   Szersza lista materiałów (dibond, poliwęglan, pianka PVC, metale) nie ma potwierdzenia ani zdjęć, więc trafia do ramek.

---

## Mapa zdjęć

Wszystkie pliki z `praca/frezowanie/zdjecia.json` (lista `zatwierdzone`), obejrzane na `kont-1.png` i `kont-7-kwadraty.png`.
Zdjęcia odrzucone (stock, Morbidelli 751, śmigło, tłoki, DALL·E, prace laserowe z 1019) nie występują nigdzie.

| media_id | plik | gdzie na stronie | alt |
|---|---|---|---|
| 2315 | `2026/08/padir-realizacja-napis-przestrzenny-tea.jpg` | hero kafel 1 (`object-position: 20% 50%`, inaczej kwadrat ucina „T”); portfolio karta 6 | hero: „Napis przestrzenny „Tea” ze złotej plexi lustrzanej”; portfolio: 1:1 z JSON |
| 2319 | `2026/08/padir-realizacja-medalion-republika-portionii.jpg` | hero kafel 2; portfolio karta 5 | hero: „Medalion z płyty MDF z wypukłym napisem po frezowaniu CNC” (bez nazwy, pisownia do potwierdzenia); portfolio: 1:1 z JSON |
| 2318 | `2026/08/padir-realizacja-frezowany-napis-ajala.jpg` | hero kafel 3 (pod nawiasem L); portfolio karta 4 | hero: „Frezowanie napisu w płycie z konglomeratu kwarcowego”; portfolio: 1:1 z JSON |
| 2317 | `2026/08/padir-realizacja-frezowana-litera-przestrzenna.jpg` | hero kafel 4; portfolio karta 3 | hero: „Frez CNC wycina literę przestrzenną z bukowego klocka”; portfolio: 1:1 z JSON |
| 2316 | `2026/08/padir-realizacja-napis-przestrzenny-team.jpg` | portfolio karta 2 (`object-position: 0% 50%`, inaczej kadr 4:3 ucina „T”) | portfolio: 1:1 z JSON |
| 2320 | `2026/08/padir-realizacja-frezowany-relief-duka.jpg` | materiały karta 3; portfolio karta 1 (`object-position: 25% 50%`, inaczej kadr 4:3 ucina „D”) | materiały: „Frezowany relief „Duka” w bloku z tworzywa, mierzony suwmiarką”; portfolio: 1:1 z JSON |
| 2256 | `2026/04/cnc-drewno.jpg` | materiały karta 1 | „Frez CNC prowadzi łukowy rowek w klejonce drewnianej” |
| 1739 | `2025/01/IMG_20250116_082620_HDR-scaled.jpg` | materiały karta 2 (plexi) | „Cienki frez CNC wycina otwór w płycie z plexi” |
| 2148 | `2025/10/IMG_20250909_084928_HDR-scaled.jpg` | na czym to polega (K10); park maszynowy (K14), zdjęcie zastępcze do czasu zdjęcia całej frezarki (T1) | „Frez CNC wycina kontury w jasnoszarej płycie, dookoła wióry” (oba miejsca) |

Pełne adresy: `https://grawerowanie-laserowe.pl/wp-content/uploads/` + kolumna „plik”.

Uzasadnienie powtórek (do wiedzy prowadzącego):
- Hero i portfolio dzielą 4 zdjęcia, tak samo jak na wzorcu 1019 (wszystkie 4 kafle hero są tam też w galerii).
- Strona potrzebuje 11 miejsc na zdjęcia poza hero, a serwis ma 9 różnych kadrów z frezarki, więc dwie powtórki są nieuniknione.
  Po rundzie 1: materiały dzielą z galerią tylko „Duka” (jedyne zdjęcie tworzywa; ramka M2 prosi o inne), a karta plexi dostała
  zdjęcie procesu 1739 (frez w płycie Altuglas), żeby galeria pokazywała „Team” jako nowy kadr (K07, usterka 10).
  Druga powtórka to 2148: stoi w K10 i w parku maszynowym; w parku tylko do czasu zdjęcia całej frezarki (T1).
- Zdjęcia procesu (2256, 2148, 1739) nie są podpisane jako realizacje. 2256 serwis pokazuje na `/uslugi-dla-przemyslu/`
  z altem „Frezowanie CNC detalu w pracowni Padir”, 1739 stoi w opublikowanym case study WOŚP. Pochodzenie 2148 (żadna
  strona go nie używa, brak altu) jest w ramce przy parku maszynowym (P23).
- Alt 2148 po rundzie 1 opisuje tylko to, co widać: kontur w jasnoszarej, nieprzezroczystej płycie i wióry. Bez „kieszeni”,
  „przezroczystej płyty” i „chłodziwa” (dysze mogą równie dobrze podawać powietrze).
- Hero: na kafel 3 (lewy dolny, pod nawiasem L) idzie „Ajala”, bo w kwadracie dół kadru to pusta płyta, a litery są
  wyżej. Litera z buku pod nawiasem straciłaby lewy dolny róg litery.

---

## Sekcje: pełna treść

### 0. ramka-robocza (K01, ramka górna)

- **Identyfikator:** ramka-robocza, bez `id`
- **Komponent:** K01, wariant „ramka na samej górze”, zaraz po arkuszach, przed `<header>`
- **Ramka (tekst stały z BRIEF):** Wersja robocza do akceptacji. Żółte ramki oznaczają miejsca do potwierdzenia przed publikacją.

---

### 1. hero (K02)

- **Identyfikator:** hero, `<header>` bez `id`
- **Komponent:** K02 hero z siatką 2x2 i nawiasem L, para przycisków K03 A + B, link ze strzałką K04
- **Tło:** białe
- **H1:** Frezowanie CNC
  (zapis w kodzie: `Frezowanie<br>CNC`)
- **Podtytuł, szary początek:** Laser tnie, frez rzeźbi.
- **Podtytuł, czarna reszta:** Napisy przestrzenne i reliefy z grubszych płyt.
- **Akapit:** Frezujemy plexi, MDF, drewno, konglomerat kwarcowy i tworzywa techniczne. Element do 2000 × 3000 mm wychodzi z maszyny w jednym kawałku, a zamówienie przyjmujemy już od jednej sztuki.
- **CTA A (tekst):** Skorzystaj z oferty
  - cel: `#kontakt`
- **CTA B (tekst):** Czytaj więcej
  - cel: `#proces`
- **Link ze strzałką (tekst):** Zobacz więcej realizacji
  - cel: `#portfolio`
- **Zdjęcia** (pełne pliki, `loading="eager" fetchpriority="high" data-no-lazy="1"`, `data-pdw-zoom`):
  1. kafel lewy górny: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-napis-przestrzenny-tea.jpg`
     alt: „Napis przestrzenny „Tea” ze złotej plexi lustrzanej”, `object-position: 20% 50%` (cała litera „T” w kwadracie)
  2. kafel prawy górny: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-medalion-republika-portionii.jpg`
     alt: „Medalion z płyty MDF z wypukłym napisem po frezowaniu CNC”
  3. kafel lewy dolny, pod nawiasem: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-frezowany-napis-ajala.jpg`
     alt: „Frezowanie napisu w płycie z konglomeratu kwarcowego”
  4. kafel prawy dolny: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-frezowana-litera-przestrzenna.jpg`
     alt: „Frez CNC wycina literę przestrzenną z bukowego klocka”
- **Ramki:** brak
- **Linki wewnętrzne:** brak (tylko kotwice)

---

### 2. dlaczego-padir (K05 wyśrodkowany + K06)

- **Identyfikator:** dlaczego-padir, bez `id`
- **Komponent:** K05 wariant wyśrodkowany, K06 trzy karty (czarna ◆, szara ✓, szara ★)
- **Tło:** białe, karty: 1 czarna `#141414`, 2 i 3 szare `#F5F5F5`
- **Etykieta:** Dlaczego Padir
- **Nagłówek (h2):** Od frezu po grawer w jednym zleceniu
- **Lead:** Do frezowanego nośnika dochodzi nieraz front z lasera, a do detalu grawerowane oznaczenie. Wszystko to powstaje w naszej warszawskiej pracowni.
- Karta 1 (czarna, ikona ◆)
  - **h3:** Pole robocze 2 × 3 m
  - **Tekst karty:** Duży napis albo nośnik ścianki zwykle frezujemy w całości. Większe elementy dzielimy na moduły i łączymy po obróbce.
- Karta 2 (szara, ikona ✓)
  - **h3:** Jedna wycena i jeden termin
  - **Tekst karty:** Frezowanie, cięcie i grawer wyceniamy razem, a gotowe części odbierasz naraz. Nie płacisz za transport detalu między zakładami. Zobacz też [wycinanie laserowe](/wycinanie-laserowe/) i [grawerowanie laserowe](/grawerowanie-laserowe/).
- Karta 3 (szara, ikona ★)
  - **h3:** Pojedyncze sztuki i prototypy
  - **Tekst karty:** Napis czy prototyp frezujemy bez minimum ilościowego, więc nie musisz zamawiać całej serii. Jeśli się pomylimy, poprawimy element.
- **Zdjęcia:** brak
- **CTA:** brak
- **Ramki:** brak
- **Linki wewnętrzne:** #1 `/wycinanie-laserowe/` anchor „wycinanie laserowe”; #2 `/grawerowanie-laserowe/` anchor „grawerowanie laserowe”
  (oba w karcie 2, szarej: kolor linku z arkusza `.pdw a`, granat na `#F5F5F5`, 9,78:1. Karta z linkami celowo nie jest
  czarna, bo granat na `#141414` byłby nieczytelny, a wzorzec nie ma stylu linku na ciemnej karcie)

---

### 3. materialy (K05 + K07)

- **Identyfikator:** materialy, `id="materialy"`
- **Komponent:** K05 do lewej + K07 (3 karty, białe na szarym tle) + 2 ramki K01 pod siatką
- **Tło:** `#F5F5F5`, karty białe
- **Etykieta:** Materiały
- **Nagłówek (h2):** W czym frezujemy
- **Lead:** Frez wybieramy do grubszych płyt i do obróbki w głąb materiału. Niżej trzy grupy materiałów, a przy każdej przykłady z naszej frezarki.
- Karta 1
  - zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/cnc-drewno.jpg`
    alt: „Frez CNC prowadzi łukowy rowek w klejonce drewnianej”
  - **h3:** MDF, sklejka i drewno
  - **Tekst karty:** Po frezie krawędź zostaje w naturalnym kolorze, bez przyciemnienia, jakie daje laser, i od razu nadaje się pod olej albo okleinę. Z buku wyfrezowaliśmy literę przestrzenną, z MDF medalion z wypukłym napisem.
- Karta 2
  - zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/IMG_20250116_082620_HDR-scaled.jpg`
    alt: „Cienki frez CNC wycina otwór w płycie z plexi”
    (zdjęcie procesu: frez w płycie z folią ALTUGLAS; „Team” zostaje tylko w galerii, K07 i usterka 10)
  - **h3:** Plexi, także gruba i lustrzana
  - **Tekst karty:** Przy plexi grubszej niż około 10 mm frez prowadzi krawędź równo w pionie, więc element dokładnie pasuje do nośnika. Brzeg wychodzi matowy. Ze złotej plexi lustrzanej powstały napisy „Tea” i „Team”.
- Karta 3
  - zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-frezowany-relief-duka.jpg`
    alt: „Frezowany relief „Duka” w bloku z tworzywa, mierzony suwmiarką”
  - **h3:** Tworzywa techniczne i konglomerat
  - **Tekst karty:** Frezujemy też detale z tworzyw technicznych. W bloku z tworzywa powstał relief „Duka”, a w płycie z konglomeratu kwarcowego napis „Ajala”. Nie wiesz, które tworzywo wybrać? Pomoże [poradnik o obróbce tworzyw](/blog/obrobka-tworzyw-sztucznych/).
- **CTA:** brak
- **Ramki** (pod siatką kart, nie jako dziecko siatki; pierwsza z `margin: 26px 0 0`, druga z `margin: 12px 0 0`):
  - M1: Do potwierdzenia z klientem: czy frezujecie metale (aluminium, mosiądz, miedź) i do jakiej grubości? Strona „Usługi dla przemysłu” obiecuje obróbkę metali 3- i 5-osiową, a wpis „Cięcie przemysłowe” mówi, że w usługach skupiacie się na „soft-materiałach”. Obecna strona o frezowaniu ma widoczną sekcję „Frezowanie w metalu” (motoryzacja, lotnictwo, „rygorystyczne normy jakościowe”) i kartę z obróbką 3- i 5-osiową aluminium, mosiądzu i miedzi oraz protokołem pomiarowym. To samo, bez miedzi, stoi w kodzie w opisie usługi dla Google. W szkicu, także w opisie dla Google, tych treści nie ma, a metale dopiszemy po potwierdzeniu.
  - M2: Do potwierdzenia z klientem: które z tych materiałów frezujecie na co dzień: dibond, poliwęglan, sklejka WBP, pianka PVC, HIPS, POM, PA6, PP? Czy z tworzyw technicznych robicie też detale montażowe z kieszeniami, gniazdami, otworami i gwintami? Jeśli tak, dopiszemy to w karcie tworzyw. Jakie są maksymalne grubości plexi, MDF i sklejki? Czy polerujecie krawędź plexi po frezie? Czy macie zdjęcie detalu z tworzywa technicznego (np. POM, PA6) albo grubej plexi po frezie? Dziś karta tworzyw powtarza zdjęcie z galerii.
- **Linki wewnętrzne:** #3 `/blog/obrobka-tworzyw-sztucznych/` anchor „poradnik o obróbce tworzyw”

---

### 4. portfolio (K09)

- **Identyfikator:** portfolio, `id="portfolio"`
- **Komponent:** K09, hybryda `.pdr-card` (kod z `wzorzec.md`, sekcja 5), wariant na białym tle: karta `#F5F5F5`,
  siatka `repeat(auto-fill, minmax(min(100%, 300px), 1fr))`, klasa `pdw-karta`, pełne pliki z `data-pdw-zoom`
- **Tło:** białe
- **Etykieta:** Portfolio
- **Nagłówek (h2):** Galeria realizacji
- **Lead:** Sześć realizacji z frezarki: trzy napisy, litera, relief i medalion. Kliknij zdjęcie, żeby zobaczyć je w całości.
- Karty (dane 1:1 z `zrodla/realizacje-karty.json`; plakietka „Frezowanie”: tło `#DE6B24`, tekst `rgb(20, 20, 20)`):
  1. **Plakietka:** Frezowanie · **Tytuł karty:** Frezowany relief „Duka” · **Materiał karty:** Tworzywo
     zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-frezowany-relief-duka.jpg`
     alt: „Frezowany relief „Duka” - Tworzywo”
  2. **Plakietka:** Frezowanie · **Tytuł karty:** Napis przestrzenny „Team” · **Materiał karty:** Plexi lustrzana
     zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-napis-przestrzenny-team.jpg`
     alt: „Napis przestrzenny „Team” - Plexi lustrzana”
  3. **Plakietka:** Frezowanie · **Tytuł karty:** Frezowana litera przestrzenna · **Materiał karty:** Buk
     zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-frezowana-litera-przestrzenna.jpg`
     alt: „Frezowana litera przestrzenna - Buk”
  4. **Plakietka:** Frezowanie · **Tytuł karty:** Frezowany napis „Ajala” · **Materiał karty:** Konglomerat kwarcowy
     zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-frezowany-napis-ajala.jpg`
     alt: „Frezowany napis „Ajala” - Konglomerat kwarcowy”
  5. **Plakietka:** Frezowanie · **Tytuł karty:** Medalion „Republika Portionii” · **Materiał karty:** MDF
     zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-medalion-republika-portionii.jpg`
     alt: „Medalion „Republika Portionii” - MDF”
  6. **Plakietka:** Frezowanie · **Tytuł karty:** Napis przestrzenny „Tea” · **Materiał karty:** Plexi lustrzana
     zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-napis-przestrzenny-tea.jpg`
     alt: „Napis przestrzenny „Tea” - Plexi lustrzana”
  (Materiał w kodzie idzie wersalikami przez `text-transform: uppercase`, w treści zostaje zapis z JSON.)
  Kadry: karta 1 „Duka” `object-position: 25% 50%`, karta 2 „Team” `object-position: 0% 50%` (bez tego kadr 4:3 ucina
  pierwszą literę napisu); pozostałe 4 karty bez zmian.
- **Ramki** (pod siatką, przed przyciskiem, `margin: 26px 0 0`):
  - P1: Do potwierdzenia z klientem: na medalionie wyfrezowano „REPUBLIKA PORTONII”, a karta w galerii realizacji ma tytuł „Republika Portionii”. Która pisownia jest poprawna? Od odpowiedzi zależy tytuł i alt tej karty tutaj i na stronie realizacji.
- **CTA (tekst):** Zobacz wszystkie realizacje
  - cel: `/przykladkowe-realizacje/#galeria` (przycisk K03 A-mały z kodu K09)
- **Linki wewnętrzne:** #4 `/przykladkowe-realizacje/#galeria` anchor „Zobacz wszystkie realizacje”

---

### 5. na-czym-to-polega (K10)

- **Identyfikator:** na-czym-to-polega, bez `id`
- **Komponent:** K10, zdjęcie z granatowym nawiasem L + tekst; padding `36px 0px 78px` (po białym portfolio)
- **Tło:** białe
- **Etykieta:** Na czym to polega
- **Nagłówek (h2):** Obracający się frez zamiast wiązki światła
- **Akapit 1:** Frez to narzędzie skrawające zamocowane we wrzecionie. Maszyna sterowana numerycznie prowadzi go po ścieżce z pliku i warstwa po warstwie zdejmuje materiał do zadanej głębokości. Tak powstają kieszenie, wypukłe litery, fazy i otwory. Krawędź wychodzi pionowa, bez stożka, który na grubej plexi zostaje po laserze.
- **Akapit 2:** Ograniczeniem jest średnica narzędzia. W narożniku wewnętrznym zawsze zostaje zaokrąglenie o promieniu co najmniej takim jak promień frezu, dlatego drobny ażur i bardzo małe detale lepiej wychodzą laserem. Oba narzędzia porównujemy we wpisie o tym, [kiedy wybrać laser, a kiedy frez](/blog/ciecie-przemyslowe/).
- **Zdjęcie:** `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/10/IMG_20250909_084928_HDR-scaled.jpg`
  alt: „Frez CNC wycina kontury w jasnoszarej płycie, dookoła wióry”
  (kadr poziomy w ramce 5:4: widać wrzeciono, frez, płytę z wiórami i pracownię w tle; bez podpisu, to zdjęcie procesu, nie realizacja.
  Zdjęcie 1739, które stało tu wcześniej, przeszło do karty plexi w sekcji materiałów)
- **CTA:** brak
- **Ramki** (w kolumnie tekstu pod akapitem 2, `margin: 18px 0 0`):
  - N1: Do potwierdzenia z klientem: jaką dokładność frezowania możemy podać w milimetrach i jak mały detal wyfrezujecie (najmniejszy frez, najmniejszy promień wewnętrzny, najcieńsza ścianka)?
- **Linki wewnętrzne:** #5 `/blog/ciecie-przemyslowe/` anchor „kiedy wybrać laser, a kiedy frez”
- Uwaga: akapity opisują technologię, nie możliwości pracowni (fakty.md, „Wiedza ogólna”). Nagłówek nie jest pytaniem
  „Na czym polega / Czym jest frezowanie CNC?” (R4).

---

### 6. proces (K05 + K11)

- **Identyfikator:** proces, `id="proces"`
- **Komponent:** K05 do lewej + K11 (4 karty kroków, ilustracje SVG)
- **Tło:** `#F5F5F5`, padding `78px 0px`, karty białe
- **Etykieta:** Jak pracujemy
- **Nagłówek (h2):** Cztery kroki do gotowego detalu
- **Lead:** Tak wygląda droga zlecenia frezowania, od pierwszej wiadomości do odbioru. Jeśli w projekcie frez spotyka się z laserem, zajrzyj do [przeglądu trzech technologii](/produkty/) w zakładce „Produkty”.
- Krok 01
  - **Numer:** 01
  - **h3:** Plik albo szkic
  - **Tekst karty:** Do frezowania najlepiej przyślij plik STEP. Przyjmiemy też DXF, DWG, IGES, STL i PDF z wymiarami, a plik ze zdjęcia lub rysunku odręcznego przygotujemy sami.
  - ilustracja: SVG kroku 01 z `zrodla/1019-sekcje/06-proces.html` bez zmian (plik na ekranie)
- Krok 02
  - **Numer:** 02
  - **h3:** Metoda i materiał
  - **Tekst karty:** Podpowiadamy, czy detal zrobić frezem, czy laserem, i z jakiej płyty. Gdy materiał jest nietypowy albo grubość budzi wątpliwości, najpierw robimy próbę.
  - ilustracja: SVG kroku 02 z `06-proces.html` bez zmian (warstwy materiału i suwaki)
- Krok 03
  - **Numer:** 03
  - **h3:** Wzorzec i frezowanie
  - **Tekst karty:** Przy serii najpierw frezujemy jedną sztukę wzorcową. Resztę robimy dopiero wtedy, gdy ją zaakceptujesz.
  - ilustracja: NOWE SVG w stylu wzorca (`viewBox="0 0 200 240"`, `stroke="#12388C"`, `stroke-width="2.4"`, zaokrąglone końce,
    wypełnienia tylko `#12388C` i `#eef1f7`, `aria-hidden="true"`): wrzeciono z frezem palcowym nad płytą widzianą
    w perspektywie, w płycie wyfrezowana prostokątna kieszeń, obok frezu trzy, cztery drobne wióry. Bez wiązki lasera.
- Krok 04
  - **Numer:** 04
  - **h3:** Grawer i odbiór
  - **Tekst karty:** Jeśli projekt tego wymaga, frezowane części grawerujemy i uzupełniamy elementami z lasera. Gotowe zamówienie odbierzesz przy Matuszewskiej 14 albo wyślemy je kurierem.
  - ilustracja: SVG kroku 04 z `06-proces.html` bez zmian (gotowy element z ptaszkiem)
- Bez napisu „szkic” w rogu ilustracji (usterka 6).
- **CTA:** brak
- **Ramki:** brak
- **Linki wewnętrzne:** #6 `/produkty/` anchor „przeglądu trzech technologii”

---

### 7. laser-i-frez (K01 + K12 ciemny pas CTA), w miejscu case study i nagród

- **Identyfikator:** laser-i-frez, bez `id`
- **Komponent:** ramka K01 + K12 ciemny pas CTA (kod „K12 ciemny pas CTA”, `margin-top: 26px` zamieniony na `margin-top: 0px`,
  bo pas otwiera sekcję); wewnątrz pasa, pod akapitem, druga ramka K01
- **Tło:** `#F5F5F5`, padding `0px 0px 82px` (dolny odstęp jak sekcja 07 na 1019, która zamyka szary blok 06+07), czyli ciąg dalszy szarego bloku procesu (sekcja procesu dostaje wtedy
  padding dolny `26px` zamiast `78px`, żeby odstęp między kartami kroków a pasem był taki jak między kartami case study a pasem na 1019)
- **Ramka nad pasem** (`margin: 0 0 18px`):
  - L1: Do potwierdzenia z klientem: czy możemy opisać jedną pracę z frezarki jako case study (wymiary, grubość, czas, typ klienta)? Kandydat: grawerowane ramki dla WOŚP ze strony /case-study-wosp/. Jedno z jej zdjęć (to samo, które stoi wyżej w karcie plexi) pokazuje frez, który robi otwór w płycie Altuglas. Czy formatki i otwory ramek robiliście na frezarce i czy możemy pokazać tę realizację tutaj, razem z nazwą WOŚP i Fundacji Ronalda McDonalda? Pozostałe prace CNC (litera, medalion, „Tea”, „Team”, „Duka”, „Ajala”) mają w serwisie po jednym zdjęciu, dlatego w tym miejscu nie ma jeszcze kart case study.
- **Etykieta pasa:** Laser i frez razem
- **Nagłówek (h2):** Nośnik z frezarki, front z lasera
  (h2 o wyglądzie h3 z K12: `font: 700 22px / 1.3`, kolor inline bez `!important`, bo reguła motywu dotyczy tylko h3.
  Sekcja nie ma innego nagłówka, a jako h3 trafiałby w konspekcie pod „Cztery kroki do gotowego detalu”)
- **Tekst pasa:** Tak powstała ścianka fotograficzna na barce na Wiśle. Fronty z lustrzanej plexi wycięliśmy laserem, bo krawędź wychodzi wtedy z połyskiem. Nośnik z MDF wyfrezowaliśmy z pionowymi krawędziami i gwintami pod montaż. Masz podobny projekt? Napisz, a rozdzielimy go między maszyny.
- **Ramka w pasie** (pod akapitem, w tej samej kolumnie tekstu, `margin: 14px 0 0`):
  - L2: Do potwierdzenia z klientem: czy nośnik ścianki na barce frezowaliście u siebie? Czy to ten sam projekt co ścianka Bondi Sands ze strony o wycinaniu? Czy możemy pokazać zdjęcie tego nośnika?
- **CTA (tekst):** Opisz swój projekt
  - cel: `#kontakt` (wariant K03 A-ciemny, wbudowany w pas)
- **Zdjęcia:** brak (nie ma zdjęcia tej realizacji; nie podstawiamy zdjęć Bondi Sands z 1019, F94)
- **Linki wewnętrzne:** brak (jedyny link do wpisu 2078 stoi w sekcji 5; zasada „jeden link do 2078 na stronę” z linki.md)
- Uwaga: bez nazwy klienta (F94, P14). Opis jest przepisanym własnymi słowami mini-case’em z wpisu 2078, gdzie pracownia
  pisze o nim w pierwszej osobie („wycięliśmy”).

---

### 8. technologia (K14)

- **Identyfikator:** technologia, `id="technologia"`
- **Komponent:** K14, blok ciemny `#141414` ze zdjęciem i trzema liczbami + 2 karty maszyn `#1C1C1C` + akapit pod kartami
- **Tło:** białe
- **Zdjęcie bloku:** `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/10/IMG_20250909_084928_HDR-scaled.jpg`
  alt: „Frez CNC wycina kontury w jasnoszarej płycie, dookoła wióry”
  (zdjęcie zastępcze: serwis nie ma zdjęcia całej frezarki; to samo zdjęcie stoi w K10, tutaj tylko do czasu zdjęcia maszyny; patrz ramka T1)
- **Etykieta:** Park maszynowy
- **Nagłówek (h2):** Frezarka CNC obok laserów Trotec
- **Akapit:** Płyty i bloki frezujemy na polu roboczym 2000 × 3000 mm. Mamy też pięć laserów CO₂ Trotec, więc fronty i oznaczenia do frezowanych elementów robimy u siebie.
- Liczby (3):
  - **Liczba:** 2 × 3 m
    **Podpis liczby:** pole robocze frezowania
  - **Liczba:** 5
    **Podpis liczby:** laserów Trotec do cięcia
  - **Liczba:** 2002
    **Podpis liczby:** od tego roku jesteśmy na rynku
- Karta maszyny 1
  - **Chip:** Frezowanie
  - **h3:** Frezarka CNC
  - **Opis maszyny:** Na niej powstają napisy przestrzenne i nośniki pod fronty z lasera.
  - **Wiersz parametru:** Pole robocze | 2000 × 3000 mm
  - w miejscu pozostałych wierszy ramka (wzorzec K14: „karta zostaje, a w miejscu wierszy parametrów stoi ramka”):
    - T1: Do potwierdzenia z klientem: producent i model frezarki (czy to ploter Kimla z wpisu „Cięcie przemysłowe”), liczba maszyn, maksymalna wysokość materiału (oś Z) i czy robicie obróbkę 5-osiową. Czy możecie przesłać zdjęcie całej maszyny i potwierdzić, że zdjęcie frezu w szarej płycie (plik IMG_20250909_084928, tu i w sekcji „Na czym to polega”) pochodzi z Waszej pracowni? Dwa pozostałe zdjęcia frezu serwis już pokazuje jako Wasze (strona „Usługi dla przemysłu” i case study WOŚP). Od którego roku frezujecie CNC? Rok 2002 z paska liczb serwis łączy głównie z obróbką laserową. Jeśli frezarka doszła później, zaznaczymy to przy liczbie albo podamy rok, od którego frezujecie.
- Karta maszyny 2
  - **Chip:** Cięcie i grawer
  - **h3:** Lasery CO₂ Trotec
  - **Opis maszyny:** Tniemy fronty z połyskiem na krawędzi i grawerujemy oznaczenia.
  - **Wiersz parametru:** Lasery do cięcia | 5
  - **Wiersz parametru:** Największe pole | 2510 × 1680 mm
  - **Wiersz parametru:** Moc | do 500 W
- **Podsumowanie pod kartami:** Moc i pole robocze każdej z pięciu maszyn znajdziesz w [opisie parku laserów Trotec](/wycinanie-laserowe/#technologia) na stronie o wycinaniu.
- **CTA:** brak
- **Linki wewnętrzne:** #8 `/wycinanie-laserowe/#technologia` anchor „opisie parku laserów Trotec”
- Uwagi: zakres mocy tylko dywizem; nie piszemy „400 W” ani „1650 × 2510” (S5, S6). Liczby w bloku nie przeczą kartom:
  „2 × 3 m” to te same 2000 × 3000 mm co w karcie frezarki, „5” to liczba z karty laserów. Po rundzie 2 „5” jest podpisane
  jako lasery do cięcia, bo 1019 mówi „To pięć laserów do wycinania w jednej hali, a do grawerowania mamy jeszcze wiele
  innych maszyn”, a karta ma chip „Cięcie i grawer”. „2002” podpisane jako rok
  wejścia na rynek („od 2002 na rynku”), nie jako początek frezowania (F100); pytanie P16 (od kiedy frezujecie) stoi w T1. Danych katalogowych plotera Kimla (do 7 m, Z do 700 mm, 24 000 obr./min,
  ATC) nie podajemy (F21, F22).

---

### 9. zaufali-nam (K15)

- **Identyfikator:** zaufali-nam, bez `id`
- **Komponent:** K15 pas logotypów, te same pliki i alty co na 1019; zmienione h2 i lead (R2: nagłówek „Współpracujemy
  z największymi” i zdanie pod nim stoją już na 1019, 1011 i stronie głównej)
- **Tło:** białe, padding `20px 0px 82px` (po białym parku)
- **Etykieta:** Zaufali nam
- **Nagłówek (h2):** Pracowaliśmy dla tych marek
- **Lead:** Firmy i instytucje z różnych branż, dla których realizowaliśmy zlecenia.
- **Zdjęcia** (bez `data-pdw-zoom`):
  - `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-klienci.png` alt: „Logotypy klientów: Time Trend, Sokołów, PKP, Dajar, Centrum Nauki Kopernik, iGF”
  - `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-willson-brown.png` alt: „Willson &amp; Brown”
  - `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-uniwersytet.jpg` alt: „Uniwersytet Warszawski”
- **Ramki** (pod logotypami, wyśrodkowana w kontenerze 920 px, `margin: 30px auto 0`):
  - Z1: Do potwierdzenia z klientem: czy któryś z tych klientów zamawiał frezowanie i czy pokazywać pasek logotypów na stronie o frezowaniu? Tekst pod nagłówkiem celowo nie łączy tych marek z frezowaniem.
- **CTA:** brak
- **Linki wewnętrzne:** brak

---

### 10. faq (K16)

- **Identyfikator:** faq, `id="faq"`
- **Komponent:** K16, 5 pytań na `<details class="pdw-faq">`, ostatnie z `border-bottom:none;`
- **Tło:** `#F5F5F5`, białe pudełko
- **Etykieta:** FAQ
- **Nagłówek (h2):** Najczęstsze pytania
- Pytanie 1
  - **Pytanie:** Jak duży element możecie wyfrezować?
  - **Odpowiedź:** W jednym kawałku do 2000 × 3000 mm. Większy napis albo ściankę składamy z modułów łączonych na zamki. Na drugim końcu skali są detale kilkumilimetrowe.
- Pytanie 2
  - **Pytanie:** Skąd mam wiedzieć, czy mój projekt jest na frez, czy na laser?
  - **Odpowiedź:** Nie musisz tego wiedzieć. Opisz, co ma powstać, podaj materiał i przybliżony wymiar, a metodę dobierzemy sami. Na frezarkę kierujemy zwykle plexi grubszą niż około 10 mm, detale z kieszeniami i reliefami oraz części, które mają pasować do innych. Laser lepiej sprawdza się przy cienkich płytach i drobnym ażurze.
- Pytanie 3
  - **Pytanie:** Ile kosztuje frezowanie i ile trwa?
  - **Odpowiedź:** Cena zależy od materiału, wielkości, liczby sztuk, stopnia skomplikowania i przygotowania pliku. Termin podajemy razem z wyceną, a przy zamówieniu ekspresowym cena może być wyższa.
- Pytanie 4
  - **Pytanie:** Czy mogę dostarczyć własny materiał?
  - **Odpowiedź:** Tak. Przywieź płyty na Matuszewską 14 albo przyślij je kurierem. W większości przypadków możemy też zamówić materiał za Ciebie.
- Pytanie 5 (ostatnie)
  - **Pytanie:** Czy powtórzycie zamówienie po kilku miesiącach?
  - **Odpowiedź:** Tak. Plik i ustawienia maszyny z pierwszego zlecenia zachowujemy, więc kolejna partia wychodzi taka sama jak pierwsza. Jeśli zamawiasz dla produkcji albo jako firma OEM, zobacz zakładkę [„Usługi dla przemysłu”](/uslugi-dla-przemyslu/).
- **Ramki** (pod białym pudełkiem FAQ, `margin: 22px 0 0`, nie wewnątrz `<details>`, żeby była widoczna bez rozwijania):
  - F1: Do potwierdzenia z klientem: jakie są typowe terminy frezowania (pojedyncza sztuka, seria, duży format)? Czy obowiązuje minimalna wartość zlecenia (wpis FAQ z 2025 r. podaje 100 zł) i czy „próbka kontrolna gratis dla nowych klientów” obejmuje frezowanie?
- **CTA:** brak
- **Linki wewnętrzne:** #7 `/uslugi-dla-przemyslu/` anchor „„Usługi dla przemysłu”” (nazwa zakładki w cudzysłowie; bez „3- i 5-osiowa” i bez metali, R1)
- Dobór pytań: nie powtarzamy pytań z `/produkty/` i `/uslugi-dla-przemyslu/` („jakie pliki”, „cięcie, frezowanie i grawer
  w jednym zleceniu”, R6), pytania „Jakie są zalety frezowania CNC?” (R4) ani pytań z 1019. Pliki są w kroku 01 procesu,
  jedno zlecenie w karcie 2 „Dlaczego Padir”.

---

### 11. kontakt (K17)

- **Identyfikator:** kontakt, `id="kontakt"`
- **Komponent:** K17, formularz `<div class="pdw-form">[contact-form-7 id="480"]</div>`; zmieniane tylko h2 sekcji i lead
- **Tło:** białe, padding `82px 0px 92px`
- **Nagłówek (h2):** Masz projekt do frezowania?
- **Lead:** Wyślij plik STEP albo choćby zdjęcie detalu. Dopisz materiał i wymiary, a przy serii także liczbę sztuk. Odeślemy wycenę z terminem.
- **Stały tekst (bez zmian z K17):** Skontaktuj się z nami
- **Stały tekst (bez zmian z K17):** Masz pytania? Chętnie pomożemy
- **Stały tekst (bez zmian z K17):** Telefon +48 22 741 36 55
- **Stały tekst (bez zmian z K17):** E-mail laser@padir.pl
- **Stały tekst (bez zmian z K17):** Adres ul. Matuszewska 14, Warszawa
- **Stały tekst (bez zmian z K17):** Godziny otwarcia Poniedziałek - Piątek: 8:30 - 16:00 Budynek C2, wejście T9
  (po rundzie 2 linia bajt w bajt jak w `12-kontakt.html`, na 1019, `/kontakt/` i w szkicu grawerowania; to zwykły dywiz,
  więc reguła 1 z BRIEF jest spełniona. Zmiana zapisu zakresów, jeśli w ogóle, jedną decyzją na wszystkich tych stronach naraz)
- **Stały tekst (bez zmian z K17):** PADIR Ewa Salabura Matuszewska 14, 03-876 Warszawa NIP: 536-104-65-17
- **Stały tekst formularza (generuje WordPress z formularza 480):** Imię i Nazwisko Adres email Telefon Treść zapytania Wyrażam zgodę na przetwarzanie moich danych osobowych, podanych w niniejszym formularzu, w celu przetworzenia zapytania i prowadzenia korespondencji przez PADIR Ewa Salabura, Matuszewska 14, 03-876 Warszawa.
- **Zdjęcia:** logo `https://grawerowanie-laserowe.pl/wp-content/uploads/2024/02/padir-logo.png` alt „Padir” (bez zmian, bez `data-pdw-zoom`)
- **Ramki:** brak
- **Linki wewnętrzne:** brak (telefon `tel:+48227413655`, e-mail `mailto:laser@padir.pl` bez zmian)

---

### 12. dane strukturalne (poza widoczną treścią)

- **Identyfikator:** dane-strukturalne, osobny blok `<!-- wp:html -->` za `<!-- /wp:group -->`, tak samo jak na 1011, 456 i 2264
- **Kod:** `<script type="application/ld+json" data-no-optimize="1">` z obiektem schema.org `Service`,
  `@id` `https://grawerowanie-laserowe.pl/frezowanie-cnc/#service` (ten sam co dziś na 1011), `provider` i `serviceLocation`
  wskazują `https://grawerowanie-laserowe.pl/#organization` (LocalBusiness ze strony `/kontakt/`), telefon `+48227413655`,
  `areaServed` Polska (jak dziś na 1011)
- **description:** Frezowanie CNC plexi, MDF, sklejki, drewna, konglomeratu kwarcowego i tworzyw technicznych. Napisy przestrzenne, reliefy i nośniki pod fronty z lasera. Elementy do 2000 × 3000 mm w jednym kawałku, zamówienia od jednej sztuki.
- **hasOfferCatalog (5 pozycji):** Frezowanie MDF, sklejki i drewna; Frezowanie plexi; Frezowanie tworzyw technicznych
  i konglomeratu kwarcowego; Napisy i litery przestrzenne; Reliefy i medaliony
- Dlaczego: obecny blok na 1011 podaje „Obróbka skrawaniem 3- i 5-osiowa detali z MDF, konglomeratu, drewna, aluminium,
  mosiądzu i tworzyw konstrukcyjnych” i „protokół pomiarowy dla każdej partii” oraz ofertę „Frezowanie aluminium i mosiądzu”.
  Szkic tych rzeczy nie potwierdza (M1, T1), więc nowy opis zawiera wyłącznie fakty z tej strony. Metale i 5 osi
  dopisujemy dopiero po odpowiedzi na M1 i T1. Bez `image` (`#primaryimage`), bo szkic nie ma obrazka wyróżniającego.
- Ramka: informacja dla klienta dopisana na końcu M1.

---

## Linki wewnętrzne: zestawienie

| # | adres | anchor | sekcja |
|---|---|---|---|
| 1 | `/wycinanie-laserowe/` | wycinanie laserowe | dlaczego-padir, karta 2 |
| 2 | `/grawerowanie-laserowe/` | grawerowanie laserowe | dlaczego-padir, karta 2 |
| 3 | `/blog/obrobka-tworzyw-sztucznych/` | poradnik o obróbce tworzyw | materialy, karta 3 |
| 4 | `/przykladkowe-realizacje/#galeria` | Zobacz wszystkie realizacje | portfolio, przycisk |
| 5 | `/blog/ciecie-przemyslowe/` | kiedy wybrać laser, a kiedy frez | na-czym-to-polega, akapit 2 |
| 6 | `/produkty/` | przeglądu trzech technologii | proces, lead |
| 7 | `/uslugi-dla-przemyslu/` | „Usługi dla przemysłu” | faq, pytanie 5 |
| 8 | `/wycinanie-laserowe/#technologia` | opisie parku laserów Trotec | technologia, pod kartami |

Wszystkie adresy mają status `publish` w `zrodla/SPIS.json`; `id="galeria"` jest na 1397, `id="technologia"` na 1019.
Bez linków do: wpisu 1660 (R8), 1578 (R3), 967 i 1873 (R4), `/uslugi-dla-horeca/` (R7, P21), szkiców 1797, 1823, 1829, 1845,
`/torebki/`, case study (żadne nie dotyczy frezu).

## Ramki „Do potwierdzenia z klientem”: zestawienie

| kod | sekcja | pytania z fakty.md |
|---|---|---|
| M1 | materialy | P04, P03 (sprzeczność S1); stary opis usługi w danych strukturalnych 1011 |
| M2 | materialy | P26, P28 (detale montażowe z tworzyw), P10, P11, P23 (zdjęcie tworzywa zamiast powtórki z galerii) |
| P1 | portfolio | pisownia z zdjecia.json (medalion 2319), P12 |
| N1 | na-czym-to-polega | P05, P09 |
| L1 | laser-i-frez | P12 (brak materiału na case study; kandydat: case study WOŚP ze zdjęciem 1739) |
| L2 | laser-i-frez | P14 |
| T1 | technologia | P01, P02, P03, P23 (oraz pochodzenie zdjęcia 2148; 2256 i 1739 serwis już pokazuje jako prace pracowni), P16 (od kiedy frezujecie, rok 2002 w pasku liczb) |
| Z1 | zaufali-nam | P24 |
| F1 | faq | P07, P08 |

## Uwagi dla prowadzącego (poza treścią strony)

- Przy przenoszeniu treści na 1011 USUNĄĆ stary blok `ld+json` z końca strony 1011 (z 5 osiami, aluminium, mosiądzem
  i protokołem pomiarowym). Nowy blok jest na końcu szkicu (sekcja 12) i zastępuje go 1:1, ten sam `@id`.
- `sklad-notatki.md` opisuje stan sprzed rundy 1 i nie był poprawiany (poza zakresem plików redakcji). Aktualne odstępstwa
  od wzorca: sekcja 7 ma `padding: 0px 0px 82px` i własne h2 w pasie (22 px, białe), za `<!-- /wp:group -->` stoi osobny
  blok `wp:html` z `ld+json` Service (sekcja 12), kafle mają `object-position` 20% (Tea w hero), 0% (Team) i 25% (Duka)
  (mapa zdjęć), a godziny w kontakcie są bajt w bajt jak w K17. Gotowe poprawki do notatek: `poprawki-r2.md`, uwaga 6.

- Po odpowiedzi na M1 i T1 (metale, 5 osi) trzeba ujednolicić `/uslugi-dla-przemyslu/` albo tę stronę: link „Poznaj
  frezowanie CNC” z 2264 prowadzi tu wprost z obietnicy obróbki 3- i 5-osiowej metali (R1).
- Alty na 2264 dla `IMG_0060` (2279) i `wbet-ds18` (2262) nie zgadzają się z kadrami (zdjecia.json, „braki”).
- Po publikacji warto dodać link do `/frezowanie-cnc/` we wpisie 2078 i w zdaniu o frezowaniu na `/przykladkowe-realizacje/`
  (linki.md, rozdz. 4).
