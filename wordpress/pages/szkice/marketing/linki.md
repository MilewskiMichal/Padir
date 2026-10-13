# Usługi dla marketingu: linkowanie wewnętrzne, kanibalizacja, title i meta

Strona: nowa strona branżowa „Usługi dla marketingu”, slug `uslugi-dla-marketingu`, szablon `page-no-title`,
komponenty `.pdl`, zapis jako NIEopublikowana (robi to człowiek prowadzący). Rodzeństwo: `/uslugi-dla-przemyslu/` (2264)
i `/uslugi-dla-horeca/` (2283).

Podstawa:
- `zrodla/SPIS.json` (statusy), `zrodla/pages-*` i `zrodla/posts-*` (`.raw.html` i `.txt`);
- `praca/marketing/fakty.md` (numery faktów Z.., F.., R.., S.., P.. w tym pliku odnoszą się do niego);
- `praca/marketing/wzorzec-pdl.md` (sloty s00-s10 i komponenty K1-K14 stron branżowych);
- szkice `praca/grawerowanie/strona.html` (nowa 456) i `praca/frezowanie/strona.html` (nowa 1011);
- tytuły SEO, opisy meta, menu i stopka: kopie publicznych stron z 9.10.2026 w `pobrane-fz-meta/` (HoReCa, Przemysł,
  `/produkty/`, strona główna, grawerowanie, frezowanie). Tytułów SEO pozostałych wpisów tam nie ma, więc porównuję
  ich tytuły z `SPIS.json` i nagłówki.

Bez liczb wyszukiwań. Wszystko poniżej wynika z tego, co serwis już pisze i jak linkuje. Częstość słów w serwisie
policzyłem skryptem `praca/marketing/linki-licz.py` (samo liczenie w `zrodla/*.txt`).

---

## 1. Główna intencja i frazy

### Intencja

Transakcyjna, B2B. Dział marketingu, agencja reklamowa albo eventowa, organizator konkursu, gali lub jubileuszu
firmy szuka wykonawcy i chce wyceny. Strona odpowiada na pytania: co zrobicie (nagrody, upominki z logo, elementy na
event), z czego, od ilu sztuk, w jakim terminie, ile kosztuje minimum, jak wysłać zapytanie. Wiedza poradnikowa
(„co dać kontrahentom”, „jak działa laser”, „jak powstaje ekspozytor”) zostaje na blogu i dostaje link.

### Jak budują to siostry

| | HoReCa 2283 | Przemysł 2264 |
|---|---|---|
| tytuł SEO | „Usługi dla HoReCa - Padir” (domyślny: tytuł strony + nazwa serwisu) | „Usługi dla przemysłu - Padir” |
| meta | „Grawerujemy szkło, sztućce, tabliczki na drzwi i karty menu dla hoteli i restauracji. Krótkie serie, powtarzalna jakość. Pracownia w Warszawie.” | „Tabliczki znamionowe, znakowanie części, cięcie i frezowanie CNC dla produkcji. Realizujemy serie powtarzalne z zachowaniem tolerancji.” |
| h1 | „Detal, którego dotyka Twój gość.” | „Precyzyjne usługi dla przemysłu.” |
| h2 | hasła z nazwą produktu: „Wszystko, co gość weźmie do ręki.”, „Logo na każdym kieliszku gościa.”, „Karty menu z drewna.”, „Lokale, które grawerujemy.” | „Grawerowanie laserowe dla wymagających.”, „Cięcie konturowe blach i tworzyw.”, „Obróbka skrawaniem 3- i 5-osiowa.” |
| h3 | produkty zakresu („Tabliczki numerów pokoi”, „Grawer na szkle i kieliszkach”) i typy klientów („Hotele sieciowe i butikowe”) | usługi („Tabliczki znamionowe”, „Kody DMC, QR i numery seryjne”) i branże („Automotive”) |
| linki wychodzące | tylko `/kontakt/` (7 razy), `/przykladkowe-realizacje/` i martwe `#produkty` | `/kontakt/`, trzy strony usług („Zobacz usługę →”), „Poznaj frezowanie CNC”, `/przykladkowe-realizacje/`, martwe `#uslugi` |
| linki przychodzące | menu „Produkty”, 456, 1011, `/produkty/`, 1397 („hoteli i restauracji”), wpisy 2009 i 2550 | menu, 456, 1011, `/produkty/`, 1397 („producentów”), wpisy 1673, 2009, 2078, 2545 |

