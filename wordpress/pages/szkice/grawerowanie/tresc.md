# Treść szkicu: Grawerowanie laserowe

Strona: szkic, który po akceptacji zastąpi treść strony 456 `/grawerowanie-laserowe/`.
Komponenty: `praca/wzorzec.md` (K01-K17). Fakty: `praca/grawerowanie/fakty.md` (numery F, S, P w nawiasach).
Zdjęcia: `praca/grawerowanie/zdjecia.json` (numery to `media_id`), wszystkie obejrzane na arkuszach
`praca/grawerowanie/autor/a-hero-materialy.png`, `b-galeria-park.png`, `c-segmenty.png`; nóż 2230 z karty
„Noże” (runda 2) i zdjęcia 2279 oraz 1614 ponownie na `red-r2/kont-r2.png`.
Księga twierdzeń: `praca/grawerowanie/ksiega.json`.

Konwencja tego pliku:
- wiersz zaczynający się od `> ` to DOKŁADNY tekst widoczny na stronie (do wklejenia 1:1);
- `> [RAMKA]` to żółta ramka K01 `p.pdw-uwaga` (wklejamy sam tekst po `[RAMKA] `);
- `<br>` w tekście to złamanie wiersza; „szary początek” w hero to `<span>` z kolorem `#6F6F7C`;
- wszystko inne (etykiety pól, uwagi, tabele) to instrukcja dla składacza, nie trafia na stronę.

Liczba słów widocznego tekstu (wiersze `> ` bez ramek, razem z niezmienionym blokiem kontaktu
i etykietami formularza CF7): **1351** (po rundzie 2 poprawek; po rundzie 1: 1372). Ramki (7 razem z górną): 260 słów, znikną przed publikacją.
Wzorzec 1019 liczony tak samo (plik `.txt`): 1066.

---

## Meta

| pole | wartość |
|---|---|
| title (pole SEO) | `Grawerowanie laserowe w Warszawie \| Pracownia Padir` (51 znaków) |
| meta description | `Grawerujemy laserem logo, numery seryjne i dedykacje. Trwały znak bez farby, od pojedynczej sztuki po serie z próbką do akceptacji. Pracownia w Warszawie.` (154 znaki) |
| slug roboczy | `grawerowanie-laserowe-szkic` |
| szablon WordPressa | `page-no-title` (jak 1019). Przy przenoszeniu na 456 przełączyć z `wp-custom-template-grawerowanie-laserowe`, bo ten dokłada drugi `<h1>`. |
| status | szkic, nieopublikowany (zapis robi prowadzący, nie agent) |

Tytuł i meta za `linki.md`, sekcja 5: nie zaczynają się od listy materiałów (R4), nie powtarzają meta strony
głównej ani `/produkty/` (R1, R10), bez półpauz.

---

## Kolejność sekcji i tła

| # | identyfikator | `id` w HTML | komponent | tło sekcji | padding |
|---|---|---|---|---|---|
| 00 | ramka-robocza | - | K01 ramka górna | - | - |
| 01 | hero | - (`<header>`) | K02 + K03 + K04 | białe | `56px 0px 72px` |
| 02 | dlaczego | - | K05 wyśrodkowany + K06 | białe | `82px 0px` |
| 03 | materialy | `materialy` | K05 + K07 (6 kart białych) | `#F5F5F5` | `82px 0px` |
| 04 | portfolio | `portfolio` | K09 (9 kart `#F5F5F5`) | białe | `82px 0px` |
| 05 | na-czym-polega | - | K10 | białe | `36px 0px 78px` |
| 06 | proces | `proces` | K05 + K11 (4 kroki, SVG) | `#F5F5F5` | `78px 0px` |
| 07 | realizacje | `realizacje` | K05 + K12 (1 karta A + ciemny pas CTA) | `#F5F5F5` | `82px 0px` |
| 08 | zastosowania | - | K05 + karty K07 w wariancie na białym (4 karty `#F5F5F5`) | białe | `82px 0px` |
| 09 | technologia | `technologia` | K14 (5 kart maszyn) | białe | `82px 0px` |
| 10 | zaufali | - | K15 | białe | `20px 0px 82px` |
| 11 | faq | `faq` | K16 (5 pytań) | `#F5F5F5` | `82px 0px` |
| 12 | kontakt | `kontakt` | K17 | białe | `82px 0px 92px` |

Kotwice używane na stronie: `#kontakt`, `#proces`, `#portfolio` (wszystkie mają sekcje).

---

## 00. ramka-robocza (K01, ramka górna)

> [RAMKA] Wersja robocza do akceptacji. Żółte ramki oznaczają miejsca do potwierdzenia przed publikacją.

---

## 01. hero (K02)

**h1** (zapis zdaniowy, usterka 14 wzorca)
> Grawerowanie<br>laserowe

**podtytuł** (szary początek do kropki, reszta czarna)
> [szary] Bez farby i naklejek. [czarny] Laser wpisuje znak w sam materiał.

**akapit**
> Pracownia w Warszawie, na rynku obróbki laserowej od 2002 roku. Grawerujemy metal, drewno, plexi, skórę i szkło, od jednej obrączki po serie tabliczek znamionowych.

(Runda 1: szkło na końcu listy, a przykład pojedynczej sztuki z metalu, bo FAQ mówi, że szkło przyjmujemy od 12 sztuk.)

**CTA** (teksty jak we wzorcu)
> Skorzystaj z oferty

cel `#kontakt` (K03 A)
> Czytaj więcej

cel `#proces` (K03 B)
> Zobacz więcej realizacji

cel `#portfolio` (K04, strzałka z `aria-hidden="true"`)

**zdjęcia** (`loading="eager" fetchpriority="high" data-no-lazy="1"`, wszystkie z `data-pdw-zoom`)

| kafel | media_id | url | alt |
|---|---|---|---|
| 1 (LG) | 2326 | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-karafka-mercure-hotel.jpg | Szklana karafka z grawerowanym logo Mercure Hotel Warszawa Grand |
| 2 (PG) | 2330 | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-noze-jbb-baldyga.jpg | Noże ze stali nierdzewnej z grawerowanym logo JBB Bałdyga na głowni |
| 3 (LD, pod nawiasem) | 2353 | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-grawerowana-sciana-dekoracyjna.jpg | Ściana z wielkoformatowych paneli z grawerowanym wzorem, podświetlona reflektorami |
| 4 (PD) | 2338 | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-panel-sterujacy-anko.jpg | Panel sterujący ze stali nierdzewnej z grawerowanymi opisami PUMP, OUTLET i I/O oraz logo anko |

