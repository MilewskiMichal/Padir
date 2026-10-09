# Arkusz zweryfikowanych faktów: Frezowanie CNC

Strona docelowa: szkic „Frezowanie CNC”, który zastąpi stronę 1011 `/frezowanie-cnc/`.
Stan źródeł: katalog `zrodla/` (strony i wpisy w `.txt` i `.raw.html`, szablon `szablon-frezowanie-cnc`, `realizacje-karty.json`, `media.json`, `SPIS.json`).
To jedyne źródło liczb i twierdzeń dla autora tekstu. Czego tu nie ma, tego nie piszemy albo stawiamy żółtą ramkę „Do potwierdzenia z klientem”.

## Jak czytać arkusz

- Każdy fakt ma plik źródłowy i dosłowny cytat w znakach « ». Cytaty są przepisane 1:1, razem z błędami, spacjami przed kropką i półpauzami ze źródła. W tekście strony półpauzy i pauzy zamieniamy na dywiz (`2-4 dni`), a zdania przebudowujemy.
- Pewność:
  - **[A]** potwierdzone w co najmniej dwóch niezależnych miejscach serwisu albo dane z zatwierdzonego wzorca 1019; można używać,
  - **[B]** jedno źródło, konkretne i wiarygodne; można używać, najlepiej w tym samym kontekście co w źródle,
  - **[C]** jedno źródło albo źródła sprzeczne, twierdzenie ryzykowne (maszyny, osie, metale, normy, liczby marketingowe); używać tylko w żółtej ramce „Do potwierdzenia z klientem”.
- Skróty plików: `1011` = `pages-1011-frezowanie-cnc.txt`, `szablon` = `szablon-frezowanie-cnc.txt`, `8` = `pages-8-produkty.txt`, `2264` = `pages-2264-uslugi-dla-przemyslu.txt`, `2283` = `pages-2283-uslugi-dla-horeca.txt`, `1019` = `pages-1019-wycinanie-laserowe.txt`, `1397` = `pages-1397-przykladkowe-realizacje.txt`, `1660` = wpis FAQ, `2078` = wpis „Cięcie przemysłowe: CNC vs laser”. Pełne nazwy plików są w każdej linii źródła.
- Status wpisów (z `SPIS.json`): opublikowane są m.in. 1578, 1660, 1873, 2043, 2078, 2147, 2208, 2293, 967. **Szkice (nieopublikowane)**: 1797 (frezowanie aluminium), 1823 (frezowanie sklejki), 1829 (czym jest frezowanie), 1845 (frezowanie tworzyw). Szkice nie są źródłem faktów o firmie, najwyżej wiedzy ogólnej.
- Najważniejsze ostrzeżenie: serwis opisuje frezowanie na dwa sposoby. Strona przemysłowa (2264) mówi o obróbce 3- i 5-osiowej metali z protokołem pomiarowym. Wpis 2078 i galeria realizacji (1397) pokazują frezowanie płyt i tworzyw („soft-materiały”): napisy przestrzenne, litery, reliefy, nośniki ekspozycji. Szczegóły w rozdziale „Sprzeczności”, S1 i S2.

---

## 1. Usługa i zakres

**F01 [A]** Padir frezuje CNC w tej samej pracowni w Warszawie, w której graweruje i wycina laserowo.
- `zrodla/pages-8-produkty.txt` «Grawerowanie laserowe, wycinanie laserowe i frezowanie CNC pod jednym dachem w Warszawie.»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Grawerowanie, wycinanie laserowe i frezowanie CNC w jednym miejscu.»
- `zrodla/posts-2208-jak-dziala-grawerowanie-laserowe.txt` «Pracujemy na laserach CO₂ i fiber, jak i również frezujemy CNC, więc dobieramy technologię do materiału i celu»

**F02 [A]** Rola frezowania wobec lasera: grubsze materiały, kształty przestrzenne, reliefy i litery 3D, obróbka na głębokość zamiast cięcia na wylot.
- `zrodla/pages-8-produkty.txt` «Obróbka skrawaniem tam, gdzie laser nie sięga: grubsze materiały, przestrzenne kształty, reliefy i litery 3D.»
- `zrodla/posts-2293-wycinanie-laserowe-precyzyjne-ciecie-plexi-sklejki-i-laminatu-na-zamowienie.txt` «Frezowanie CNC ma sens przy grubszych materiałach, obróbce przestrzennej i tam, gdzie potrzebna jest głębokość, a nie samo cięcie na wylot.»
- `zrodla/posts-2208-jak-dziala-grawerowanie-laserowe.txt` «CNC potrafi wejść znacznie głębiej niż standardowy grawer laserowy np. niektóre tabliczki z mosiądzu, głębokie żłobienia, obróbka bardziej „rzeźbiarska”.»

**F03 [A]** Wycięcie, frezowanie i grawer można zamówić w jednym zleceniu: jedna oferta, jeden termin, jedna faktura, bez wożenia detalu między zakładami.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Wycinamy detal, frezujemy, a na końcu grawerujemy oznaczenia. Jedna oferta, jeden termin, jedna faktura.»
- `zrodla/pages-8-produkty.txt` «Detal jest wycinany, frezowany i znakowany w jednej pracowni, więc nie krąży między zakładami.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Klienci unikają w ten sposób kosztów logistyki między zakładami.»

**F04 [B]** Łączenie technologii w jednym projekcie: front tnie laser, nośnik frezuje CNC. Serwis podaje to jako własny przykład (ścianka foto na barce na Wiśle).
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Nośnik + front — CNC na nośnik, laser na front.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Fronty z lustrzanego PMMA wycięliśmy laserem (krawędź „poler”), a nośnik z MDF — na CNC (pion, gwinty).»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «To także metoda pierwszego wyboru dla nośników pod fronty laserowe»

**F05 [B]** Co daje frezowanie (wg serwisu): pionowa krawędź bez stożka, fazy, gniazda, frezy dekoracyjne, otwory pod łączniki, wiercenie i gwintowanie.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «CNC frezuje materiał narzędziem o określonej średnicy. Dostajesz krawędź pionową (bez stożka), możliwość wykonywania faz, gniazd, frezów dekoracyjnych i otworów pod łączniki.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «a przy tym pozwala wiercić, gwintować, fazować.»
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «CNC tnie grube i trudniejsze materiały, wycina też otwory pod produkty (np. okrągłe gniazda na szminki).»

**F06 [A]** Ograniczenie frezowania: średnica frezu. Minimalny promień wewnętrzny równa się promieniowi narzędzia, więc mikrodetal i drobne ażury lepiej wychodzą laserem.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Minimalne promienie wewnętrzne = promień narzędzia. Do mikro-detalu i puzzli lepszy będzie laser.»
- `zrodla/posts-2208-jak-dziala-grawerowanie-laserowe.txt` «mniejsze detale bywają trudniejsze (bo ogranicza Cię średnica frezu)»
- Wartości liczbowej (najmniejszy frez, najmniejszy promień) serwis nie podaje: pytanie P09.

**F07 [A]** Krawędź po frezowaniu jest matowa. Serwis mówi, że można ją wypolerować (mechanicznie lub płomieniowo), ale nie mówi wprost, że Padir robi to jako usługę.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «„Z pudełka” krawędź jest matowa , ale w razie potrzeby możesz ją wypolerować mechanicznie lub płomieniowo»
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «Krawędzie po frezie są matowe, czasem wymagają wygładzenia»
- Polerowanie jako usługa: pytanie P11.

**F08 [B]** Sklejka i MDF po CNC mają neutralną krawędź (bez przyciemnienia, jakie daje laser), gotową do oleju lub okleiny. Kto chce „surowej” krawędzi, dostaje frezowanie.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Sklejka/MDF: obie metody działają — laser zostawia ciepłą, przyciemnioną krawędź (charakter), CNC — neutralną, gotową do oleju/okleiny.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Jeśli chcesz „surowo” — tniemy CNC.»

**F09 [A]** Pojedyncze sztuki, prototypy i serie. Zamówienia od 1 sztuki.
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Zamówienia przyjmujemy już od 1 sztuki .»
- `zrodla/pages-1011-frezowanie-cnc.txt` «Czy mogę zamówić frezowanie prototypu? Tak, frezowanie CNC jest idealne do tworzenia prototypów»
- `zrodla/pages-8-produkty.txt` «Ta sama droga niezależnie od tego, czy zamawiasz jedną sztukę, czy serię na pięć tysięcy.»

**F10 [A]** Doradztwo: Padir dobiera metodę (laser czy frezarka) i materiał, pomaga dostosować projekt pod frezowanie, odtwarza plik ze zdjęcia lub rysunku.
- `zrodla/pages-8-produkty.txt` «Mówimy, czy to zadanie dla lasera, czy dla frezarki, w jakim materiale wyjdzie najlepiej i ile to kosztuje.»
- `zrodla/pages-1011-frezowanie-cnc.txt` «Tak, oferujemy wsparcie w zakresie optymalizacji projektu pod kątem frezowania CNC, aby zapewnić najlepsze rezultaty.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Jeśli masz tylko rysunek odręczny lub fotografię, też damy radę, odtworzymy plik u siebie.»