Wnioski:
- Siostry niosą frazy w meta, h2 i h3, a tytuł SEO „Usługi dla … - Padir” nie zawiera niczego, czego ktoś szuka.
  Dla marketingu proponuję własny tytuł SEO (punkt 5). „Usługi dla marketingu” zostaje nazwą strony, eyebrow w hero
  i pozycją menu.
- Linkowanie wychodzące sióstr jest ubogie (HoReCa poza kontaktem i galerią nigdzie nie prowadzi). Nowa strona ma
  9 linków kontekstowych (punkt 3) i nie powtarza martwych kotwic.

### Frazy, pod które strona ma stanąć, i gdzie już są

| fraza (rdzeń) | miejsce na nowej stronie | fakt | gdzie już jest w serwisie |
|---|---|---|---|
| statuetki (na zamówienie, z plexi, jubileuszowe), nagrody dla firm, wyróżnienia | title, h1, h2 sekcji `#nagrody`, meta | F01, F02, F04, F05 | nigdzie w tytule ani h1. h2 „Tworzenie nagród i statuetek” w ramce „Nowość” na 1019 (`#nagrody`); h3 „Statuetki i nagrody” na `/produkty/` („Wyroby własne”); h2 „Statuetki i nagrody jubileuszowe” we wpisie 2177; karty INSOFT i „Statuetka z plexi” oraz zdanie „Robimy statuetki i nagrody” na 1397; akapit „Eventy, nagrody, statuetki” we wpisie 2208; kafel „Marketing i wydarzenia” w szkicu 456 |
| puchary | title, h1, zakres (bez materiału i technologii, F10) | Z02 | prawie nigdzie: jedno ogólne zdanie we wpisie 2208 i kafel w szkicu 456. Nowa strona będzie jedyną z tą frazą w tytule |
| upominki z logo, gadżety z logo (reklamowe, firmowe) | title, meta, h2 sekcji `#upominki` | F12-F21, F24 | rozproszona po wpisach: 2177 (tytuł „Prezenty firmowe z grawerem…”), 2009 (h2 „Upominki korporacyjne…”), „gadżety reklamowe” w 1757, 968, 762, 1868 i na 1212; `/produkty/` („upominki firmowe i okolicznościowe”, link do 1812); szkic 456 („Najczęściej grawerowane przedmioty”). Żadna strona ofertowa nie ma jej w tytule |
| napisy i logo przestrzenne (na event, do recepcji, na stoisko) | h2 sekcji `#event`, zakres | F37-F39, Z04 | 1397 (karty „Napis przestrzenny Tea/Team”, „Logo przestrzenne BOKO”, „Frezowana litera przestrzenna”), wpis 2293 („litery i logotypy przestrzenne”), obecna 1011 (karta HoReCa „Litery przestrzenne…”), `/produkty/` („litery 3D”), case BOKO na 1019 |
| dekoracje na event, ścianka fotograficzna | h2 sekcji `#event`, meta | F41-F44 | 1019 (case „Ścianka fotograficzna Bondi Sands”, h3 „Elewacja budynku na event”), case 2470, wpis 2293 („dekoracje eventowe”), wpis 2078 (mini-case ścianki), wpis 2009 (h2 „Branża eventowa”, o gadżetach) |
| ekspozytory POS | jedna karta zakresu z linkiem | F33-F35 | wpis 2043 (cały temat), 2293, 1397, `/produkty/` |
| segment: dla marek i agencji, na galę, konkurs, jubileusz firmy | lead, K10 „Kto zamawia”, meta | F47, F03 | 1397 („Pracujemy dla marek i agencji”), `/produkty/` („Projekt pod wydarzenie albo jubileusz firmy”) |
| Warszawa | tekst (odbiór, adres), wariant tytułu | L01, L04 | wszędzie; meta HoReCa kończy się „Pracownia w Warszawie.” |

Wniosek: statuetki/nagrody i puchary nie mają dziś żadnej strony ofertowej, a upominki z logo mają tylko wpisy
poradnikowe. Nowa strona przejmuje te trzy frazy jako pierwsza strona sprzedażowa (title, h1, meta). Napisy
przestrzenne, dekoracje eventowe i POS są już podzielone między wycinanie (1019, 2293), frezowanie (1011) i wpisy,
więc tutaj idą do h2 i tekstu, zawsze w kontekście marki i wydarzenia, nie do tytułu.

---

## 2. Kanibalizacja

Podział ról po publikacji:
- `/uslugi-dla-marketingu/`: oferta dla segmentu i wycena; główna strona dla „statuetki”, „puchary”, „upominki z logo”,
  „nagrody dla firm”;
