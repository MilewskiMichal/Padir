# Artykuł nr 6 do WhitePress: dane do wklejenia

Plik generowany przez `zrodla/zbuduj.py`. Nie edytuj go ręcznie, popraw `zrodla/tresc.html` i uruchom skrypt ponownie.

Długości: treść 6401 znaków ze spacjami (sama treść, bez tytułu i leadu), z tytułem i leadem 6806; tytuł 78 znaków; lead 327 znaków; uwagi dla wydawcy 1513 znaków (wersja krótka 359).

## Tytuł

```
Wycinanie laserem z plexi i sklejki: jak przygotować plik, żeby nie przepłacić
```

## Lead

```
Za wycinanie laserem płaci się głównie za czas pracy maszyny, a ten w dużej mierze zależy od pliku. Te same litery z plexi mogą kosztować więcej tylko dlatego, że w projekcie zostały zdublowane linie albo niepotrzebne detale. Pokazujemy, co podnosi koszt, jak przygotować projekt i czego spodziewać się po plexi, sklejce i MDF.
```

## Treść (HTML, do trybu źródła / HTML w edytorze)

Bez obrazów: obrazy wstawia wydawca według tabeli niżej.

```html
<h2>Za co płacisz przy cięciu laserem</h2>

<p>Laser nie potrzebuje wykrojnika ani formy. Nie płacisz więc za narzędzie, tylko za materiał, przygotowanie pliku i czas pracy maszyny. Ten czas zależy od kilku rzeczy, na które masz wpływ już przy projektowaniu:</p>

<ul>
<li>długości wszystkich linii cięcia, bo każdy ażur, ząbek i ozdobnik to dodatkowa droga dla głowicy,</li>
<li>liczby kształtów i otworów, bo przy każdym z nich laser zaczyna cięcie od nowa,</li>
<li>grubości materiału, bo grubszą płytę laser tnie wolniej, a czasem w dwóch przejściach,</li>
<li>powierzchni graweru, bo wypełnienie dużego pola trwa dłużej niż samo cięcie konturu,</li>
<li>zdublowanych linii, przez które laser tnie to samo miejsce dwa razy.</li>
</ul>

<p>Do tego dochodzi materiał. Często liczy się go w całych arkuszach albo ich częściach, więc znaczenie ma też to, ile elementów zmieści się na jednej płycie.</p>

<h2>Plik, który nie podnosi ceny</h2>

<p>Do cięcia potrzebny jest wektor, czyli rysunek zapisany jako linie, a nie piksele. Pracownie przyjmują zwykle pliki DXF, SVG, AI, CDR albo PDF wyeksportowany z programu do grafiki wektorowej. Zdjęcie albo zrzut ekranu trzeba najpierw przerysować, a to osobna praca.</p>

<p>Zanim wyślesz plik, sprawdź w nim kilka rzeczy:</p>

<ul>
<li>wymiary 1:1 w milimetrach, takie, jakie ma mieć gotowy element,</li>
<li>zamknięte kontury, bo przez przerwę w linii element nie wypadnie z arkusza,</li>
<li>brak zdublowanych linii, które powstają często przy kopiowaniu i łączeniu obiektów,</li>
<li>teksty zamienione na krzywe,</li>
<li>osobne kolory albo warstwy dla cięcia, graweru i płytkiego nacinania.</li>
</ul>

<p>W wielu pracowniach najcieńsza czerwona linia oznacza cięcie, ale zanim wyślesz plik, zapytaj wykonawcę, jak on to oznacza. Uważaj też na napisy, które mają być otworem w płycie, jak w szablonie albo ażurowym panelu. Środki liter O, A czy R wypadną wtedy razem z resztą. Można dodać cienkie mostki, przykleić płytę na podkład albo zostawić te miejsca jako grawer.</p>

<p>Najdrobniejsze detale też mają swoją granicę. Zwykle przyjmuje się, że żaden fragment nie powinien być węższy niż grubość materiału. Cienki mostek w sklejce 6 mm łatwo przypalić albo złamać przy wyjmowaniu.</p>

<h2>Plexi, sklejka czy MDF</h2>

<p>Plexi, czyli akryl, tnie się na gładką, prawie polerowaną krawędź. Gotowy element nie wymaga szlifowania, dlatego z plexi robi się litery, standy i statuetki. Jeśli na tym samym elemencie ma być grawer, lepiej sprawdza się plexi lana, bo daje wyraźniejszy, mleczny znak niż ekstrudowana.</p>

<p>Sklejka ma ciepły, naturalny wygląd, a jej krawędź po cięciu jest ciemna i lekko przypalona. Im grubsza płyta, tym ciemniejsza krawędź i wolniejsze cięcie. Liczy się też jakość arkusza: sęki i klej w środkowych warstwach potrafią zostawić miejsca, w których laser nie przetnie płyty do końca. Dlatego pracownie wolą sprawdzone płyty, często brzozowe.</p>

<p>MDF jest tani i równy, ale jego krawędź po cięciu nie wygląda idealnie. Jest ciemna i potrafi się lekko strzępić, więc MDF najlepiej sprawdza się tam, gdzie element i tak będzie malowany albo oklejony. Przy drewnie i MDF dym zostawia też wokół cięcia jasnobrązowy nalot. Jeśli powierzchnia ma zostać surowa, zapytaj, czy pracownia zabezpiecza płytę folią albo czyści elementy po cięciu.</p>

<p>Jak pod laserem zachowują się <a href="https://grawerowanie-laserowe.pl/blog/wycinanie-laserowe-precyzyjne-ciecie-plexi-sklejki-i-laminatu-na-zamowienie/">plexi, sklejka i laminat</a> i w jakich grubościach zwykle się je tnie, opisuje osobny poradnik.</p>

<h2>Wpusty, zatrzaski i szczelina cięcia</h2>

<p>Laser nie tnie linią o zerowej grubości. Wiązka odparowuje wąski pas materiału, tak zwaną szczelinę cięcia. To zwykle ułamek milimetra, zależnie od materiału i grubości. Przy pojedynczych literach nie ma to znaczenia. Przy elementach składanych na wcisk, jak modele z zębatkami czy pudełka na wpusty, ta różnica decyduje, czy części wejdą w siebie ciasno, luźno, czy wcale.</p>

<p>Jeśli projektujesz takie połączenia, napisz o tym w zamówieniu. Pracownia może dopasować wymiary wpustów do swojego materiału albo najpierw wyciąć próbny fragment. To kosztuje mniej niż cała seria do poprawki.</p>

<h2>Rozkrój, czyli więcej elementów z jednej płyty</h2>

<p>Przy serii opłaca się ułożyć elementy na arkuszu jak najciaśniej. Takie układanie, nazywane rozkrojem, robi zwykle pracownia, ale możesz jej pomóc już w projekcie. Nie zaokrąglaj narożników bez potrzeby i daj znać, czy kierunek słojów sklejki ma znaczenie. Prostokątne elementy da się czasem ustawić tak, żeby miały wspólną krawędź, a wtedy laser tnie jedną linię zamiast dwóch. Przy powtarzalnych seriach, które branża nazywa czasem wykrawaniem laserowym, dobry rozkrój wyraźnie zmniejsza zużycie materiału.</p>

<p>Element większy niż stół lasera da się podzielić na moduły i połączyć po obróbce. Warto to zaplanować w projekcie, żeby łączenia wypadły tam, gdzie będą najmniej widoczne.</p>

<h2>Czego laserem się nie tnie</h2>

<p>Laser CO2 nie zastąpi każdej maszyny. Bardzo grube płyty i obróbka przestrzenna to zadanie dla frezarki CNC. PVC odpada ze względów bezpieczeństwa, bo przy cięciu wydziela związki chloru, szkodliwe dla ludzi i dla maszyny. Przy nietypowym tworzywie zapytaj przed wyceną, czy w ogóle nadaje się pod laser.</p>

<h2>Ile to kosztuje i ile trwa</h2>

<p>Ponieważ nie trzeba robić formy, opłaca się nawet pojedyncza sztuka albo prototyp. Pracownie mają za to zwykle minimalną kwotę zlecenia. Drobne, proste elementy to często kilka minut pracy lasera, a termin zależy przede wszystkim od kolejki i wielkości serii.</p>

<p>Przykład z Warszawy: <a href="https://grawerowanie-laserowe.pl/">pracownia Padir</a> z Targówka ma w jednej hali pięć laserów CO2 marki Trotec, od formatu A4 po arkusze ponad 2,5 m. Największe pole robocze to 2510 × 1680 mm, a tolerancja cięcia sięga 0,1 mm. Plexi tnie zwykle w grubościach 2-10 mm, a sklejkę i MDF w grubościach 3-12 mm. Cięcie i grawerowanie laserem łączy w jednym zleceniu, na przykład wycina tabliczkę i od razu nanosi na nią opis. Zlecenia przyjmuje od jednej sztuki, najniższa kwota zamówienia to 100 zł, a mniejsze zlecenia są zwykle gotowe w około dwa dni robocze. Ofertę na <a href="https://grawerowanie-laserowe.pl/wycinanie-laserowe/">wycinanie laserem</a>, z galerią realizacji i opisem maszyn, pokazuje na osobnej stronie.</p>

<h2>Lista kontrolna przed wysłaniem pliku</h2>

<ul>
<li>Wektor w skali 1:1, wymiary w milimetrach.</li>
<li>Zamknięte kontury, bez zdublowanych linii, teksty zamienione na krzywe.</li>
<li>Cięcie, grawer i nacinanie rozdzielone kolorami albo warstwami.</li>
<li>Detale nie węższe niż grubość materiału, środki liter w otworach rozwiązane mostkami albo podkładem.</li>
<li>Materiał i grubość, a przy plexi także kolor i rodzaj: lana czy ekstrudowana.</li>
<li>Liczba sztuk i informacja, czy są elementy składane na wcisk.</li>
</ul>

<p>Z takim plikiem wycena jest szybka, a cena nie rośnie przez rzeczy, których nie widać na pierwszy rzut oka.</p>
```

