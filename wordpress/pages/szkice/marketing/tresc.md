# Usługi dla marketingu: treść strony (autor tekstu, 13.10.2026)

Plik dla składacza `praca/marketing/strona.html`. Komponenty K1-K12 według `praca/marketing/wzorzec-pdl.md`
(arkusz z p. 2.1 bez zmian + dopisek z p. 2.4). Fakty wyłącznie z `praca/marketing/fakty.md` i od zleceniodawcy;
każde twierdzenie ma wpis w `praca/marketing/ksiega.json`. Zdjęcia wyłącznie z `praca/marketing/zdjecia.json`
(obejrzane przeze mnie na arkuszach `praca/marketing/autor/kont-a.png`, `kont-b.png` i w pełnym pliku INSOFT).

Konwencja zapisu:
- wiersze zaczynające się od `> ` to DOKŁADNY widoczny tekst do wklejenia; `<br>` = łamanie wiersza w nagłówku;
  `[anchor](/adres/)` = link w środku tekstu (w HTML: `<a href="/adres/">anchor</a>`);
- `&rarr;` w etykietach linków kart wstawia składacz, jak u sióstr (tu zapisane jako „→”);
- żadnych żółtych ramek ani napisu o wersji roboczej. Pytania do klienta są tylko w `praca/marketing/pytania.md`
  (sekcja „Autor tekstu”, A01-A05, oraz wcześniejsze P01-P32, L01-L04, W01-W02).

---

## 0. Meta

| pole | wartość |
|---|---|
| Tytuł strony w WordPressie i nazwa w menu „Produkty” | `Usługi dla marketingu` (po „Usługi dla HoReCa”) |
| Slug | `uslugi-dla-marketingu` |
| Szablon | `page-no-title`, status: szkic (zapisuje człowiek prowadzący) |
| Title SEO (53 znaki, wpisać ręcznie w pole SEO) | `Statuetki, puchary i upominki z logo dla firm \| Padir` |
| Meta description (152 znaki) | `Statuetki i nagrody z plexi, puchary, upominki z logo, napisy przestrzenne i dekoracje na event dla marek i agencji. Od 1 sztuki, wycena graweru w 24 h.` |

Redakcja, runda 1 (13.10.2026): zmiany z `praca/marketing/poprawki-r1.md` są już wpisane poniżej i w `ksiega.json`.
Wycena w 24 h tylko przy grawerze i statuetkach, bez ścianek i dekoracji (do odpowiedzi na A04).
Redakcja, runda 2 (13.10.2026): zmiany z `praca/marketing/poprawki-r2.md` są wpisane poniżej (notki „R2”) i w `ksiega.json`.

Mapa sekcji i teł (7 sekcji między hero a pasem, nieparzyście, zaczyna i kończy wash):

| s | id | tło | komponent | eyebrow |
|---|---|---|---|---|
| s00 | - | białe (hero) | K1 | Usługi dla marketingu |
| s01 | - | wash | K2 + K3 (3 karty) | Trzy światy |
| s02 | `zakres` | białe | K2 + K4 (5 + karta CTA) | Zakres |
| s03 | `nagrody` | wash | K7 `--rev` (zdjęcie z lewej) | Statuetki i nagrody |
| s04 | `event` | białe | K7 (zdjęcie z prawej) | Eventy i wnętrza |
| s05 | `upominki` | wash | K2 + K8 (6 kart) | Upominki z logo |
| s06 | - | białe | K2 + K9 (8 zdjęć + przycisk) | Realizacje |
| s07 | - | wash | K2 + K11 (7 pytań) | FAQ |
| s08 | - | białe | K12 pas | - |

Kotwice na stronie: `#zakres` (hero), `#upominki`, `#event`, `#nagrody` (karty K3). Każda ma swoje `id` w tabeli wyżej.
K5 (przed/po) i K6 (kroki) pomijam: pary zdjęć tego samego przedmiotu nie ma (W01), a kroki dublowałyby szkic
nowej strony grawerowania. K10 („Kto zamawia”) pomijam, bo trzy grupy odbiorców niesie już K3.

---

## s00. Hero (K1), `<section class="pdl-hero">`

- **Etykieta (eyebrow):**
  > Usługi dla marketingu
- **H1** (jedyny na stronie):
  > Statuetki, puchary<br>i upominki z logo.
- **Lead (`.pdl-lead`):**
  > Dla działów marketingu i agencji, które szykują galę albo upominki dla klientów.