Uwagi: kafel 3 to ściana, bo wzór idzie przez cały kadr i nawias L nie zasłoni sedna. Plik ściany ma tylko
959 × 539 px: w kaflu wystarczy, w lightboxie będzie miękki (warto poprosić klienta o oryginał, zdjecia.json, braki).
Klienci w altach (Mercure, JBB Bałdyga, anko) w tym samym kontekście co karty galerii 1397 (F151, F154, F156).
Żadne z czterech zdjęć nie stoi na wzorcu 1019.

---

## 02. dlaczego (K05 wyśrodkowany + K06)

**etykieta**
> Dlaczego Padir

**h2**
> Zlecasz raz, odbierasz gotowe

**lead**
> Nie potrzebujesz dużego nakładu ani pliku od grafika. Przedmiot nie musi też jeździć między warsztatami.

**karta 1** (czarna, ikona ◆)
> Pojedyncze sztuki

> Jedna obrączka czy jeden nóż to u nas zwykłe zlecenie. Plik i ustawienia lasera zachowujemy. Przy kolejnym zamówieniu, nawet po roku, nie zaczynamy od zera.

(Runda 2: bez obietnicy, że kolejna partia wyjdzie „taka sama”, bo karta Drewno mówi, że dwie sztuki nie będą
identyczne, i bez szkieletu zdania z `/produkty/` i `/uslugi-dla-horeca/`. Archiwum pliku „dla każdego klienta”
podaje `pages-2283`, więc zdanie pasuje też do pojedynczych sztuk.)

**karta 2** (szara, ikona ✓)
> Wystarczy zdjęcie logo

> Nie masz pliku wektorowego? Przyślij zdjęcie znaku albo odręczny szkic, a plik do graweru przygotujemy u siebie.

**karta 3** (szara, ikona ★)
> Grawer, cięcie i frez razem

> Jeśli przedmiot trzeba też wyciąć albo sfrezować, zrobimy to w tej samej pracowni, w ramach jednego zamówienia. Zobacz wycinanie laserowe i frezowanie CNC.

**linki wewnętrzne** (zwykłe linki w tekście karty 3, kolor z arkusza `.pdw`)
- `/wycinanie-laserowe/`, anchor „wycinanie laserowe”
- `/frezowanie-cnc/`, anchor „frezowanie CNC”

Uwaga: karty nie kopiują haseł 1019 („Nowoczesne technologie”, „Gwarancja udanego produktu”, „Doświadczenie
i profesjonalizm”) ani ogólników ze starej 456 (fakty N05, linki R9). Każda karta to konkret z fakty.md.

---

## 03. materialy (K05 do lewej + K07), `id="materialy"`, sekcja `#F5F5F5`, karty białe

**etykieta**
> Materiały

**h2** (nie „Materiały w których grawerujemy” ani „Materiały do grawerowania laserowego”, R4)
> Na czym grawerujemy

**lead**
> Szkło pod wiązką matowieje, a drewno ciemnieje. Na aluminium i powlekanej stali zostaje jasny ślad, a na gołej stali efekt zależy od wykończenia. Dlatego ustawienia lasera dobieramy do konkretnego przedmiotu.

**karty** (6, w tej kolejności; zdjęcie 16:10, `loading="lazy" decoding="async" data-pdw-zoom`)