## Treść (czysty tekst, gdy edytor nie ma trybu HTML)

Wiersz zaczynający się od `[H2] ` to śródtytuł: usuń znacznik `[H2] ` i ustaw wiersz jako nagłówek H2, bez zmiany liter. Wiersze zaczynające się od `- ` zamień na listę punktowaną. Linki ustaw ręcznie według tabeli „Linki”.

```
[H2] Za co płacisz przy cięciu laserem

Laser nie potrzebuje wykrojnika ani formy. Nie płacisz więc za narzędzie, tylko za materiał, przygotowanie pliku i czas pracy maszyny. Ten czas zależy od kilku rzeczy, na które masz wpływ już przy projektowaniu:

- długości wszystkich linii cięcia, bo każdy ażur, ząbek i ozdobnik to dodatkowa droga dla głowicy,
- liczby kształtów i otworów, bo przy każdym z nich laser zaczyna cięcie od nowa,
- grubości materiału, bo grubszą płytę laser tnie wolniej, a czasem w dwóch przejściach,
- powierzchni graweru, bo wypełnienie dużego pola trwa dłużej niż samo cięcie konturu,
- zdublowanych linii, przez które laser tnie to samo miejsce dwa razy.

Do tego dochodzi materiał. Często liczy się go w całych arkuszach albo ich częściach, więc znaczenie ma też to, ile elementów zmieści się na jednej płycie.

[H2] Plik, który nie podnosi ceny

Do cięcia potrzebny jest wektor, czyli rysunek zapisany jako linie, a nie piksele. Pracownie przyjmują zwykle pliki DXF, SVG, AI, CDR albo PDF wyeksportowany z programu do grafiki wektorowej. Zdjęcie albo zrzut ekranu trzeba najpierw przerysować, a to osobna praca.

Zanim wyślesz plik, sprawdź w nim kilka rzeczy:

- wymiary 1:1 w milimetrach, takie, jakie ma mieć gotowy element,
- zamknięte kontury, bo przez przerwę w linii element nie wypadnie z arkusza,
- brak zdublowanych linii, które powstają często przy kopiowaniu i łączeniu obiektów,
- teksty zamienione na krzywe,
- osobne kolory albo warstwy dla cięcia, graweru i płytkiego nacinania.

W wielu pracowniach najcieńsza czerwona linia oznacza cięcie, ale zanim wyślesz plik, zapytaj wykonawcę, jak on to oznacza. Uważaj też na napisy, które mają być otworem w płycie, jak w szablonie albo ażurowym panelu. Środki liter O, A czy R wypadną wtedy razem z resztą. Można dodać cienkie mostki, przykleić płytę na podkład albo zostawić te miejsca jako grawer.

Najdrobniejsze detale też mają swoją granicę. Zwykle przyjmuje się, że żaden fragment nie powinien być węższy niż grubość materiału. Cienki mostek w sklejce 6 mm łatwo przypalić albo złamać przy wyjmowaniu.

[H2] Plexi, sklejka czy MDF

Plexi, czyli akryl, tnie się na gładką, prawie polerowaną krawędź. Gotowy element nie wymaga szlifowania, dlatego z plexi robi się litery, standy i statuetki. Jeśli na tym samym elemencie ma być grawer, lepiej sprawdza się plexi lana, bo daje wyraźniejszy, mleczny znak niż ekstrudowana.

Sklejka ma ciepły, naturalny wygląd, a jej krawędź po cięciu jest ciemna i lekko przypalona. Im grubsza płyta, tym ciemniejsza krawędź i wolniejsze cięcie. Liczy się też jakość arkusza: sęki i klej w środkowych warstwach potrafią zostawić miejsca, w których laser nie przetnie płyty do końca. Dlatego pracownie wolą sprawdzone płyty, często brzozowe.

MDF jest tani i równy, ale jego krawędź po cięciu nie wygląda idealnie. Jest ciemna i potrafi się lekko strzępić, więc MDF najlepiej sprawdza się tam, gdzie element i tak będzie malowany albo oklejony. Przy drewnie i MDF dym zostawia też wokół cięcia jasnobrązowy nalot. Jeśli powierzchnia ma zostać surowa, zapytaj, czy pracownia zabezpiecza płytę folią albo czyści elementy po cięciu.

Jak pod laserem zachowują się plexi, sklejka i laminat i w jakich grubościach zwykle się je tnie, opisuje osobny poradnik.

[H2] Wpusty, zatrzaski i szczelina cięcia

Laser nie tnie linią o zerowej grubości. Wiązka odparowuje wąski pas materiału, tak zwaną szczelinę cięcia. To zwykle ułamek milimetra, zależnie od materiału i grubości. Przy pojedynczych literach nie ma to znaczenia. Przy elementach składanych na wcisk, jak modele z zębatkami czy pudełka na wpusty, ta różnica decyduje, czy części wejdą w siebie ciasno, luźno, czy wcale.

Jeśli projektujesz takie połączenia, napisz o tym w zamówieniu. Pracownia może dopasować wymiary wpustów do swojego materiału albo najpierw wyciąć próbny fragment. To kosztuje mniej niż cała seria do poprawki.

[H2] Rozkrój, czyli więcej elementów z jednej płyty

Przy serii opłaca się ułożyć elementy na arkuszu jak najciaśniej. Takie układanie, nazywane rozkrojem, robi zwykle pracownia, ale możesz jej pomóc już w projekcie. Nie zaokrąglaj narożników bez potrzeby i daj znać, czy kierunek słojów sklejki ma znaczenie. Prostokątne elementy da się czasem ustawić tak, żeby miały wspólną krawędź, a wtedy laser tnie jedną linię zamiast dwóch. Przy powtarzalnych seriach, które branża nazywa czasem wykrawaniem laserowym, dobry rozkrój wyraźnie zmniejsza zużycie materiału.

Element większy niż stół lasera da się podzielić na moduły i połączyć po obróbce. Warto to zaplanować w projekcie, żeby łączenia wypadły tam, gdzie będą najmniej widoczne.

[H2] Czego laserem się nie tnie

Laser CO2 nie zastąpi każdej maszyny. Bardzo grube płyty i obróbka przestrzenna to zadanie dla frezarki CNC. PVC odpada ze względów bezpieczeństwa, bo przy cięciu wydziela związki chloru, szkodliwe dla ludzi i dla maszyny. Przy nietypowym tworzywie zapytaj przed wyceną, czy w ogóle nadaje się pod laser.

[H2] Ile to kosztuje i ile trwa

Ponieważ nie trzeba robić formy, opłaca się nawet pojedyncza sztuka albo prototyp. Pracownie mają za to zwykle minimalną kwotę zlecenia. Drobne, proste elementy to często kilka minut pracy lasera, a termin zależy przede wszystkim od kolejki i wielkości serii.

Przykład z Warszawy: pracownia Padir z Targówka ma w jednej hali pięć laserów CO2 marki Trotec, od formatu A4 po arkusze ponad 2,5 m. Największe pole robocze to 2510 × 1680 mm, a tolerancja cięcia sięga 0,1 mm. Plexi tnie zwykle w grubościach 2-10 mm, a sklejkę i MDF w grubościach 3-12 mm. Cięcie i grawerowanie laserem łączy w jednym zleceniu, na przykład wycina tabliczkę i od razu nanosi na nią opis. Zlecenia przyjmuje od jednej sztuki, najniższa kwota zamówienia to 100 zł, a mniejsze zlecenia są zwykle gotowe w około dwa dni robocze. Ofertę na wycinanie laserem, z galerią realizacji i opisem maszyn, pokazuje na osobnej stronie.

[H2] Lista kontrolna przed wysłaniem pliku

- Wektor w skali 1:1, wymiary w milimetrach.
- Zamknięte kontury, bez zdublowanych linii, teksty zamienione na krzywe.
- Cięcie, grawer i nacinanie rozdzielone kolorami albo warstwami.
- Detale nie węższe niż grubość materiału, środki liter w otworach rozwiązane mostkami albo podkładem.
- Materiał i grubość, a przy plexi także kolor i rodzaj: lana czy ekstrudowana.
- Liczba sztuk i informacja, czy są elementy składane na wcisk.

Z takim plikiem wycena jest szybka, a cena nie rośnie przez rzeczy, których nie widać na pierwszy rzut oka.
```

