# Grawerowanie laserowe: poprawki po rundzie 1 weryfikacji

Plik strony: `praca/grawerowanie/strona.html`. Zaktualizowane też `tresc.md` (teksty, opisy zdjęć, tabela ramek,
liczba słów 1293 → 1372, ramki 198 → 260) i `ksiega.json` (161 → 171 wpisów, każdy cytat sprawdzony skryptem
w pliku źródłowym, wpisy „DO POTWIERDZENIA” zgodne z ramkami na stronie).

Kontrola: `python3 -I sprawdz_szkic.py praca/grawerowanie/strona.html --szkic` kończy się kodem **0**
(0 błędów, 0 ostrzeżeń, 32 zdjęcia, 1 × h1, 7 ramek).

Render w ramie motywu (Chromium, font Poppins, skrypt `red-r1/render.py` w katalogu roboczym): przy 1440, 1100,
1024, 768, 390 i 360 px nie ma poziomego przewijania (scrollWidth = szerokość okna). Zrzuty kontrolne:
`red-r1/r1-1440-realizacje.png`, `r1-390-realizacje.png`, `r1-1440-zastosowania.png`, `r1-1024-zastosowania.png`,
`r1-1440-technologia.png`, `r1-1440-portfolio.png`, `r1-1440-materialy.png`. Kopia strony sprzed poprawek:
`red-r1/strona-przed-r1.html`.