- strony usług (456, 1019, 1011): technologia i materiały, odsyłają do branż;
- `/grawerowanie-laserowe/prezenty/` (1812): prezenty osobiste na okazje (klient indywidualny);
- wpisy: poradniki („co dać”, „jak działa”, „jak powstaje ekspozytor”).

### K1. 1019 `/wycinanie-laserowe/`, ramka „Nowość: Tworzenie nagród i statuetek” (największe ryzyko)
To jedyna opublikowana strona z h2 o nagrodach, a sama zapowiada: „Osobna strona poświęcona nagrodom powstaje”.
Nowa strona de facto nią jest (P11).
- Nie używać h2 „Tworzenie nagród i statuetek”. Nie przepisywać zdań ramki („Projektujemy i wykonujemy statuetki,
  nagrody jubileuszowe i wyróżnienia, wycinane i grawerowane w plexi, drewnie i innych materiałach.”, „Każda
  w indywidualnym kształcie, dopasowanym do okazji i identyfikacji marki.”). Fakty F01 i F02 własnymi słowami.
- Nie linkować do `/wycinanie-laserowe/#nagrody` (link w kółko, a ramka obiecuje „wkrótce”). Kierunek odwrotny:
  ramka na 1019 linkuje tutaj (punkt 4).
- Case studies z 1019 (Bondi Sands, BOKO): bez zdań z bloków „Wyzwanie / Rozwiązanie / Efekt”. Bondi Sands tylko
  wspólnym mianownikiem z S02: lustrzana, złota ścianka foto na letni event nad Wisłą, gotowa w terminie. Bez „plaży”
  i bez „barki”.
- Bez „Nowość” i bez „od lat robimy statuetki” (S10).

### K2. Wpis 2177 „Prezenty firmowe z grawerem. Co się sprawdza i ile to trwa”
Najbliższy temat dla upominków, do tego h2 „Statuetki i nagrody jubileuszowe”. W treści serwisu ma jeden link
przychodzący (z 2208), poza blokiem najnowszych wpisów na stronie głównej.
- Nowa strona nie ma „prezenty firmowe” w title, h1 ani h2. Używa „upominki z logo” i „gadżety z logo”. „Prezenty
  firmowe” najwyżej w anchorze linku do 2177, co wzmacnia wpis na jego frazę.
- Nie powielać układu wpisu (kubki, wino, świece, statuetki, powerbanki, drobiazgi) jako sekcji z poradami. Zakres na
  stronie to lista rzeczy do zamówienia, bez porad typu „anodowane aluminium daje czysty, jasny ślad”, „guma i soft
  touch: odradzamy”, „zapytanie w październiku”, „pięć błędów”, „prosty test: czy ten prezent przetrwa styczeń”,
  „statuetki nikt nie używa, ona ma stać i przypominać”, „różnicowanie serii kosztuje niewiele, bo zmienia się plik”.
- Fakty z 2177 (100 zł, odpowiedź w 24 h, od 1 sztuki, sztuka do akceptacji przed serią) wolno, zdań nie.
- „Większość prezentów firmowych ląduje w szufladzie…” nie wraca (fakty.md, rozdział 8).

### K3. 1812 `/grawerowanie-laserowe/prezenty/` („Grawerowanie na prezent”)
Prezenty osobiste: komunia, ślub, walentynki, rodzice. Inna intencja, ryzyko małe, ale dwa linki dziś mylą role:
wpis 2009 linkuje do 1812 anchorem „Grawerowane upominki korporacyjne”, a wpis 2177 kończy się przyciskiem „Zobacz
ofertę prezentów” do 1812 (punkt 4).
- Na nowej stronie bez „grawerowane prezenty”, „prezent z grawerem”, „na każdą okazję” i okazji osobistych.
- Nie przenosić „+20% wartości” i „zapłacą o 20% więcej” (BRIEF) ani adresu „Budynek B8, wejście 1A” (S08).
- W treści głównej bez linku do 1812 (rezerwa: FAQ o pojedynczym prezencie prywatnym).

### K4. Wpis 2009 „5 branż, które z powodzeniem wykorzystują grawer laserowy do zwiększenia sprzedaży”
h2 „Upominki korporacyjne [półpauza] subtelna sztuka budowania relacji” i „Branża eventowa [półpauza] wydarzenia,
które pozostają w pamięci”. Wpis linkuje sekcje gastronomii i elektroniki do sióstr, sekcja eventowa nie ma celu.
- Nie przepisywać list produktów z wpisu jako oferty (pióra, powerbanki z logo eventu, paski do smartwatchy, smycze,
  skrzynki na wino, notesy). Smycze i paski nie mają realizacji (P23).