## Linki (3, wszystkie dofollow, w kolejności ważności)

| # | Anchor (dokładnie) | Adres | Rodzaj |
|---|---|---|---|
| 1 | „wycinanie laserem” | https://grawerowanie-laserowe.pl/wycinanie-laserowe/ | fraza |
| 2 | „pracownia Padir” | https://grawerowanie-laserowe.pl/ | marka, strona główna |
| 3 | „plexi, sklejka i laminat” | https://grawerowanie-laserowe.pl/blog/wycinanie-laserowe-precyzyjne-ciecie-plexi-sklejki-i-laminatu-na-zamowienie/ | opisowy |

## Zdjęcie główne

`zdjecia/zdjecie-glowne-napis-tea-plexi-lustrzana-padir.jpg`, alt: Przestrzenny napis Tea wycięty laserem z lustrzanej plexi na sklejce, podpis: Napis z lustrzanej plexi na sklejce, wycięty laserem. Fot. Padir

## Obrazy w treści (jako załączniki)

| Klucz | Plik | Gdzie w tekście | Alt | Podpis |
|---|---|---|---|---|
| ig1 | `infografiki/ig1-co-podnosi-cene-ciecia-laserem.png` | pod leadem, przed pierwszym śródtytułem „Za co płacisz przy cięciu laserem” | Infografika: sześć rzeczy, które podnoszą cenę cięcia laserem | Na większość tych kosztów masz wpływ już w pliku. Grafika: Padir |
| drzewko | `zdjecia/azurowe-drzewko-sklejka-padir.jpg` | w sekcji „Za co płacisz przy cięciu laserem”, zaraz pod listą punktowaną | Ażurowe drzewko z sowami wycięte laserem ze sklejki | Ażur ze sklejki: im więcej drobnych wycięć, tym dłużej pracuje laser. Fot. Padir |
| ig2 | `infografiki/ig2-plik-do-ciecia-lista-kontrolna.png` | na końcu sekcji „Plik, który nie podnosi ceny”, przed śródtytułem „Plexi, sklejka czy MDF” | Infografika: lista kontrolna pliku do cięcia laserem, z przykładem mostków w literze O | Co sprawdzić w pliku przed wysłaniem do cięcia. Grafika: Padir |
| ig3 | `infografiki/ig3-plexi-sklejka-mdf-krawedz.png` | na końcu sekcji „Plexi, sklejka czy MDF”, przed śródtytułem „Wpusty, zatrzaski i szczelina cięcia” | Infografika: jak po cięciu laserem wygląda krawędź plexi, sklejki, MDF i laminatu | Krawędź po cięciu zależy od materiału. Grafika: Padir |
| zebatki | `zdjecia/zebatki-sklejka-wpusty-padir.jpg` | na końcu sekcji „Wpusty, zatrzaski i szczelina cięcia”, przed śródtytułem „Rozkrój, czyli więcej elementów z jednej płyty” | Ruchomy model zębatek ze sklejki złożony na wpusty | Model zębatek ze sklejki, składany na wpusty. Fot. Padir |