Wynik: 34 uwagi wprowadzone (w całości, częściowo albo inną drogą), 2 odrzucone w całości (#14, #36).
Odrzucone części uwag częściowo wprowadzonych są opisane przy każdej z nich.

---

## Weryfikacja wspólna: zdjęcia case study WOŚP (#1, #7, #10, #11, #32, #33)

Pobrałem trzy pliki z biblioteki. `IMG_0840-rotated.jpg` (1738) i `IMG_0840-1-rotated.jpg` (1740) są identyczne
bajt w bajt: oba mają 267 476 B, md5 `4b012d94424494b82e1d7f57560ccc11`, 1512 × 2016 px. `1.jpg` (1737) też ma
1512 × 2016, czyli 3:4. Obejrzałem oba kadry i ich dolne pasy (`red-r1/case-obok.png`, `red-r1/case-doly.png`):
grawer („Dinozaur”, „Julek l.6”, logotypy Fundacji, padir i 33. Finału) leży na dole ramy 1738, na ok. 86-90%
wysokości, czyli poza kadrem 4:3 ciętym od środka. Na ramie z kotem grawer nie jest widoczny. Czwarte zdjęcie
z `/case-study-wosp/` (`IMG_20250116_082620_HDR`, 1739) pokazuje frez CNC i stoi już na szkicu frezowania
(`praca/frezowanie/strona.html`, alt „Cienki frez CNC wycina otwór w płycie z plexi”).

**Co zrobiłem:** lewa kolumna karty A to teraz dwa pionowe kafle 3:4 obok siebie. Kot (1737) jest pod nawiasem L
(promień 90 px, nawias 118 px jak w K12), dinozaur (1738) w prawym kaflu z promieniem miniatury. Nic nie jest
przycinane, a grawer u dołu ramy widać bez lightboxa (zrzuty 1440 i 390 px). 1740 usunięty. Kolejność wziąłem
z #7, a nie z #32, bo przy dinozaurze pod nawiasem łuk 70-90 px zasłaniałby na telefonie początek tytułu
„Dinozaur” w lewym dolnym rogu ramy.

---

## Uwagi po kolei

### 1. [fakty, ważny] Drugi kafelek case study to duplikat
**Wprowadzona.** Zasadna (patrz weryfikacja wspólna). Usunięty kafel 1740. Zamiast wariantu „kot na całą
szerokość” wybrałem układ dwóch kafli 3:4 z #7, bo pokazuje też grawer.

### 2. [fakty, ważny] FAQ: 4-5 dni dotyczy serii prezentów firmowych
**Wprowadzona.** Potwierdzone w `posts-2177`: „4 Seria Przy prezentach zwykle 4 do 5 dni roboczych od chwili, gdy
materiał jest u nas.”, czyli krok po próbce w tekście o prezentach firmowych. FAQ 2 mówi teraz: „Serię prezentów
firmowych robimy zwykle w 4-5 dni roboczych, licząc od dnia, w którym dostaniemy przedmioty.” (pełna odpowiedź
w #16). Opcjonalną część też wprowadziłem: ramka pod FAQ („pytania 1-3”) pyta, czy terminy z pytania 2 są aktualne
i czy podać termin serii innej niż prezenty (P08). Księga: wpis 141 z pełnym cytatem kroku „Seria”.

### 3. [fakty, ważny] Laser UV, „inne maszyny”, flexx
**Wprowadzona częściowo.** Cytaty potwierdzone: `pages-2283` „Głowica obrotowa CO2 lub laser UV”, `pages-1019`
„a do grawerowania mamy jeszcze wiele innych maszyn”. W `fakty.md` jest pytanie P02, którego nie miała żadna ramka.
Dopisałem do ramki pod kartami maszyn trzy pytania: czy laser fiber to osobna maszyna, czy źródło fiber w Speedy 360
z opcją flexx; czy macie laser UV i czy grawerujecie nim szkło; jakie „inne maszyny do grawerowania” ma na myśli
strona Wycinanie laserowe. (Pytanie o flexx najpierw dałem do ramki w karcie fiber, ale karty maszyn zrobiły się
przez to wyraźnie wyższe, więc przeniosłem je do ramki pod kartami.)
**Odrzucona część:** nie przepisałem zdania z „Na czym to polega” na „szkło laserem CO₂ na głowicy obrotowej”.
Obecne zdanie ma źródło (`pages-2283`: „Laser CO2 z głowicą obrotową prowadzi grawer wokół całego naczynia.”),
a wersja z głowicą pomija płaskie szkło, więc byłoby to nowe zawężenie bez źródła. Niepewność co do UV
obsługuje ramka.

### 4. [fakty, drobny] WOŚP: przekręcona kolejność zdarzeń
**Wprowadzona** (z językiem z #23). Potwierdzone w `pages-12`: „W ramach podziękowania za tę pomoc, dzieci
przygotowały wzruszające rysunki … Podczas rozmów z Fundacją narodził się pomysł, aby … przekazać na aukcję”.
Wyzwanie: „Dzieci, którym pomaga dom Fundacji Ronalda McDonalda, przygotowały rysunki w podziękowaniu za tę pomoc.
W rozmowach z Fundacją padł pomysł, by przekazać je na aukcję WOŚP. Trzeba je było oprawić tak, żeby dobrze wypadły
na licytacji.” Nie użyłem „Razem z Fundacją postanowiliśmy”, bo źródło nie mówi, kto podjął decyzję. Księga: wpisy 88
i 89 z nowymi cytatami.

### 5. [fakty, drobny] „3,55 m/s” bez „do”
**Wprowadzona** (razem z #29). Liczba została „3,55 m/s”, a podpis brzmi „maks. prędkość graweru na laserze
Speedy 360”. Tak samo robi wzorzec 1019 („400 W” / „maks. moc cięcia”), a „do 3,55 m/s” 30-punktową czcionką
łamałoby się w wąskim kaflu.

### 6. [fakty, drobny] Alt „Stalowy detal” bez pokrycia
**Wprowadzona.** W `pages-2264-…raw.html` są trzy alty tego pliku, w tym „Element z aluminium po obróbce”.
Obejrzałem zdjęcie (`red-r1/wbet.png`): ciemnoszary detal z radełkiem i śladami toczenia, materiału nie da się
rozstrzygnąć. Nowy alt: „Toczony metalowy detal z grawerowanym oznaczeniem WBET-DS-18”. Księga: wpis 101 (cytat
z altu „Element WBET DS18” i adnotacja, że materiału nie podajemy).

### 7. [wzorzec, ważny] K12: dwa razy ten sam kadr, grawer ucięty
**Wprowadzona** dokładnie w proponowanym układzie (kot pod nawiasem, dinozaur obok, oba 3:4). Alty z „Ramka”
(#23). Zrzuty po zmianie: `r1-1440-realizacje.png`, `r1-390-realizacje.png`.

### 8. [wzorzec, drobny] Linki w kartach zastosowań: styl spoza wzorca
**Wprowadzona.** Potwierdzone: 1019 K04 ma `font: 800 15px / 1 Poppins…; text-decoration: none;` i SVG z dwiema
polyline, 1397 ma `.pdr-cta{…font-weight:800;…text-decoration:none}` z tym samym szewronem. Cztery linki mają teraz
wagę 800, 15 px, granat, bez podkreślenia, statyczny podwójny szewron (`aria-hidden="true"`), a ostatnie słowo
i szewron są w `white-space: nowrap`. Bez animacji, więc arkusz dodatków bez zmian.

### 9. [wzorzec, drobny] K07: 4 karty, układ 3 + 1
**Wprowadzona.** `wzorzec.md`, K07: „Liczba kart: wielokrotność 3”. Zewnętrzna siatka
`minmax(min(100%, 542px), 1fr)` z dwiema parami kart. Zmierzone: 1440 px 4 karty po 277 px w jednym rzędzie,
1100/1024/768 px układ 2 × 2, 390/360 px jedna kolumna, bez poziomego przewijania.

### 10. [technika, ważny] Prawy mały kafel to duplikat
**Wprowadzona częściowo.** Duplikat usunięty (weryfikacja wspólna).
**Odrzucona część:** podmiana na `IMG_20250116_082620_HDR` (frezarka CNC wierci płytę Altuglas). To zdjęcie
frezowania, nie graweru, i stoi już na szkicu frezowania. Na stronie graweru wprowadzałoby w błąd.

### 11. [technika, ważny] Kadr 4:3 ucina grawer na dużym zdjęciu
**Wprowadzona inną drogą.** Kafle są teraz 3:4, jak oba pliki, więc `object-position` nie jest potrzebne:
zdjęcie mieści się w całości, a grawer u dołu ramy jest widoczny.

### 12. [technika, drobny] Złamany link ma interlinię 37 px
**Wprowadzona.** Każdy z czterech linków ma `display: inline-block`. Linia po złamaniu ma własne `line-height`
1,4. Na zrzucie 1440 px dwulinijkowe linki mają zwarty odstęp.

### 13. [technika, drobny] Wymiary łamią się w środku
**Wprowadzona.** `2510&nbsp;×&nbsp;1680&nbsp;mm` w akapicie technologii i `ok.&nbsp;0,3&nbsp;mm` w karcie fiber,
do tego `200&nbsp;mm` w nowym opisie Speedy 300. Kontrola nie zgłasza problemu z encjami.

### 14. [technika, drobny] Kontrast placeholdera w formularzu 4,15:1
**Odrzucona.** Problem jest prawdziwy, ale `wzorzec.md`, usterka 19 rozstrzyga: „słabe kontrasty arkusza
formularza: placeholder 4,17:1 … znane, arkusza nie zmieniamy (spójność z 1019)”. Sam weryfikator proponuje zmianę
tylko razem ze wzorcem. Do decyzji dla prowadzącego: poprawić `rgba(255,255,255,.45)` → `.55` jednocześnie na 1019
i w obu szkicach.

### 15. [język, ważny] Hero: szkło „od pojedynczej sztuki” vs FAQ „szkło od 12 sztuk”
**Wprowadzona.** Hero: „Grawerujemy metal, drewno, plexi, skórę i szkło, od jednej obrączki po serie tabliczek
znamionowych.” Ramka o progu 12 sztuk dla klienta indywidualnego zostaje.

### 16. [język, ważny] FAQ „Ile czeka się na grawer?”
**Wprowadzona z poprawką.** Pytanie: „Ile się czeka na grawer?”. Odpowiedź: „Małe zlecenia zajmują zwykle około
2 dni roboczych, a pojedyncze rzeczy czasem zrobimy od ręki, więc warto wcześniej zadzwonić. Serię prezentów
firmowych robimy zwykle w 4-5 dni roboczych, licząc od dnia, w którym dostaniemy przedmioty. Przed świętami,
w listopadzie i grudniu, terminy się wydłużają, więc dokładny termin podamy przy wycenie.” Propozycja weryfikatora
„W listopadzie i grudniu kolejka jest dłuższa” to dosłowny fragment `posts-2177`, a BRIEF mówi „Fakty tak, zdania nie”,
więc przeredagowałem. „Podamy przy wycenie” ma źródło: „Odpowiadamy w ciągu 24 godzin, z ceną i terminem.”
(nowy wpis w księdze).

### 17. [język, ważny] Nadmiar trójek
**Wprowadzona.** Karta „Pojedyncze sztuki”: „Jedna obrączka czy jeden nóż to u nas zwykłe zlecenie. Plik i ustawienia
lasera z każdej serii zachowujemy, więc kolejna partia, nawet po roku, wyjdzie taka sama jak pierwsza.” (dalej od
szkieletu zdania z `/produkty/`). Karta „Grawer, cięcie i frez razem”: „Jeśli przedmiot trzeba też wyciąć albo
sfrezować, zrobimy to w tej samej pracowni, w ramach jednego zamówienia.” Laser fiber: „Numery seryjne i kody na stali,
aluminium i mosiądzu.” Noże: „Logo albo monogram na głowni lub rękojeści.” Akapit „Materiały” i karta „Prezenty”
w #20 i #22. Wyliczenia materiałów („stal, aluminium, mosiądz”) to listy rzeczowe, nie retoryczne trójki, więc zostały.

### 18. [język, ważny] Skóra: „wtłoczony”, kopia tabeli z bloga
**Wprowadzona częściowo, z inną treścią.** Zasadne: zdanie powtarza strukturę i listę z `posts-2177`, a „bez farby”
padało czwarty raz. Nowy tekst: „Grawer wychodzi ciemniejszy od lica skóry, z naturalnie przyciemnionymi
krawędziami. Sprawdza się na etui, okładkach notesów i podkładkach.” Źródła: `posts-2177` „Ciemniejszy odcisk
wpisany w materiał.” i `pages-2283` „Grawer tłoczony, bez farby i bez naklejek, z naturalnym przyciemnieniem krawędzi.”
**Odrzucona część:** teza, że „wtłoczony” to błąd merytoryczny. Padir sam nazywa grawer na skórze „tłoczonym”
(`pages-2283`, dwa razy). Nie przyjąłem też „lekko ją wypala”, bo nie ma źródła.

### 19. [język, ważny] Drewno: „Laser przyciemnia rysunek”
**Wprowadzona.** „Dąb, orzech, akacja, bambus, sklejka i MDF. Grawer na drewnie wychodzi ciemniejszy od tła, a jego
odcień zależy od gatunku i układu słojów. Dwie sztuki z tym samym wzorem nie będą identyczne.” Sprawdziłem źródło
na „gatunek”: `posts-2208` „różne gatunki reagują inaczej” i „jasne tło i ciemniejszy grawer” (nowe wpisy w księdze).
Zniknęła „każda deska”, która nie pasowała do pokrywki świecy na zdjęciu.

### 20. [język, drobny] Bliskie parafrazy innych stron
**Wprowadzona.** Technologia: „Jeśli projekt jest większy, grawerujemy go w częściach i składamy po obróbce.” Plexi
(razem z #35): „Na przezroczystej plexi grawer jest mlecznobiały i świeci, gdy podświetlisz płytę od krawędzi.”
Lead „Na czym grawerujemy”: „Szkło pod wiązką matowieje, a drewno ciemnieje. Na aluminium i powlekanej stali zostaje
jasny ślad, a na gołej stali efekt zależy od wykończenia. Dlatego ustawienia lasera dobieramy do konkretnego
przedmiotu.” Zastrzeżenie o gołej stali i powłoce ma źródło w `posts-2177` (dwa nowe wpisy w księdze).

### 21. [język, drobny] Nagłówki
**Wprowadzona z poprawką.** Case study H2: „Realizacja z bliska”, lead: „Jedno zlecenie rozpisane krok po kroku.”
Technologia H2: „Park maszynowy do graweru”. Opis SP2000: „Gdy płyta nie mieści się na mniejszych maszynach.”
**Odrzucona część:** lead „Jedno zlecenie z galerii, …”. Case WOŚP nie ma karty w galerii: w
`zrodla/realizacje-karty.json` żadna z 44 kart nie wspomina WOŚP ani ramek.

### 22. [język, drobny] Prezenty: łańcuch „na … na … na”
**Wprowadzona z poprawką.** „Dedykacje z okazji komunii czy ślubu, wygrawerowane na zegarku, biżuterii, łyżeczce albo
ramce na zdjęcie.” Bez „jubileuszu” z propozycji, bo w źródłach (`pages-1812`, `pages-456`) jest komunia, ślub
i walentynki, a jubileuszu nie ma. Wpis księgi „Prezenty: inne okazje” usunięty, bo to twierdzenie zniknęło ze strony.

### 23. [język, drobny] WOŚP: „narysowały prace”, blok Efekt, „Rama”/„ramka”
**Wprowadzona.** Efekt: „Oprawione rysunki miały trafić na licytację, a cały dochód z niej na onkologię i hematologię
dziecięcą. Ramki i grawer wykonaliśmy bezpłatnie.” Oba alty z „Ramka z przezroczystej plexi…”. Wyzwanie zbudowałem
z #4, bo wersja z #23 („przygotowały rysunki na aukcję WOŚP”) zostawiała błędną kolejność zdarzeń.

### 24. [język, drobny] Proces: lead, krok 02, krok 04
**Wprowadzona z poprawką.** Lead: „Cztery kroki od pliku do odbioru, takie same przy jednej sztuce i przy serii.
Przy serii albo nowym materiale dochodzi próbka.” Krok 02: „… Jeśli nie masz materiału, zwykle możemy go zamówić
za Ciebie. Laser i jego ustawienia dobieramy do tego, co trafi pod wiązkę.” Krok 04: „Gotowe rzeczy odbierzesz u nas
na Matuszewskiej 14 albo wyślemy je kurierem na Twój adres.”
**Odrzucona część:** „Przed serią dochodzi tylko próbka” przeczyłoby krokowi 03 („Przy serii i nowym materiale…”).
W kroku 02 zostawiłem „zwykle”, bo źródło (`posts-1660`) mówi „W większości przypadków możemy samodzielnie zamówić”.

### 25. [język, drobny] Portfolio: lead bez orzeczenia
**Wprowadzona.** „Tu widzisz 9 z 24 prac grawerskich z naszej galerii. Kliknij zdjęcie, żeby obejrzeć je z bliska.”
Liczba 24 sprawdzona: 24 karty z „eng” w `realizacje-karty.json`.

### 26. [język, drobny] Na czym to polega: „w niej”, szablon/przyrząd, anchor
**Wprowadzona.** Akapit 1: „Laser zdejmuje z powierzchni mikrowarstwę materiału, a w jej miejscu zostaje rysunek.
Wiązka nie dotyka przedmiotu, dlatego nie dociska cienkich i delikatnych rzeczy.” (bez zdania o farbie, które
powtarzało hero). Akapit 2: „przyrząd” zamiast „szablon” (zgodnie z altem zdjęcia obok; w źródle „podstawkę / szablon”),
link z anchorem „Jak działa grawerowanie laserowe” w cudzysłowie, czyli tytuł wpisu 2208 z `SPIS.json`.

### 27. [język, drobny] Dwa znaczenia słowa „detal”
**Wprowadzona.** Lead „Dlaczego Padir”: „Przedmiot nie musi też jeździć między warsztatami.” Karta 3 i lead galerii
poprawione w #17 i #25. Speedy 300 ma teraz „drobne detale” (znaczenie: szczegóły).

### 28. [język, drobny] FAQ: „bywa kruche pod wiązką”, „próba”
**Wprowadzona.** „Cienkie szkło może pod wiązką pęknąć, dlatego przy nim i przy nietypowych materiałach zaczynamy
od próbki.” Źródło `posts-2208`: „choć szkło przy laserze też potrafi pęknąć”.

### 29. [język, drobny] „na Trotec Speedy 360”, „wyższych przedmiotach”
**Wprowadzona.** Podpis liczby: „maks. prędkość graweru na laserze Speedy 360” (z #5). Speedy 300: „Personalizacja
i drobne detale, także na przedmiotach do 200&nbsp;mm wysokości.”

### 30. [język, drobny] Zastosowania: „tych obszarów”, karta hotelowa
**Wprowadzona.** Lead: „Grawerujemy dla firm i osób prywatnych. Każdy z czterech obszarów poniżej ma u nas osobną
stronę z przykładami.” (wszystkie cztery strony są opublikowane, `SPIS.json`). Hotele: „Logo lokalu na szkle
i sztućcach, numery pokoi i plakietki dla obsługi. Grawer zrobimy też na naczyniach, które lokal już ma.”

### 31. [język, drobny] Szkło: pleonazmy; kolejność „filc i tkaniny, papier, karton”
**Wprowadzona z poprawką.** Szkło: „Okrągłe naczynia mocujemy w głowicy obrotowej, dzięki czemu grawer może biec
wokół całego obwodu.” (zamiast „wzór może okrążyć całe szkło”, które brzmi nienaturalnie). Akapit: „Grawerujemy też
filc, tkaniny, papier i karton, a nawet skórkę owoców.”

### 32. [zdjęcia, ważny] Case study: ten sam kadr dwa razy
**Wprowadzona częściowo.** Układ dwóch kafli 3:4 bez przycinania, jak proponuje uwaga.
**Odrzucona część:** kolejność (dinozaur pod nawiasem, łuk 70 px, nawias 96 px). Przyjąłem wariant z #7 (kot pod
nawiasem, wymiary nawiasu z K12), żeby nawias nie zachodził na tytuł „Dinozaur”. Nie dodałem trzeciego kafla ani
ramki z prośbą o zbliżenie graweru: grawer jest teraz widoczny w kaflu, a w bibliotece nie ma trzeciego zdjęcia ramki.

### 33. [zdjęcia, ważny] Case study: kadr 4:3 bez graweru
**Wprowadzona inną drogą** (jak #11): kafle 3:4 bez kadrowania, alt opisuje to, co widać.

### 34. [zdjęcia, drobny] Galeria: karta sztućców pokazuje sam rozbłysk
**Wprowadzona częściowo, wariant minimalny.** Obejrzałem kadr (`red-r1/sztucce-kadry.png`): środek 4:3 to sam trzonek
z rozbłyskiem, przy `object-position: 15% 50%` widać szyjkę i część czerpaka łyżki. Dopisane do stylu `<img>`
(zrzut `r1-1440-portfolio.png`).
**Odrzucona część:** podmiana na panel „anko” z hero. `wzorzec.md`, K09: „bez powtórzeń zdjęć z hero i K07 na tej samej
stronie”. To reguła katalogu dla portfolio i jest ważniejsza niż wyjątek z usterki 10. Zapasowej, nieużytej karty
„Grawerowanie” nie ma (`tresc.md`, dobór 9 z 21).

### 35. [zdjęcia, drobny] Karta „Plexi i tworzywa” ze zdjęciem ładowarki
**Wprowadzona.** Zdjęcie potwierdzone (zdjecia.json 2357 i podgląd: czarna obudowa enel x z oplotem). H3: „Tworzywa
i plexi”, tekst: „Obudowy i panele z tworzyw. Każde tworzywo reaguje inaczej, więc serię zaczynamy od próbki. Na
przezroczystej plexi grawer jest mlecznobiały i świeci, gdy podświetlisz płytę od krawędzi.” Źródła w księdze
(`pages-2264`: obudowy, panele, CO2 na tworzywach).
**Odrzucona część:** nowa ramka z prośbą o zdjęcie graweru w plexi. Karta po zmianie zgadza się ze zdjęciem, grawer
w plexi widać w case study na tej samej stronie, a ramki służą informacjom, bez których nie da się pisać.

### 36. [zdjęcia, drobny] Alty galerii „Tytuł - Materiał”
**Odrzucona.** `wzorzec.md`, K09: pola z `zrodla/realizacje-karty.json` „bez przepisywania, 1:1”, w tym `alt`. To
zatwierdzone realizacje i te same alty stoją na 1397. Alt plakiety („Plakieta myśliwska „Skalisko” - Mosiądz”) nie
twierdzi, że relief jest grawerem. Jeśli alty mają być opisowe, trzeba to zmienić w całej galerii (JSON + 1397 + oba
szkice). Decyzja należy do prowadzącego, nie do jednego szkicu.

---

## Pliki zmienione w tej rundzie

- `praca/grawerowanie/strona.html`: wszystkie zmiany opisane wyżej.
- `praca/grawerowanie/tresc.md`: teksty 1:1 ze stroną, nowa tabela zdjęć case study, opis siatki i linków
  w zastosowaniach, nota o kadrze sztućców, tabela ramek (P02, P08), liczba słów.
- `praca/grawerowanie/ksiega.json`: 41 wpisów zmienionych, 11 dodanych, 1 usunięty („Prezenty: inne okazje”).
  Wszystkie 171 cytatów jest w swoich plikach źródłowych, wpisy ramek zgadzają się z tekstem na stronie.
- Skrypty i dowody tej rundy: `red-r1/` w katalogu roboczym (`popraw_strone.py`, `popraw_ksiege.py`,
  `popraw_tresc.py`, `render.py`, zrzuty `r1-*.png`, kopie plików sprzed zmian).
