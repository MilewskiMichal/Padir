# Grawerowanie laserowe: poprawki po rundzie 2 weryfikacji

Plik strony: `praca/grawerowanie/strona.html`. Zaktualizowane też `tresc.md` (teksty 1:1 ze stroną, opisy zdjęć,
uwagi do składu, tabela linków, liczba słów 1372 → 1351, ramki bez zmian: 7, 260 słów), `ksiega.json`
(171 → 173 wpisy: 5 dodanych, 3 usunięte, 12 zmienionych) i `sklad-notatki.md` (sekcja 08, o co prosiła uwaga 2,
przy okazji nieaktualny opis sekcji 07 i wiersz z wynikiem kontroli).

Kontrola: `python3 -I sprawdz_szkic.py praca/grawerowanie/strona.html --szkic` kończy się kodem **0**
(0 błędów, 0 ostrzeżeń, 80 499 zn., 1567 słów razem z ramkami, 32 zdjęcia, 1 × h1, 7 ramek).
Na stronie nie ma pauzy, półpauzy, znaku minus (U+2014, U+2013, U+2212) ani `&&`.

Księga: skrypt `red-r2/popraw_ksiege.py` po zapisie sprawdza każdy cytat w jego pliku źródłowym, a wpisy
„DO POTWIERDZENIA” w ramkach strony. Wynik: 0 cytatów bez pokrycia. `red-r2/zgodnosc.py` sprawdza, czy każdy wiersz
`> ` z `tresc.md` stoi na stronie. Nie zgadzają się tylko dwa wiersze z konwencji liczenia słów, tak samo jak przed
tą rundą: etykiety formularza (generuje je CF7) i ostatnia karta galerii, w której plakietka stoi w DOM przed tytułem.

Render w ramie motywu (Chromium, Poppins z plików, skrypty `red-r2/render.py` i `red-r2/linie.py`): przy 1440,
1280, 1100, 1024, 768, 390, 360 i 320 px nie ma poziomego przewijania (scrollWidth = szerokość okna) ani elementów
wystających poza ekran. Pomiary: `red-r2/pomiar.json`. Zrzuty: `red-r2/r2-1440-zastosowania.png`,
`r2-768-zastosowania.png`, `r2-390-zastosowania.png`, `r2-1440-technologia.png`, `r2-390-realizacje.png`,
`r2-*-proces.png`, `r2-*-materialy.png`. Kopie plików sprzed rundy: `red-r2/*-przed-r2.*`.