- Nie przenosić „Deloitte 2022, 36%”, „inwestycja, która szybko się zwraca”, równania z Instagramem (rozdział 8).
- Z nowej strony bez linku do 2009. W drugą stronę tak (punkt 4).

### K5. Wpis 1757 „Grawerowanie Laserowe w Biznesie - Jak Może Pomóc w Promocji Twojej Marki?”
„Marketing” pada tu 12 razy, h2 „Korzyści z Wykorzystania Grawerowanych Przedmiotów w Strategii Marketingowej”. Wpis
ma jednak h2 „Case Study [półpauza] do stworzenia.” (resztka szablonu) i obietnicę „nasi graficy” bez pokrycia (F53).
- Na nowej stronie bez nagłówków o „strategii marketingowej”, „promocji marki” i „korzyściach”. Strona mówi
  o produktach i zamówieniu.
- Bez linku do 1757, dopóki ma placeholder. Dla klienta: poprawić wpis albo zostawić jako poradnik z linkiem do nowej
  strony.

### K6. Wpisy 968, 762, 1868 i strona 1212: „gadżety reklamowe”
Ogólne wzmianki w poradnikach, ryzyko małe. Nowa strona może mieć „gadżety z logo” w meta i tekście. Nie kopiuje
przykładów z tych tekstów (drewniane długopisy, torby i odzież z logo w 762, „ekologiczne gadżety” w 968) ani
twierdzeń o lojalności klientów (968).

### K7. Wpis 2043 (ekspozycje dla marek kosmetycznych) i wpis 2293 (wycinanie laserowe)
2043 to jedyna treść o ekspozytorach. 2293 ma zdania „Najwięcej realizacji robimy dla reklamy i punktu sprzedaży:
ekspozytory, standy, displaye, listwy, podstawki.” i „Drugi duży obszar to litery i logotypy przestrzenne. Wycinamy
je z plexi lub sklejki, w rozmiarach od małych tabliczek po duże napisy na ścianę.”
- Ekspozytory to na nowej stronie jedna karta zakresu z linkiem do 2043. Bez słownika „dekoracja, ekspozytor,
  gloryfier”, bez pianki, HIPS i folii, bez marek BOSS, YSL, Versace (P14), bez „25-30% sprzedaży”.
- Dwóch zdań z 2293 nie przepisywać. PVC i poliwęglanu nie łączyć z laserem (S09).

### K8. 1011 `/frezowanie-cnc/` i szkic nowej 1011
Frezowanie ma „litery 3D” (`/produkty/`), kartę „Litery przestrzenne…” przy HoReCa na obecnej 1011, a szkic ma
sekcję „Nośnik z frezarki, front z lasera” o ściance foto.
- Litery frezowane to na nowej stronie jedna wzmianka z linkiem do `/frezowanie-cnc/`. Bez frezów, kerfu i pola 2 × 3 m.
- Nie przepisywać akapitu szkicu frezowania o ściance („Fronty z lustrzanej plexi wycięliśmy laserem…”).
- Spójność: szkic frezowania pisze „ścianka fotograficzna na barce na Wiśle” (za wpisem 2078), 1019 „na plaży”.
  Na nowej stronie żadna z tych wersji (S02, P08, L04 w `pytania.md`).

