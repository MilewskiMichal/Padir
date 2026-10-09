# Frezowanie CNC: poprawki po rundzie 2 weryfikacji

Plik: `praca/frezowanie/strona.html`. Weryfikatorzy zgłosili 17 uwag. Wprowadziłem 16, w tym 5 z korektą proponowanego
brzmienia (2, 4, 7, 11, 13; uwaga 17 połączona z 2). Odrzuciłem jedną, uwagę 6, bo dotyczy pliku spoza mojej listy
(`sklad-notatki.md`). Gotowe poprawki do tego pliku są niżej, przy uwadze 6, a w `tresc.md` doszedł odsyłacz dla prowadzącego.
Zmiany treści są przeniesione 1:1 do `tresc.md`, a źródła do `ksiega.json` (199 wpisów, było 192;
`narzedzia-fz/sprawdz_ksiege.py`: 0 błędów).

Kontrola końcowa:
- `python3 -I sprawdz_szkic.py praca/frezowanie/strona.html --szkic`: **kod 0**, 0 błędów, 0 ostrzeżeń, 20 zdjęć, 1 h1, 10 ramek.
- `tresc.md` porównany maszynowo z widocznym tekstem strony (`red-r2/frez/porownaj.py`): 126 pól i ramek, 0 rozbieżności.
- Sekcja kontaktu porównana z `zrodla/1019-sekcje/12-kontakt.html` (difflib). Różnią się tylko h2, lead i poprawka
  `min(100%, 320px)` z katalogu usterek. Linia godzin jest bajt w bajt taka jak we wzorcu.
- Licznik `wer-jezyk-r2-licz.py` na nowym tekście (`red-r2/frez/tekst-po.txt`): „jeden*” 6 (było 11), „krawęd*” 5 (było 6,
  w sekcji materiałów 2), „daje/Daje” 1 (było 3), „pion*” 3 (było 4).
- `narzedzia-fz/licz_tresc.py` (NG=5): wspólne ciągi z innymi stronami te same co po rundzie 1, czyli etykiety przycisków
  wzorca, dane kart galerii, „iges stl i pdf z”, „przyjmujemy już od jednej sztuki” i „większe elementy dzielimy na moduły”.
  Długość 1046 słów z blokiem kontaktu, 970 bez niego.
- W `strona.html`, `tresc.md` i tym raporcie nie ma pauzy, półpauzy, minusa (U+2014, U+2013, U+2212) ani podwójnego
  ampersandu (sprawdzone w Pythonie).

## Zestawienie

| # | soczewka, waga | uwaga (skrót) | decyzja |
|---|---|---|---|
| 1 | fakty, ważny | karta tworzyw: „bryły z kieszeniami i gniazdami pod montaż” bez źródła firmowego | wprowadzona |
| 2 | fakty, drobny | M1 sugeruje, że metale są na 1011 tylko w kodzie | wprowadzona z korektą |
| 3 | fakty, drobny | „Cięcie i grawer” + „Liczba maszyn 5” zaniża park | wprowadzona |
| 4 | fakty, drobny | rok 2002 pod h2 o frezarce, brak pytania P16 | wprowadzona z korektą |
| 5 | wzorzec, drobny | godziny w K17 zmienione tylko na tej stronie | wprowadzona |
| 6 | wzorzec, drobny | `sklad-notatki.md` opisuje stan sprzed rundy 1 | odrzucona (plik poza zakresem), poprawki rozpisane niżej |
| 7 | język, ważny | tik „jeden” (11 form) | wprowadzona z korektą leadu |
| 8 | język, ważny | „pełny pion krawędzi”, „krawędź” i „daje” w sekcji materiałów | wprowadzona |
| 9 | język, drobny | karta 3: „czekać, aż uzbiera się seria”, czasy | wprowadzona |
| 10 | język, drobny | „od … po” jako ozdobnik (galeria, frezarka) | wprowadzona |
| 11 | język, drobny | definicja frezu powtarza h2 | wprowadzona z korektą |
| 12 | język, drobny | „zlecenie na frezarkę” | wprowadzona |
| 13 | język, drobny | krok 04: podwójne „je”, zmiana podmiotu | wprowadzona z korektą |
| 14 | język, drobny | „laserów” dwa razy w zdaniu pod parkiem | wprowadzona |
| 15 | język, drobny | FAQ 5: „dokładka” | wprowadzona |
| 16 | język, drobny | alt kafla 4: „frezowanie … na frezarce” | wprowadzona |
| 17 | język, drobny | M1 „zgodnym z tą stroną”, L2 jako pytanie alternatywne | wprowadzona (M1 razem z uwagą 2) |