**F11 [A]** Elementy większe niż pole robocze dzielone są na moduły (wpis 2078 mówi wprost o modułach z zamkami przy CNC i laserze).
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Większe elementy dzielimy na moduły z zamkami.»
- `zrodla/pages-8-produkty.txt` «Większe realizacje rozkładamy na moduły i łączymy je już po obróbce»

**F12 [B]** Wyrób własny z udziałem frezowania: torebki Padir ze sklejki, cięte laserowo i frezowane CNC, malowane ręcznie w pracowni na Targówku, sprzedawane w osobnym sklepie Padir Store.
- `zrodla/pages-8-produkty.txt` «Torebki ze sklejki, cięte laserowo i frezowane CNC, malowane ręcznie w pracowni na Targówku.»
- `zrodla/pages-8-produkty.txt` «Osobny sklep Padir Store»
- Uwaga: link `/torebki/` z produktów NIE występuje w `SPIS.json`, więc nie linkujemy.

**F13 [B]** HoReCa: drewniane karty menu, oznaczenia stolików, deski do serwisu. Strona HoReCa pisze o frezowaniu konturu i grawerze w jednej operacji (ale w tym samym bloku pisze też o wycinaniu konturu, patrz S8).
- `zrodla/pages-2283-uslugi-dla-horeca.txt` «Frezujemy kontur i grawerujemy treść w jednej operacji.»
- `zrodla/pages-2283-uslugi-dla-horeca.txt` «Drewniane karty menu, oznaczenia stolików, tabliczki rezerwacyjne, deski do serwisu i etui na rachunek.»

---

## 2. Technologia i maszyny

**F20 [A]** Pole robocze frezowania: 2000 × 3000 mm. Jedyny parametr maszyny CNC potwierdzony w kilku miejscach.
- `zrodla/pages-1011-frezowanie-cnc.txt` «Wielkość pola roboczego frezarek, na których pracujemy to: 2000mm x 3000mm»
- `zrodla/pages-1011-frezowanie-cnc.txt` «Maksymalny obszar roboczy to 2000 na 3000mm»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Nasza frezarka oferuje maksymalne pole pracy wielkości 2000 × 3000 mm .»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «W typowych usługach: laser ok. 2510×1680 mm, CNC ok. 2000×3000 mm.»
- Nie wiadomo, czy to jedna maszyna, czy kilka (S4, pytanie P01). Wysokości osi Z i grubości materiału serwis nie podaje (P02).

**F21 [C]** Ploter CNC marki Kimla: jedyna nazwa producenta frezarki w całym serwisie, tylko we wpisie 2078. Wpis nie mówi wprost „nasza maszyna”, opisuje cechy konstrukcji, a duże pola robocze przypisuje katalogowi producenta.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «W plotera CNC Kimla kluczem jest stół próżniowy (także w wersji hybrydowej: próżnia + T-rowki).»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Producent wymienia typowe pola robocze (długości do 7 m, szerokości do 2,6 m, Z nawet do ~700 mm), ale w praktyce w usługach najczęściej spotykasz około 2,0×3,0 m»
- Nie wolno pisać „do 7 m” ani „Z do 700 mm” jako parametrów Padiru: to dane katalogowe producenta. Model i wyposażenie: pytanie P01.

**F22 [C]** Wyposażenie opisane we wpisie 2078 (bez potwierdzenia, że to stan maszyny Padiru): stół próżniowy, wrzeciono do 24 000 obr./min, automatyczna korekcja długości narzędzia, serwonapędy AC, magazyn narzędzi ATC, szczotka i odciąg wiórów; jako opcje: nóż oscylacyjny, bigownik, nóż do folii, pisak, dozownik, sondy, oś obrotowa.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Wrzeciono: do 24 000 obr./min, zapas mocy (klasa przemysłowa); automatyczna korekcja długości.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Napędy i ATC: serwa AC high-speed, magazyn narzędzi (ATC) — szybkie zmiany frezów, powtarzalność.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Opcje: nóż oscylacyjny, bigownik, nóż do folii, pisak, dozownik, sondy (dotyk/laser), oś obrotowa.»
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «Frezowanie CNC: Obracający się frez oraz nóż oscylacyjny wycina kształty w prawie każdym materiale – od plexi, przez piankę PVC i HIPS, po dibond czy aluminium.»
- Pytania P01 i P19.

**F23 [C]** Obróbka skrawaniem 3- i 5-osiowa. Źródło jest jedno (strona przemysłowa), a karta na obecnej stronie 1011 to kopia tego zdania. Brak nazwy maszyny 5-osiowej; wpis 2078 wymienia oś obrotową tylko jako opcję.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Frezowanie CNC Obróbka skrawaniem 3- i 5-osiowa detali z aluminium, mosiądzu, miedzi, tworzyw konstrukcyjnych i drewna.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Obróbka skrawaniem 3- i 5-osiowa. Detale z aluminium, mosiądzu, miedzi, tworzyw konstrukcyjnych i drewna.»
- `zrodla/pages-1011-frezowanie-cnc.txt` «Obróbka skrawaniem 3- i 5-osiowa detali z aluminium, mosiądzu, miedzi i tworzyw konstrukcyjnych.»
- Patrz S2, pytanie P03.

**F24 [A]** Lasery w tej samej pracowni (kontekst „trzy technologie w jednej pracowni”): pięć laserów CO2 Trotec w jednej hali, od formatu A4 po arkusze ponad 2,5 m, moc do 500 W. Do tego laser włóknowy (fiber) do metali.
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Pięć maszyn CO₂ marki Trotec, od formatu A4 po arkusze ponad 2,5 metra i moc do 500 W.»
- `zrodla/pages-1019-wycinanie-laserowe.txt` «To pięć laserów do wycinania w jednej hali, a do grawerowania mamy jeszcze wiele innych maszyn.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Pracujemy laserem włóknowym na metalach i CO2 na tworzywach.»

**F25 [A]** Park laserów Trotec (wzorzec 1019; na stronie zamienić półpauzy na dywiz, „60-200 W”):
- Trotec SP2000: pole 2510 × 1680 mm, CO2 180-500 W, dostęp z 4 stron. `zrodla/pages-1019-wycinanie-laserowe.txt` «Trotec SP2000 Nasz największy laser do wielkoformatowych nakładów. Pole robocze 2510 × 1680 mm Moc CO₂ 180-500 W Dostęp z 4 stron»; potwierdza `zrodla/pages-8-produkty.txt` «Największy laser, na którym pracujemy, to Trotec SP 2000 z polem roboczym 2510 na 1680 mm i mocą regulowaną od 180 do 500 W.»
- Trotec SP500: pole 1245 × 710 mm, CO2 60-200 W, materiał do 112 mm, pass-through. `zrodla/pages-1019-wycinanie-laserowe.txt` «Trotec SP500 Duże arkusze, wysokie materiały i tryb pass-through. Pole robocze 1245 × 710 mm Moc CO₂ 60–200 W Wys. materiału do 112 mm»
- Trotec Q500: pole 1300 × 900 mm, CO2 60-120 W, grawer od 4 pt. `zrodla/pages-1019-wycinanie-laserowe.txt` «Trotec Q500 Szybkie cięcie i precyzyjny grawer w jednej maszynie. Pole robocze 1300 × 900 mm Moc CO₂ 60–120 W Grawer od 4 pt»
- Trotec Speedy 360: pole 813 × 508 mm, CO2 60-120 W, grawer do 3,55 m/s. `zrodla/pages-1019-wycinanie-laserowe.txt` «Trotec Speedy 360 Szybki grawer średniego formatu z opcją flexx. Pole robocze 813 × 508 mm Moc CO₂ 60–120 W Prędkość graweru do 3,55 m/s»
- Trotec Speedy 300: pole 726 × 432 mm, CO2 25-120 W, materiał do 200 mm. `zrodla/pages-1019-wycinanie-laserowe.txt` «Trotec Speedy 300 Precyzyjny grawer do drobnych detali i personalizacji. Pole robocze 726 × 432 mm Moc CO₂ 25–120 W Wys. materiału do 200 mm»
- Na stronie o frezowaniu wystarczy jedno zdanie o laserach z odesłaniem do `/wycinanie-laserowe/`. NIE powtarzać „400 W maks. moc cięcia” ani „1650 × 2510” (S5, S6).

**F26 [B]** W parku maszynowym jest też zgrzewarka ultradźwiękowa (kontekst: ekspozytory).
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «Posiadamy też w swoim parku maszynowym zgrzewarkę ultradźwiękową»

---

## 3. Parametry i dokładność

**F30 [A]** Wymiar detali: od kilkumilimetrowych po wielkoformatowe (do pola 2000 × 3000 mm, F20).
- `zrodla/pages-8-produkty.txt` «Od detali kilkumilimetrowych po elementy wielkoformatowe.»
- `zrodla/pages-8-produkty.txt` «Frezowanie od detali kilkumilimetrowych po elementy wielkoformatowe»
- Stare zdanie z 1011 „do kilkudziesięciu centymetrów” jest sprzeczne z polem 2000 × 3000 mm (S3), nie przenosić.