## Uwagi dla wydawcy (pole „Uwagi” / „Komentarz do zamówienia”)

```
Dzień dobry, prosimy o publikację tekstu bez zmian w treści i w linkach. W artykule są 3 linki dofollow, prosimy zostawić je w podanym brzmieniu: „wycinanie laserem” https://grawerowanie-laserowe.pl/wycinanie-laserowe/; „pracownia Padir” https://grawerowanie-laserowe.pl/; „plexi, sklejka i laminat” https://grawerowanie-laserowe.pl/blog/wycinanie-laserowe-precyzyjne-ciecie-plexi-sklejki-i-laminatu-na-zamowienie/. Zdjęcie główne: zdjecie-glowne-napis-tea-plexi-lustrzana-padir.jpg. W załącznikach są 3 infografiki i 2 zdjęcia do wstawienia w tekst: ig1-co-podnosi-cene-ciecia-laserem.png pod leadem, przed pierwszym śródtytułem „Za co płacisz przy cięciu laserem”; azurowe-drzewko-sklejka-padir.jpg w sekcji „Za co płacisz przy cięciu laserem”, zaraz pod listą punktowaną; ig2-plik-do-ciecia-lista-kontrolna.png na końcu sekcji „Plik, który nie podnosi ceny”, przed śródtytułem „Plexi, sklejka czy MDF”; ig3-plexi-sklejka-mdf-krawedz.png na końcu sekcji „Plexi, sklejka czy MDF”, przed śródtytułem „Wpusty, zatrzaski i szczelina cięcia”; zebatki-sklejka-wpusty-padir.jpg na końcu sekcji „Wpusty, zatrzaski i szczelina cięcia”, przed śródtytułem „Rozkrój, czyli więcej elementów z jednej płyty”. W pliku artykul.docx pod każdym obrazem jest podpis (kursywą), a pod nim osobno tekst alternatywny (ALT), który nie jest częścią podpisu. Jeśli to możliwe, prosimy o powiększanie infografik po kliknięciu, bo na telefonie ich tekst jest drobny. Wszystkie zdjęcia i grafiki należą do zamawiającego (Padir). Dziękujemy.
```

## Uwagi dla wydawcy, wersja krótka (gdy pole ma limit znaków)

```
Dzień dobry, prosimy o publikację bez zmian w treści i w linkach (3 linki dofollow, anchory i adresy jak w tekście). Zdjęcie główne: zdjecie-glowne-napis-tea-plexi-lustrzana-padir.jpg. Obrazy z załączników prosimy wstawić w miejscach pokazanych w artykul.docx, tam są też teksty alternatywne i podpisy. Wszystkie zdjęcia i grafiki należą do Padir. Dziękujemy.
```