## Uwagi

### 1. Karta tworzyw technicznych: wprowadzona
Sprawdzone: `posts-2078` („możliwość wykonywania faz, gniazd…”) opisuje metodę CNC przy akrylu, sklejce i MDF, a nie
tworzywa techniczne. `posts-2043` (gniazda na szminki) fakty.md F93 oznacza jako niepotwierdzoną pracę Padiru. `posts-2147`
to poradnik bez ani jednego „frezujemy”. Jedyne źródło firmowe to `pages-1397`: „napisy przestrzenne oraz detale frezujemy na
maszynach CNC w MDF, konglomeracie i tworzywach technicznych”. P28 nie trafiło wcześniej do żadnej ramki.
Zmiany:
- karta 3: „Frezujemy też detale z tworzyw technicznych.” zamiast „Z tworzyw technicznych frezujemy bryły z kieszeniami
  i gniazdami pod montaż.”;
- M2, po „…POM, PA6, PP?”: „Czy z tworzyw technicznych robicie też detale montażowe z kieszeniami, gniazdami, otworami
  i gwintami? Jeśli tak, dopiszemy to w karcie tworzyw.”;
- księga: wpisy 66-68 (2078, 2043, 2147) zastąpione jednym cytatem z `pages-1397`, dodany wpis M2 z P28;
- `tresc.md`: karta 3, M2, a w zestawieniu ramek przy M2 dopisane P28.

### 2. Ramka M1 a widoczna oferta metali na 1011: wprowadzona z korektą
Sprawdzone w `pages-1011-frezowanie-cnc.txt`: jest widoczna sekcja „Frezowanie w metalu” („motoryzacja, lotnictwo
i inżynieria”, „spełnia najbardziej rygorystyczne normy jakościowe”) i karta „Obróbka skrawaniem 3- i 5-osiowa detali
z aluminium, mosiądzu, miedzi i tworzyw konstrukcyjnych. Protokół pomiarowy do każdej partii.”. Uwaga ma rację.
Korekta propozycji: zdanie „w kodzie opis usługi dla Google z tymi samymi metalami” byłoby nieścisłe, bo `ld+json` na 1011
wymienia aluminium i mosiądz, ale nie miedź (sprawdzone w `pages-1011-frezowanie-cnc.raw.html`). Przy okazji trzeba było
też rozwiązać dwuznaczność z uwagi 17.
Nowy koniec M1: „Obecna strona o frezowaniu ma widoczną sekcję „Frezowanie w metalu” (motoryzacja, lotnictwo, „rygorystyczne
normy jakościowe”) i kartę z obróbką 3- i 5-osiową aluminium, mosiądzu i miedzi oraz protokołem pomiarowym. To samo, bez
miedzi, stoi w kodzie w opisie usługi dla Google. W szkicu, także w opisie dla Google, tych treści nie ma, a metale dopiszemy
po potwierdzeniu.”
Księga: trzy nowe wpisy z cytatami z `pages-1011-frezowanie-cnc.txt`, a wpis o `ld+json` doprecyzowany („bez miedzi”).

### 3. Liczba laserów: wprowadzona
Sprawdzone w `pages-1019-wycinanie-laserowe.txt`: „5 laserów do wycinania w jednej hali” i „To pięć laserów do wycinania
w jednej hali, a do grawerowania mamy jeszcze wiele innych maszyn.”, a `pages-2264`: „Pracujemy laserem włóknowym na metalach
i CO2 na tworzywach.”. Pod chipem „Cięcie i grawer” wiersz „Liczba maszyn 5” zaniżał więc park.
Zmiany: wiersz „Lasery do cięcia | 5”, podpis liczby „laserów Trotec do cięcia”. Akapit („Mamy też pięć laserów CO₂ Trotec”),
chip i h3 karty zostają bez zmian. W księdze wpis 124 ma teraz pełny cytat z „wiele innych maszyn”. W `tresc.md` zmienione
oba pola i uwaga pod sekcją 8.