- **Tekst (`.pdl-txt`):**
  > Lasery do graweru i cięcia oraz frezarka CNC stoją w naszej pracowni w Warszawie. Zamówisz u nas jedną statuetkę na jubileusz albo ściankę na firmowy event.

  (R1: bez kolejnych trójek pod H1 i bez „jednej pracowni”, która stoi w H2 sekcji s01.)
- **Przyciski:**
  - główny: > Wyceń zamówienie
    cel: `/kontakt/`
  - ghost: > Co robimy
    cel: `#zakres`
- **Liczby (`li.pdl-stat`, 3 sztuki: `<b>` / `<span>`):**
  > od 2002 roku
  > obrabiamy laserem
  > od 1 sztuki
  > minimum 100 zł
  > 24 h
  > na wycenę graweru

  (R1: krótszy podpis drugiego kafelka, żeby przy 390 px liczby układały się 2 + 1 jak u sióstr;
  „na wycenę graweru”, bo źródła dają 24 h tylko przy grawerze, A04. R2: „minimum 100 zł” zamiast „zlecenie od 100 zł”,
  bez drugiego „od” w kafelku; przy 390 i 360 px nadal 2 + 1.)
- **Zdjęcia** (kadr 3:4; w obu `loading="eager" fetchpriority="high" decoding="async" data-no-lazy="1"`):
  1. `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-statuetka-jubileuszowa-insoft.jpg`
     (pełny plik 750×1000, media 2340; `url_medium` ma tylko 225×300)
     alt: `Jubileuszowa statuetka z przezroczystej plexi ze złotą tabliczką INSOFT 25 lat`
     (alt z `zdjecia.json` kończy się „na 25-lecie firmy”; zgadza się to z tabliczką, ale serwis pisze tylko „INSOFT 25 lat”, więc alt trzyma się tego brzmienia; por. A02)
  2. `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-boko-slup-768x1024.jpg` (media 2525, zamiennik hero z `zdjecia.json`)
     alt: `Pionowe logo BOKO z pomarańczowych liter na lustrzanej plexi, na słupie w kawiarni`
     (R1: ścianka Bondi Sands 2522 przeszła do karty 3 w s01, bo tamten kadr 2322 pokazywał rozpoznawalną osobę (P32), a 2522
     stoi też w hero /wycinanie-laserowe/. Alt z `zdjecia.json` „na lustrzanym słupie” jest błędny: lustrzana jest tablica z plexi, słup jest biały.)
- **Linki:** `/kontakt/` („Wyceń zamówienie”), `#zakres` („Co robimy”).

---

## s01. Trzy światy (K2 + K3), `<section class="pdl-sec pdl-sec--wash">`

- **Etykieta:**
  > Trzy światy
- **H2:**
  > Firma, agencja, organizator.<br>Jedna pracownia.
- **Tekst nagłówka:**
  > Dział marketingu zamawia co innego niż agencja, a jeszcze co innego organizator konkursu.

  (R1: trzy grupy klientów jak „Hotel, restauracja, bar” na HoReCa; zdanie-zapowiedź usunięte.)

Karty (`article.pdl-card`, zdjęcie 4:3, `loading="lazy" decoding="async"`):

**Karta 1**
- zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/5-edited-768x768.webp` (media 1623)
  alt: `Matowa bordowa bombka z grawerem świątecznych życzeń od firmy`
  (własny upominek Padiru, bez podpisu „dla klienta”, R14)
- H3:
  > Działy marketingu firm
- tekst:
  > Upominki z logo dla kontrahentów i zespołu, statuetka na rocznicę firmy, logo przestrzenne do recepcji. Każdy upominek w serii może dostać imię odbiorcy.

  (R2: „rocznicę”, bo „na jubileusz” stało już w hero, w karcie Zakresu i w H2 #nagrody.)
- link:
  > Upominki z logo →
  cel: `#upominki`

