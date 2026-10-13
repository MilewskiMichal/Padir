# Usługi dla marketingu: poprawki po weryfikacji, runda 2

Redaktor prowadzący, 13.10.2026. Plik strony: `praca/marketing/strona.html`. Kopie sprzed rundy: `red-marketing-r2/strona-przed.html`,
`tresc-przed.md`, `ksiega-przed.json`, `pytania-przed.md`.

## Wynik

- 20 uwag. Każdą sprawdziłem na źródłach w `zrodla/`, w kadrach i w renderze.
- Wprowadzone: 18 (1-5, 7-19). Część w innym brzmieniu niż propozycja. Dwie pary dotyczyły tego samego zdania i połączyłem je: 2 i 7 (karta organizatorów), 4 i 11 (FAQ o nazwiskach).
- Nie wprowadzone: 2 (6 i 20). Problemy są prawdziwe, ale dotyczą cudzych plików (`sklad-notatki.md`, `zdjecia.json`). Gotowe łatki są niżej w „Dla innych”, a aktualne liczby strony w „Stan strony po rundzie 2”.
- `python3 -I sprawdz_szkic.py praca/marketing/strona.html --pdl`: błędy 0, ostrzeżenia 0, kod 0 (z `--szkic` też kod 0). Nie ma ramek `pdw-uwaga` ani napisu o wersji roboczej.
- JSON-LD parsuje się (`json.loads`).
- `red-marketing-r2/tresc_vs_strona.py`: 109 z 109 wierszy „> ” z `tresc.md` występuje dosłownie na stronie, a 21 z 21 altów się zgadza.
- `ksiega.json`: 184 → 188 wpisów (`red-marketing-r2/ksiega_r2.py`): 17 zmienionych, 4 usunięte, 8 dodanych. Każdy cytat sprawdzony dosłownie w pliku źródłowym (0 braków). Skrypt weryfikatora `praca/marketing/wer-fakty-r2-cytaty.py` też daje „ok”.
- Powtórzenia w widocznym tekście, przed → po: „na event” 5 → 3, „jubileusz” 5 → 4, „gal-” 7 → 5, „sztuk-” 11 → 7, „dostaniesz” 2 → 1.

## Uwagi