### 4. Rok 2002 i pytanie P16: wprowadzona z korektą
Sprawdzone: P16 nie było w żadnej ramce. Źródła roku 2002: `pages-8` i `pages-2487` „od 2002 na rynku obróbki laserowej”,
`pages-2283` „od 2002 roku w branży” (grawer dla HoReCa), `pages-2264` „od 2002 na rynku precyzyjnej obróbki”.
Korekta propozycji: zdanie „Rok 2002 … pochodzi ze stron o obróbce laserowej” pomijałoby 2264, więc piszę „głównie”.
Dopisane na końcu T1: „Od którego roku frezujecie CNC? Rok 2002 z paska liczb serwis łączy głównie z obróbką laserową. Jeśli
frezarka doszła później, zaznaczymy to przy liczbie albo podamy rok, od którego frezujecie.”. Pasek liczb bez zmian. Księga:
wpis DO POTWIERDZENIA z P16 i cytat z `pages-8`. W `tresc.md` zmienione T1, zestawienie ramek i uwaga pod sekcją 8.

### 5. Godziny otwarcia: wprowadzona
Sprawdzone: `12-kontakt.html`, `wzorzec.md` (K17, w. 802), `pages-1019…raw.html`, `pages-20-kontakt.raw.html` i
`praca/grawerowanie/strona.html` mają „Poniedziałek - Piątek: 8:30 - 16:00”. Katalog wzorca (w. 809-810): „Dane firmy,
godziny, logo, karta formularza: bez zmian”. Spacjowany dywiz to wciąż dywiz, więc reguła 1 z BRIEF jest spełniona.
Ta uwaga wyklucza się z uwagą 23 z rundy 1. Wybrałem wersję lepiej popartą wzorcem i źródłem: zapis stały na wszystkich
stronach i w obu szkicach.
Zmiana: linia przywrócona bajt w bajt (porównanie powłoką: IDENTYCZNE). `tresc.md`: pole stałego tekstu i dopisek, że ewentualną
zmianę zapisu trzeba zrobić jedną decyzją na wszystkich stronach. Księga: wpis 177 opisany na nowo, a obok niego cytat
z `/kontakt/`.

### 6. Notatki ze składu: odrzucona (plik poza zakresem), poprawki rozpisane
Problem jest prawdziwy. Sprawdziłem `sklad-notatki.md`: wiersz 7 tabeli ma `0px 0px 78px` i h3 w pasie, „Kontrola” mówi
o końcu pliku bajt w bajt jak `98-koniec.html`, nie ma tam `object-position` ani `ld+json` w „Dla prowadzącego”,
a pkt 13 twierdzi, że godziny są bez zmian. Według BRIEF („Każdy agent pisze TYLKO do plików wskazanych w swoim zadaniu”)
mogę jednak pisać tylko do `strona.html`, `tresc.md`, `ksiega.json` i tego raportu. Dlatego:
- w `tresc.md` („Uwagi dla prowadzącego”) dopisałem, że `sklad-notatki.md` jest nieaktualny, i wymieniłem cztery aktualne
  odstępstwa. `tresc.md` ma je już w treści: sekcja 7 (h2 w pasie, `0px 0px 82px`), sekcja 12 i uwaga o usunięciu
  starego `ld+json`, mapa zdjęć (`object-position`), sekcja 11 (godziny);
- gotowe poprawki dla składacza:
  1. Wiersz 7 tabeli: `| 7 | laser-i-frez | #F5F5F5, 0px 0px 82px | K01 (L1), K12 ciemny pas CTA z własnym h2 (22 px, biały; sekcja bez nagłówka K05) i K03 A-ciemny, K01 (L2) w pasie | 07-realizacje.html (pas pod kartami) |`.
  2. „Kontrola”, po zdaniu o `98-koniec.html`: „Za `<!-- /wp:group -->` stoi osobny blok `wp:html` z `ld+json` Service,
     tak jak na 1011, 456 i 2264 (uwaga 5, runda 1).”
  3. „Odstępstwa”, nowy punkt: „Kadry: `object-position` 20% (Tea w hero), 0% (Team) i 25% (Duka) w galerii, żeby kafel
     nie ucinał liter (uwagi 26 i 27, runda 1).”
  4. „Dla prowadzącego”: „Przy przenoszeniu na 1011 usunąć stary blok `ld+json` Service (5 osi, aluminium, mosiądz).”
  5. Pkt 13 może zostać w obecnym brzmieniu („godziny … bez zmian”), bo po uwadze 5 znów jest prawdziwy.