Wynik: wszystkie 17 uwag wprowadzone, w tym #3 i #4 jedną zmianą, bo dotyczą tego samego przycisku. Dwie
z drobną zmianą wariantu (#4: wybrany napis; #9: brzmienie H2). Żadna nie została odrzucona w całości.

---

## Uwagi po kolei

### 1. [fakty, ważny] Alt zdjęcia parku maszyn: „Aluminiowe szablony”
**Wprowadzona.** Sprawdzone: jedyny opis pliku w serwisie to `pages-2264-…raw.html`,
`alt="Detal po obróbce CNC w pracowni Padir"`, w `media.json` (2279) alt jest pusty. „Aluminiowe” pochodziło tylko
z `zdjecia.json`, czyli z oceny wzrokowej. Kadr obejrzałem (`wer-fakty-r2-0060.png` i własna kontaktówka
`red-r2/kont-r2.png`). Widać blachę z zagiętymi uszami, wiercone otwory, brązowe napisy „C,D - otwory do szuflad
z frontami nakładanymi”, „E - otwory do szuflad z frontami wpuszczanymi” i punkt wiązki. Materiału nie da się
rozstrzygnąć, „metalowe” widać. Teza weryfikatora, że brązowy ślad wskazuje na stal, jest tylko domysłem, ale nie
ma wpływu na poprawkę.
Nowy alt (strona i `tresc.md`): „Metalowe szablony z grawerowanymi oznaczeniami otworów pod szuflady, w trakcie
znakowania laserem”. Księga: nowy wpis w sekcji „09 technologia” z cytatem altu ze strony przemysłowej
i adnotacją, że materiału nie podajemy (tak jak przy WBET).

### 2. [wzorzec, drobny] Linki w kartach zastosowań nie stoją u dołu karty
**Wprowadzona.** Sposób sprawdzony we wzorcu: `09-technologia.html`, karta
`display: flex; flex-direction: column;` i blok parametrów z `margin-top: auto`. W 4 kartach: kontener
`… overflow: hidden; display: flex; flex-direction: column;`, blok tekstu
`padding: 24px 26px 26px; flex: 1 1 auto; display: flex; flex-direction: column;`, a link zaczyna styl od
`align-self: flex-start; margin-top: auto;`. Opis zachował `margin: 0px 0px 14px`. Zmiana objęła tylko sekcję
zastosowań (skrypt zamienia wyłącznie w jej obrębie, 4 trafienia); karty materiałów nie mają linków i zostały bez
zmian. Arkusz dodatków bez zmian.
Pomiar po zmianie: każdy z 4 linków kończy się 26 px nad dołem karty przy 1440, 1280, 1100, 1024, 768, 390, 360
i 320 px. Wcześniej przy 1440 link „Noże z grawerem” był 21 px wyżej od pozostałych (zrzut
`red-r2/r2-1440-zastosowania.png`). Opis dopisany w `tresc.md` (sekcja 08) i w `sklad-notatki.md` (sekcja 08).

### 3. [wzorzec, drobny] Przycisk „Cała historia ramek dla WOŚP” łamie się na telefonie
**Wprowadzona.** Napis skrócony do „Cała historia ramek”, styl bez zmian. Pomiar: 221 × 53 px, jeden wiersz przy
1440, 1280, 1100, 1024, 768, 390 i 360 px (przed zmianą przy 390 px: 286 × 68 px, dwa wiersze). Zrzut
`red-r2/r2-390-realizacje.png`. `tresc.md`: tekst przycisku i tabela linków (anchor nr 6).

### 4. [technika, drobny] Ten sam przycisk: ciasne dwa wiersze przy line-height 1
**Wprowadzona** tą samą zmianą co #3.
**Odrzucony wariant:** „Zobacz pełny case” z 1019. Wybrałem „Cała historia ramek”, bo to link wewnętrzny,
a opisowy anchor mówi, dokąd prowadzi. Wzorcowy tekst jest ogólny i ma anglicyzm. Zostaje jedna rzecz: przy 320 px
(rodzic 216 px) przycisk nadal ma dwa wiersze, a „Zobacz pełny case” (209 px) zmieściłby się. Uwaga #4 sprawdzała
360 i 390 px, a 320 px to dziś rzadka szerokość. Jeśli klient chce wsparcia także dla niej, wystarczy podmienić napis.

### 5. [technika, drobny] Wartości parametrów maszyn łamią się między liczbą a jednostką
**Wprowadzona w całości, z częścią opcjonalną.** Spacje nierozdzielające w 13 wartościach: `726&nbsp;×&nbsp;432&nbsp;mm`,
`813&nbsp;×&nbsp;508&nbsp;mm`, `1300&nbsp;×&nbsp;900&nbsp;mm`, `2510&nbsp;×&nbsp;1680&nbsp;mm`, `do&nbsp;200&nbsp;mm`,
`do&nbsp;3,55&nbsp;m/s`, `od&nbsp;4&nbsp;pt`, `z&nbsp;4&nbsp;stron`, `25-120&nbsp;W`, 2 × `60-120&nbsp;W`, `180-500&nbsp;W`.
Styl spanów bez zmian.
Pomiar zakresami tekstu (`red-r2/linie.py`, liczba wierszy samego tekstu, bo wysokość spanu rozciąga flex):
przed zmianą przy 1440 i 1280 px łamało się 6 wartości, przy 1024 i 768 px 5, przy 1100 px „do 3,55 m/s”. Po zmianie
żadna wartość się nie łamie i żadna nie wychodzi poza kartę przy 1440, 1280, 1100, 1024, 768, 390, 360 i 320 px.
Łamią się tylko etykiety („Pole / robocze”, „Prędkość / graweru”), jak przewidział weryfikator. Zrzut
`red-r2/r2-1440-technologia.png`. Notatka o nbsp w `tresc.md` zaktualizowana.

### 6. [język, ważny] „Pojedyncze sztuki”: obietnica identycznej partii
**Wprowadzona.** Sprawdzone: karta Drewno mówi „Dwie sztuki z tym samym wzorem nie będą identyczne.”, a zdanie
z rundy 1 miało szkielet z `pages-8` („…trafiają do archiwum, więc dozamówienie po roku wygląda identycznie…”)
i z `pages-2283` („Archiwizujemy plik wzorcowy i parametry procesu dla każdego klienta, więc plakietka zamówiona po
roku wygląda identycznie…”). Nowy tekst: „Jedna obrączka czy jeden nóż to u nas zwykłe zlecenie. Plik i ustawienia
lasera zachowujemy. Przy kolejnym zamówieniu, nawet po roku, nie zaczynamy od zera.” Księga: wpis przepięty na
cytat z `pages-2283` („dla każdego klienta”, „po roku”), bo ten obejmuje też pojedyncze sztuki.

### 7. [język, ważny] Proces: „albo” w leadzie, „i” w kroku 03
**Wprowadzona.** Źródło (`pages-8`): „Przy seriach i przy nowych materiałach najpierw powstaje wzorzec do
akceptacji.”, czyli dwa osobne przypadki. Lead: „Cztery kroki od pliku do odbioru, przy jednej sztuce i przy
serii.” Krok 03: „Przy serii albo nowym materiale najpierw grawerujemy jedną sztukę. Resztę robimy, gdy
zaakceptujesz wzór, miejsce i głębokość.” Księga: wpis leadu zmieniony, wpis „Przy serii albo nowym materiale
dochodzi próbka” usunięty (tego zdania już nie ma), wpis kroku 03 z „albo”.

### 8. [język, drobny] Skóra i Drewno: ten sam szkielet „Grawer … wychodzi ciemniejszy od …”
**Wprowadzona.** Skóra: „Laser zostawia na licu ciemniejszy odcisk. Sprawdza się na etui, okładkach notesów
i podkładkach.” Źródło: `posts-2177` „Ciemniejszy odcisk wpisany w materiał.” Karta Drewno bez zmian. Na stronie
nie ma już „przyciemnionymi”. Zostają „ciemnieje” w leadzie i po jednym „ciemniejszy” w dwóch kartach, za każdym
razem w innej budowie zdania. Księga: wpis Skóry zmieniony, dwa wpisy o „przyciemnionych krawędziach” usunięte.

### 9. [język, drobny] Zastosowania: H2 „Dla kogo grawerujemy” i lead
**Wprowadzona z poprawką.** Sprawdzone: fragment „ma u nas osobną stronę z” stoi w `pages-8-produkty.txt`
i `pages-1011-frezowanie-cnc.txt`, lead powtarzał czasownik z H2. Lead (jak w propozycji): „Każda z czterech kart
prowadzi do osobnej strony z przykładami.”
**Odrzucony wariant:** H2 „Grawer w firmie i na prezent”. „W firmie” brzmi jak miejsce wykonania graweru.
Dałem „Grawer dla firm i na prezent”, które obejmuje obie grupy kart. „Dla firm” ma źródło w `pages-1397`
(„Pracujemy dla marek i agencji, hoteli i restauracji, producentów…”), „na prezent” to opublikowana strona 1812
„Grawerowanie na prezent” (nowy wpis w księdze z `SPIS.json`). W tej sekcji nie było „id”, kotwice bez zmian.

### 10. [język, drobny] Speedy 300 podaje 200 mm dwa razy, Speedy 360 „w wersji z opcją”
**Wprowadzona.** Speedy 300: „Personalizacja i drobne detale, także na wysokich przedmiotach.” (liczba zostaje
w wierszu „Wys. materiału / do 200 mm”). Speedy 360: „Grawer średniego formatu, w wersji flexx.” Źródło
(`pages-1019`): „Szybki grawer średniego formatu z opcją flexx.” „W wersji flexx” znaczy to samo, a nie przepisuje
zdania wzorca. Ramka pod kartami pyta nadal o flexx słowami źródła. Księga: oba wpisy zmienione, cytaty bez zmian.

### 11. [język, drobny] FAQ „Ile się czeka na grawer?”: „terminy … termin”, dwa „więc”
**Wprowadzona.** Ostatnie zdanie: „Przed świętami, w listopadzie i grudniu, czeka się dłużej, a dokładny termin
podamy przy wycenie.” Na stronie (bez ramek) „więc” pada teraz 3 razy zamiast 5. Księga: wpis zmieniony, cytat
z `posts-2177` („kolejka jest dłuższa”) bez zmian.

### 12. [język, drobny] FAQ 1: „sam uchwyt kosztowałby”
**Wprowadzona.** Sprawdzone w `pages-8`: „…bo poniżej tej liczby przygotowanie uchwytu kosztuje więcej niż sama
praca.” Nowe zdanie: „Wyjątkiem jest szkło: przyjmujemy je od 12 sztuk, bo przy mniejszej liczbie przygotowanie
uchwytu kosztowałoby więcej niż praca lasera.” Księga: wpis zmieniony.

### 13. [język, drobny] Case study, Efekt: elipsa orzeczenia przy różnej liczbie
**Wprowadzona.** „Oprawione rysunki miały trafić na licytację, a cały dochód z niej miał wesprzeć onkologię
i hematologię dziecięcą. Ramki i grawer wykonaliśmy bezpłatnie.” „Miał wesprzeć” zachowuje czas ze źródła
(`pages-12`: „zostanie przekazany na wsparcie onkologii i hematologii dziecięcej”). Księga: wpis zmieniony.

### 14. [język, drobny] Case study, lead „krok po kroku”
**Wprowadzona.** „Jedno zlecenie opisane od wyzwania do efektu.” Zgadza się z trzema blokami karty
i z leadem 1019 („…wyzwanie, rozwiązanie i efekt…”), ale go nie kopiuje.

### 15. [język, drobny] Lead nad formularzem: „plik albo zdjęcie przedmiotu”
**Wprowadzona.** „Prześlij plik albo zdjęcie znaku i napisz, na czym ma być grawer i ile sztuk potrzebujesz. Cenę
i termin podamy w ciągu 24 godzin.” Teraz zgadza się z krokiem 01 i kartą „Wystarczy zdjęcie logo”. Zdjęcie
przedmiotu jako pytanie o wykonalność zostaje w ciemnym pasie „Nie wiesz, czy da się to wygrawerować?”. Księga:
nowy wpis „12 kontakt” z cytatem z `pages-8` („Jeśli masz tylko logo ze zdjęcia albo rysunek odręczny, odtworzymy
plik u siebie.”).

### 16. [zdjęcia, drobny] Karta „Noże”: drugi raz znak „Whiskey in the Jar”
**Wprowadzona.** Sprawdzone: nóż 1450 i łyżka w galerii mają ten sam znak WHISKEY IN THE JAR (`wer-zdj-4.png`, kafle
#3 i #10). `zdjecia.json` sam ostrzega przy 1450. Zamiennik 2230 jest w `zdjecia.json` jako zatwierdzony,
praca_padir „tak”, i stoi na opublikowanej stronie noży (`pages-2228-…raw.html`, `uag-image-2230`). Plik
`…-768x1365.jpeg` odpowiada HTTP 200 i jest w `media.json` jako `url_medium`. Obejrzałem go na własnej kontaktówce
(`red-r2/kont-r2.png`) i w kaflu 16:10 na `wer-zdjecia-r2-alternatywy.png`. W renderze 1440 i 768 px środek kadru
pokazuje czarną głownię z całym białym napisem GRZYB (`r2-1440-zastosowania.png`, `r2-768-zastosowania.png`).
Nowy `<img>` dokładnie jak w propozycji (alt „Czarny nóż składany z grawerowanym napisem GRZYB na głowni”,
`loading="lazy" decoding="async" data-pdw-zoom`). Opis karty: „Imię, logo albo monogram na głowni lub rękojeści. Jeden
nóż na prezent albo seria z logo marki.” Koszt zmiany: to zdjęcie z telefonu na tekturze (jakość 3 zamiast 4), ale
w kaflu jest ostre, a karta pokazuje inny rodzaj zlecenia (napis osobisty na czarnej powłoce zamiast logo).
`tresc.md` (karta 4) i księga zaktualizowane: wpis zdjęcia z cytatem z `pages-2228`, nowy wpis „Noże: imię” z cytatem
„Imię, data lub krótka dedykacja sprawiają, że zwykły przedmiot zyskuje osobisty wymiar.”

### 17. [zdjęcia, drobny] Karta metalu: opis nie wspomina pendrive’a ze zdjęcia
**Wprowadzona.** Zdjęcie 1614 obejrzane (`red-r2/kont-r2.png`): polerowany pendrive z ciemnym napisem „Ewa”.
Źródło: `posts-1546` „Powerbanki, Kable USB i Pendrive’y z Grawerem”. Opis: „Noże, sztućce, zegarki, pendrive’y,
panele i tabliczki. Metal znakujemy laserem fiber. Najmocniejszy kontrast daje czarna powłoka proszkowa, spod której
wychodzi jasny metal.” Zdjęcie i alt bez zmian. `tresc.md` (karta 2) i nowy wpis w księdze.

---

## Pliki zmienione w tej rundzie

- `praca/grawerowanie/strona.html`: wszystkie zmiany opisane wyżej (skrypt `red-r2/popraw_strone.py`, każda zamiana
  z kontrolą liczby trafień).
- `praca/grawerowanie/tresc.md`: teksty 1:1 ze stroną, opisy zdjęć 2230 i 2279, notatki „Runda 2”, nbsp, tabela linków,
  liczba słów 1351 (skrypt `red-r2/popraw_tresc.py`, liczenie `red-r2/licz_slowa.py`, ta sama metoda co 1372).
- `praca/grawerowanie/ksiega.json`: 173 wpisy. Dodane: zdjęcie parku (09), pendrive’y (03), „na prezent” (08),
  „Noże: imię” (08), kontakt „zdjęcie znaku” (12). Usunięte: dwa wpisy o przyciemnionych krawędziach skóry, lead
  procesu o próbce. Zmienione: karta „Pojedyncze sztuki”, Skóra, lead i krok 03 procesu, Efekt WOŚP, H2 i lead
  zastosowań, zdjęcie noża, Speedy 300, Speedy 360, FAQ 1, FAQ 2.
- `praca/grawerowanie/sklad-notatki.md`: sekcja 08 (link przypięty do dołu karty, aktualny styl linku i siatki),
  sekcja 07 (dwa kafle 3:4, bez 1740, nowy napis przycisku), wiersz z wynikiem kontroli.
- Skrypty i dowody: `red-r2/` w katalogu roboczym.