| # | waga, soczewka | miejsce | decyzja | co zmieniono / dlaczego |
|---|---|---|---|---|
| 1 | ważny, fakty | #nagrody, akapit i alt 2332 | wprowadzona ze zmianą brzmienia | Sprawdziłem pełny kadr (`red-marketing-r2/kont-r2.png`, `red-marketing-r2/2332-podglad.png`) i wycinki weryfikatora. Duża tafla z zaokrągloną krawędzią jest przezroczysta: przez nią widać czerwone tło. Czarna jest tylko sylwetka pary. Akapit: „W wyróżnieniu z tańczącą parą sylwetkę wycięliśmy z czarnej plexi, a taflę pod nią z przezroczystej.” Wziąłem „taflę pod nią” zamiast „podkład”, bo jest jaśniejsze. Alt: „Wyróżnienie z przezroczystej plexi z czarną sylwetką pary tanecznej i okrągłą tabliczką”. Zamiast „z sylwetką … z czarnej plexi” jest „z czarną sylwetką”, żeby nie było czterech „z” i dwóch „plexi”. „Grawerowaną” wypadło. W ksiega.json wpis o kadrze nie cytuje już błędnego opisu z zdjecia.json, tylko wskazuje plik 2332 w media.json i opisuje, co widać. Zmiany w zdjecia.json: patrz „Dla innych”. |
| 2 | ważny, fakty | s01, karta 3 | wprowadzona, połączona z 7 | „Statuetki i puchary dla laureatów. Na samo wydarzenie zrobimy też ściankę do zdjęć.” Potwierdzone: BRIEF-marketing.md zostawia nakłady pucharów otwarte, a wpisy 43-44 opierały się na ogólnych zdaniach z 1019 i 1660, w których o pucharach nie ma mowy. Usunąłem oba wpisy z księgi. „Od 1 sztuki” zostaje w hero, a „Jedna sztuka albo seria dla laureatów” przy statuetkach w karcie Zakresu. Nowego pytania nie ma, bo to obejmują P01 i P04. |
| 3 | drobny, fakty | Zakres, karta „Napisy, logo i oznakowanie” | wprowadzona | „Litery, logotypy i napisy przestrzenne z plexi albo sklejki. Plexi wychodzi spod lasera z gładką, błyszczącą krawędzią.” Potwierdzone w 2293: „Grubsza sklejka zostawia ciemniejszą krawędź” oraz „czysta krawędź, która przy akrylu wychodzi gładka od razu po cięciu”. W 2043: „krawędzie wychodzą gładkie i błyszczące”. Wpis 65 w księdze dostał cytat o akrylu, a za nim doszedł wpis z 2043. |
| 4 | drobny, fakty | FAQ „Każda nagroda ma mieć inne nazwisko…” | wprowadzona, połączona z 11 | „Przed serią grawerujemy jeden egzemplarz do akceptacji, a resztę robimy po Twojej zgodzie.” Potwierdzone: 2177 („Grawerujemy jedną sztukę do akceptacji…”) i pages-8 („Produkcja rusza dopiero po Twoim „tak”.”) nie mówią, że klient próbkę dostaje. HoReCa („zobaczysz wynik na swoim materiale”) dotyczy innej branży i darmowej próbki dla nowych klientów. Pytanie R03 jest w pytania.md. Do księgi doszedł wpis z cytatem z pages-8. |
| 5 | drobny, wzorzec | #nagrody, „Na 25-lecie” | wprowadzona | `Na <span style="white-space:nowrap">25-lecie</span> firmy INSOFT`. Styl nie ma border-*, a dywiz zostaje „-”. Pomiar po zmianie (`red-marketing-r2/render.py`, pole `lam`): „25-” i „lecie” leżą w tym samym wierszu przy 1440, 1366, 1280, 1024, 390 i 360 px. |
| 6 | drobny, wzorzec | `sklad-notatki.md` | nie wprowadzona w pliku | Potwierdzone. Notatki opisują stan sprzed rundy 1: 2322 w karcie 3, podpis „minimum 100 zł za zlecenie”, liczby 1 + 1 + 1, 1147 słów, wysokość 7964 / 13 949 px. Plik należy do składacza, a BRIEF.md każe agentowi pisać tylko do plików z jego zadania. Moje pliki to strona.html, ksiega.json, tresc.md, pytania.md i ten raport. Aktualne liczby są w sekcji „Stan strony po rundzie 2”, a łatka dla składacza w „Dla innych”. |
| 7 | ważny, język | s01, karta 3 | wprowadzona ze zmianą | Jak w 2. „Na wręczenie nagród” z propozycji nie wziąłem. Po zmianach z uwag 8 i 10 „wręcz-” stałoby trzy razy na jednym ekranie (H2 Zakresu „wręcza”, karta 3, akapit #nagrody „wręczasz”). Jest „Na samo wydarzenie”, czyli brzmienie sprzed rundy 1, bez zawężenia do gali. W karcie nie ma już ani „gal”, ani „konkursów”. |
| 8 | drobny, język | #nagrody, ostatnie zdanie | wprowadzona | „Zamawiasz statuetki lub puchary? Napisz, ilu masz laureatów i kiedy wręczasz nagrody.” Wpis 103 w księdze ma teraz to brzmienie (cytat z pages-8 bez zmian). |
| 9 | drobny, język | s01, karta 1 | wprowadzona | „statuetka na rocznicę firmy”. Karta Zakresu bez zmian. |
| 10 | drobny, język | nagłówki Zakresu | wprowadzona, z jedną zmianą w leadzie | H2 Zakresu: „Wszystko, co marka<br>wręcza i pokazuje.” (formuła sióstr, sprawdzona w 2283 i 2264). H3 karty 4: „Ścianki i dekoracje eventowe” (2293: „dekoracje eventowe”), tak samo nazwa usługi w JSON-LD. Lead pod H2 zmieniłem z „dla marek i agencji” na „dla firm i agencji”, bo „marka… marek” stało zaraz obok siebie. H2 #event i link karty 2 zmieniłem według uwagi 19. „na event” stoi teraz tylko w H2 #event, w linku do niego i na przycisku tej sekcji. |
| 11 | drobny, język | FAQ, „sztuka” 3 razy | wprowadzona ze zmianą | Całość: „Tak. Nazwiska, kategorie i lata wstawiamy z Twojej listy do pliku, więc każda nagroda dostaje swój napis. Przed serią grawerujemy jeden egzemplarz do akceptacji, a resztę robimy po Twojej zgodzie. Gdyby któraś nagroda wyszła z błędem, poprawimy ją.” Zostawiłem „z Twojej listy do pliku”, bo „do pliku z Twojej listy” można przeczytać jako plik z listy. „Dostaniesz” wypadło przez uwagę 4. „Poprawimy tę sztukę” odrzuciłem: odsyłacz do „błąd” jest niejasny. „Sztuka” nie pada w odpowiedzi ani razu. |
| 12 | drobny, język | #upominki, „Stal z powłoką” | wprowadzona ze zmianą | „Grawer może biec dookoła całego naczynia.” Wziąłem „biec” zamiast potocznego „iść”, bo „napis biegnie dookoła” to naturalna kolokacja. Źródło bez zmian (2177, głowica obrotowa). |
| 13 | drobny, język | #event, akapit | wprowadzona | „Litery i logo z plexi oraz sklejki tniemy laserem…” |
| 14 | drobny, język | #upominki, akapit | wprowadzona | „<a href="/grawerowanie-laserowe/">Grawer laserowy</a> zostawia znak w samym materiale, więc nie zejdzie jak nadruk.” Anchor linku #3 to teraz „Grawer laserowy” (tabela linków w tresc.md poprawiona, linki.md: patrz „Dla innych”). |
| 15 | drobny, język | FAQ „Ile kosztuje najmniejsze zlecenie?” | wprowadzona | Usunięte „, razem z terminem”. Wpis 168 w księdze cytuje teraz pages-8: „Napisz, ile sztuk i na kiedy, a wrócimy z terminem i ceną.” |
| 16 | drobny, język | FAQ, pytanie o dozamówienie | wprowadzona | „Za rok domówimy kilka sztuk. Będą takie same jak pierwsze?” |
| 17 | drobny, język | hero, drugi kafelek liczb | wprowadzona | `<span>minimum 100&nbsp;zł</span>`. Zmierzone: kafelek ma 128 px (wcześniej 138), a przy 390 i 360 px liczby układają się 2 + 1 jak u sióstr. |
| 18 | ważny, zdjęcia | galeria, kafel 1 (2520) | wprowadzona ze zmianą miejsca | Sprawdziłem sam (`red-marketing-r2/boko_dopasuj.py`): 2520 pokrywa się z wierszami 256-768 pliku 2525 przy x = 0, średnia różnica jasności 1,7/255. To ten sam kadr, a nie osobne zbliżenie. 2520 usunięte. Wstawiłem 2066 (`69A6E5DE-…-768x960.jpg`), alt „Czarna butelka termiczna z grawerowanym imieniem i małym logo”. Plik jest w zatwierdzonych w zdjecia.json, obejrzany na `red-marketing-r2/kont-r2.png`, nie stoi na 2283, 2264 ani 1019. Na zrzucie kafla 1:1 (`red-marketing-r2/butelka-kafel-1440.png`) widać imię i logo padir. Kafel stoi na końcu galerii, a nie za kubkiem, żeby dwa ciemne naczynia nie stały obok siebie (przy 390 px kubek i butelka są w różnych wierszach). Lead: „Napisy z plexi, ścianka w trakcie cięcia, plakieta i upominki z grawerem. …”. Wpisy 149-150 (2520) usunięte z księgi, a wpis 2066 dodany. |
| 19 | drobny, zdjęcia | #event, H2 a zdjęcie | wprowadzona | H2: „Ścianki i dekoracje<br>na event.” Link karty 2: „Ścianki i dekoracje na event &rarr;”. Potwierdzone na kadrze 2516: sama elewacja z tkaniną, bez ścianki i napisu. Do księgi doszedł wpis z 2470: „Tkanina odsłoniła się razem z plenerową „Carmen” Teatru Polskiego”, czyli dekoracja na wydarzenie. |
| 20 | drobny, zdjęcia | `zdjecia.json` (2527, 2525, 2520) | nie wprowadzona w pliku | Potwierdzone (grep: alt 2527 „…w trakcie cięcia na laserze…”, alt 2525 „…na lustrzanym słupie”, przy 2525 „galeria (kafel 1:1 ze środka)”). Plik nie jest mój (jak w rundzie 1), a sam weryfikator pisze, że zmiana wymaga zgody właściciela. Gotowa łatka jest w „Dla innych” razem z poprawką opisu 2332 z uwagi 1. Na stronie wszystkie alty są już poprawne, a 2520 zniknęło. |

## Stan strony po rundzie 2 (zamiast nieaktualnych liczb w `sklad-notatki.md`)

Render: `red-marketing-r2/render.py` (rama `marketing/zywa-horeca.html`, sieć zablokowana, zdjęcia z lokalnych kopii; 2066 pobrane do `red-marketing-r2/pobrane/`). Pomiar: `red-marketing-r2/po-pomiar.json`, zrzuty `red-marketing-r2/po-1440-s00…s08.png` i `po-390-s00…s08.png`. Obejrzałem s00 (390), s01, s02, s03, s04 i s06 (1440 i 390).

| co | wartość |
|---|---|
| sprawdzarka | 30 988 znaków, 1096 słów, 21 zdjęć, h1 = 1, ramek 0 |
| wysokość strony | 7878 px przy 1440, 13 803 px przy 390, 13 986 px przy 360 |
| sekcje przy 1440 (s00…s08) | 640, 868, 1043, 620, 669, 1158, 935, 889, 398 |
| liczby w hero | 1440: w jednym rzędzie; 390 i 360: 2 + 1 (podpis „minimum 100 zł”) |
| przewijanie w bok, wystające elementy, niewczytane zdjęcia | 0 / 0 / 0 przy wszystkich sześciu szerokościach |
| „25-lecie” | w jednym wierszu przy 1440, 1366, 1280, 1024, 390, 360 |
| karta 3 w s01 | 2522 `wyc-bondi-plaza` (cała ścianka, bez ludzi); 2322 nie ma na stronie |
| galeria | 8 kafli: 2315, 2324, 2527, 2354, 1607, 1614, 2035, 2066; szyld BOKO tylko w hero (2525) |

## Zmienione pliki

- `praca/marketing/strona.html`: zmiany z tabeli wyżej, plus nazwa czwartej usługi w JSON-LD („Ścianki i dekoracje eventowe”).
- `praca/marketing/tresc.md`: tekst zgodny ze stroną (109/109 wierszy, 21/21 altów), notki „R2” przy zmienionych miejscach, lista galerii, tabela linków (#3 i kotwica `#event`), nazwa usługi w K14.
- `praca/marketing/ksiega.json`: 184 → 188. Zmienione 20, 32, 42, 46, 65, 100, 101, 102, 103, 113, 124, 127, 155, 161, 163, 164 i 168 (numeracja sprzed zmian). Usunięte 43, 44, 149 i 150. Dodane: link karty 2, H2 i lead Zakresu, krawędź plexi z 2043, H3 karty 4, okrągła tabliczka 2332, H2 #event z 2470, kafel 2066, „resztę robimy po Twojej zgodzie”.
- `praca/marketing/pytania.md`: dopisana sekcja „Redakcja, runda 2” z R03 (próbka przed serią: wysyłka czy akceptacja na zdjęciu, czy płatna). Wcześniejsze wpisy bez zmian (diff pokazuje tylko dopisek).
- Robocze (nie produkcja): `red-marketing-r2/` (kopie „przed”, `render.py`, `ksiega_r2.py`, `boko_dopasuj.py`, `tresc_vs_strona.py`, kontaktówka `kont-r2.png`, podgląd `2332-podglad.png`, zrzuty `po-*`).

## Dla innych (nie moje pliki, nie zmieniałem)

- `praca/marketing/zdjecia.json` (autor przeglądu zdjęć), w `zatwierdzone`:
  - 2332: `"co_widac"` zacząć od „Wyróżnienie z przezroczystej plexi z sylwetką pary tanecznej z czarnej plexi i gwiazdkami, na czerwonym tle.” (reszta o tabliczce bez zmian); `"alt": "Wyróżnienie z przezroczystej plexi z czarną sylwetką pary tanecznej i okrągłą tabliczką"`.
  - 2527: `"alt": "Lustrzana ścianka eventowa w trakcie wycinania na maszynie w pracowni Padir"`.
  - 2525: `"alt": "Pionowe logo BOKO z pomarańczowych liter na lustrzanej plexi, na słupie w kawiarni"`; z `nadaje_sie_na` usunąć „galeria (kafel 1:1 ze środka)”.
  - 2520: `"uwagi": "Wycinek pliku 2525 (wiersze 256-768 w wersji 768 px, różnica 1,7/255), to samo ujęcie. Nie używać na jednej stronie z 2525."`
- `praca/marketing/sklad-notatki.md` (składacz):
  - (1) W „Do wiadomości prowadzącego” zastąpić punkt o 2322/P32 zdaniem: „s01, karta 3: od rundy 1 zdjęcie 2522 (cała ścianka, bez ludzi); 2322 nie ma na stronie.”
  - (2) Punkt o kafelkach zmienić na: „Na 390 px kafelki liczb w hero układają się 2 + 1 jak u sióstr (podpis „minimum 100 zł”).”
  - (3) W tabelach wpisać wartości z sekcji „Stan strony po rundzie 2”.
  - (4) Przy s06 dopisać, że galeria ma 2066 zamiast 2520.
- `praca/marketing/linki.md`: anchor #3 to teraz „Grawer laserowy”, a kotwica karty 2 do `#event` brzmi „Ścianki i dekoracje na event”. Adresy bez zmian.
- `praca/marketing/sklad.html` i zrzuty `sklad-*.png` nadal pokazują wersję sprzed rundy 1. Aktualny podgląd jest w `red-marketing-r2/po.html` i `po-*.png`.