**F31 [B]** Grubość akrylu a wybór metody: do ok. 10 mm laser, powyżej ok. 10 mm CNC (pion krawędzi, pasowanie); duże litery 3D z akrylu 15-20 mm: CNC.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Akryl powyżej ~10 mm: CNC dla pełnego pionu i pasowania.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Jeżeli stawiasz duże litery 3D z akrylu 15–20 mm i zależy Ci na perfekcyjnym spasowaniu z nośnikiem — bierz CNC .»
- Maksymalna grubość materiału przy frezowaniu: brak (P02, P10).

**F32 [B]** Tolerancje jako wskazówka projektowa (nie obietnica): dekor i signage ±0,3-0,5 mm, elementy pasowane ±0,1-0,2 mm z uwzględnieniem promienia frezu.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Tolerancje: dekor i signage „wybaczą” ±0,3–0,5 mm; elementy pasowane — celuj w ±0,1–0,2 mm i uwzględnij kerf (laser) lub promień frezu (CNC).»
- Używać tylko jako rady „jak projektować”, nie jako „gwarantujemy”. Deklarowana tolerancja frezowania: P05.

**F33 [C]** „±0,01 mm dokładność pozycjonowania”: statystyka w nagłówku strony przemysłowej, bez wskazania, której maszyny (lasera czy frezarki) dotyczy.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «od 2002 na rynku precyzyjnej obróbki ±0,01 mm dokładność pozycjonowania 24-72 h typowa seria»
- Nie mylić z „±0,05 mm” (dotyczy ponownego znakowania laserem: `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «z precyzją ±0,05 mm») ani z „0,1 mm” (tolerancja cięcia laserem). Pytanie P05.

**F34 [C]** „Wysoka gładkość powierzchni, bez śladów mocowania”: jedno źródło, twierdzenie jakościowe.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Wysoka gładkość powierzchni, bez śladów mocowania»

**F35 [B]** Frezowanie ma limit wysokości obrabianego przedmiotu; serwis każe to sprawdzić przed zleceniem (bez liczby).
- `zrodla/posts-1578-wycinanie-laserowe-vs-frezowanie-cnc.txt` «Frezowanie ma również swoje limity wysokości, dlatego przed przygotowaniem zlecenia, skontaktuj się ze specjalistą»
- Liczba (oś Z, maks. wysokość): P02.

---

## 4. Materiały

**F40 [A]** Drewno, sklejka, MDF. Realizacje: litera przestrzenna z buku, medalion z MDF.
- `zrodla/pages-8-produkty.txt` «Drewno i sklejka Grawer, cięcie i frezowanie. Meble, prototypy, dekoracje, opakowania.»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «napisy przestrzenne oraz detale frezujemy na maszynach CNC w MDF, konglomeracie i tworzywach technicznych»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowanie Frezowana litera przestrzenna Buk»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowanie Medalion „Republika Portionii” MDF»

**F41 [A]** Plexi (PMMA), także lustrzana, szczególnie grube przekroje. Realizacje: napisy przestrzenne „Tea” i „Team” z plexi lustrzanej.
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowanie Napis przestrzenny „Tea” Plexi lustrzana»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowanie Napis przestrzenny „Team” Plexi lustrzana»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «CNC ogarnia: PMMA (zwłaszcza grube przekroje wymagające pionu), sklejkę (także WBP), MDF, dibond/ACP, PC i inne tworzywa „no-laser”»

**F42 [A]** Tworzywa techniczne. Strona przemysłowa wymienia POM, PA6, PP, PMMA; realizacja: relief „Duka” z tworzywa.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Tworzywa techniczne POM, PA6, PP, PMMA. Cięcie laserowe, grawerowanie i frezowanie jako alternatywa dla nadruku i tłoczenia.»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowanie Frezowany relief „Duka” Tworzywo»

**F43 [A]** Konglomerat kwarcowy. Realizacja: frezowany napis „Ajala”.
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Frezowanie Frezowany napis „Ajala” Konglomerat kwarcowy»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «w MDF, konglomeracie i tworzywach technicznych»

**F44 [B]** Materiały, których laser nie lubi albo nie tnie, idą na CNC: sklejka wodoodporna WBP, poliwęglan (PC), dibond/ACP, PVC.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Dibond/PC: praktycznie zawsze CNC.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Grube PMMA, pasowania, kompozyty (dibond/PC), WBP, gniazda i fazki — CNC.»
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «nie wszystko da się ciąć laserem (np. zwykłe PVC wydziela toksyczne opary), więc czasem do akcji wkracza frezarka.»
- Uwaga na sprzeczność z produktami, gdzie PVC jest na liście cięcia laserem (S9).

**F45 [B]** Pianka PVC (np. Komatex) i HIPS: łatwo się frezują, typowe na ekspozytory.
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «Pianka PVC: Lekka i tania płyta z PCV spienionego (np. Komatex). Łatwo poddaje się frezowaniu CNC»

**F46 [A]** Kompozyty (w tym dibond) jako materiał frezowany.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Materiały: tworzywa, kompozyty, dibond, MDF/sklejka, drewno i pochodne»
- `zrodla/pages-1011-frezowanie-cnc.txt` «takich jak metal, drewno, tworzywa sztuczne, czy kompozyty»

**F47 [C]** Metale: aluminium, mosiądz, miedź (strona przemysłowa, karta na 1011, stary tekst 1011 „Frezowanie w metalu”). Sprzeczne z wpisem 2078 i z galerią, w której nie ma żadnej frezowanej realizacji z metalu (S1).
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Aluminium i stopy Al Anodowane, surowe, lotnicze. Grawer, cięcie laserowe i frezowanie, czyli pełna obróbka aluminium w jednej pracowni.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Mosiądz i miedź Elementy armatury, złącza, złączki elektryczne, tabliczki ozdobne. Grawer kontrastowy, frezowanie precyzyjne, polerowanie końcowe.»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Drewna (sklejki, deski itp.). Aluminium i mosiądzu . Laminatów, plexi i innych tworzyw sztucznych.» (lista materiałów, które Padir może zamówić; nie mówi o frezowaniu)
- Stali nikt w serwisie nie wiąże z frezowaniem: `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Stal niskowęglowa i nierdzewna w umiarkowanych grubościach, głównie cięcie blach i znakowanie.» Nie pisać o frezowaniu stali. Pytanie P04.

**F48 [A]** Materiał może dostarczyć klient (osobiście albo kurierem) albo Padir go zamówi. FAQ wymienia wprost frezowanie.
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Gdzie przysłać lub przywieźć materiał do grawerowania, cięcia lub frezowania? Czekamy na Ciebie pod adresem: ul. Matuszewska 14, 03-876 Warszawa Możesz tu dostarczyć swój materiał osobiście lub przesłać go kurierem.»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «W większości przypadków możemy samodzielnie zamówić potrzebny materiał, abyś nie musiał się tym zajmować.»

**F49 [A]** Przy nietypowym materiale albo wątpliwej grubości najpierw próba lub próbka.
- `zrodla/pages-8-produkty.txt` «przy nietypowym surowcu robimy próbę przed produkcją»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Jeśli masz wątpliwość co do grubości czy materiału — daj znać, przygotujemy próbkę.»

---

## 5. Zastosowania i branże

**F50 [A]** Napisy i litery przestrzenne, litery 3D, reliefy, medaliony: to pokazuje galeria CNC.
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «napisy przestrzenne oraz detale frezujemy na maszynach CNC»
- `zrodla/pages-8-produkty.txt` «grubsze materiały, przestrzenne kształty, reliefy i litery 3D.»

**F51 [B]** Ekspozycja, POS, eventy, scenografia: nośniki pod fronty laserowe, gniazda pod produkty, otwory, gwinty.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «W większości zleceń w retailu, eventach i małej produkcji nie ścigamy się ze stalą. Liczy się PMMA (akryl), sklejka, MDF i kompozyty.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «To także metoda pierwszego wyboru dla nośników pod fronty laserowe»

**F52 [B]** Grupy klientów pracowni (wszystkie usługi, nie tylko CNC): marki i agencje, hotele i restauracje, producenci, koła łowieckie, klienci indywidualni.
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Pracujemy dla marek i agencji, hoteli i restauracji , producentów , kół łowieckich oraz klientów indywidualnych.»
- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Robimy statuetki i nagrody, ekspozytory POS, litery i logotypy reklamowe, personalizowane upominki, oznakowanie wnętrz i prototypy.»

**F53 [B]** Przemysł: producenci maszyn, OEM, zakłady przemysłowe (strona przemysłowa, wszystkie usługi). Obecna strona 1011 ma sekcję „Dla kogo pracujemy” z odesłaniem do `/uslugi-dla-przemyslu/` i `/uslugi-dla-horeca/` (oba adresy opublikowane).
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Pracujemy z producentami maszyn, firmami OEM i zakładami przemysłowymi.»
- `zrodla/pages-1011-frezowanie-cnc.txt` «Dla kogo pracujemy Frezujemy dla przemysłu i dla gastronomii.»
- Konkretne branże przemysłowe (automotive, lotnictwo, medycyna) i normy z 2264 dotyczą głównie znakowania; z frezowaniem wiąże je tylko jedno zdanie («frezowane korpusy» w „Lotnictwo i kolej”). Na stronie CNC ich nie używać bez potwierdzenia (P22).

**F54 [C]** Meble, fronty, panele 3D i panele akustyczne jako zastosowanie frezowania: tylko ogólne zdania (stary tekst 1011, wpis 967), bez realizacji Padiru.
- `zrodla/pages-1011-frezowanie-cnc.txt` «Często frezowanymi elementami są również panele akustyczne»
- `zrodla/pages-8-produkty.txt` «Meble, prototypy, dekoracje, opakowania.» (dotyczy drewna i sklejki we wszystkich trzech technologiach)

---

## 6. Terminy, nakłady, minimum zamówienia, wycena

**F60 [A]** Minimum ilościowe: od 1 sztuki (F09). Jedyne minimum ilościowe w serwisie dotyczy szkła (12 sztuk), czyli nie frezowania.
- `zrodla/pages-8-produkty.txt` «Minimum zamówienia pojawia się tylko przy szkle, które grawerujemy od 12 sztuk»

**F61 [C]** Minimalny koszt usługi 100 zł: jedno źródło (FAQ ze stycznia 2025), nie wiadomo, czy aktualne i czy dotyczy frezowania.
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Minimalny koszt usługi wynosi 100 zł .»
- Pytanie P08.

**F62 [A]** Na cenę wpływa m.in. rodzaj usługi (w tym frezowanie), liczba sztuk, wielkość, przygotowanie pliku, materiał, stopień skomplikowania i termin; ekspres może kosztować więcej.
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Rodzaj usługi (grawerowanie, cięcie, frezowanie).»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Termin realizacji – jeśli zależy Ci na ekspresowym wykonaniu, cena może być wyższa.»

**F63 [A]** Termin podawany jest w wycenie. Terminów specyficznych dla frezowania serwis nie podaje; liczby z innych stron dotyczą znakowania, gastronomii albo usług ogólnie (S7).
- `zrodla/pages-8-produkty.txt` «Konkretny termin podajemy w wycenie.»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «W przypadku większych i bardziej złożonych projektów termin realizacji ustalamy indywidualnie.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Przy sensownym briefie: od następnego dnia do ok. 3 dni roboczych — zależnie od kolejki, nakładu i obróbki po cięciu.» (wpis o CNC i laserze łącznie: [B], najbliższe źródło dla frezowania)
- Pytanie P07.

**F64 [A]** Pliki: DXF, DWG, STEP, IGES, STL, PDF z wymiarowaniem; do frezowania preferowany STEP. Do grawerowania wektory AI, EPS, SVG; pracownia działa głównie w CorelDRAW.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «DXF, DWG, STEP, IGES, PDF z wymiarowaniem oraz pliki STL. Dla frezowania preferujemy STEP, dla cięcia DXF.»
- `zrodla/pages-8-produkty.txt` «Do frezowania wolimy STEP, do cięcia DXF.»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «W naszej firmie pracujemy głównie w CorelDRAW, jednak radzimy sobie również z innymi formatami (np. .ai, .pdf, .eps).»

**F65 [A]** Co napisać w zapytaniu: liczba sztuk, materiał (własny czy do zamówienia), wymiary i grubość, termin, opis; przy frezowaniu także podział na moduły, mocowania (otwory, gwinty), tolerancje (dekor czy pasowanie), sposób odbioru.
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Ilość sztuk. Rodzaj materiału (czy dostarczasz własny, czy mamy go zamówić?). Wymiary (jeśli są określone). Oczekiwany termin realizacji.»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «wektora (SVG/ PDF /AI/EPS) lub zgody na przerysowanie, wymiarów końcowych i grubości, informacji o materiale i wykończeniu, podziale na moduły, opisanych mocowaniach»

**F66 [A]** Przy seriach i nowych materiałach najpierw wzorzec do akceptacji; produkcja rusza po akceptacji klienta.
- `zrodla/pages-8-produkty.txt` «Przy seriach i przy nowych materiałach najpierw powstaje wzorzec do akceptacji. Produkcja rusza dopiero po Twoim „tak”.»
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «W przypadku zleceń hurtowych lub nietypowych projektów często proponujemy wykonanie próbnego graweru/cięcia na małym fragmencie materiału.»

**F67 [B]** Próbka kontrolna gratis dla nowych klientów (strona przemysłowa, w sekcji materiałów wszystkich usług).
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Próbka kontrolna gratis dla nowych klientów.»
- Czy obejmuje frezowanie: dopisane do P08.

**F68 [A]** Parametry procesu i plik wzorcowy idą do archiwum, więc dozamówienie wychodzi identycznie.
- `zrodla/pages-8-produkty.txt` «Parametry procesu i plik wzorcowy trafiają do archiwum, więc dozamówienie po roku wygląda identycznie jak pierwsza partia.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Archiwizujemy pliki wzorcowe i parametry procesu, co gwarantuje identyczność oznaczeń między partiami.»

**F69 [B]** Kontakt techniczny: technolog odpowiada tego samego dnia, dobiera metodę, potwierdza tolerancje i podaje termin (strona przemysłowa).
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Nie znalazłeś swojej? Napisz do nas, technolog odpowie tego samego dnia.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Prześlij plik DXF, STEP lub zwykłe zdjęcie detalu. Technolog dobierze metodę, potwierdzi tolerancje i poda termin.»

---

## 7. Kontrola jakości, dokumentacja, normy

**F70 [B]** Protokół pomiarowy do każdej partii frezowanej. Źródło jedno (2264, powtórzone trzy razy; karta 1011 to kopia). Pasuje do ogólnej praktyki protokołów na stronie przemysłowej. Używać w kontekście zleceń seryjnych/przemysłowych; zakres pomiaru do potwierdzenia.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Dokładność wymiarowa potwierdzona protokołem pomiarowym dla każdej partii.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Protokół pomiarowy do każdej partii produkcyjnej»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Do każdej serii dołączamy protokół: liczba sztuk, materiał, parametry procesu, wyniki skanowania kodów i zdjęcia próby kontrolnej.» (protokół przy znakowaniu)
- Pytanie P06.

**F71 [C]** Świadectwo zgodności i deklaracja materiałowa na życzenie (strona przemysłowa, kontekst serii znakowanych).
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Na życzenie wystawiamy świadectwo zgodności i deklarację materiałową.»

**F72 [B]** NDA i poufność dla projektów B2B / OEM.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Usługi kontraktowe z oznaczeniem klienta końcowego, umowa o poufności, archiwizacja wzorca.»

**F73 [A]** Gwarancja poprawki: przy pomyłce Padir poprawia element (zdanie jest na wzorcu 1019 i na obecnej 1011).
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Dostarczamy produkty najwyższej jakości, a jeśli dojdzie do pomyłki, zawsze poprawiamy element.»
- `zrodla/pages-1011-frezowanie-cnc.txt` «jeżeli jednak dojdzie do jakiejś pomyłki – zawsze poprawiamy produkt.»
- Bez frazy „najwyższej jakości” (zakazany wypełniacz).

**F74 [C] Normy:** listy norm z 2264 (IATF 16949, AS9100, ISO 13485, MDR itd.) to normy branż klientów, nie certyfikaty Padiru. Na stronie CNC nie sugerować żadnej certyfikacji.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Detale ze stopów aluminium i stali narzędziowej, numery seryjne, kody DMC, frezowane korpusy. AS9100 EN 9100 IRIS»

---

## 8. Odbiór, lokalizacja, kontakt

**F80 [A]** Adres: ul. Matuszewska 14, 03-876 Warszawa, budynek C2, wejście (brama) T9.
- `zrodla/pages-1019-wycinanie-laserowe.txt` «PADIR Ewa Salabura Matuszewska 14, 03-876 Warszawa NIP: 536-104-65-17»
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Budynek C2, wejście T9»
- `zrodla/pages-20-kontakt.txt` «Odwiedź nas na ul. Matuszewska 14 (budynek C2 brama T9) w Warszawie»

**F81 [A]** Godziny: poniedziałek-piątek 8:30-16:00.
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Godziny otwarcia Poniedziałek – Piątek: 8:30 – 16:00»
- `zrodla/pages-20-kontakt.txt` «Poniedziałek – Piątek: 8:30 – 16:00»

**F82 [A]** Telefon biura +48 22 741 36 55 (drugi numer +48 22 741 36 70), e-mail laser@padir.pl. Format numeru brać ze wzorca 1019.
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Telefon +48 22 741 36 55 E-mail laser@padir.pl»
- `zrodla/pages-20-kontakt.txt` «Biuro +48 22 741 36 55 +48 22 741 36 70 laser@padir.pl»

**F83 [B]** Osoby kontaktowe: właściciel Ewa Salabura (608 311 993, ewa@padir.pl), obsługa klienta Aldona Fidos (608 292 248, aldona@padir.pl). Tylko strona Kontakt.
- `zrodla/pages-20-kontakt.txt` «Właściciel Ewa Salabura 608 311 993 ewa@padir.pl Obsługa klienta Aldona Fidos 608 292 248 aldona@padir.pl»

**F84 [A]** Odbiór osobisty przy Matuszewskiej 14 albo kurier.
- `zrodla/pages-8-produkty.txt` «Osobiście przy ulicy Matuszewskiej 14 w Warszawie albo kurierem pod wskazany adres.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Odbiór osobisty przy ulicy Matuszewskiej 14 w Warszawie lub kurier.»

**F85 [B]** Pracownia na Targówku (dzielnica).
- `zrodla/pages-8-produkty.txt` «malowane ręcznie w pracowni na Targówku»

---

## 9. Realizacje i klienci wymienieni z nazwy

**F90 [A]** Galeria `/przykladkowe-realizacje/` ma filtr „Frezowanie CNC” z 6 realizacjami (6 kart `cnc` w `realizacje-karty.json`). Zatwierdzone tytuły, materiały i zdjęcia:

| tytuł (dosłownie) | materiał | zdjęcie pełne |
|---|---|---|
| Napis przestrzenny „Tea” | Plexi lustrzana | `uploads/2026/08/padir-realizacja-napis-przestrzenny-tea.jpg` |
| Napis przestrzenny „Team” | Plexi lustrzana | `uploads/2026/08/padir-realizacja-napis-przestrzenny-team.jpg` |
| Frezowana litera przestrzenna | Buk | `uploads/2026/08/padir-realizacja-frezowana-litera-przestrzenna.jpg` |
| Frezowany napis „Ajala” | Konglomerat kwarcowy | `uploads/2026/08/padir-realizacja-frezowany-napis-ajala.jpg` |
| Medalion „Republika Portionii” | MDF | `uploads/2026/08/padir-realizacja-medalion-republika-portionii.jpg` |
| Frezowany relief „Duka” | Tworzywo | `uploads/2026/08/padir-realizacja-frezowany-relief-duka.jpg` |

- `zrodla/pages-1397-przykladkowe-realizacje.txt` «Grawerowanie laserowe 24 Wycinanie laserowe 20 Frezowanie CNC 6» (łącznie 44 karty; przycisk „Wszystkie” w kodzie startuje z liczbą 45, a licznik obok pokazuje «44 realizacje», więc liczby ogółem na stronie CNC nie podajemy)
- `zrodla/realizacje-karty.json` «"kategorie": "cnc", "plakietka": "Frezowanie"» (6 rekordów, tytuły i materiały jak w tabeli)
- Dodatkowo w bibliotece jest kadr poziomy reliefu: `zrodla/media.json` «"alt": "Frezowany relief Duka, frezowanie CNC"» (id 2362, `padir-hero-frezowany-relief-duka.jpg`, 1632 × 920).
- Kontekst: „Tea”, „Team”, „Ajala”, „Duka”, „Republika Portionii” to tytuły prac (napisy na nich), a nie przedstawieni klienci. Serwis nie mówi, dla kogo powstały, jakie mają wymiary ani grubość. Pisać o nich tak jak galeria: tytuł + materiał (P12).
- Zdjęć nie oglądałem; opisy alt w serwisie są niespójne (S10). Przed podpisaniem kadru ktoś musi go zobaczyć.

**F91 [B]** Strona przemysłowa pokazuje w „Realizacje: Detale z naszej pracowni” zdjęcia z obróbki CNC, opisane tylko w alt: frezowane śmigło (alt z nazwą Callfly), element „WBET DS18”, detal po obróbce CNC, frezowanie CNC w drewnie. Tych prac nie ma w galerii 1397.
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Realizacje Detale z naszej pracowni. Wycinek zleceń przemysłowych z ostatnich miesięcy.»
- `zrodla/pages-2264-uslugi-dla-przemyslu.raw.html` «alt="Frezowane śmigło Callfly"» oraz «alt="Frezowane śmigło, realizacja Padir"» (`uploads/2026/04/smiglo-callfly.jpg`)
- `zrodla/pages-2264-uslugi-dla-przemyslu.raw.html` «alt="Element WBET DS18"» oraz ten sam plik jako «alt="Element z aluminium po obróbce"» (`uploads/2026/04/wbet-ds18.jpg`)
- `zrodla/pages-2264-uslugi-dla-przemyslu.raw.html` «alt="Detal po obróbce CNC w pracowni Padir"» (`uploads/2026/04/IMG_0060.jpg`)
- `zrodla/pages-2264-uslugi-dla-przemyslu.raw.html` «alt="Frezowanie CNC w drewnie"» oraz «alt="Frezowanie CNC detalu w pracowni Padir"» (`uploads/2026/04/cnc-drewno.jpg`)
- Nazwy „Callfly” i „WBET” są tylko w tekście alternatywnym, nie w treści strony. Bez potwierdzenia nie wymieniać ich jako klientów w tekście (P13).

**F92 [B]** Logotypy „Zaufali nam / Współpracujemy z największymi”: na obecnej 1011 sześć logotypów, na wzorcu 1019 te same plus Willson & Brown i Uniwersytet Warszawski. Kontekst ogólny („tworzyliśmy produkty dla marek”), nie frezowanie. Można powtórzyć sekcję logotypów w tym samym ogólnym kontekście, nie wolno sugerować, że te firmy zamawiały frezowanie.
- `zrodla/pages-1019-wycinanie-laserowe.raw.html` «alt="Logotypy klientów: Time Trend, Sokołów, PKP, Dajar, Centrum Nauki Kopernik, iGF"»
- `zrodla/pages-1019-wycinanie-laserowe.raw.html` «alt="Willson &amp; Brown"» oraz «alt="Uniwersytet Warszawski"»
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Tworzyliśmy produkty dla wielu rozpoznawalnych marek.»
- `zrodla/pages-1011-frezowanie-cnc.raw.html` pliki `time-trend-300x108.png`, `sokolow-300x133.png`, `pkp-300x132.png`, `dajar-300x132.png`, `kopernik-300x87.png`, `igf-300x151.png` pod nagłówkiem `zrodla/pages-1011-frezowanie-cnc.txt` «Współpracujemy z największymi»

**F93 [C]** Ekspozytory dla marek kosmetycznych (wpis 2043): BOSS opisany jako „jedna z naszych realizacji”, ale bez frezowania; ekspozytor YSL z „frezowanymi gniazdami” pokazany jako „przykładowa realizacja”, bez jasnego stwierdzenia, że to praca Padiru. Na stronie CNC nie wymieniać tych marek.
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «Przykład na jednej z naszych realizacji : Gloryfier dla BOSS»
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «w części środkowej precyzyjnie frezowane gniazda na produkty, poniżej duży monogram YSL z plexi»
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «przyjrzyjmy się kilku przykładowym realizacjom»
- Pytanie P15.

**F94 [B]** Ścianka foto na barce na Wiśle: front z lustrzanego PMMA laserem, nośnik z MDF na CNC. Wpis nie podaje nazwy klienta. Case Bondi Sands na 1019 opisuje ściankę „nad Wisłą” na plaży i tylko cięcie; związku obu historii serwis nie potwierdza.
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «Ścianka foto na barce na Wiśle.»
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Efektowna, lustrzana ścianka na letni event nad Wisłą»
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Instalacja stanęła na plaży w wyznaczonym dniu»
- Nie łączyć Bondi Sands z frezowaniem bez potwierdzenia (P14).

**F95 [A] Zdjęcia na obecnej 1011 to zdjęcia stockowe** (tytuły w bibliotece mediów), więc nie mogą udawać realizacji ani maszyny Padiru: hero `AdobeStock_243435162` (id 1017), sekcja treści `AdobeStock_439101752` (id 1012), materiały `pexels-pixabay-48799` (id 1312). W bibliotece jest też `industrial metalworking cutting process by milling cutter` (id 1045, AdobeStock).
- `zrodla/media.json` «"tytul": "AdobeStock_243435162"», «"tytul": "AdobeStock_439101752"», «"tytul": "pexels-pixabay-48799"», «"tytul": "industrial metalworking cutting process by milling cutter"»
- Własnego zdjęcia frezarki Padiru w serwisie nie znalazłem (P23).

---

## 10. Doświadczenie firmy

**F100 [A]** Na rynku od 2002 roku. Uwaga na kontekst: produkty i case studies mówią „na rynku obróbki laserowej”, strona przemysłowa „precyzyjnej obróbki”, HoReCa „w branży”. Nigdzie nie ma daty rozpoczęcia frezowania.
- `zrodla/pages-8-produkty.txt` «od 2002 na rynku obróbki laserowej»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «od 2002 na rynku precyzyjnej obróbki»
- `zrodla/pages-2283-uslugi-dla-horeca.txt` «od 2002 roku w branży»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Dwadzieścia cztery lata pracy z technologami, kierownikami produkcji i działami jakości.» (2002 + 24 = 2026, zgodne)
- Na stronie CNC bezpieczna forma: „pracownia działa od 2002 roku”, bez „frezujemy od 2002” (P16).

**F101 [C]** Statystyki ze strony O nas („20 + Lat”, „16 000+”, „2500+”) dotyczą grawerowania, a strona jest niedokończonym szablonem (angielskie teksty zastępcze). Na stronie CNC nie używać.
- `zrodla/pages-10-o-nas.txt` «20 + Lat lat na rynku grawerowania 16 000+ zrealizowanych projektów grawerowania 2500+ unikatowych klientów rocznie»
- `zrodla/pages-10-o-nas.txt` «Experience the fusion of imagination and expertise with Études Architectural Solutions.»

---

## Sprzeczności

**S1. Jakie materiały frezuje Padir: metale czy „soft-materiały”.**
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Obróbka skrawaniem 3- i 5-osiowa. Detale z aluminium, mosiądzu, miedzi, tworzyw konstrukcyjnych i drewna.» (to samo na karcie obecnej 1011 i w starej sekcji 1011 „Frezowanie w metalu”)
- kontra `zrodla/posts-2078-ciecie-przemyslowe.txt` «(możliwości maszyny są szersze, ale w usługach celowo skupiamy się na „soft-materiałach”)» oraz «W większości zleceń w retailu, eventach i małej produkcji nie ścigamy się ze stalą.»
- kontra `zrodla/pages-1397-przykladkowe-realizacje.txt` «napisy przestrzenne oraz detale frezujemy na maszynach CNC w MDF, konglomeracie i tworzywach technicznych» (wszystkie 6 realizacji CNC: plexi, buk, konglomerat, MDF, tworzywo; żadnego metalu)
- Ocena: bardziej wiarygodne jest 1397 + 2078, bo opisuje to, co faktycznie pokazano na zdjęciach, a 2078 opisuje maszynę i praktykę usługową. Strona 2264 jest nowa, ale jej sekcja CNC nie ma ani jednej realizacji z metalu w treści (jedyne zdjęcia metalu, „Element z aluminium po obróbce”, to alt pliku `wbet-ds18.jpg`, bez opisu technologii). Do szkicu: materiały z 1397 jako fakt, metale tylko w żółtej ramce (P04).

**S2. Obróbka 5-osiowa a opis maszyny.**
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «obróbka skrawaniem 3- i 5-osiowa»
- kontra `zrodla/posts-2078-ciecie-przemyslowe.txt` «Opcje: nóż oscylacyjny, bigownik, nóż do folii, pisak, dozownik, sondy (dotyk/laser), oś obrotowa.» (ploter Kimla ze stołem próżniowym, oś obrotowa tylko jako opcja; nigdzie mowy o 5 osiach)
- Ocena: nie da się rozstrzygnąć. Ploter z polem 2000 × 3000 mm (F20) to maszyna do płyt; 5 osi wymaga konkretnej maszyny, której serwis nie nazywa. Do potwierdzenia (P03), do tego czasu żółta ramka.

**S3. Wielkość obrabianych elementów na samej stronie 1011.**
- `zrodla/pages-1011-frezowanie-cnc.txt` «jesteśmy w stanie pracować z detalami o wymiarach od kilku milimetrów aż do kilkudziesięciu centymetrów»
- kontra ta sama odpowiedź: `zrodla/pages-1011-frezowanie-cnc.txt` «Maksymalny obszar roboczy to 2000 na 3000mm», oraz `zrodla/pages-8-produkty.txt` «Od detali kilkumilimetrowych po elementy wielkoformatowe.»
- Ocena: wiarygodne jest 2000 × 3000 mm (cztery źródła, F20) i sformułowanie z produktów. „Kilkadziesiąt centymetrów” to błąd starego tekstu.

**S4. Jedna frezarka czy kilka.**
- `zrodla/pages-1011-frezowanie-cnc.txt` «Wielkość pola roboczego frezarek, na których pracujemy to: 2000mm x 3000mm»
- kontra `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Nasza frezarka oferuje maksymalne pole pracy wielkości 2000 × 3000 mm .»
- Ocena: nie wiadomo. FAQ jest nowszy (styczeń 2025) i bardziej konkretny, ale to też nie przesądza. Pisać bezosobowo („pole robocze 2000 × 3000 mm”), liczba maszyn do potwierdzenia (P01).

**S5. Pole robocze największego lasera (ważne, jeśli strona CNC odwołuje się do lasera).**
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Największy laser posiada pole robocze o wymiarach 2500 × 1650 mm .»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Pole robocze 1680 × 2510 mm» (odwrócona kolejność)
- kontra `zrodla/pages-1019-wycinanie-laserowe.txt` «Pole robocze 2510 × 1680 mm» i `zrodla/pages-8-produkty.txt` «2510 na 1680 mm»
- Ocena: wiarygodne 2510 × 1680 mm (wzorzec 1019, produkty, brief). Wartości z FAQ i kolejność z 2264 nie przenosić.

**S6. Maksymalna moc lasera.**
- `zrodla/pages-1019-wycinanie-laserowe.txt` «400 W maks. moc cięcia»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Moc od 20 W do 500 W»
- kontra `zrodla/pages-1019-wycinanie-laserowe.txt` «Moc CO₂ 180-500 W» i «moc do 500 W», `zrodla/pages-8-produkty.txt` «mocą regulowaną od 180 do 500 W»
- Ocena: wiarygodne 180-500 W dla SP2000 i „do 500 W” (brief, reguła 10: „do 400 W” to znany błąd, który wciąż wisi w statystyce na 1019). „Od 20 W” na 2264 nie ma pokrycia w żadnym modelu Trotec z parku (najmniejszy zakres to 25-120 W); może dotyczyć lasera fiber, którego parametrów serwis nie podaje.

**S7. Terminy realizacji (żaden nie dotyczy wprost frezowania).**
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Przy mniejszych zleceniach zazwyczaj mieścimy się w przedziale około 2 dni roboczych , czasem nawet jesteśmy w stanie zrealizować zamówienie w 1 dzień .»
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «od następnego dnia do ok. 3 dni roboczych»
- `zrodla/pages-2264-uslugi-dla-przemyslu.txt` «Serie do 500 sztuk zwykle 24 do 48 godzin od zatwierdzenia próbki. Serie od 500 do 5000 sztuk: 2 do 4 dni roboczych.» oraz «24-72 h typowa seria»
- `zrodla/pages-2283-uslugi-dla-horeca.txt` «Typowe zamówienie dla lokalu to od 5 do 10 dni roboczych od zatwierdzenia próbki.»
- oraz `zrodla/posts-1578-wycinanie-laserowe-vs-frezowanie-cnc.txt` «W porównaniu z wycinaniem laserowym, frezowanie CNC może być czasochłonne, zwłaszcza przy skomplikowanych projektach.»
- Ocena: liczby z 2264 dotyczą serii znakowanych, z 2283 zamówień gastronomicznych, z 1660 usług ogólnie. Najbliższe frezowaniu jest 2078 (wpis o CNC i laserze), ale to wciąż widełki dla obu technologii. Do szkicu: „termin podajemy w wycenie” (F63) + żółta ramka z pytaniem P07.

**S8. Karty menu z drewna: frez czy laser.**
- `zrodla/pages-2283-uslugi-dla-horeca.txt` «Frezujemy kontur i grawerujemy treść w jednej operacji.»
- kontra ten sam blok: `zrodla/pages-2283-uslugi-dla-horeca.txt` «Wycinanie i grawerowanie konturu w jednym przejściu»
- Ocena: nie da się rozstrzygnąć („w jednym przejściu” brzmi jak laser). Na stronie CNC nie podawać kart menu jako przykładu frezowania bez potwierdzenia (P21).

**S9. PVC: laser czy CNC.**
- `zrodla/pages-8-produkty.txt` «Metale miękkie, plexi, poliwęglan, PVC, drewno, skóra, filc i tkaniny.» (lista materiałów cięcia laserowego)
- kontra `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «nie wszystko da się ciąć laserem (np. zwykłe PVC wydziela toksyczne opary), więc czasem do akcji wkracza frezarka.» oraz `zrodla/posts-2147-obrobka-tworzyw-sztucznych.txt` «Uwagę zwraca PVC. W wielu zakładach jest wykluczane z cięcia laserem z uwagi na emisję chloru i zagrożenie dla urządzeń.»
- Ocena: bardziej wiarygodne 2043/2147 (konkretne uzasadnienie, dwa źródła). Na stronie CNC można napisać, że PVC i piankę PVC obrabiamy frezem; nie pisać, że laser tnie PVC. Do potwierdzenia przy okazji P26.

**S10. Opisy tych samych zdjęć CNC są różne (do sprawdzenia wzrokiem przed podpisem).**
- `zrodla/pages-8-produkty.raw.html` plik `padir-realizacja-frezowany-napis-ajala.jpg` z «alt="Głowica frezarki CNC wycinająca litery w płycie"»
- kontra `zrodla/realizacje-karty.json` ten sam plik: «"alt": "Frezowany napis „Ajala” - Konglomerat kwarcowy"»
- `zrodla/pages-2264-uslugi-dla-przemyslu.raw.html` plik `padir-realizacja-logo-przestrzenne-boko.jpg` (realizacja z wycinania laserowego) z «alt="Element z tworzywa technicznego"»
- `zrodla/pages-8-produkty.raw.html` «alt="Złoty napis przestrzenny „Tea”"» kontra `zrodla/pages-1397-przykladkowe-realizacje.txt` «Napis przestrzenny „Tea” Plexi lustrzana» (możliwe, że to złota plexi lustrzana; kolor do sprawdzenia na zdjęciu)
- Ocena: za wiążące uznać `realizacje-karty.json` (zatwierdzona galeria). Opisy z 8 i 2264 nie są źródłem faktów o tych pracach.

**S11. Dla kogo frezuje Padir.**
- `zrodla/pages-1011-frezowanie-cnc.txt` «Frezujemy dla przemysłu i dla gastronomii. Zlecenia seryjne i pojedyncze detale trafiają do nas głównie z tych dwóch stron.» oraz karta HoReCa «Litery przestrzenne, oznaczenia wnętrz, deski do serwisu i elementy wystroju dla hoteli oraz restauracji.»
- kontra galeria i wpisy: realizacje CNC to napisy, litery, relief, medalion (1397), a 2078 wskazuje retail, eventy i małą produkcję (F51). Strona HoReCa nie wspomina liter przestrzennych ani frezowania desek (deski są tam grawerowane laserem).
- Ocena: twierdzenie „głównie przemysł i gastronomia” nie ma pokrycia w realizacjach. Linki do obu stron można zostawić jako „zobacz też”, ale bez tezy o głównych klientach (P22).

**S12. Drobne niespójności kontaktowe.**
- `zrodla/pages-1011-frezowanie-cnc.txt` «Zadzwoń do nas pod nr.: +48 227 413 655» kontra `zrodla/pages-1019-wycinanie-laserowe.txt` «Telefon +48 22 741 36 55» (ten sam numer, inny zapis; brać zapis z 1019)
- `zrodla/pages-1019-wycinanie-laserowe.txt` «Budynek C2, wejście T9» kontra `zrodla/pages-20-kontakt.txt` «Budynek C2, Brama T9» (brać zapis ze wzorca 1019)

**S13. Minimum zamówienia.**
- `zrodla/posts-1660-faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow.txt` «Minimalny koszt usługi wynosi 100 zł .»
- kontra `zrodla/pages-8-produkty.txt` «Pojedyncze sztuki bez minimum zamówienia.» (kontekst: prezenty)
- Ocena: formalnie to dwie różne rzeczy (minimum wartości kontra minimum ilości), ale klient przeczyta to jako sprzeczność. Na stronie CNC pisać „od 1 sztuki”, kwotę 100 zł tylko po potwierdzeniu (P08).

---

## Twierdzenia bez pokrycia na obecnej stronie (1011 i szablon), których NIE przenosimy

Marketing, ogólniki i liczby, których nie potwierdza żadne inne źródło (albo które przeczą innym źródłom):

1. `zrodla/szablon-frezowanie-cnc.txt` «Twórz wyjątkowe formy z precyzją CNC» oraz «Ta metoda doskonale sprawdza się w produkcji elementów o wysokiej jakości i dokładności.» (slogan i ogólnik, zero konkretu)
2. `zrodla/pages-1011-frezowanie-cnc.txt` «Proces ten gwarantuje wysoką dokładność, powtarzalność oraz możliwość obróbki dużych i małych serii produkcyjnych.» („gwarantuje” bez liczby)
3. `zrodla/pages-1011-frezowanie-cnc.txt` «Wykorzystujemy zaawansowane maszyny CNC, co pozwala na precyzyjną i efektywną obróbkę» (brak modeli, „zaawansowane” bez pokrycia)
4. `zrodla/pages-1011-frezowanie-cnc.txt` «Zawsze staramy się dostarczyć produkty najwyższej jakości» (zakazany wypełniacz; sama obietnica poprawki zostaje, F73)
5. `zrodla/pages-1011-frezowanie-cnc.txt` «Nasz zespół to specjaliści z wieloletnim doświadczeniem, którzy dbają o każdy detal Twojego projektu.» (brak danych o zespole CNC)
6. `zrodla/pages-1011-frezowanie-cnc.txt` «z niezwykłą dokładnością, sięgającą nawet ułamków milimetra» (bez liczby; tolerancja frezowania nieznana, P05)
7. `zrodla/pages-1011-frezowanie-cnc.txt` «W branży meblarskiej frezowanie CNC wykorzystywane jest do produkcji niestandardowych mebli, a w elektronice do obróbki obudów i komponentów.» (ogólnik o technologii, bez realizacji Padiru)
8. `zrodla/pages-1011-frezowanie-cnc.txt` «Dzięki zastosowaniu nowoczesnych technologii, takich jak symulacje CAD/CAM, możemy dokładnie przewidzieć, jak będzie wyglądał produkt końcowy» (tylko tu; P17)
9. `zrodla/pages-1011-frezowanie-cnc.txt` «Technologia ta jest idealna zarówno dla dużych korporacji, jak i mniejszych przedsiębiorstw poszukujących dokładnych i trwałych komponentów.»
10. `zrodla/pages-1011-frezowanie-cnc.txt` «frezowanie CNC umożliwia tworzenie unikatowych elementów dekoracyjnych, takich jak panele 3D» oraz «Często frezowanymi elementami są również panele akustyczne, a samo frezowanie CNC pozwala również wdrażać unikatowe rozwiązania architektoniczne.» (brak realizacji)
11. `zrodla/pages-1011-frezowanie-cnc.txt` «frezowanie CNC jest nieocenionym narzędziem w produkcji precyzyjnych, niestandardowych rozwiązań dla wymagających klientów»
12. `zrodla/pages-1011-frezowanie-cnc.txt` «jesteśmy w stanie pracować z detalami o wymiarach od kilku milimetrów aż do kilkudziesięciu centymetrów, zapewniając najwyższą dokładność i jakość wykonania» (sprzeczne z 2000 × 3000 mm, S3; „najwyższą” bez pokrycia)
13. `zrodla/pages-1011-frezowanie-cnc.txt` «Dokładność, która robi różnicę – Frezowanie CNC. Twórz z nami stawiając na precyzję i niezawodność.»
14. `zrodla/pages-1011-frezowanie-cnc.txt` «W swojej historii tworzyliśmy produkty dla największych marek» (superlatyw; logotypy nie dotyczą frezowania, F92)
15. `zrodla/pages-1011-frezowanie-cnc.txt` «Doskonałe dla stolarzy, projektantów wnętrz oraz twórców unikatowych mebli»
16. `zrodla/pages-1011-frezowanie-cnc.txt` «Frezowanie CNC w metalu łączy wytrzymałość i precyzję, tworząc komponenty o niezrównanej dokładności. Idealne dla branż takich jak motoryzacja, lotnictwo i inżynieria» (metale niepotwierdzone, S1; branże bez realizacji)
17. `zrodla/pages-1011-frezowanie-cnc.txt` «możemy kształtować metal w sposób, który spełnia najbardziej rygorystyczne normy jakościowe» (żadna norma ani certyfikat w źródłach, F74)
18. `zrodla/pages-1011-frezowanie-cnc.txt` «Technologia ta umożliwia tworzenie komponentów o wysokiej wytrzymałości i doskonałej jakości powierzchni» oraz «od elektroniki po medycynę» (branże bez realizacji)
19. `zrodla/pages-1011-frezowanie-cnc.txt` «Grawerowanie w tworzywach sztucznych Frezowanie CNC w tworzywach sztucznych» (błędny nagłówek: „Grawerowanie” w sekcji o frezowaniu)
20. `zrodla/pages-1011-frezowanie-cnc.txt` «Strona o materiałach w budowie» (zaślepka)
21. `zrodla/pages-1011-frezowanie-cnc.txt` «Frezujemy dla przemysłu i dla gastronomii. Zlecenia seryjne i pojedyncze detale trafiają do nas głównie z tych dwóch stron.» (S11)
22. `zrodla/pages-1011-frezowanie-cnc.txt` karta HoReCa «Litery przestrzenne, oznaczenia wnętrz, deski do serwisu i elementy wystroju dla hoteli oraz restauracji.» (strona HoReCa tego nie potwierdza, S11)
23. Karta „Usługi dla przemysłu” na 1011 («Obróbka skrawaniem 3- i 5-osiowa detali z aluminium, mosiądzu, miedzi i tworzyw konstrukcyjnych. Protokół pomiarowy do każdej partii.») ma źródło na 2264, ale wymaga potwierdzenia: przenosić tylko w żółtej ramce (F23, F47, F70).
24. Zdjęcia stockowe na 1011 (F95) nie mogą zostać jako ilustracja „naszej pracy” ani „naszej maszyny”.

Dla porządku, także w innych źródłach są twierdzenia, których nie przenosimy na stronę CNC:
- `zrodla/posts-2078-ciecie-przemyslowe.txt` «i to już rozwiązuje 99% zleceń w soft-materiałach» oraz «potrafią skrócić czas całego procesu o połowę» (liczby marketingowe bez źródła)
- `zrodla/posts-2043-tworzenie-ekspozycji-dla-marek-kosmetycznych.txt` «Według badań rynkowych odpowiednia prezentacja może zwiększyć sprzedaż eksponowanego produktu nawet o 25-30%.»
- `zrodla/posts-1845-frezowanie-tworzyw-sztucznych-na-czym-polega-jak-wyglada-specyfika-frezowania-tworzyw-sztucznych.txt` «Nie potrzeba tutaj operatora, który czuwałby nad maszyną» (szkic, nieopublikowany, nieprawdziwe uogólnienie)

---

## Luki i pytania do klienta

Czego strona o frezowaniu potrzebuje, a serwis nie podaje. Każde pytanie można wstawić do żółtej ramki „Do potwierdzenia z klientem: …”.

- **P01** Na jakich frezarkach pracujecie: producent i model (czy to ploter Kimla z wpisu „Cięcie przemysłowe”) i ile ich jest? Strona raz pisze „frezarka”, raz „frezarki”.
- **P02** Czy pole 2000 × 3000 mm to jedna maszyna? Jaka jest maksymalna wysokość materiału (oś Z) i maksymalna grubość płyty, którą frezujecie?
- **P03** Czy robicie obróbkę 5-osiową? Jeśli tak, na jakiej maszynie i do jakiej wielkości detalu? Czy macie oś obrotową (4. oś)?
- **P04** Czy frezujecie metale: aluminium, mosiądz, miedź? Do jakiej grubości? Czy zdanie z bloga „w usługach celowo skupiamy się na soft-materiałach” jest nadal aktualne?
- **P05** Jaką dokładność frezowania możemy podać (w mm)? Czego dotyczy „±0,01 mm dokładność pozycjonowania” ze strony przemysłowej: frezarki, lasera czy całej pracowni?
- **P06** Czy do każdej partii frezowanej dołączacie protokół pomiarowy? Co mierzycie i czym? Czy dotyczy to też pojedynczych sztuk?
- **P07** Jakie są typowe terminy frezowania: pojedyncza sztuka, seria (np. 50 liter), duży format? Czy widełki „24-72 h” lub „od następnego dnia do ok. 3 dni roboczych” obejmują CNC?
- **P08** Czy obowiązuje minimalna wartość zlecenia (FAQ z 2025 r. podaje 100 zł) i czy dotyczy frezowania? Czy „próbka kontrolna gratis dla nowych klientów” obejmuje frezowanie?
- **P09** Jak mały detal możecie wyfrezować: najmniejszy frez, najmniejszy promień wewnętrzny, najcieńsza ścianka lub mostek?
- **P10** Jakie maksymalne grubości frezujecie w plexi, MDF, sklejce, tworzywach technicznych? Czy litery 3D z akrylu 15-20 mm (przykład z bloga) to Wasza typowa praca?
- **P11** Jakie wykończenie oferujecie po frezowaniu: polerowanie krawędzi plexi (mechaniczne, płomieniowe), szlifowanie, malowanie, lakierowanie, olejowanie? Czy montujecie elementy (dystanse, podświetlenie LED, klejenie)?
- **P12** Czy możemy opisać realizacje CNC z galerii („Tea”, „Team”, litera z buku, „Ajala”, „Republika Portionii”, „Duka”): wymiary, grubość, dla jakiego typu klienta, ile trwało? Czy nazwy na pracach można podać jako nazwy klientów?
- **P13** Śmigło (alt „Callfly”) i element „WBET DS18” ze strony przemysłowej: czy to frezowanie, z jakiego materiału, czy wolno wymienić Callfly i WBET z nazwy?
- **P14** Ścianka foto na barce na Wiśle (blog): czy to projekt Bondi Sands i czy nośnik z MDF był frezowany u Was?
- **P15** Ekspozytory YSL z frezowanymi gniazdami (blog o ekspozycjach): czy to Wasza realizacja i czy możemy ją pokazać na stronie CNC?
- **P16** Od kiedy frezujecie CNC? Data „od 2002” w serwisie dotyczy obróbki laserowej.
- **P17** Czy przed frezowaniem robicie symulację CAD/CAM albo wizualizację do akceptacji? Czy przygotowujecie model 3D (np. relief) od zera, czy tylko z pliku klienta?
- **P18** Czy przyjmujecie do frezowania modele 3D (STL) i robicie z nich reliefy 3D?
- **P19** Czy macie nóż oscylacyjny, bigownik lub nóż do folii (cięcie pianek, kartonu, folii) na ploterze CNC?
- **P20** Jak dzielicie elementy większe niż 2000 × 3000 mm: moduły z zamkami, łączenia klejone, inne?
- **P21** Drewniane karty menu dla lokali: kontur frezujecie czy wycinacie laserem?
- **P22** Kto najczęściej zamawia u Was frezowanie: przemysł i gastronomia (jak pisze obecna strona) czy reklama, eventy i agencje (jak wynika z galerii)? Dla jakich branż przemysłowych frezowaliście realne detale?
- **P23** Czy macie własne zdjęcia frezarki i stanowiska CNC? Obecna strona ma tylko zdjęcia stockowe.
- **P24** Czy któryś z klientów z paska logotypów (Time Trend, Sokołów, PKP, Dajar, Centrum Nauki Kopernik, iGF, Willson & Brown, Uniwersytet Warszawski) zamawiał frezowanie? Czy pokazać pasek logotypów na stronie CNC?
- **P25** Jakie płyty macie zwykle na stanie do frezowania (plexi, MDF, sklejka, dibond, pianka PVC), a co klient musi dostarczyć?
- **P26** Które z tych materiałów obrabiacie na CNC: dibond, poliwęglan, sklejka WBP, PVC i pianka PVC, HIPS, POM, PA6, PP?
- **P27** Czy konglomerat kwarcowy (napis „Ajala”) lub kamień frezujecie regularnie, czy to była jednorazowa praca?
- **P28** Czy na CNC robicie też wiercenie, gwintowanie, fazowanie i frezowanie kieszeni (gniazd pod produkty)?
- **P29** Czy robicie grawer mechaniczny frezem (np. głęboki grawer w mosiądzu), czy tylko grawer laserowy?

---

## Wiedza ogólna (nie fakty o firmie)

Poniższe zdania opisują technologię, a nie możliwości Padiru. Można z nich korzystać w sekcji „Na czym to polega” (wzorzec 1019 ma taką sekcję), formułując je jako ogólną wiedzę, bez „u nas” i bez liczb przypisanych pracowni. Źródła są tylko dla porządku.

- Frezowanie to obróbka skrawaniem: obracające się narzędzie (frez) usuwa materiał warstwa po warstwie, a ruchy maszyny steruje komputer (CNC). Źródła: `posts-1578` «Frezowanie CNC, czyli frezowanie sterowane numerycznie, to proces obróbki materiałów, w którym specjalne narzędzie tnące, tzw. frez, usuwa materiał z powierzchni obrabianej części.»; `posts-1829` (szkic).
- Laser i frez dają inną krawędź: laser CO2 zostawia wąską szczelinę i błyszczącą krawędź na akrylu, ale przy dużej grubości krawędź robi się lekko zbieżna (stożek); frez daje krawędź pionową, za to nie wejdzie w narożnik ostrzejszy niż jego promień. Źródło: `posts-2078` «W akrylu ok. 10 mm to moment, w którym stożek zaczyna być zauważalny technicznie (nadal bywa akceptowalny wizualnie).»
- Tworzywa termoplastyczne przy frezowaniu łatwo się nagrzewają i mogą się uplastycznić; pomaga mniejsza głębokość skrawania, wyższe obroty i dobre odprowadzanie wióra. Źródło: `posts-2147` «W praktyce pomaga mniejsza głębokość skrawania, wyższe obroty i skuteczne odprowadzanie wióra.»
- Dobór tworzywa do funkcji: POM stabilny wymiarowo, poliamid higroskopijny, PTFE odporny chemicznie; przy częściach z gwintami, gniazdami i pasowaniami zwykle wybiera się CNC, przy płaskich panelach laser. Źródło: `posts-2147` «Wybierz CNC , gdy część ma bryłową geometrię, gniazda, gwinty, wymagane pasowania i stabilność wymiarową w montażu; najlepiej sprawdza się z POM, PET, PA, PE, PTFE, PEEK, PVDF.»
- PVC nie nadaje się do cięcia laserem (chlor, opary), więc tnie się je mechanicznie. Źródło: `posts-2147`, `posts-2043` (patrz S9).
- Frezowanie zużywa narzędzia i wytwarza wióry; przy skomplikowanych kształtach bywa wolniejsze od lasera. Źródło: `posts-1578` «Narzędzia tnące używane w frezowaniu CNC zużywają się i wymagają regularnej wymiany lub ostrzenia»
- Przy metalu i szkle frezowanie wymaga chłodzenia i odpowiednich narzędzi. Źródło: `posts-2208` «Przy CNC obróbka metalu i szkła wymaga większej ostrożności, chłodzenia, odpowiednich narzędzi.»
- Typowe średnice frezów do sklejki 4-16 mm, stopy aluminium z krzemem poniżej 12% skrawają się najlepiej, rodzaje frezów (V, fazowe, zaokrąglające): to treści ze szkiców i starych wpisów (`posts-1823`, `posts-1797`, `posts-1873`), wyłącznie wiedza podręcznikowa. Nie przypisywać ich Padirowi.

---

## Linki wewnętrzne, które wolno użyć (opublikowane w `SPIS.json`)

`/uslugi-dla-przemyslu/`, `/uslugi-dla-horeca/`, `/przykladkowe-realizacje/`, `/wycinanie-laserowe/`, `/grawerowanie-laserowe/`, `/produkty/`, `/kontakt/`, `/case-study/`, `/blog/ciecie-przemyslowe/`, `/blog/obrobka-tworzyw-sztucznych/`, `/blog/wycinanie-laserowe-vs-frezowanie-cnc/`, `/blog/frezowanie-drewna-na-czym-polega-i-jakie-efekty-mozna-uzyskac/`, `/blog/frezowanie-cnc-w-nowoczesnym-designie-mebli/`, `/blog/faq-czyli-odpowiedzi-na-najczesciej-zadawane-pytania-klientow/`.
Nie linkować: `/torebki/` (brak w SPIS), wpisów 1797, 1823, 1829, 1845 (szkice).