### K9. Szkic nowej 456: „Branże, w których grawerujemy” i „Najczęściej grawerowane przedmioty”
Szkic ma kafel „Marketing i wydarzenia” (opis „Statuetki i puchary na gale i konkursy oraz grawerowane upominki z logo
dla klientów i pracowników.”, link „Grawer dla marketingu”) oraz kafle: Kieliszki, Prezenty, Noże, Powerbanki
i pendrive'y, Kubki i butelki termiczne, Tabliczki znamionowe. FAQ szkicu: „Czy zrobicie grawer na jednej sztuce?”,
„Ile się czeka na grawer?”, „Od czego zależy cena?”, „Czy mogę przynieść własny przedmiot?”.
- Siatka upominków na nowej stronie nie powtarza opisów kafli 456 (np. „Logo firmy albo imię na metalowej obudowie.
  Sprawdzają się jako upominek na konferencję albo dla klientów.”) i lepiej, żeby nie miała tych samych h3 („Kubki
  i butelki termiczne”, „Powerbanki i pendrive'y”). Pisze od strony zamówienia firmowego: seria z logo, różne imiona
  w jednej serii (F50), wysyłka kurierem (L04).
- FAQ nowej strony: inne pytania i inne zdania niż FAQ szkicu 456 i FAQ `/produkty/`. Te same fakty (100 zł; 2 dni
  albo od ręki za dopłatą) innymi słowami.
- Opis kafla „Marketing i wydarzenia” nie wraca na nowej stronie w tym samym brzmieniu.

### K10. Siostry 2283 i 2264
- Nie przenosić: „Próbka graweru gratis dla nowych klientów”, „Próbka kontrolna gratis” (S06, P19); zdania „Wycena
  w 24 godziny.” jeden do jednego (fakt F74 innymi słowami); liczb z hero sióstr („setki i tysiące”, „5-10 dni”,
  „24-72 h”, „±0,01 mm”); kroków K6; „NDA dla każdego projektu B2B” (P21); formuły „Jeden dostawca, jeden termin,
  jedna faktura.” (F51 własnymi słowami).
- Kieliszki i karafki z logo to rdzeń HoReCa (h2 „Logo na każdym kieliszku gościa.”). Na nowej stronie szkło tylko
  jako upominek (np. karafka Mercure w kontekście prezentu, R05), bez nagłówka o kieliszkach.

### K11. `/produkty/` (8) i 1397: rozdzielniki
`/produkty/` ma kartę „Statuetki i nagrody” („Plexi, drewno, szkło i metal. Projekt pod wydarzenie albo jubileusz
firmy.”), 1397 zdanie „Robimy statuetki i nagrody, ekspozytory POS, litery i logotypy reklamowe, personalizowane
upominki…”. Zdań nie przepisywać. Szkła i metalu przy statuetkach nie podawać (S11, P02).

### K12. Szkice
1841 „Długopisy z grawerem jako wsparcie marketingowe dla firm”: gdyby wyszedł, celowałby w „marketing”. Wtedy wpis
bierze frazę „długopisy z grawerem” i linkuje do nowej strony, a nie odwrotnie. 1786 i 1731 („Najczęściej
grawerowane przedmioty”) bez linków.

### Czego nie powielać (skrót)
- ramka „Nowość” i case studies z 1019 (zdania), h2 „Tworzenie nagród i statuetek”;
- układ i porady wpisu 2177, zdanie o szufladzie;
- listy produktów i statystyki z 2009, korzyści i placeholder z 1757, słownik, materiały i marki z 2043;
- dwa zdania z 2293, karta „Statuetki i nagrody” z `/produkty/`, zdanie o zakresie z 1397;
- kafle i FAQ szkicu 456, akapit o ściance ze szkicu 1011;
- „gratis”, liczby z hero i kroki sióstr; „20%” z 1812.

---

## 3. Linki wewnętrzne do wstawienia (9)

Wszystkie adresy mają status `publish` w `SPIS.json`; kotwicę `#galeria` na 1397 sprawdziłem w kodzie. Zapis względny
(`/adres/`), jak u sióstr. Sekcje według slotów z `wzorzec-pdl.md` (3.1). Id sekcji to propozycja dla autora treści
(jeśli je zmieni, zmienia też kotwice): s02 `id="zakres"` (cel przycisku ghost w hero), s04 K7 `id="nagrody"`,
s05 K7 `id="event"`, s06 K8 `id="upominki"`. Karty K3 w s01 prowadzą do tych trzech id (kotwice na stronie, poza
licznikiem).

| # | adres | anchor (propozycja) | sekcja | po co |
|---|---|---|---|---|
| 1 | `/blog/firmowe-prezenty-z-grawerem/` | „poradnik o prezentach firmowych z grawerem” (np. „Co sprawdza się jako upominek dla klientów i ile trwa seria, opisaliśmy w poradniku o prezentach firmowych z grawerem.”) | s06 Upominki (K8), zdanie pod siatką | oddaje frazę poradnikową wpisowi (K2) i daje mu drugi link w treści |
| 2 | `/grawerowanie-laserowe/grawerowanie-na-nozu/` | „noże z grawerem” (karta: noże z logo albo monogramem, także w kompletach prezentowych, F24) | s06 Upominki, karta noży | jedyna opublikowana strona produktu-upominku z ofertą dla firm |
| 3 | `/grawerowanie-laserowe/` | „grawerem laserowym” (np. „Logo na kubkach, szkle i obudowach nanosimy grawerem laserowym, więc znak jest w materiale, a nie na nim.”, W02) | s06 Upominki, tekst nagłówka K2 | strona usługi, jak „Zobacz usługę” u Przemysłu |
| 4 | `/wycinanie-laserowe/` | „wycinaniu laserowym” (np. „Litery, logo i ścianki z plexi i sklejki tniemy laserem. Więcej o tym na stronie o wycinaniu laserowym.”, F37, Z04) | s05 Event (K7), tekst | strona usługi; NIE `#nagrody` (K1) |
| 5 | `/frezowanie-cnc/` | „frezowanie CNC” (np. „Grubsze litery z drewna albo konglomeratu robimy na frezarce, zobacz frezowanie CNC.”, F39, F40) | s05 Event, tekst albo punkt listy | strona usługi |
| 6 | `/blog/tworzenie-ekspozycji-dla-marek-kosmetycznych/` | „jak robimy ekspozycje dla marek kosmetycznych” | s02 Zakres (K4), karta „Ekspozytory” | jedyna treść o POS; strona jej nie powiela (K7) |
| 7 | `/case-study/zamek-sulkowskich/` | „800 metrów tkaniny na elewację Zamku Sułkowskich” (rola Padiru: cięcie z projektu klienta, F44) | s05 Event, tekst albo punkt listy | opublikowany case eventowy. Zdjęcia zamku nie podpisywać jako realizacji bez obejrzenia (BRIEF: na murze jest cudza instalacja) |
| 8 | `/przykladkowe-realizacje/#galeria` | „Zobacz wszystkie realizacje” (przycisk ghost pod siatką, poprawka U10 z `wzorzec-pdl.md`) | s07 Realizacje (K9) | galeria |
| 9 | `/materialy-do-grawerowania/` | „listę materiałów do grawerowania” (FAQ np. „Mamy już kubki z hurtowni. Wygrawerujecie na nich logo?”, odpowiedź z F48 i F18, na końcu „Sprawdź listę materiałów do grawerowania albo przyślij zdjęcie przedmiotu.”) | s09 FAQ (K11) | typowe pytanie agencji; inne niż „Czy mogę przynieść własny przedmiot?” w szkicu 456 |

Poza licznikiem, z szablonu: `/kontakt/` (hero, K6, K7, karta CTA w K4, pas K12; sprawdzarka go wymaga)
i `/przykladkowe-realizacje/` w pasie K12 („Zobacz realizacje”).

Zasady anchorów:
- opisują cel, każdy inny; bez nazw klientów (wyjątek: case zamku, który ma nazwę w adresie i tytule); bez „kliknij
  tutaj”; bez „Zobacz zakres →” (tak `/produkty/` linkuje do sióstr);
- jeden link do danego adresu na stronie (wyjątek: `/kontakt/` i `/przykladkowe-realizacje/` z szablonu);
- w zdaniach przykładowych tylko fakty z `fakty.md`; to propozycje brzmienia, nie gotowy tekst.

Linki na tej samej stronie: wyłącznie `href="#id"`. Nie pisać `/uslugi-dla-marketingu/#…`: `sprawdz_szkic.py` bez
`--szkic` uzna to za błąd (adres jest na liście `PLANOWANE`, czyli strony jeszcze nie ma).

### Rezerwa (zamiennie, łącznie nie więcej niż 10)
- `/wycinanie-laserowe/#realizacje`, anchor „ścianka Bondi Sands i logo BOKO”, zamiast #4, jeśli sekcja Event
  pokazuje te dwa case'y (id `realizacje` jest na 1019). Nie dawać dwóch linków do 1019.
- `/blog/wycinanie-laserowe-precyzyjne-ciecie-plexi-sklejki-i-laminatu-na-zamowienie/`, anchor „litery i logotypy
  z plexi i sklejki”, zamiennie z #4.
- `/grawerowanie-laserowe/prezenty/`, anchor „prezent z grawerem dla jednej osoby”, tylko w FAQ o pojedynczym
  prezencie prywatnym (K3).
- `/case-study/`, anchor „nietypowe projekty”, jeśli na stronie będzie zdanie o realizacjach spoza katalogu.
- `/produkty/`, anchor „grawer, cięcie i frezowanie w jednym zleceniu” (F51), zamiennie z #3-#5.

### Nie linkować
- szkice 1841, 1786, 1731, 2530; `/torebki/` i `/realizacje/` (nie ma ich w `SPIS.json`);
- `/wycinanie-laserowe/#nagrody` (K1) i „Zobacz pełny case” Bondi Sands (`#`);
- wpisy 2009, 1757, 968, 762, 1868 (K4-K6: twierdzenia bez pokrycia, placeholder, ogólniki);
- wpis 1546 (anegdoty bez wykonawcy, Ekstraklasa niepotwierdzona: F29, F31, F32, P12, P13);
- wpis 1851 (prezent na urodziny, klient indywidualny);
- wpis 2078 (barka kontra plaża, „99%”: S02, rozdział 8), dopóki nie ma odpowiedzi na P08;
- wpis 1660 (błędne „2500 × 1650 mm”, S04);
- `/case-study-wosp/` (akcja charytatywna, R12, inny kontekst);
- `/o-nas/` w treści (liczby D03 bez potwierdzenia, P20);
- siostry `/uslugi-dla-horeca/` i `/uslugi-dla-przemyslu/` w treści: one też się nawzajem nie linkują, wystarczy menu.

---

## 4. Gdzie potem dodać link DO nowej strony (rekomendacja, teraz nic nie zmieniamy)

Kolejność: najpierw publikacja strony marketingowej, potem linki do niej. Szkic 456 już linkuje do
`/uslugi-dla-marketingu/` (kafel „Marketing i wydarzenia” w sekcji „Branże, w których grawerujemy”, anchor „Grawer dla
marketingu”), więc nowej 456 nie wolno opublikować przed stroną marketingową. Sprawdzarka zgłasza to w szkicu jako
ostrzeżenie, a bez `--szkic` jako błąd.

| prio | gdzie | miejsce | anchor | warunek, uwaga |
|---|---|---|---|---|
| 1 | menu „Produkty” | po „Usługi dla HoReCa” | „Usługi dla marketingu” | tak jak siostry |
| 2 | szkic nowej 456 | kafel „Marketing i wydarzenia” | „Grawer dla marketingu” (już jest) | publikować po stronie marketingowej albo razem z nią |
| 2a | obecna 456, jeśli marketing wejdzie przed nową 456 | sekcja „Grawerujemy dla przemysłu i dla gastronomii.” (dwie karty) | trzecia karta „Usługi dla marketingu” | zmienić też nagłówek sekcji |
| 3 | 1019, ramka „Nowość: Tworzenie nagród i statuetek” | w miejsce zdania „Osobna strona poświęcona nagrodom powstaje, wkrótce znajdziesz tu pełną ofertę i realizacje.” | „statuetki, puchary i nagrody dla firm” → `/uslugi-dla-marketingu/#nagrody`; przycisk „Zapytaj o nagrodę na zamówienie” zostaje przy `#kontakt` | zależy od P11; najlepiej jedną edycją razem z wdrożeniem krótszego formularza na 1019 (zadanie w toku) |
| 3a | 1019, case „Ścianka fotograficzna Bondi Sands” | przycisk „Zobacz pełny case” (dziś `#`) | „Ścianki i dekoracje na event” → `/uslugi-dla-marketingu/#event` albo usunąć przycisk | dopóki nie ma pełnego case'u (P08); nie udawać case'u |
| 4 | `/produkty/` | sekcja „Trzy grupy klientów, trzy różne potrzeby.” (dziś 3 karty, do sióstr i do 1812) | czwarta karta „Marketing i eventy” z „Zobacz zakres →”, jak karty sióstr | zmienić nagłówek i siatkę (4 karty) |
| 4a | `/produkty/` | karta „Statuetki i nagrody” w „Wyroby własne”, dziś „Zobacz realizacje →” do 1397 | „Zobacz statuetki i nagrody →” → `/uslugi-dla-marketingu/#nagrody` | przy okazji materiały „szkło i metal” do potwierdzenia (P02) |
| 5 | 1397 `/przykladkowe-realizacje/` | zdanie „Pracujemy dla marek i agencji, hoteli i restauracji, producentów…” | „marek i agencji” | dwa kolejne człony już linkują do sióstr |
| 6 | szkic nowej 1011 | sekcja „Nośnik z frezarki, front z lasera” | „ścianki i dekoracje na event” → `/uslugi-dla-marketingu/#event` | obecna 1011: trzecia karta w „Frezujemy dla przemysłu i dla gastronomii.”, jeśli marketing wejdzie wcześniej |
| 7 | wpis 2009 | sekcja „Branża eventowa” | „Branża eventowa” albo „nagrody i gadżety na eventy” | tak jak sekcje gastronomii i elektroniki linkują do sióstr. Przy okazji anchor „Grawerowane upominki korporacyjne” (dziś do 1812, prezenty na komunię i ślub) lepiej przestawić na wpis 2177 (L03) |
| 8 | wpis 2177 | koniec sekcji „Statuetki i nagrody jubileuszowe”; przycisk „Zobacz ofertę prezentów” (dziś do 1812) | „statuetki i nagrody na zamówienie”; przycisk → „Zobacz ofertę dla firm” `/uslugi-dla-marketingu/#upominki` | 1812 ma i tak kilkanaście linków przychodzących |
| 9 | wpis 2208 | akapity „Reklama i branding” albo „Eventy, nagrody, statuetki” | „statuetki i nagrody na eventy” | jeden link; wpis ma też resztki szablonu w h3 („Strategic ulting”, „Digital Marketing”) |
| 10 | wpis 2043 | ostatni akapit | „ekspozytory i dekoracje dla marek” | |
| 11 | wpis 2293 | sekcja „Zastosowania wycinania laserowego” | „litery i logotypy przestrzenne” | |
| 12 | wpisy 1546, 1757, 2078 | 1546 po odpowiedziach na P12 i P13; 1757 po usunięciu placeholdera; 2078 po P08 | | niski priorytet |
| 13 | stopka | dziś: trzy usługi, Poznaj Padir, Kontakt, Blog, Polityka; sióstr nie ma | nie dodawać samej strony marketingowej; ewentualnie kolumna „Branże” z trzema stronami naraz | spójność z siostrami |
| 14 | strona główna | dziś bez linków do sióstr | bez zmian; ewentualnie później blok trzech branż | |
| 15 | `/case-study/` (2487) | gdy powstanie pełny case Bondi Sands | | P08 |

Z menu, 456, 1019, `/produkty/`, 1397, 1011 i pięciu wpisów nowa strona dostałaby linki z 11 miejsc. Siostry mają dziś
po 6-8 stron linkujących plus menu.

---

## 5. Title, meta description, nazwa w menu

Wszystko bez myślników i półpauz. Liczone znaki ze spacjami.

**Nazwa w menu i tytuł strony w WordPressie:** `Usługi dla marketingu` (21 znaków; konwencja „Usługi dla przemysłu”,
„Usługi dla HoReCa”). Slug `uslugi-dla-marketingu`. Ten sam tekst w eyebrow hero.

**Title (53 znaki):**
`Statuetki, puchary i upominki z logo dla firm | Padir`

Wariant lokalny (53 znaki): `Statuetki, puchary i upominki z logo | Padir Warszawa`

Tytuł trzeba wpisać ręcznie w pole SEO. Bez tego serwis wstawi „Usługi dla marketingu - Padir” jak u sióstr, czyli
tytuł bez żadnej frazy. Separator „|”, jak w propozycji tytułu dla nowej 456.

**Meta description (144 znaki):**
`Statuetki i nagrody z plexi, puchary, upominki z logo, napisy przestrzenne i dekoracje na event dla marek i agencji. Od 1 sztuki, wycena w 24 h.`

Źródła (fakty, nie zdania):
- statuetki i nagrody z plexi: F01, F04 (`pages-1019-wycinanie-laserowe.txt` «wycinane i grawerowane w plexi, drewnie
  i innych materiałach», karty INSOFT i „Statuetka z plexi”);
- puchary: Z02 (zleceniodawca, 13.10.2026), bez materiału i technologii (F10);
- upominki z logo: F12 (`pages-8-produkty.txt` «upominki firmowe i okolicznościowe»), F15, F75 («plik z logo»);
- napisy przestrzenne: F37, F39; dekoracje na event: F43 (`posts-2293-…txt` «dekoracje eventowe i wnętrzarskie»);
- dla marek i agencji: F47 (`pages-1397-przykladkowe-realizacje.txt` «Pracujemy dla marek i agencji»);
- od 1 sztuki: F67; wycena w 24 h: F74.

Meta nie zaczyna się od „Grawerujemy…” (tak zaczyna HoReCa) i nie zawiera „prezenty firmowe” (2177) ani listy
materiałów (`/materialy-do-grawerowania/`, obecna meta 456).

**h1 (propozycja dla autora, 2 wiersze po 18 znaków jak u sióstr):** `Statuetki, puchary<br>i upominki z logo.`
Nie w title ani h1: „prezenty firmowe” (2177), „grawerowanie laserowe” (456), „wycinanie laserowe” (1019),
„prezent z grawerem” (1812), „usługi dla marketingu” jako jedyna fraza.

---

## 6. Pytania dopisane do `pytania.md`

Dopisałem sekcję „Linkowanie i nazwa” z pytaniami L01-L04 (osobna numeracja, żeby nie zderzyć się z P..):
nazwa strony i menu, zgoda na linki z istniejących stron, anchor „Grawerowane upominki korporacyjne” we wpisie 2009,
spójność opisu ścianki foto w szkicu frezowania.