### 7. Tik „jeden”: wprowadzona z korektą leadu
Sprawdzone: przed poprawką 11 form (licznik). „w jednym kawałku” stało 3 razy, a karta 2 miała zeugmat „oddajemy frez,
cięcie i grawer”.
Zmiany:
- lead: „…Wszystko to powstaje w naszej warszawskiej pracowni.” Propozycja „robimy u siebie” powtarzałaby „robimy u siebie”
  z akapitu parku maszynowego;
- karta 1: h3 „Pole robocze 2 × 3 m”, tekst „Duży napis albo nośnik ścianki zwykle frezujemy w całości. Większe elementy
  dzielimy na moduły i łączymy po obróbce.”;
- karta 2: „Frezowanie, cięcie i grawer wyceniamy razem, a gotowe części odbierasz naraz.” (h3 i reszta bez zmian);
- park, h2: „Frezarka CNC obok laserów Trotec”.
Księga: zaktualizowane opisy twierdzeń (lead, karta 1, karta 2, park) i nowy wpis „frezujemy w całości” z cytatem z 2078
(„Jak duże formaty w jednym kawałku? … CNC ok. 2000×3000 mm.”). Teraz zostaje 6 form, a „w jednym kawałku” stoi
w hero i w FAQ 1.

### 8. Sekcja materiałów: „pion”, „krawędź”, „daje”: wprowadzona
Sprawdzone: `posts-2078` „Akryl powyżej ~10 mm: CNC dla pełnego pionu i pasowania.” i „„błysk” kontra „pion””. Zwrot jest
przepisanym żargonem z wpisu. Pionową krawędź opisuje już K10 („Krawędź wychodzi pionowa, bez stożka”).
Zmiany: z leadu usunięte „Daje też pionową krawędź.”. Karta plexi: „Przy plexi grubszej niż około 10 mm frez prowadzi krawędź
równo w pionie, więc element dokładnie pasuje do nośnika. Brzeg wychodzi matowy.”. Karta 1 bez zmian. Księga: wpis o pionowej
krawędzi przeniesiony z leadu do karty 2, opisy wpisów 56, 58 i 59 dopasowane.

### 9. Karta 3 „Pojedyncze sztuki i prototypy”: wprowadzona
„Napis czy prototyp frezujemy bez minimum ilościowego, więc nie musisz zamawiać całej serii. Jeśli się pomylimy, poprawimy
element.” Źródła bez zmian: `pages-8` (minimum tylko przy szkle), 1660 (od 1 sztuki), 1019 i 1011 (poprawka przy pomyłce).
Zdanie nadal mówi tylko o naszej pomyłce (uwaga 15 z rundy 1).

### 10. „Od … po”: wprowadzona
Sprawdzone: kolejność kart w HTML to Duka, Team, litera, Ajala, medalion, Tea. Napisy to „Team”, „Ajala” i „Tea”.
Lead galerii: „Sześć realizacji z frezarki: trzy napisy, litera, relief i medalion. Kliknij zdjęcie, żeby zobaczyć je
w całości.”. Opis frezarki: „Na niej powstają napisy przestrzenne i nośniki pod fronty z lasera.” (napisy: `pages-1397`,
nośniki: 2078). h2 „Od frezu po grawer w jednym zleceniu” zostaje, tak jak proponuje uwaga.

### 11. Definicja frezu: wprowadzona z korektą
Propozycja „…zamocowane we wrzecionie maszyny.” stała tuż przed zdaniem „Maszyna sterowana numerycznie…”, więc
„maszyny. Maszyna” dałoby nowe powtórzenie. Wersja: „Frez to narzędzie skrawające zamocowane we wrzecionie.”. To wiedza
ogólna, widoczna też na zdjęciach 2317 i 2148. W księdze wpis z cytatem z 2078 („Osłona-szczotka wokół wrzeciona”).