**Karta 2**
- zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/08/IMG_7207-768x576.jpg` (media 2054)
  alt: `Ekspozytor kosmetyków z lustrzanej plexi i drewna w kształcie plastra miodu`
- H3:
  > Agencje reklamowe i eventowe
- tekst:
  > Ścianki fotograficzne, napisy przestrzenne i ekspozytory według projektu agencji. Cięcie i frezowanie zamawiasz w jednym zleceniu, z jedną fakturą.
- link:
  > Ścianki i dekoracje na event →
  cel: `#event`
  (R2: link brzmi jak nowy H2 sekcji #event.)

**Karta 3**
- zdjęcie: `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-bondi-plaza-768x960.jpg` (media 2522, pionowe 4:5),
  w `<img>` `style="object-position:50% 35%"` (w kadrze 4:3 cała ścianka z logo, bez ludzi)
  alt: `Złota lustrzana ścianka fotograficzna na letni event nad Wisłą`
  (R1: zamiast 2322, na którym głównym motywem był rozpoznawalny model z deską, zgoda niepewna: P32.)
  Uwaga: obie statuetki z galerii stoją już w hero (2340) i w sekcji nagród (2332), więc karta organizatorów ma zdjęcie
  ścianki. Gdy klient przyśle zdjęcie pucharu, trzeciej statuetki albo nagród na gali (P07, P26, P29, A05), podmienić tutaj.
- H3:
  > Organizatorzy gal i konkursów
- tekst:
  > Statuetki i puchary dla laureatów. Na samo wydarzenie zrobimy też ściankę do zdjęć.

  (R2: bez nakładu, bo „od jednej sztuki do całej serii” obejmowało też puchary, a nakłady pucharów to P01 i P04;
  „od 1 sztuki” zostaje w hero, a seria przy statuetkach w karcie Zakresu. Bez echa „gal i konkursów” z H3.)
- link:
  > Statuetki i puchary →
  cel: `#nagrody`

Linki sekcji: `#upominki`, `#event`, `#nagrody` (każda karta w inne miejsce, U12).

---

## s02. Zakres (K2 + K4), `<section class="pdl-sec" id="zakres">`

- **Etykieta:**
  > Zakres
- **H2:**
  > Wszystko, co marka<br>wręcza i pokazuje.
- **Tekst nagłówka:**
  > Pięć grup zamówień dla firm i agencji. Lasery CO₂ grawerują i tną plexi, drewno, skórę i papier, laser fiber znakuje metal, a grubsze płyty i litery przestrzenne obrabia frezarka CNC.

(R2: H2 w formule sióstr „Wszystko, co…”; wręcza: statuetki i upominki, pokazuje: napisy, ścianki, ekspozytory.
Poprzednie „Od statuetki po ściankę na event” powtarzało H3 karty 4 i H2 #event. „dla firm”, żeby nie stało „marka… marek” obok siebie.)

Karty (`article.pdl-p`: H3 `.pdl-h3`, tekst `.pdl-txt-sm`, lista `ul > li`):

**1.**
> Statuetki, puchary i nagrody
> Statuetkę zaprojektujemy na jubileusz firmy czy galę konkursu. Robimy też puchary.
> - Statuetki jubileuszowe, nagrody i wyróżnienia
> - Statuetki z plexi i drewna, wycinane i grawerowane
> - Jedna sztuka albo seria dla laureatów

(Bez materiałów pucharów, szkła i metalu przy statuetkach, nakładów i terminów: P01, P02, P04.)

**2.**
> Upominki i gadżety z logo
> Logo, imię albo życzenia na rzeczach, które dajesz klientom i pracownikom.
> - Kubki termiczne, szkło, noże, powerbanki
> - Skrzynki na wino, świece, notesy
> - Od jednej sztuki do dużej serii

**3.**
> Napisy, logo i oznakowanie
> Litery, logotypy i napisy przestrzenne z plexi albo sklejki. Plexi wychodzi spod lasera z gładką, błyszczącą krawędzią.
> - Do recepcji albo na stoisko
> - Pojedyncza litera albo cały napis
> - Oznakowanie wnętrz, np. „Tylko dla personelu”

(R2: gładka krawędź tylko przy plexi; wpis 2293 mówi o sklejce: „Grubsza sklejka zostawia ciemniejszą krawędź”.)

**4.**
> Ścianki i dekoracje eventowe
> Ścianki fotograficzne z płyt wielkoformatowych i dekoracje z plexi, sklejki i tkaniny. Duże formaty składamy z modułów.
> - Lustrzana plexi, także złota
> - Elementy gotowe do szybkiego montażu
> - Cięcie według projektu agencji albo klienta

(Bez montażu na miejscu i bez zabudowy stoisk: P15, P16. R1: bez „złoconych wykończeń”, bo czyta się to jak usługę złocenia;
złota jest lustrzana plexi. Innych kolorów plexi lustrzanej nie podajemy: pytanie R02. R2: H3 „eventowe” (2293: „dekoracje
eventowe”), żeby nie powtarzać „na event” z H2 #event; tak samo nazwa usługi w JSON-LD.)

**5.**
> Ekspozytory i opakowania
> Ekspozytory i standy POS na produkty oraz opakowania z wkładami. Przykłady opisaliśmy we wpisie o tym, [jak robimy ekspozycje dla marek kosmetycznych](/blog/tworzenie-ekspozycji-dla-marek-kosmetycznych/).
> - Plexi lustrzana, drewno, sklejka
> - Cięcie, gięcie plexi, klejenie i grawer logo
> - Prototyp albo makieta do akceptacji

(Bez PVC i poliwęglanu przy laserze, bez marek z wpisu 2043: S09, P14, P18.)

**Karta CTA (`.pdl-p pdl-p--cta`, ostatnia):**
> Masz tylko pomysł?
> Wystarczy szkic, zdjęcie podobnej rzeczy albo opis. Doradzimy materiał i przygotujemy plik do cięcia albo graweru.
> Opisz projekt →
cel linku: `/kontakt/`

Linki sekcji: `/blog/tworzenie-ekspozycji-dla-marek-kosmetycznych/` (anchor „jak robimy ekspozycje dla marek kosmetycznych”, linki.md #6), `/kontakt/` („Opisz projekt”).

---

## s03. Statuetki i nagrody (K7 `--rev`), `<section class="pdl-sec pdl-sec--wash" id="nagrody">`, `<div class="pdl-detail pdl-detail--rev">`

- **Etykieta:**
  > Statuetki i nagrody
- **H2:**
  > Statuetki z plexi<br>na galę i jubileusz.
- **Tekst:**
  > Kształt statuetki wycinamy laserem, a napisy grawerujemy. Na 25-lecie firmy INSOFT powstała statuetka z przezroczystej plexi ze złotą tabliczką. W wyróżnieniu z tańczącą parą sylwetkę wycięliśmy z czarnej plexi, a taflę pod nią z przezroczystej. Zamawiasz statuetki lub puchary? Napisz, ilu masz laureatów i kiedy wręczasz nagrody.

  (R1: bez „wyróżnienia tanecznego” i bez „dla tancerzy”, bo na tabliczce są osoby prywatne ze studia tańca, P31.
  R2: z czarnej plexi jest tylko sylwetka, tafla pod nią jest przezroczysta (kadr 2332; opis w `zdjecia.json` jest tu błędny).
  W HTML „25-lecie” jest w `<span style="white-space:nowrap">`, żeby wiersz nie łamał się na dywizie („Na 25-” / „lecie”).)
- **Lista z ptaszkami (`.pdl-checks`):**
  > - Kształt z sylwetką, logo albo motywem okazji
  > - Na każdej sztuce inne nazwisko, kategoria albo rok
  > - Grawer w przezroczystej plexi świeci, gdy podświetlisz ją od krawędzi
- **Przycisk:**
  > Zapytaj o statuetki
  cel: `/kontakt/`
- **Zdjęcie** (4:3, lazy): `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-statuetka-z-plexi.jpg` (pełny plik 900×600, media 2332)
  alt: `Wyróżnienie z przezroczystej plexi z czarną sylwetką pary tanecznej i okrągłą tabliczką`
  (na pełnym pliku czytelne imiona i nazwisko osób prywatnych, P31; w tekście ich nie podaję. R2: alt bez „czarnej plexi”
  jako materiału całości i bez „grawerowanej” tabliczki, bo źródła nie mówią, kto ją grawerował.)
- **Linki:** `/kontakt/`.

Uwagi do treści: nie kopiuję zdań z ramki „Nowość” na `/wycinanie-laserowe/` ani nagłówka „Tworzenie nagród
i statuetek”; nie piszę „nowość” ani „od lat” (S10). Pod tę sekcję ma później linkować ramka na 1019 (`#nagrody`, linki.md p. 4).

---

## s04. Eventy i wnętrza (K7), `<section class="pdl-sec" id="event">`, `<div class="pdl-detail">`

- **Etykieta:**
  > Eventy i wnętrza
- **H2:**
  > Ścianki i dekoracje<br>na event.
- **Tekst:**
  > Dla Bondi Sands wycięliśmy złotą lustrzaną ściankę fotograficzną na letni event nad Wisłą. Była gotowa na umówiony dzień. Litery i logo z plexi oraz sklejki tniemy laserem, a napisy z grubszego materiału, na przykład z buku, powstają na frezarce. Obie techniki opisujemy na stronach o [wycinaniu laserowym](/wycinanie-laserowe/) i [frezowaniu CNC](/frezowanie-cnc/).
- **Lista z ptaszkami:**
  > - Napisy „Tea” i „Team” z lustrzanej plexi na sklejce, cięte laserem
  > - Logo kawiarni BOKO z lustrzanej plexi, na słupie i na pomarańczowym kole
  > - [Tkanina na elewację Zamku Sułkowskich](/case-study/zamek-sulkowskich/): 800 metrów wyciętych według projektu klienta

  (R1: anchor linku do frezowania to teraz „frezowaniu CNC”, a do case study „Tkanina na elewację Zamku Sułkowskich”.
  R2: H2 „Ścianki i dekoracje”, bo jedyne zdjęcie sekcji to dekoracja z tkaniny, a nie ścianka ani napis; napisy zostają
  w akapicie i na liście. Link karty 2 w s01 brzmi tak samo. „z plexi oraz sklejki”, bez dwóch „i” w pięciu słowach.)
- **Przycisk:**
  > Wyceń dekorację na event
  cel: `/kontakt/`
- **Zdjęcie** (4:3, lazy): `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/hero-zamek-sulkowskich-v2.jpg` (pełny plik 1536×864, media 2516)
  alt: `Elewacja Zamku Sułkowskich pokryta złoto-czerwoną tkaniną wyciętą laserowo`
  (kadr 4:3 ze środka; u dołu tylko górna krawędź muru, cudzej instalacji z dzianiny w tym pliku nie widać; nie przesuwać kadru w dół)
- **Linki:** `/wycinanie-laserowe/` („wycinaniu laserowym”, linki.md #4, NIE `#nagrody`), `/frezowanie-cnc/` („frezowaniu CNC”, #5),
  `/case-study/zamek-sulkowskich/` („Tkanina na elewację Zamku Sułkowskich”, #7), `/kontakt/`.

Uwagi do treści: Bondi Sands bez „plaży” i „barki” i bez technologii ścianki (S02, P08, L04); bez zdań z case study
na 1019. Tea i Team jako cięcie laserowe (Z04), choć galeria ma dziś plakietkę „Frezowanie”.

---

## s05. Upominki z logo (K2 + K8), `<section class="pdl-sec pdl-sec--wash" id="upominki">`

- **Etykieta:**
  > Upominki z logo
- **H2:**
  > Logo, które<br>się nie zetrze.
- **Tekst nagłówka:**
  > [Grawer laserowy](/grawerowanie-laserowe/) zostawia znak w samym materiale, więc nie zejdzie jak nadruk. Co sprawdza się jako upominek, opisaliśmy w [poradniku o prezentach firmowych z grawerem](/blog/firmowe-prezenty-z-grawerem/).

  (R1: H2 nie powtarza już karty Zakresu ani eyebrow; bez „i ile trwa seria”, bo wpis 2177 podaje 4-5 dni, którego nie ma
  w terminach od zleceniodawcy, P04. R2: „Grawer laserowy zostawia znak” zamiast „Znak robimy grawerem”; anchor linku #3
  to teraz „Grawer laserowy”.)

Karty (`article.pdl-mat`: zdjęcie 16:10 lazy, `<h3 class="pdl-h4">`, tekst `.pdl-txt-sm`), 6 sztuk jak u sióstr:

**a.** zdjęcie `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/08/IMG_7380-768x576.jpg` (media 2068), alt `Butelka termiczna z grawerowanym imieniem`
> Stal z powłoką
> Kubki i butelki termiczne. Grawer może biec dookoła całego naczynia.

(R2: bez pleonazmu „objąć… dookoła”.)

**b.** zdjęcie `https://grawerowanie-laserowe.pl/wp-content/uploads/2024/04/IMG_2836-768x512.webp` (media 1009), alt `Kieliszek do wina z grawerowanym logo`
> Szkło
> Kieliszki i karafki z logo na upominek. Grawer na szkle wychodzi matowy i jasny, bez farby.

(Szkło tylko jako upominek, bez nagłówka o kieliszkach: rdzeń HoReCa. Na zdjęciu logo samego Padiru, alt bez „dla klienta”.)

**c.** zdjęcie `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-macbook-the-last-dance-768x373.jpg` (media 2339), alt `Grawer z motywem imprezy na pokrywie laptopa`
> Aluminium i elektronika
> Powerbanki, pendrive'y i laptopy. Grawerujemy samą obudowę i nie ruszamy tego, co działa w środku.

**d.** zdjęcie `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/IMG_1207-768x1024.webp` (media 2233), alt `Seria noży z grawerowanym logo na głowniach`,
w `<img>` `style="object-position:50% 82%"` (R1: kadr 16:10 ze środka gubił logo JBB; przy 82% widać je na 3-4 głowniach)
> Stal nierdzewna
> Noże z logo firmy, pojedynczo albo w kompletach prezentowych. Szczegóły na stronie o [nożach z grawerem](/grawerowanie-laserowe/grawerowanie-na-nozu/).

**e.** zdjęcie `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/4-edited-e1736263438391-768x431.webp` (media 1622), alt `Świeca z drewnianą pokrywką z grawerem świątecznych życzeń od firmy`
> Drewno i skóra
> Skrzynki na wino, drewniane pokrywki świec, notesy, kalendarze i skórzane etui. Na pokrywce świecy wygrawerujemy życzenia od firmy, jak na zdjęciu.

**f.** zdjęcie `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-grawer-wow-na-owocach-768x384.jpg` (media 2331), alt `Owoce ze znakowaniem laserowym napisu WOW!`
> Skórka owoców
> Logo albo hasło na jabłkach, gruszkach czy dyniach, bez naklejki. Na stoisko promocyjne albo event.

(Okazji zdjęcia „WOW!” nie znamy, P24: tekst mówi o zastosowaniu usługi, nie o tym, że to był event.)

Linki sekcji: `/grawerowanie-laserowe/` („Grawer laserowy”, linki.md #3), `/blog/firmowe-prezenty-z-grawerem/` („poradniku o prezentach firmowych z grawerem”, #1), `/grawerowanie-laserowe/grawerowanie-na-nozu/` („nożach z grawerem”, #2).
Kanibalizacja: tytuły kart to materiały, nie kafle szkicu nowej strony grawerowania („Kubki i butelki termiczne”,
„Powerbanki i pendrive'y”, „Noże”); bez porad z wpisu 2177 i bez „prezenty firmowe” w nagłówkach.

---

## s06. Realizacje (K2 + K9), `<section class="pdl-sec">`

- **Etykieta:**
  > Realizacje
- **H2:**
  > Nasze prace<br>z bliska.
- **Tekst nagłówka:**
  > Napisy z plexi, ścianka w trakcie cięcia, plakieta i upominki z grawerem. Pełna galeria pokazuje też realizacje dla innych branż.

  (R1: H2 bez „nagród”, bo w galerii nie ma żadnej nagrody, a plakieta to P03; bez kolejnej trójki. R2: bez „Logo”,
  bo logo BOKO zostało tylko w hero.)
- **8 zdjęć** (kadr 1:1, lazy, bez podpisów), w tej kolejności:
  1. `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-napis-przestrzenny-tea-768x512.jpg` (2315), alt `Złoty napis przestrzenny Tea z lustrzanej plexi`,
     w `<img>` `style="object-position:15% 50%"` (R1: przy kadrze ze środka ucinało lewe ramię litery T)
  2. `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-podswietlana-litera-r-768x512.jpg` (2324), alt `Podświetlana przestrzenna litera R z plexi`
  3. `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/09/wyc-bondi-ciecie-768x960.jpg` (2527), alt `Lustrzana ścianka eventowa w trakcie wycinania na maszynie w pracowni Padir`
     (R1: bez „na laserze”; media 2527 mówi „na maszynie”, na kadrze głowica z odciągiem jak przy frezarce, technologia: P08.
     Alt w `zdjecia.json` przy 2527 nadal ma „na laserze” i trzeba go poprawić przy następnym składzie.)
  4. `https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-plakieta-mysliwska-skalisko.jpg` (2354, pełny plik 753×1000, bo `url_medium` ma 226×300), alt `Metalowa plakieta z reliefem dzika i grawerowaną datą na wstędze`
  5. `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/3-768x1024.webp` (1607), alt `Granatowy kubek termiczny z grawerowanym imieniem`
  6. `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/8-edited-768x576.webp` (1614), alt `Metalowy pendrive z grawerowanym imieniem`
  7. `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/07/IMG_9416-768x576.webp` (2035), alt `Metalowa skrzynka narzędziowa z grawerowaną tabliczką`
  8. `https://grawerowanie-laserowe.pl/wp-content/uploads/2025/08/69A6E5DE-29D8-4BEA-9765-6E0862C9017F-768x960.jpg` (2066), alt `Czarna butelka termiczna z grawerowanym imieniem i małym logo`
     (R2: zamiast 2520 `wyc-boko-litery`, który jest wycinkiem 2525 z hero: wiersze 256-768, średnia różnica 1,7/255,
     `red-marketing-r2/boko_dopasuj.py`. 2066 jest w `zdjecia.json` (zatwierdzone), nie stoi na HoReCa, Przemyśle ani 1019;
     w kadrze 1:1 ze środka widać imię i logo padir. Na końcu, a nie obok kubka, żeby dwa ciemne naczynia nie stały obok siebie.)
- **Przycisk** (ghost, `style="margin-top:32px"` na `.pdl-btns`, poprawka U10):
  > Zobacz wszystkie realizacje
  cel: `/przykladkowe-realizacje/#galeria`
- **Linki:** `/przykladkowe-realizacje/#galeria` (linki.md #8; `id="galeria"` jest na 1397, sprawdzone).

Zdjęcia celowo spoza hero, K3, K7 i K8 (U13); po R2 bez wyjątku (szyld BOKO tylko w hero). Napis „Team” (2316) pominięty: w kadrze 1:1 obcina litery; „Tea” mieści się lepiej.

---

## s07. FAQ (K2 + K11), `<section class="pdl-sec pdl-sec--wash">`

- **Etykieta:**
  > FAQ
- **H2:**
  > Zanim wyślesz<br>zapytanie.
- **Tekst nagłówka:**
  > Odpowiedzi, które przydadzą się przed wyceną. Twojego pytania tu nie ma? [Napisz do nas](/kontakt/).

Pytania (`details.pdl-q`, domyślnie zamknięte; odpowiedź w `.pdl-q-a > p.pdl-txt-sm`):

**Q1**
> Mamy upominki od innego dostawcy. Wygrawerujecie na nich logo?
> Tak. Dostawca może wysłać je kurierem prosto do nas, możesz je też przywieźć sam. Termin liczymy od dnia, w którym przedmioty do nas dotrą. Przy tworzywach najpierw robimy próbę na jednej sztuce. Sprawdź [listę materiałów do grawerowania](/materialy-do-grawerowania/) albo przyślij zdjęcie przedmiotu.

**Q2**
> Każda nagroda ma mieć inne nazwisko. Zrobicie to w jednej serii?
> Tak. Nazwiska, kategorie i lata wstawiamy z Twojej listy do pliku, więc każda nagroda dostaje swój napis. Przed serią grawerujemy jeden egzemplarz do akceptacji, a resztę robimy po Twojej zgodzie. Gdyby któraś nagroda wyszła z błędem, poprawimy ją.

(R2: źródła mówią tylko, że Padir graweruje sztukę do akceptacji, nie że klient ją dostaje: pytanie R03. „Sztuka” raz zamiast trzech razy.)

**Q3**
> Ile kosztuje najmniejsze zlecenie?
> 100 zł. Tyle wynosi minimum za jedno zlecenie bez względu na liczbę sztuk, więc jedną statuetkę też u nas zamówisz. Cenę większej serii podamy w wycenie.

(R2: bez „razem z terminem”: termin w wycenie stoi w następnej odpowiedzi i w pasie kontaktu.)

**Q4**
> Wydarzenie jest blisko. Jak szybko zrobicie grawer?
> Grawer zrobimy w ciągu 2 dni albo od ręki za dodatkową opłatą. Termin serii statuetek, upominków czy dekoracji podajemy w wycenie, dlatego w zapytaniu od razu wpisz datę wydarzenia.

(R1: słowa i szyk zleceniodawcy, bez „nawet” i bez przesuwania „za dodatkową opłatą” na początek. Poprzednie brzmienie
przypisywało dopłatę także do 2 dni, czemu przeczą wpisy 1660 i 2177 („około 2 dni roboczych”, „często w dwa dni robocze”).
Odczyt rozstrzygnie A01. Gdy klient potwierdzi, że 2 dni są w standardzie: „Grawer zrobimy zwykle w ciągu 2 dni, a za
dodatkową opłatą nawet od ręki.” Bez „4-5 dni” i bez listopada/grudnia: to jest już w FAQ szkicu grawerowania.)

**Q5**
> Mamy projekt od grafika. W jakim formacie go wysłać?
> Najwygodniej w wektorach: AI, EPS, SVG albo PDF, a elementy do cięcia także w DXF lub DWG. Jeśli masz tylko zdjęcie logo albo szkic, przygotujemy plik na jego podstawie. Przy trudnych plikach może dojść dodatkowy koszt.

**Q6**
> Za rok domówimy kilka sztuk. Będą takie same jak pierwsze?
> Tak. Plik wzorcowy i parametry graweru archiwizujemy, więc nowe sztuki nie będą się różnić od tych sprzed roku. Przydaje się to przy nagrodach wręczanych co roku i przy upominkach dla nowych osób w zespole.

**Q7**
> Odbierzemy zamówienie sami czy wyślecie je kurierem?
> Jak wolisz. Gotowe zamówienie odbierzesz w pracowni przy ul. Matuszewskiej 14 w Warszawie, od poniedziałku do piątku w godz. 8:30-16:00, albo wyślemy je kurierem pod wskazany adres.

Linki sekcji: `/kontakt/` („Napisz do nas”), `/materialy-do-grawerowania/` („listę materiałów do grawerowania”, linki.md #9).
Pytania celowo inne niż w FAQ szkicu grawerowania („Czy zrobicie grawer na jednej sztuce?”, „Ile się czeka na grawer?”,
„Od czego zależy cena?”, „Czy mogę przynieść własny przedmiot?”), na `/produkty/` („Jakie pliki przyjmujecie?”,
„Realizujecie pojedyncze sztuki?”) i u sióstr.

---

## s08. Pas kontaktu (K12), `<section class="pdl-sec">` + `<div class="pdl-band">`

- **H2:**
  > Napisz, co i na kiedy.
- **Tekst:**
  > Przyślij logo albo szkic nagrody. Dopisz liczbę sztuk i datę wydarzenia. Przy grawerze i statuetkach wycenę z terminem dostaniesz w ciągu 24 godzin.

  (R1: 24 h tylko przy grawerze i statuetkach, za wpisem 2177, który obejmuje statuetkę INSOFT; ścianki i dekoracje po A04 i R01.)
- **Przyciski:**
  - główny (biały): > Wyceń zamówienie
    cel: `/kontakt/`
  - ghost: > Zobacz realizacje
    cel: `/przykladkowe-realizacje/`
- **Linki:** `/kontakt/`, `/przykladkowe-realizacje/` (z szablonu, poza licznikiem).

---

## K14. JSON-LD `Service` (opcjonalnie, drugi blok `wp:html` za grupą)

Tylko fakty ze źródeł, bez podwójnego ampersandu. Propozycja wartości:
- `@id`: `https://grawerowanie-laserowe.pl/uslugi-dla-marketingu/#service`
- `name` / `serviceType`: `Statuetki, puchary i upominki z logo dla firm`
- `description`: `Statuetki i nagrody z plexi i drewna, puchary, upominki z logo, napisy przestrzenne, ścianki i dekoracje na event oraz ekspozytory dla marek i agencji. Zamówienia od 1 sztuki.`
- `url`: `https://grawerowanie-laserowe.pl/uslugi-dla-marketingu/`
- `provider`: `{"@id":"https://grawerowanie-laserowe.pl/#organization"}`, `areaServed`: Polska
- `hasOfferCatalog.itemListElement` (5 usług z K4): `Statuetki, puchary i nagrody`, `Upominki i gadżety z logo`, `Napisy, logo i oznakowanie`, `Ścianki i dekoracje eventowe`, `Ekspozytory i opakowania` (R2: nazwa czwartej usługi jak H3 karty 4)
- `audience`: `BusinessAudience`, `Działy marketingu, agencje reklamowe i eventowe, organizatorzy konkursów i gal`

---

## Zestawienie linków (9 kontekstowych + szablon)

| # | adres | anchor | sekcja |
|---|---|---|---|
| 1 | `/blog/firmowe-prezenty-z-grawerem/` | poradniku o prezentach firmowych z grawerem | s05 tekst nagłówka |
| 2 | `/grawerowanie-laserowe/grawerowanie-na-nozu/` | nożach z grawerem | s05 karta d |
| 3 | `/grawerowanie-laserowe/` | Grawer laserowy | s05 tekst nagłówka |
| 4 | `/wycinanie-laserowe/` | wycinaniu laserowym | s04 tekst |
| 5 | `/frezowanie-cnc/` | frezowaniu CNC | s04 tekst |
| 6 | `/blog/tworzenie-ekspozycji-dla-marek-kosmetycznych/` | jak robimy ekspozycje dla marek kosmetycznych | s02 karta 5 |
| 7 | `/case-study/zamek-sulkowskich/` | Tkanina na elewację Zamku Sułkowskich | s04 lista |
| 8 | `/przykladkowe-realizacje/#galeria` | Zobacz wszystkie realizacje | s06 przycisk |
| 9 | `/materialy-do-grawerowania/` | listę materiałów do grawerowania | s07 Q1 |
| - | `/kontakt/` | Wyceń zamówienie, Opisz projekt, Zapytaj o statuetki, Wyceń dekorację na event, Napisz do nas | s00, s02, s03, s04, s07, s08 |
| - | `/przykladkowe-realizacje/` | Zobacz realizacje | s08 |
| - | `#zakres`, `#upominki`, `#event`, `#nagrody` | Co robimy, Upominki z logo, Ścianki i dekoracje na event, Statuetki i puchary | s00, s01 |

Wszystkie adresy mają status `publish` w `zrodla/SPIS.json` (sprawdzone 13.10.2026). Nie linkuję: `/wycinanie-laserowe/#nagrody`,
wpisów 2009, 1757, 1546, 2078, 1660, szkiców 1841, 1786, 1731, `/o-nas/`, sióstr w treści.