1. zdjęcie 1009 https://grawerowanie-laserowe.pl/wp-content/uploads/2024/04/IMG_2836-scaled.webp
   (lżejsza wersja: https://grawerowanie-laserowe.pl/wp-content/uploads/2024/04/IMG_2836-768x512.webp),
   alt: Kieliszek do wina z grawerowanym logo padir na drewnianym blacie
> Szkło

> Kieliszki, karafki, szklanki rocks i butelki. Okrągłe naczynia mocujemy w głowicy obrotowej, dzięki czemu grawer może biec wokół całego obwodu.

2. zdjęcie 1614 https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/8-edited-scaled.webp
   (lżejsza: https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/8-edited-768x576.webp),
   alt: Metalowy pendrive z grawerowanym imieniem Ewa (runda 2: pendrive’y dopisane do listy w karcie, żeby opis
   zgadzał się ze zdjęciem; źródło `posts-1546` „Powerbanki, Kable USB i Pendrive’y z Grawerem”)
> Stal, aluminium, mosiądz

> Noże, sztućce, zegarki, pendrive’y, panele i tabliczki. Metal znakujemy laserem fiber. Najmocniejszy kontrast daje czarna powłoka proszkowa, spod której wychodzi jasny metal.

3. zdjęcie 1622 https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/4-edited-e1736263438391.webp
   (lżejsza: https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/4-edited-e1736263438391-768x431.webp),
   alt: Świeca z drewnianą pokrywką z grawerowanymi życzeniami świątecznymi
> Drewno i sklejka

> Dąb, orzech, akacja, bambus, sklejka i MDF. Grawer na drewnie wychodzi ciemniejszy od tła, a jego odcień zależy od gatunku i układu słojów. Dwie sztuki z tym samym wzorem nie będą identyczne.

4. zdjęcie 2357 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-ladowarka-enel-x.jpg,
   alt: Ładowarka z grawerowanym logo enel x na obudowie z tworzywa
> Tworzywa i plexi

> Obudowy i panele z tworzyw. Każde tworzywo reaguje inaczej, więc serię zaczynamy od próbki. Na przezroczystej plexi grawer jest mlecznobiały i świeci, gdy podświetlisz płytę od krawędzi.

   (Runda 1: karta zaczyna się od tworzyw, bo zdjęcie pokazuje obudowę ładowarki z tworzywa, nie plexi. Grawer w plexi widać w case study WOŚP.)

5. zdjęcie 2350 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-tabliczka-znamionowa.jpg,
   alt: Tabliczka znamionowa z laminatu grawerskiego ze znakiem CE i danymi technicznymi
> Laminat grawerski

> Dwuwarstwowy materiał na tabliczki znamionowe: laser zdejmuje wierzchnią warstwę i odsłania kolor spodu. Kształt z otworami pod nity lub śruby wycinamy w tej samej operacji.

6. zdjęcie 2327 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-torebka-lago-di-garda.jpg,
   alt: Torebka z grawerowanym logo Lago di Garda
> Skóra

> Laser zostawia na licu ciemniejszy odcisk. Sprawdza się na etui, okładkach notesów i podkładkach.

   (Runda 2: inny szkielet niż w karcie Drewno, bez podwójnego „ciemn-” w jednym zdaniu.)

   ramka w karcie 6, pod akapitem:
> [RAMKA] Do potwierdzenia z klientem: czy torebka „Lago di Garda” ze zdjęcia jest ze skóry naturalnej (tak podaje galeria realizacji), czy ze sklejki (tak podpisano ją na stronie Produkty)? Jeśli ze sklejki, w tej karcie damy skórzany kapelusz z galerii.

   Zapas dla karty 6 (gdy torebka odpadnie): 2323
   https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-grawer-na-skorzanym-kapeluszu.jpg,
   alt: Rondo skórzanego kapelusza z grawerowanymi inicjałami HH (to zdjęcie stoi też w Materiałach na 1019).

**akapit pod kartami** (styl jak podpis pod parkiem K14: `font: 300 15px / 1.7 Poppins, sans-serif; color: rgb(107, 107, 107);`, `margin: 34px 0px 0px;`; na `#F5F5F5` kontrast 4,89)
> Grawerujemy też filc, tkaniny, papier i karton, a nawet skórkę owoców. Nie ma tu Twojego materiału? Zajrzyj na pełną listę materiałów albo napisz do nas.

**linki wewnętrzne**
- `/materialy-do-grawerowania/`, anchor „pełną listę materiałów”
- `#kontakt`, anchor „napisz do nas”

Uwagi: tytuły kart to same nazwy materiałów (R4). Karta szkła mówi o kieliszkach bez progu ilościowego, próg
12 sztuk jest w FAQ. Tabliczka 2350 to wzór z danymi Padiru, nie zlecenie klienta, więc alt opisuje przedmiot
i nie mówi o realizacji. Żadne zdjęcie z tej sekcji nie powtarza się w galerii ani w hero.

---

## 04. portfolio (K09, hybryda `.pdr-card`), `id="portfolio"`, sekcja biała, karty `#F5F5F5`

**etykieta**
> Portfolio

**h2**
> Galeria realizacji

**lead**
> Tu widzisz 9 z 24 prac grawerskich z naszej galerii. Kliknij zdjęcie, żeby obejrzeć je z bliska.

**karty** (9, trzy rzędy po 3; dane 1:1 z `zrodla/realizacje-karty.json`: `pelne`, `alt`, `tytul`, `material`,
`plakietka`; plakietka „Grawerowanie” tło `#12388C`, tekst `rgb(255, 255, 255)`)

| # | tytuł (h3, widoczny) | materiał (widoczny, wersaliki z CSS) | plakietka | `pelne` | `alt` |
|---|---|---|---|---|---|
| 1 | MacBook „The Last Dance” | Grawer na laptopie | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-macbook-the-last-dance.jpg | MacBook „The Last Dance” - Grawer na laptopie |
| 2 | Obrączka z grawerem | Stal, czerń | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-obraczka-z-grawerem.jpg | Obrączka z grawerem - Stal, czerń |
| 3 | Grawer szkła na laserze | Szkło | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-grawer-szkla-na-laserze.jpg | Grawer szkła na laserze - Szkło |
| 4 | Plakieta myśliwska „Skalisko” | Mosiądz | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-plakieta-mysliwska-skalisko.jpg | Plakieta myśliwska „Skalisko” - Mosiądz |
| 5 | Grawer „WOW!” na owocach | Znakowanie owoców | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-grawer-wow-na-owocach.jpg | Grawer „WOW!” na owocach - Znakowanie owoców |
| 6 | Znakowanie laserowe sztućców | Stal nierdzewna | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-znakowanie-laserowe-sztuccow.jpg | Znakowanie laserowe sztućców - Stal nierdzewna |
| 7 | Kubek termiczny padir | Stal, powłoka | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-kubek-termiczny-padir.jpg | Kubek termiczny padir - Stal, powłoka |
| 8 | Grawer monogramu „JC” | Metal szlachetny | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-grawer-monogramu-jc.jpg | Grawer monogramu „JC” - Metal szlachetny |
| 9 | Łyżka „Whiskey in the Jar” | Stal nierdzewna | Grawerowanie | https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-lyzka-whiskey-in-the-jar.jpg | Łyżka „Whiskey in the Jar” - Stal nierdzewna |

Widoczny tekst kart (do liczenia słów; plakietka „Grawerowanie” na każdej karcie):
> MacBook „The Last Dance” Grawer na laptopie Grawerowanie
> Obrączka z grawerem Stal, czerń Grawerowanie
> Grawer szkła na laserze Szkło Grawerowanie
> Plakieta myśliwska „Skalisko” Mosiądz Grawerowanie
> Grawer „WOW!” na owocach Znakowanie owoców Grawerowanie
> Znakowanie laserowe sztućców Stal nierdzewna Grawerowanie
> Kubek termiczny padir Stal, powłoka Grawerowanie
> Grawer monogramu „JC” Metal szlachetny Grawerowanie
> Łyżka „Whiskey in the Jar” Stal nierdzewna Grawerowanie

**CTA pod siatką** (przycisk z kodu K09, `wzorzec.md` sekcja 5)
> Zobacz wszystkie realizacje

cel `/przykladkowe-realizacje/#galeria` (link wewnętrzny, `id="galeria"` istnieje na 1397)

Dobór 9 z 21 kart „Grawerowanie” i dlaczego bez pozostałych 12:
- w hero: Karafka „Mercure Hotel”, Noże „JBB Bałdyga”, Grawerowana ściana dekoracyjna, Panel sterujący „anko”;
- w kartach materiałów: Ładowarka „enel X”, Tabliczka znamionowa, Torebka „Lago di Garda”;
- w sekcji zastosowań („Grawer dla firm i na prezent”): Szklanka „Binkowski Resort” (karta HoReCa);
- stoją już na 1019 (usterka 10, zdjecia.json): Statuetka z plexi, Statuetka jubileuszowa „INSOFT”, Grawer na skórzanym kapeluszu (zapas karty Skóra);
- Kieliszek do wina padir (2342): ten sam kieliszek co w karcie Szkło (1009); zdjecia.json ostrzega też, że w kaflu 4:3 kieliszek trafia na brzeg kadru.

Uwagi do kadrów: MacBook (1000 × 486) i sztućce (1000 × 430) to szerokie kadry. MacBook: w kaflu 4:3 widać środek
z grawerem (arkusz `a-hero-materialy.png`). Sztućce (runda 1): środek kadru pokazywał sam rozbłysk na trzonku,
więc `<img>` ma `object-position: 15% 50%;` i w kaflu widać też szyjkę łyżki. Napis na owocach jest drobny, widać go
dopiero w lightboxie. Karta 3 (głowica nad kieliszkiem padir) pokazuje proces na tym samym typie kieliszka co
karta Szkło, ale to inna scena i inny plik.

---

## 05. na-czym-polega (K10), bez `id`, padding `36px 0px 78px` (po białym portfolio)

**zdjęcie** 1808 https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/IMG_0074_11zon.webp
(lżejsza: https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/IMG_0074_11zon-768x768.webp),
alt: Dekiel zegarka w przyrządzie pod laserem podczas grawerowania dedykacji

**etykieta**
> Na czym to polega

**h2** (nie „Na czym polega grawerowanie laserowe?” ani „Czym jest…”, R3)
> Wiązka światła zamiast rylca

**akapit 1**
> Laser zdejmuje z powierzchni mikrowarstwę materiału, a w jej miejscu zostaje rysunek. Wiązka nie dotyka przedmiotu, dlatego nie dociska cienkich i delikatnych rzeczy.

**akapit 2**
> Drewno, plexi, skórę i szkło grawerujemy laserami CO₂, a metal laserem fiber. Przy seriach przygotowujemy przyrząd, w którym każda sztuka leży w tym samym miejscu. Więcej o obu typach laserów piszemy w poradniku „Jak działa grawerowanie laserowe”.

**link wewnętrzny**
- `/blog/jak-dziala-grawerowanie-laserowe/`, anchor „Jak działa grawerowanie laserowe” (tytuł wpisu; cudzysłów „” poza linkiem)

Uwaga: bez wykładu o długościach fal, głębokości 0,2 i 0,5 mm i porównania z CNC (R3, zostają we wpisie 2208).
Zdanie o bezdotykowej pracy to wiedza ogólna o technologii (fakty.md, sekcja 14), nie parametr pracowni.

---

## 06. proces (K05 do lewej + K11), `id="proces"`, sekcja `#F5F5F5`, `padding: 78px 0px`

**etykieta**
> Jak pracujemy

**h2**
> Od pomysłu do gotowego graweru

**lead** (bez zdania wzorca o „zdjęciach, które opowiadają historię”, usterka 6)
> Cztery kroki od pliku do odbioru, przy jednej sztuce i przy serii.

**kroki** (ilustracje SVG 01, 02, 03 i 04 z `zrodla/1019-sekcje/06-proces.html` bez zmian; ikona 03 to wiązka
lasera i pasuje do graweru; BEZ napisu „szkic” w rogu ilustracji)

01
> Plik albo zdjęcie

> Przyślij plik AI, EPS, SVG, PDF lub CDR albo zdjęcie znaku. Napisz też, ile sztuk potrzebujesz i na kiedy.

02
> Materiał i ustawienia

> Przedmiot przywieź albo wyślij kurierem. Jeśli nie masz materiału, zwykle możemy go zamówić za Ciebie. Laser i jego ustawienia dobieramy do tego, co trafi pod wiązkę.

03
> Próbka i grawer

> Przy serii albo nowym materiale najpierw grawerujemy jedną sztukę. Resztę robimy, gdy zaakceptujesz wzór, miejsce i głębokość.

04
> Odbiór

> Gotowe rzeczy odbierzesz u nas na Matuszewskiej 14 albo wyślemy je kurierem na Twój adres.

Uwaga: proces nie kopiuje pięciu kroków z `/produkty/` (R10) ani kroków 1019. Runda 2: warunek próbki tylko
w kroku 03 i ze spójnikiem „albo” (seria to jeden przypadek, nowy materiał drugi; źródło: „Przy seriach i przy
nowych materiałach…”), lead bez powtórki tego warunku.

---

## 07. realizacje (K05 do lewej + K12), `id="realizacje"`, sekcja `#F5F5F5`

**etykieta**
> Case study

**h2** (nie „Projekt od A do Z”, usterka 2; krótka fraza nominalna jak na 1019)
> Realizacja z bliska

**lead**
> Jedno zlecenie opisane od wyzwania do efektu.

**karta A** (zdjęcia z lewej, nawias granatowy z lewej)

zdjęcia (wszystkie z `data-pdw-zoom`), runda 1: dwa pionowe kafle 3:4 obok siebie (`grid-template-columns: 1fr 1fr; gap: 12px;`)
zamiast układu 4:3 + dwie kwadratowe miniatury:

| miejsce | media_id | url | alt |
|---|---|---|---|
| lewy 3:4, pod nawiasem L (`border-radius: 18px 18px 18px 90px`, nawias 118 px jak w K12) | 1737 | https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/1.jpg | Ramka z przezroczystej plexi z dziecięcym rysunkiem kota |
| prawy 3:4 (`border-radius: 18px 6px 18px 18px`) | 1738 | https://grawerowanie-laserowe.pl/wp-content/uploads/2025/01/IMG_0840-rotated.jpg | Ramka z przezroczystej plexi z rysunkiem dziecka, u dołu grawerowany tytuł pracy i logotypy |

Uwagi do zdjęć: to jedyne zdjęcia ramek z opublikowanego case study (`/case-study-wosp/`). Oba pliki mają
1512 × 2016 px, czyli dokładnie 3:4, więc kafle niczego nie ucinają i grawer u dołu ramy 1738 („Dinozaur”, podpis,
logotypy) jest widoczny bez lightboxa. 1740 (`IMG_0840-1-rotated.jpg`) usunięty: to bajt w bajt ten sam plik co 1738
(267 476 B, ten sam md5). Kot stoi pod nawiasem celowo, żeby nawias nie zasłonił tytułu „Dinozaur” w lewym dolnym
rogu drugiej ramy. Czwarte zdjęcie z case study (1739, frez CNC nad płytą plexi) jest na szkicu frezowania i na stronę
graweru nie pasuje.

**chip**
> Akcja charytatywna / ramki

**h3**
> Ramki na rysunki dzieci dla WOŚP

**Wyzwanie** (mikroetykieta „Wyzwanie” bez zmian)
> Wyzwanie

> Dzieci, którym pomaga dom Fundacji Ronalda McDonalda, przygotowały rysunki w podziękowaniu za tę pomoc. W rozmowach z Fundacją padł pomysł, by przekazać je na aukcję WOŚP. Trzeba je było oprawić tak, żeby dobrze wypadły na licytacji.

**Rozwiązanie**
> Rozwiązanie

> Każdą ramkę dopasowaliśmy do wymiarów konkretnego rysunku. Wygrawerowaliśmy na niej imię dziecka, tytuł pracy oraz logotypy WOŚP i Fundacji.

**Efekt**
> Efekt

> Oprawione rysunki miały trafić na licytację, a cały dochód z niej miał wesprzeć onkologię i hematologię dziecięcą. Ramki i grawer wykonaliśmy bezpłatnie.

**przycisk** (K03 A-mały, zamiast martwego `href="#"` wzorca, usterka 7; runda 2: krótszy napis, żeby przycisk
stał w jednym wierszu także przy 390 i 360 px, jak „Zobacz pełny case” na 1019)
> Cała historia ramek

cel `/case-study-wosp/` (link wewnętrzny)

**ciemny pas CTA** (K12, bez zapowiedzi „wkrótce”, usterka 13)
> Nietypowy przedmiot

> Nie wiesz, czy da się to wygrawerować?

> Opisz przedmiot i materiał albo przyślij zdjęcie. Sprawdzimy, czy laser sobie z nim poradzi i jak to zrobić.

> Zapytaj o grawer

cel `#kontakt` (K03 A-ciemny)

Uwaga: jedna karta zamiast dwóch, bo to jedyne opublikowane case study z grawerem. Case z tłokami jest na
`/uslugi-dla-przemyslu/` i nie wolno go powielać (R5). Fundacja Ronalda McDonalda i WOŚP są wymienione z nazwy
w tym samym kontekście co na `/case-study-wosp/` i `/case-study/` (F159).

---

## 08. zastosowania (K05 do lewej + karty K07 na białym tle), bez `id`

Sekcja zastępuje blok nagród ze slotu 08 wzorca (patrz „Pominięte sekcje wzorca”). Karty jak K07, ale
`background: rgb(245, 245, 245)` (zasada „karta przeciwna do tła”, wzorzec.md 2.3). Siatka (runda 1): K07 wymaga
liczby kart podzielnej przez 3, a kart są 4, więc dwie pary w zewnętrznej siatce, żeby nie było układu 3 + 1:
zewnętrzna `repeat(auto-fit, minmax(min(100%, 542px), 1fr)); gap: 22px; margin-top: 44px;` (542 = 2 × 260 + 22),
w niej dwie siatki `repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 22px;` po dwie karty. Zmierzone:
1440 px 4 w rzędzie, 1100/1024/768 px 2 × 2, 390/360 px jedna kolumna, bez poziomego przewijania.
Pod opisem w każdej karcie jeden link tekstowy w stylu CTA ze wzorca (K04 na 1019, `.pdr-cta` na 1397): waga 800,
granat, bez podkreślenia, podwójny szewron SVG bez animacji; ostatnie słowo i szewron w `white-space: nowrap`:
`<a href="…" style="display: inline-block; font: 800 15px / 1.4 Poppins, sans-serif; color: rgb(18, 56, 140); text-decoration: none;">… <span style="white-space: nowrap;">[ostatnie słowo]<svg viewBox="0 0 36 40" width="16" height="18" fill="none" stroke="#12388C" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display: inline-block; vertical-align: -3px; margin-left: 6px;"><polyline points="6,6 20,20 6,34"></polyline><polyline points="18,6 32,20 18,34"></polyline></svg></span></a>`
(`display: inline-block`, bo rodzic dziedziczy z motywu 24 px / 37,2 px i złamany link miał 37 px odstępu;
granat na `#F5F5F5` 9,78:1). Opis karty ma `margin: 0px 0px 14px;` jak w K07.
Runda 2: link przypięty do dołu karty tak jak wiersze parametrów w K14. Karta ma dodatkowo
`display: flex; flex-direction: column;`, blok tekstu `flex: 1 1 auto; display: flex; flex-direction: column;`,
a link na początku stylu `align-self: flex-start; margin-top: auto;`. Wszystkie 4 linki kończą się 26 px nad dołem
karty przy 1440, 1280, 1100, 1024, 768, 390, 360 i 320 px (pomiar `red-r2/pomiar.json`).

**etykieta**
> Zastosowania

**h2**
> Grawer dla firm i na prezent

**lead**
> Każda z czterech kart prowadzi do osobnej strony z przykładami.

(Runda 2: nagłówek obejmuje oba rodzaje kart, firmy i prezenty; lead bez powtórki czasownika z h2 i bez fragmentu
„ma u nas osobną stronę z”, który stoi na `/produkty/` i `/frezowanie-cnc/`.)

**karta 1**
zdjęcie 2262 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/wbet-ds18.jpg
(lżejsza: https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/wbet-ds18-768x576.jpg),
alt: Toczony metalowy detal z grawerowanym oznaczeniem WBET-DS-18 (runda 1: bez „stalowy”, bo strona przemysłowa w jednym z altów
nazywa ten detal aluminiowym, a na zdjęciu materiału nie da się rozstrzygnąć)
> Przemysł

> Numery seryjne i partii, kody Data Matrix i QR, tabliczki znamionowe oraz opisy na obudowach i panelach.

> Oznaczenia dla przemysłu

link `/uslugi-dla-przemyslu/`

**karta 2**
zdjęcie 2347 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/08/padir-realizacja-szklanka-binkowski-resort.jpg,
alt: Szklanka z grawerowanym logo Binkowski Resort
> Hotele i restauracje

> Logo lokalu na szkle i sztućcach, numery pokoi i plakietki dla obsługi. Grawer zrobimy też na naczyniach, które lokal już ma.

> Grawer dla hoteli i restauracji

link `/uslugi-dla-horeca/`

**karta 3**
zdjęcie 1891 https://grawerowanie-laserowe.pl/wp-content/uploads/2025/02/IMG_9004.jpg
(lżejsza: https://grawerowanie-laserowe.pl/wp-content/uploads/2025/02/IMG_9004-768x576.jpg),
alt: Dwie łyżeczki z grawerem w czerpakach i na trzonkach
> Prezenty

> Dedykacje z okazji komunii czy ślubu, wygrawerowane na zegarku, biżuterii, łyżeczce albo ramce na zdjęcie.

> Pomysły na prezent z grawerem

link `/grawerowanie-laserowe/prezenty/`

**karta 4**
zdjęcie 2230 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/WhatsApp-Image-2026-03-31-at-22.54.41.jpeg
(lżejsza, wstawiona: https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/WhatsApp-Image-2026-03-31-at-22.54.41-768x1365.jpeg),
alt: Czarny nóż składany z grawerowanym napisem GRZYB na głowni
(runda 2: zamiast noża 1450 z logo „Whiskey in the Jar”, bo ten sam znak jest na łyżce w galerii; plik pionowy,
w kaflu 16:10 środek kadru pokazuje głownię z całym napisem GRZYB, sprawdzone przy 1440 i 768 px)
> Noże

> Imię, logo albo monogram na głowni lub rękojeści. Jeden nóż na prezent albo seria z logo marki.

> Noże z grawerem

link `/grawerowanie-laserowe/grawerowanie-na-nozu/`

Uwagi: anchory opisowe, inne niż „Zobacz zakres →” z `/produkty/` (R10). Bez list cykli zmywarki, norm,
terminów serii, „+20%” i podsekcji okazji (R5, R6, R7). Znak „Whiskey in the Jar” jest na stronie tylko raz
(łyżka w galerii).

---

## 09. technologia (K14), `id="technologia"`, sekcja biała

**zdjęcie w bloku** 2279 https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/IMG_0060-rotated.jpg
(lżejsza: https://grawerowanie-laserowe.pl/wp-content/uploads/2026/04/IMG_0060-768x768.jpg),
alt: Metalowe szablony z grawerowanymi oznaczeniami otworów pod szuflady, w trakcie znakowania laserem
(runda 2: bez „aluminiowe”, bo żadne źródło nie podaje materiału, a kadr go nie rozstrzyga; widać blachę
z zagiętymi uszami i napisy „otwory do szuflad z frontami nakładanymi / wpuszczanymi”)
(prawdziwe zdjęcie z pracowni Padiru, z punktem wiązki; alt nie nazywa maszyny, bo jej nie znamy; NIE kopiować
błędnego altu ze strony przemysłowej „Detal po obróbce CNC”)

**etykieta** (na ciemnym, `#7FB0F5`)
> Technologia

**h2**
> Park maszynowy do graweru

**akapit**
> Pracujemy na laserach CO₂ marki Trotec i na laserze fiber do metali. Największy, Trotec SP2000, ma pole robocze 2510 × 1680 mm. Jeśli projekt jest większy, grawerujemy go w częściach i składamy po obróbce.

(W HTML wymiar ze spacjami nierozdzielającymi: `2510&nbsp;×&nbsp;1680&nbsp;mm`, tak samo `ok.&nbsp;0,3&nbsp;mm` w karcie fiber.
Runda 2: spacje nierozdzielające też we wszystkich wartościach wierszy parametrów, np. `726&nbsp;×&nbsp;432&nbsp;mm`,
`do&nbsp;3,55&nbsp;m/s`, `25-120&nbsp;W`, `od&nbsp;4&nbsp;pt`, `z&nbsp;4&nbsp;stron`; przy 1440, 1280, 1100, 1024 i 768 px
łamią się już tylko etykiety, np. „Pole / robocze”.)

**liczby** (3, spójne z akapitem i kartami; bez „400 W”, usterka 4)

| liczba | podpis |
|---|---|
| od 2002 | w obróbce laserowej |
| 120 µm | średnica plamki lasera |
| 3,55 m/s | maks. prędkość graweru na laserze Speedy 360 |

> od 2002 w obróbce laserowej
> 120 µm średnica plamki lasera
> 3,55 m/s maks. prędkość graweru na laserze Speedy 360

**karty maszyn** (5; zakresy wyłącznie z dywizem, wymiary ze znakiem `×` i spacjami)

| chip | h3 | opis | wiersz 1 | wiersz 2 | wiersz 3 |
|---|---|---|---|---|---|
| Grawer / detal | Trotec Speedy 300 | Personalizacja i drobne detale, także na wysokich przedmiotach. | Pole robocze: 726 × 432 mm | Moc CO₂: 25-120 W | Wys. materiału: do 200 mm |
| Grawer / detal | Trotec Speedy 360 | Grawer średniego formatu, w wersji flexx. | Pole robocze: 813 × 508 mm | Moc CO₂: 60-120 W | Prędkość graweru: do 3,55 m/s |
| Cięcie i grawer | Trotec Q500 | Gdy element trzeba wyciąć i oznaczyć na jednej maszynie. | Pole robocze: 1300 × 900 mm | Moc CO₂: 60-120 W | Grawer: od 4 pt |
| Wielki format | Trotec SP2000 | Gdy płyta nie mieści się na mniejszych maszynach. | Pole robocze: 2510 × 1680 mm | Moc CO₂: 180-500 W | Dostęp: z 4 stron |
| Metal | Laser fiber | Numery seryjne i kody na stali, aluminium i mosiądzu. | Min. wysokość znaku: ok. 0,3 mm | (ramka zamiast wierszy 2 i 3) | |

(W wierszu parametru część przed dwukropkiem to nazwa, `#8A8A94`, po dwukropku wartość, `#E8E8EE`; dwukropka nie wstawiamy.)

> Grawer / detal Trotec Speedy 300 Personalizacja i drobne detale, także na wysokich przedmiotach. Pole robocze 726 × 432 mm Moc CO₂ 25-120 W Wys. materiału do 200 mm
> Grawer / detal Trotec Speedy 360 Grawer średniego formatu, w wersji flexx. Pole robocze 813 × 508 mm Moc CO₂ 60-120 W Prędkość graweru do 3,55 m/s
> Cięcie i grawer Trotec Q500 Gdy element trzeba wyciąć i oznaczyć na jednej maszynie. Pole robocze 1300 × 900 mm Moc CO₂ 60-120 W Grawer od 4 pt
> Wielki format Trotec SP2000 Gdy płyta nie mieści się na mniejszych maszynach. Pole robocze 2510 × 1680 mm Moc CO₂ 180-500 W Dostęp z 4 stron
> Metal Laser fiber Numery seryjne i kody na stali, aluminium i mosiądzu. Min. wysokość znaku ok. 0,3 mm

ramka w karcie „Laser fiber”, pod wierszem parametru (ramka ma własne tło, działa na `#1C1C1C`):
> [RAMKA] Do potwierdzenia z klientem: producent i model lasera fiber, moc źródła, pole robocze i liczba takich maszyn. Przydałoby się też zdjęcie tej maszyny do tej sekcji, bo w bibliotece go nie ma.

ramka pod siatką kart, przed akapitem podsumowania (bezpośrednio w kontenerze, nie w siatce):
> [RAMKA] Do potwierdzenia z klientem: moce laserów Trotec podajemy w zakresach, tak jak na stronie Wycinanie laserowe. Czy podać moc źródeł zamontowanych w waszych maszynach? Czy Speedy 300 i Speedy 360 to lasery, na których grawerujecie na co dzień? Czy laser fiber to osobna maszyna, czy źródło fiber w Speedy 360 z opcją flexx? Czy macie laser UV (strona HoReCa: „Głowica obrotowa CO2 lub laser UV”) i czy grawerujecie nim szkło? Jakie „inne maszyny do grawerowania” ma na myśli strona Wycinanie laserowe i czy dopisać je tutaj?

**akapit podsumowania pod kartami**
> Nie musisz wiedzieć, który laser wybrać. Dobierzemy go do materiału i liczby sztuk.

Uwagi: z pięciu Treców z 1019 pomijamy SP500 (duże arkusze i pass-through to cięcie). SP2000 zostaje, bo stara 456
mówi wprost, że to największy laser, na którym Padir graweruje (F23). Opisy maszyn napisane od nowa, parametry
1:1 z 1019. Bez OptiMotion, InPack i „20-500 W” (N02, N03).

---

## 10. zaufali (K15), bez `id`, `padding: 20px 0px 82px`

**etykieta**
> Zaufali nam

**h2** (ZMIANA względem K15: nie „Współpracujemy z największymi”, fakty N04, linki R9)
> Marki, dla których pracowaliśmy

**lead** (ZMIANA względem K15: zdanie nie jest kopią 1019)
> Wybrane logotypy z naszej listy klientów.

ramka pod leadem, przed obrazkiem logotypów (styl K01 w treści, ale `margin: 0px auto 26px; max-width: 600px; text-align: left;`):
> [RAMKA] Do potwierdzenia z klientem: czy ten pas logotypów może stać na stronie grawerowania? Które z tych marek zamawiały u was właśnie grawer?

**logotypy**: bez zmian z K15 (te same trzy pliki i alty co na 1019, bez `data-pdw-zoom`). Nie dopisujemy marek.

---

## 11. faq (K16), `id="faq"`, sekcja `#F5F5F5`

**etykieta**
> FAQ

**h2**
> Najczęstsze pytania

**pytanie 1**
> Czy zrobicie grawer na jednej sztuce?

> Tak, pojedyncze sztuki robimy na co dzień. Wyjątkiem jest szkło: przyjmujemy je od 12 sztuk, bo przy mniejszej liczbie przygotowanie uchwytu kosztowałoby więcej niż praca lasera.

**pytanie 2**
> Ile się czeka na grawer?

> Małe zlecenia zajmują zwykle około 2 dni roboczych, a pojedyncze rzeczy czasem zrobimy od ręki, więc warto wcześniej zadzwonić. Serię prezentów firmowych robimy zwykle w 4-5 dni roboczych, licząc od dnia, w którym dostaniemy przedmioty. Przed świętami, w listopadzie i grudniu, czeka się dłużej, a dokładny termin podamy przy wycenie.

(Runda 1: 4-5 dni dotyczy w źródle kroku „Seria” prezentów firmowych, po próbce, nie każdego prezentu.)

**pytanie 3**
> Od czego zależy cena?

> Od liczby sztuk, wielkości graweru, materiału i tego, czy trzeba przygotować plik. Ekspresowy termin może kosztować więcej. Dokładną cenę podajemy po przesłaniu zapytania.

**pytanie 4**
> Czy mogę przynieść własny przedmiot?

> Tak. Przywieź go na Matuszewską 14 albo przyślij kurierem. Cienkie szkło może pod wiązką pęknąć, dlatego przy nim i przy nietypowych materiałach zaczynamy od próbki.

**pytanie 5** (ostatnie: `<details>` z `style="border-bottom:none;"`, usterka 17)
> Jak długo wytrzyma grawer?

> Tak długo jak materiał. To ślad w samej powierzchni, a nie farba, więc nie zmyje się ani nie odklei. Jeśli jednak powierzchnia ściera się od ciągłego tarcia, z czasem zużyje się razem z grawerem.

ramki pod białym pudełkiem FAQ (w kontenerze 860 px, pierwsza z `margin: 26px 0 14px`, druga `margin: 0`):
> [RAMKA] Do potwierdzenia z klientem (pytania 1-3): czy próg 12 sztuk przy szkle dotyczy też klienta indywidualnego, np. jednego kieliszka na prezent? Czy terminy z pytania 2 są aktualne i czy podać też termin serii innej niż prezenty? Czy dopisać minimalny koszt usługi 100 zł, który podaje blog?
> [RAMKA] Do potwierdzenia z klientem (pytanie 4): kto odpowiada, jeśli podczas graweru pęknie szkło powierzone przez klienta, i jak to opisać na stronie?

Uwagi: pytania napisane od nowa, nie powtarzają FAQ z `/produkty/` („Czy grawer się zetrze?”, „Jakie pliki
przyjmujecie?”) ani z 1019 (R10). Terminów serii HoReCa (5-10 dni) i przemysłu (24-48 h) tu nie ma (R5, R6).
Wpisu FAQ 1660 nie linkujemy (R11).

---

## 12. kontakt (K17), `id="kontakt"`

**h2 sekcji**
> Masz projekt do grawerowania?

**lead nad kartami**
> Prześlij plik albo zdjęcie znaku i napisz, na czym ma być grawer i ile sztuk potrzebujesz. Cenę i termin podamy w ciągu 24 godzin.

**reszta bez zmian z K17** (karta formularza `[contact-form-7 id="480"]`, logo, telefon +48 22 741 36 55, e-mail
laser@padir.pl, adres, godziny, „Budynek C2, wejście T9”, dane firmy z NIP). Tekst widoczny bez zmian, liczony do sumy słów:
> Skontaktuj się z nami Masz pytania? Chętnie pomożemy
> Telefon +48 22 741 36 55 E-mail laser@padir.pl Adres ul. Matuszewska 14, Warszawa
> Godziny otwarcia Poniedziałek - Piątek: 8:30 - 16:00 Budynek C2, wejście T9
> PADIR Ewa Salabura Matuszewska 14, 03-876 Warszawa NIP: 536-104-65-17

Etykiety i zgoda formularza (generuje WordPress z formularza 480, liczone tylko do sumy słów):
> Imię i Nazwisko Adres email Telefon Treść zapytania Wyrażam zgodę na przetwarzanie moich danych osobowych, podanych w niniejszym formularzu, w celu przetworzenia zapytania i prowadzenia korespondencji przez PADIR Ewa Salabura, Matuszewska 14, 03-876 Warszawa.

---

## Linki wewnętrzne (10, wszystkie `publish` w `zrodla/SPIS.json`, zapis względny)

| # | adres | anchor | sekcja |
|---|---|---|---|
| 1 | `/wycinanie-laserowe/` | wycinanie laserowe | 02 dlaczego, karta 3 |
| 2 | `/frezowanie-cnc/` | frezowanie CNC | 02 dlaczego, karta 3 |
| 3 | `/materialy-do-grawerowania/` | pełną listę materiałów | 03 materialy, akapit pod kartami |
| 4 | `/przykladkowe-realizacje/#galeria` | Zobacz wszystkie realizacje | 04 portfolio, przycisk |
| 5 | `/blog/jak-dziala-grawerowanie-laserowe/` | Jak działa grawerowanie laserowe | 05 na-czym-polega, akapit 2 |
| 6 | `/case-study-wosp/` | Cała historia ramek | 07 realizacje, przycisk |
| 7 | `/uslugi-dla-przemyslu/` | Oznaczenia dla przemysłu | 08 zastosowania, karta 1 |
| 8 | `/uslugi-dla-horeca/` | Grawer dla hoteli i restauracji | 08 zastosowania, karta 2 |
| 9 | `/grawerowanie-laserowe/prezenty/` | Pomysły na prezent z grawerem | 08 zastosowania, karta 3 |
| 10 | `/grawerowanie-laserowe/grawerowanie-na-nozu/` | Noże z grawerem | 08 zastosowania, karta 4 |

Kotwice na stronie: `#kontakt` (hero, materiały, pas CTA), `#proces` (hero), `#portfolio` (hero).
Nie linkujemy: wpis 1660 (R11), wpis 1868 (R2), szkice 1731, 1786, 1832, 2530, 14, adresy spoza SPIS.json (R12).

## Ramki do potwierdzenia (6 + ramka górna)

| # | sekcja | pytanie z listy |
|---|---|---|
| 1 | 03 materialy, karta Skóra | P18 |
| 2 | 09 technologia, karta Laser fiber | P01, P32 |
| 3 | 09 technologia, pod kartami | P03, P04, P02 (laser UV), flexx, „inne maszyny” z 1019 |
| 4 | 10 zaufali | P16 |
| 5 | 11 faq, pod pudełkiem | P09, P08, P10 |
| 6 | 11 faq, pod pudełkiem | P28 |

## Pominięte lub zastąpione sekcje wzorca

1. **Slot 08 „Tworzenie nagród i statuetek” (K13, `#nagrody`)**: zastąpiony sekcją „Dla kogo grawerujemy”
   (karty K07). Blok nagród stoi już na `/wycinanie-laserowe/#nagrody` (R9), jedyne dobre zdjęcie statuetki
   z grawerem (INSOFT 2340) jest w tym bloku na 1019, a strona musi podpiąć dwie strony potomne i dwie
   segmentowe (linki.md, punkt 3 i 4). Statuetki są wspomniane przy plexi tylko pośrednio; bez osobnej sekcji.
2. **Slot 07, druga karta case study (karta B)**: brak drugiego opublikowanego case study z grawerem. Case
   z tłokami należy do `/uslugi-dla-przemyslu/` (R5), case manufaktury biżuterii ze starej 456 nie ma
   pokrycia (N01). Zostaje jedna karta A i ciemny pas CTA.
3. **Slot 09, karta Trotec SP500**: pominięta (maszyna do cięcia dużych arkuszy), w jej miejscu karta lasera
   fiber, bo to jedyny laser do metali.

## Czego celowo NIE ma (kanibalizacja i fakty bez pokrycia)

- bloku „Materiały w których grawerujemy” ze strony głównej i h2 „Na czym polega grawerowanie laserowe?” (R1, R3);
- listy „co warto wygrawerować” i akapitu „dla kogo” pisanego ogólnie (R2);
- norm (GS1, ISO/IEC 16022, 765/2008/WE), „przechodzą audyt”, case’u z tłokami, cykli zmywarki, 480 kieliszków (R5, R6, N11);
- „+20% wartości”, „największe marki”, „sztuka, która trwa”, „miękkie stopy”, „20-500 W”, OptiMotion i InPack (N02-N09, 12b);
- dokładności ±0,01 mm i ±0,05 mm, głębokości 0,2 i 0,5 mm, lasera UV w tekście (tylko pytanie w ramce, P02), głowicy 3D, liczb z „O nas” (S08, F30, F31, S09);
- minimalnego kosztu 100 zł w tekście (tylko pytanie w ramce, P10).