### 12. „Zlecenie na frezarkę”: wprowadzona
„Tak wygląda droga zlecenia frezowania, od pierwszej wiadomości do odbioru.”

### 13. Krok 04: wprowadzona z korektą
Propozycja „Gotowe elementy odbierzesz…” stała tuż po „…uzupełniamy elementami z lasera.”. Wersja: „Gotowe zamówienie
odbierzesz przy Matuszewskiej 14 albo wyślemy je kurierem.”. Jeden podmiot na zdanie, czas przyszły jak w krokach 01 i 03,
a „je” odnosi się do „zamówienia” także wtedy, gdy graweru nie ma. Źródło `pages-8` bez zmian.

### 14. „Laserów” dwa razy w zdaniu: wprowadzona
„Moc i pole robocze każdej z pięciu maszyn znajdziesz w opisie parku laserów Trotec na stronie o wycinaniu.” Anchor i link
`/wycinanie-laserowe/#technologia` bez zmian.

### 15. FAQ 5, „dokładka”: wprowadzona
„Tak. Plik i ustawienia maszyny z pierwszego zlecenia zachowujemy, więc kolejna partia wychodzi taka sama jak pierwsza.”
Sedno odpowiedzi (powtórka jest taka sama) zostaje. Ze zdaniem z `pages-8` („…więc dozamówienie po roku wygląda
identycznie jak pierwsza partia.”) nowe zdanie dzieli już tylko „jak pierwsza”, a NG=5 nie znajduje wspólnego ciągu.

### 16. Alt kafla 4 w hero: wprowadzona
Obejrzane: kontaktówka `red-r2/frez/kont-2317.png` (media 2317, `padir-realizacja-frezowana-litera-przestrzenna.jpg`)
i `wer-fakty-2317.jpg`. Na zdjęciu wrzeciono z frezem wycina kontur litery „A” w drewnianym klocku na stole maszyny.
Nowy alt: „Frez CNC wycina literę przestrzenną z bukowego klocka”. Materiał „Buk” pochodzi z `realizacje-karty.json`.
Alt w galerii („Frezowana litera przestrzenna - Buk”) bez zmian. W `tresc.md` zmieniony alt w hero i w mapie zdjęć.

### 17. Dwuznaczne ramki M1 i L2: wprowadzona
M1: dwuznaczne „zgodnym z tą stroną” zniknęło, nowe brzmienie jest przy uwadze 2.
L2: „Do potwierdzenia z klientem: czy nośnik ścianki na barce frezowaliście u siebie? Czy to ten sam projekt co ścianka Bondi
Sands ze strony o wycinaniu? Czy możemy pokazać zdjęcie tego nośnika?”. Zamiast proponowanego „jego zdjęcie” piszę
„zdjęcie tego nośnika”, bo po rozbiciu na osobne pytania „jego” odnosiłoby się do „projektu”.

## Pliki

- `praca/frezowanie/strona.html`: wszystkie zmiany opisane wyżej.
- `praca/frezowanie/tresc.md`: treść 1:1 ze stroną, mapa zdjęć (alt 2317), uwagi pod sekcją 8, zestawienie ramek (P28 przy M2,
  P16 przy T1), godziny w sekcji 11, długość, odsyłacz o `sklad-notatki.md` w „Uwagach dla prowadzącego”.
- `praca/frezowanie/ksiega.json`: 199 wpisów (było 192). Usunięte wpisy 2078, 2043 i 2147 o „bryłach i gniazdach”,
  dodane: 1397 (detale z tworzyw), P28, P16 z cytatem z `pages-8`, trzy cytaty z widocznej oferty metali na 1011,
  „frezujemy w całości” (2078), „wrzeciono” (2078) i godziny na `/kontakt/`. Opisy pozostałych zmienionych twierdzeń
  zaktualizowane. Stan przed rundą 2: `red-r2/frez/ksiega-przed-r2.json`.
- Nie ruszałem: `sklad-notatki.md` (uwaga 6), `zdjecia.json`, `fakty.md`.
