# Wzorzec .pdl: katalog komponentów stron branżowych

Do składania strony „Usługi dla marketingu” (`/uslugi-dla-marketingu/`, szablon `page-no-title`).
Źródła: `zrodla/pages-2283-uslugi-dla-horeca.raw.html` (HoReCa) i `zrodla/pages-2264-uslugi-dla-przemyslu.raw.html` (Przemysł).
Obie siostry mają ten sam arkusz co do znaku (diff linii 1-149 pusty) i ten sam układ 11 sekcji.
Zrzuty i pomiary: 13.10.2026, Playwright (`/opt/pw-browsers/chromium`) w ramie `marketing/zywa-horeca.html`, 1440 i 390 px.
Na żywej HoReCa tekst kontenera jest identyczny z plikiem `.raw.html` (porównane słowo po słowie), więc zrzuty pokazują stronę produkcyjną.

Spis: 0. Pliki pomocnicze · 1. Opakowanie · 2. Arkusz, tokeny, kontrast, dopisek · 3. Komponenty K1-K14, mapa sekcji, tła, siatki · 4. Usterki szablonu U1-U19 · 5. Lista kontrolna składacza

---

## 0. Pliki pomocnicze (wszystkie w `praca/marketing/`)

| plik | co to |
|---|---|
| `wzorzec-horeca-1440.png`, `wzorzec-horeca-390.png` | cała HoReCa w ramie motywu, stan obecny |
| `wzorzec-horeca-1440-sNN.png`, `wzorzec-horeca-390-sNN.png` | każda `<section>` osobno; NN = numer z mapy sekcji (p. 3.1) |
| `wzorzec-przemysl-…png` | to samo dla Przemysłu |
| `wzorzec-*-pomiar.json` | przewijanie w bok, niewczytane zdjęcia, każda para kolor tekstu/tło z kontrastem i progiem, tła i wysokości sekcji |
| `wzorzec-horeca-poprawiona.html`, `wzorzec-przemysl-poprawiona.html` | siostry z naniesionymi poprawkami U1, U2, U4-U11 (dowód: `sprawdz_szkic.py --pdl` kod 0, pomiar kontrastu 0 błędów w 1440 i 390) |
| `wzorzec-horeca-poprawiona-1440-sNN.png`, `wzorzec-horeca-poprawiona-390-s07.png` | zrzuty po poprawkach |
| `wzorzec-pdl-dopisek.css` | dopisek do arkusza z p. 2.4, gotowy do wklejenia |
| `wzorzec-podglad.py` | lokalny podgląd dowolnego pliku z `<div class="pdl">` w ramie żywej HoReCa, bez WordPressa |

Podgląd strony składacza (zdjęcia bierze z `podglad-media/`, brakujące dociąga do `praca/marketing/wzorzec-media/`):

```
cd S && python3 -I praca/marketing/wzorzec-podglad.py praca/marketing/strona.html praca/marketing/podglad --sekcje
```

Wynik: `podglad-1440.png`, `podglad-390.png`, `podglad-<szer>-sNN.png` i `podglad-pomiar.json` (klucz `zly_kontrast` ma być pusty, `przewijanie_w_bok` = 0, `niezaladowane` = []).
Opcja `--css PLIK.css` dokleja CSS na koniec arkusza (do testów).

---

## 1. Opakowanie strony

Plik `praca/marketing/strona.html` to cała treść strony w zapisie bloków, dokładnie w tej postaci co `zrodla/*.raw.html`.
`szkic_wdroz.py marketing` czyta właśnie ten plik i zapisuje go jako szkic `uslugi-dla-marketingu`, szablon `page-no-title` (uruchamia to człowiek prowadzący, nie agent).

Drzewo:

```
<!-- wp:group {align:full, padding 0, margin 0} -->          blok Grupa, pełna szerokość
  <div class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding:0">
    <!-- wp:html -->                                         JEDEN blok Własny HTML na całą stronę
    <div class="pdl">                                        kontener, do niego zawężony arkusz
      <style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">  arkusz W ŚRODKU .pdl, jako pierwsze dziecko
      <section class="pdl-hero">                             s00
      <section class="pdl-sec pdl-sec--wash">                s01 (szare tło)
      <section class="pdl-sec">                              s02 (białe tło)
      …                                                      na przemian
      <section class="pdl-sec"> … <div class="pdl-band">     ostatnia: pas CTA na białym
    </div>
    <!-- /wp:html -->
  </div>
<!-- /wp:group -->
(opcjonalnie) <!-- wp:html --> <script type="application/ld+json"> … <!-- /wp:html -->   tylko na 2264, K14
```

Gotowy szkielet do skopiowania (komentarze bloków dosłownie z 2283):

```html
<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"0","bottom":"0","left":"0","right":"0"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding:0">
<!-- wp:html -->
<div class="pdl">
<style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">
[[arkusz z p. 2.1 bez znaczników style, a na końcu dopisek z p. 2.4]]
</style>
[[sekcje K1 … K12]]
</div>
<!-- /wp:html -->
</div>
<!-- /wp:group -->
```

Jak to odtworzyć i czego pilnować:

- Komentarz `<!-- wp:group … -->` przepisz znak w znak (JSON w jednej linii). Inny JSON albo brak `"align":"full"` i edytor uzna blok za uszkodzony, a szare tła `--wash` skończą się na szerokości treści zamiast iść od krawędzi do krawędzi okna (rodzic `post-content` ma `is-layout-constrained`).
- Wszystko w JEDNYM bloku `wp:html`. Liczba `<!-- wp:html -->` = liczba `<!-- /wp:html -->`, tak samo `wp:group` (sprawdzarka, reguła `bloki`).
- Arkusz leży W ŚRODKU `<div class="pdl">`. To inaczej niż na stronach `.pdw` (1019), gdzie arkusz stoi obok kontenera. Atrybuty `data-no-optimize="1" data-no-minify="1" data-no-ucss="1"` obowiązkowe (LiteSpeed).
- Szablon `page-no-title` nie pokazuje tytułu WordPressa, więc jedyny `<h1>` to `.pdl-h1` w hero.
- Bez formularza CF7. Kontakt to przyciski do `/kontakt/` (sprawdzarka `--pdl` wymaga co najmniej jednego).
- Blok Własny HTML nie dostaje `wpautop`, ale `wptexturize` zmienia widoczny tekst: „ - ” ze spacjami na półpauzę, `--` na pauzę, proste cudzysłowy na drukarskie. Pisz od razu „…” i zakresy bez spacji (`2-3 dni`). Wnętrza `<style>` i `<script>` texturize nie rusza.
- Żadnych żółtych ramek `pdw-uwaga` ani napisu „Wersja robocza” (decyzja zleceniodawcy 13.10.2026; sprawdzarka bez `--szkic` traktuje je jako błąd).

---

## 2. Arkusz .pdl

### 2.1 Arkusz dosłownie z 2283 (linie 5-149; w 2264 identyczny)

Kopiuj bez zmian. Poprawki idą osobnym dopiskiem na końcu (p. 2.4), żeby dało się je porównać z siostrami.

```html
<style data-no-optimize="1" data-no-minify="1" data-no-ucss="1">
.pdl{--pdl-navy:#12388C;--pdl-green:#175C43;--pdl-rust:#DE6B24;--pdl-ink:#141414;
  --pdl-mute:#5f5f5f;--pdl-grey:#9a9aa6;--pdl-line:#ededed;--pdl-wash:#F5F5F5;
  font-family:var(--wp--preset--font-family--poppins,'Poppins',sans-serif);color:var(--pdl-ink);}
.pdl *,.pdl *::before,.pdl *::after{box-sizing:border-box;}
.pdl img{max-width:100%;height:auto;}
.pdl h1,.pdl h2,.pdl h3,.pdl h4{color:#141414!important;margin:0;letter-spacing:-.015em;}
.pdl p{margin:0;}
.pdl a{color:var(--pdl-navy);}
.pdl-wrap{max-width:1220px;margin:0 auto;padding:0 24px;}
.pdl-eyebrow{display:inline-block;font-weight:600;font-size:13px;line-height:1;letter-spacing:.14em;
  text-transform:uppercase;color:var(--pdl-navy);margin:0 0 16px;}
.pdl-h1{font-weight:800;font-size:clamp(36px,5vw,58px);line-height:1.05;}
.pdl-h2{font-weight:700;font-size:clamp(26px,3.6vw,38px);line-height:1.14;}
.pdl-h3{font-weight:700;font-size:19px;line-height:1.3;}
.pdl-h4{font-weight:700;font-size:16.5px;line-height:1.3;}
.pdl-lead{font-weight:700;font-size:clamp(18px,2.2vw,22px);line-height:1.4;color:#141414;}
.pdl-txt{font-weight:300;font-size:16.5px;line-height:1.75;color:var(--pdl-mute);}
.pdl-txt-sm{font-weight:300;font-size:15px;line-height:1.7;color:var(--pdl-mute);}

/* przyciski */
.pdl-btns{display:flex;gap:14px;flex-wrap:wrap;align-items:center;}
.pdl-btn{display:inline-flex;align-items:center;gap:9px;font-weight:700;font-size:15.5px;line-height:1;
  text-decoration:none;padding:15px 26px;border-radius:16px 4px 16px 16px;transition:transform .18s,box-shadow .18s;}
.pdl-btn--main{background:var(--pdl-navy);color:#fff!important;}
.pdl-btn--main:hover{transform:translateY(-2px);box-shadow:0 14px 26px -14px rgba(18,56,140,.8);}
.pdl-btn--ghost{border:1.5px solid #d9d9d9;color:var(--pdl-ink)!important;}
.pdl-btn--ghost:hover{border-color:var(--pdl-navy);color:var(--pdl-navy)!important;}

/* HERO */
.pdl-hero{padding:52px 0 64px;}
.pdl-hero-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:52px;align-items:center;}
.pdl-hero-copy>*+*{margin-top:20px;}
.pdl-stats{display:flex;gap:12px;flex-wrap:wrap;list-style:none;padding:0;margin:28px 0 0;}
.pdl-stat{background:#fff;border:1px solid var(--pdl-line);border-radius:14px 4px 14px 14px;padding:11px 16px;}
.pdl-stat b{display:block;font-weight:800;font-size:16px;color:var(--pdl-navy);}
.pdl-stat span{font-weight:300;font-size:12.5px;color:var(--pdl-grey);}
.pdl-hero-media{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.pdl-shot{position:relative;overflow:hidden;border-radius:28px 8px 28px 28px;aspect-ratio:3/4;background:#eef1f7;}
.pdl-shot:nth-child(2){border-radius:8px 28px 28px 28px;margin-top:32px;}
.pdl-shot img{width:100%;height:100%;object-fit:cover;display:block;}

/* sekcje */
.pdl-sec{padding:76px 0;}
.pdl-sec--wash{background:var(--pdl-wash);}
.pdl-head{max-width:760px;margin-bottom:40px;}
.pdl-head .pdl-txt{margin-top:14px;}

/* karty filarow */
.pdl-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:22px;}
.pdl-card{background:#fff;border:1px solid var(--pdl-line);border-radius:34px 10px 34px 34px;overflow:hidden;
  display:flex;flex-direction:column;transition:transform .24s cubic-bezier(.2,.7,.2,1),box-shadow .24s;}
.pdl-card:hover{transform:translateY(-6px);box-shadow:0 26px 50px -30px rgba(20,20,20,.5);}
.pdl-card-img{aspect-ratio:4/3;background:#eef1f7;overflow:hidden;}
.pdl-card-img img{width:100%;height:100%;object-fit:cover;display:block;}
.pdl-card-body{padding:22px 24px 26px;display:flex;flex-direction:column;gap:11px;flex:1;}
.pdl-card-link{margin-top:auto;font-weight:700;font-size:14.5px;color:var(--pdl-navy);text-decoration:none;}
.pdl-card-link:hover{text-decoration:underline;}

/* karty produktowe z lista */
.pdl-prod{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,330px),1fr));gap:22px;}
.pdl-p{background:#fff;border:1px solid var(--pdl-line);border-radius:34px 10px 34px 34px;padding:26px 28px;
  display:flex;flex-direction:column;gap:12px;transition:border-color .2s;}
.pdl-p:hover{border-color:#d2d2d2;}
.pdl-p ul{list-style:none;margin:4px 0 0;padding:0;display:flex;flex-direction:column;gap:8px;}
.pdl-p li{position:relative;padding-left:20px;font-weight:300;font-size:14.5px;line-height:1.55;color:var(--pdl-mute);}
.pdl-p li::before{content:"";position:absolute;left:0;top:8px;width:7px;height:7px;border-radius:2px;background:var(--pdl-navy);}
.pdl-p--cta{background:var(--pdl-navy);border-color:transparent;}
.pdl-p--cta .pdl-h3,.pdl-p--cta .pdl-txt-sm{color:#fff!important;}
.pdl-p--cta a{color:#fff!important;font-weight:700;text-decoration:underline;text-underline-offset:4px;}

/* przed / po */
.pdl-ba{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:22px;margin-bottom:38px;}
.pdl-ba-item{background:#fff;border:1px solid var(--pdl-line);border-radius:34px 10px 34px 34px;overflow:hidden;}
.pdl-ba-item img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block;}
.pdl-ba-body{padding:20px 24px 24px;display:flex;flex-direction:column;gap:9px;}
.pdl-tag{align-self:flex-start;font-weight:700;font-size:11px;letter-spacing:.06em;text-transform:uppercase;
  color:#fff!important;padding:6px 12px;border-radius:20px;}
.pdl-tag--before{background:var(--pdl-rust);}
.pdl-tag--after{background:var(--pdl-green);}

/* kroki (kolejnosc niesie informacje) */
.pdl-steps{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:20px;counter-reset:k;}
.pdl-step{counter-increment:k;background:#fff;border:1px solid var(--pdl-line);
  border-radius:24px 6px 24px 24px;padding:22px 22px 24px;}
.pdl-step::before{content:counter(k,decimal-leading-zero);display:block;font-weight:800;font-size:13px;
  color:var(--pdl-navy);letter-spacing:.08em;margin-bottom:10px;}

/* sekcja szczegolowa */
.pdl-detail{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:52px;align-items:center;}
.pdl-detail--rev .pdl-detail-media{order:-1;}
.pdl-detail-copy>*+*{margin-top:18px;}
.pdl-detail-media img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;border-radius:34px 10px 34px 34px;}
.pdl-checks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:11px;}
.pdl-checks li{position:relative;padding-left:26px;font-weight:300;font-size:15.5px;line-height:1.6;color:var(--pdl-mute);}
.pdl-checks li::before{content:"";position:absolute;left:0;top:6px;width:12px;height:7px;
  border:solid var(--pdl-green);border-width:0 0 2.5px 2.5px;transform:rotate(-45deg);}

/* materialy */
.pdl-mats{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:20px;}
.pdl-mat{background:#fff;border:1px solid var(--pdl-line);border-radius:28px 8px 28px 28px;overflow:hidden;}
.pdl-mat img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block;}
.pdl-mat-body{padding:18px 20px 22px;display:flex;flex-direction:column;gap:8px;}

/* galeria */
.pdl-gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,220px),1fr));gap:14px;}
.pdl-gal img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block;border-radius:22px 6px 22px 22px;}

/* branze */
.pdl-branze{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:20px;}
.pdl-branza{background:#fff;border:1px solid var(--pdl-line);border-radius:28px 8px 28px 28px;padding:24px 26px;
  display:flex;flex-direction:column;gap:10px;}
.pdl-branza-num{font-weight:800;font-size:12.5px;letter-spacing:.1em;color:var(--pdl-rust);}
.pdl-chips{display:flex;gap:7px;flex-wrap:wrap;margin-top:4px;}
.pdl-chip{font-weight:600;font-size:11px;letter-spacing:.04em;color:var(--pdl-navy);
  background:#E6ECF7;border-radius:20px;padding:5px 11px;}

/* FAQ */
.pdl-faq{display:flex;flex-direction:column;gap:10px;max-width:900px;}
.pdl-q{background:#fff;border:1px solid var(--pdl-line);border-radius:20px 6px 20px 20px;overflow:hidden;}
.pdl-q summary{cursor:pointer;list-style:none;padding:20px 24px;font-weight:700;font-size:16px;line-height:1.4;
  display:flex;justify-content:space-between;align-items:flex-start;gap:16px;}
.pdl-q summary::-webkit-details-marker{display:none;}
.pdl-q summary::after{content:"+";font-weight:400;font-size:24px;line-height:1;color:var(--pdl-navy);flex:none;}
.pdl-q[open] summary::after{content:"\2212";}
.pdl-q-a{padding:0 24px 22px;}

/* pas CTA */
.pdl-band{background:var(--pdl-navy);border-radius:44px 12px 44px 44px;padding:52px 44px;
  display:flex;gap:32px;align-items:center;justify-content:space-between;flex-wrap:wrap;}
.pdl-band .pdl-h2,.pdl-band .pdl-txt{color:#fff!important;}
.pdl-band .pdl-txt{opacity:.86;margin-top:12px;max-width:52ch;}
.pdl-band .pdl-btn--main{background:#fff;color:var(--pdl-navy)!important;}
.pdl-band .pdl-btn--ghost{border-color:rgba(255,255,255,.5);color:#fff!important;}

@media (max-width:640px){
  .pdl-sec{padding:56px 0;}
  .pdl-band{padding:36px 26px;border-radius:34px 10px 34px 34px;}
  .pdl-hero-media{gap:10px;}
  .pdl-shot:nth-child(2){margin-top:20px;}
}
@media (prefers-reduced-motion:reduce){.pdl *{animation:none!important;transition:none!important;}}
</style>
```

### 2.2 Adnotacja: reguły w użyciu

Sprawdzone skryptem na obu stronach: każda klasa zdefiniowana w arkuszu występuje w znacznikach, żadna klasa użyta w znacznikach nie jest niezdefiniowana. Martwych reguł nie ma.
W treści sióstr są tylko dwa atrybuty `style`: `margin-bottom:20px` na `<h3>` „Jak to działa” i `margin-top:32px` na `.pdl-btns` pod krokami.

| blok arkusza (komentarz) | reguły | komponent |
|---|---|---|
| baza | `.pdl`, `.pdl *`, `.pdl img`, `.pdl h1..h4`, `.pdl p`, `.pdl a`, `.pdl-wrap`, `.pdl-eyebrow`, `.pdl-h1..h4`, `.pdl-lead`, `.pdl-txt`, `.pdl-txt-sm` | wszystkie |
| przyciski | `.pdl-btns`, `.pdl-btn`, `--main`, `--ghost` (+ hover) | K13, używane w K1, K6, K7, K9, K12 |
| HERO | `.pdl-hero`, `-grid`, `-copy`, `.pdl-stats`, `.pdl-stat`, `.pdl-hero-media`, `.pdl-shot` | K1 |
| sekcje | `.pdl-sec`, `--wash`, `.pdl-head` | K2 |
| karty filarów | `.pdl-cards`, `.pdl-card`, `-img`, `-body`, `-link` | K3 |
| karty produktowe z listą | `.pdl-prod`, `.pdl-p`, `.pdl-p ul/li`, `.pdl-p--cta` | K4 |
| przed / po | `.pdl-ba`, `-item`, `-body`, `.pdl-tag`, `--before`, `--after` | K5 |
| kroki | `.pdl-steps`, `.pdl-step` (licznik CSS `k`, 01-04) | K6 |
| sekcja szczegółowa | `.pdl-detail`, `--rev`, `-copy`, `-media`, `.pdl-checks` | K7 |
| materiały | `.pdl-mats`, `.pdl-mat`, `-body` | K8 |
| galeria | `.pdl-gal` | K9 |
| branże | `.pdl-branze`, `.pdl-branza`, `-num`, `.pdl-chips`, `.pdl-chip` | K10 |
| FAQ | `.pdl-faq`, `.pdl-q`, `summary`, `.pdl-q-a` | K11 |
| pas CTA | `.pdl-band` (+ przyciski odwrócone) | K12 |
| media 640 px, reduced-motion | mniejsze paddingi sekcji i pasa, mniejsze przesunięcie drugiego zdjęcia w hero; wyłączenie animacji | wszystkie |

Tokeny:

| token | wartość | gdzie użyty (liczba `var()`) |
|---|---|---|
| `--pdl-navy` | `#12388C` | eyebrow, linki, liczba w `.pdl-stat`, przycisk główny, karta CTA, pas, chip, numer kroku, „+” w FAQ, kwadracik listy `.pdl-p` (14) |
| `--pdl-green` | `#175C43` | plakietka „Po”, ptaszek `.pdl-checks` (2) |
| `--pdl-rust` | `#DE6B24` | plakietka „Przed”, numer `.pdl-branza-num` (2) |
| `--pdl-ink` | `#141414` | kolor bazowy `.pdl`, tekst przycisku ghost (2) |
| `--pdl-mute` | `#5f5f5f` | `.pdl-txt`, `.pdl-txt-sm`, punkty list (4) |
| `--pdl-grey` | `#9a9aa6` | tylko podpis liczby w hero `.pdl-stat span` (1) |
| `--pdl-line` | `#ededed` | ramki kart (8) |
| `--pdl-wash` | `#F5F5F5` | tło `.pdl-sec--wash` (1) |

Kolory wpisane na sztywno: `#141414` (h1-h4 z `!important`, `.pdl-lead`), `#fff` (tło kart, tekst na granacie), `#d9d9d9` (ramka ghost), `#d2d2d2` (ramka `.pdl-p` na hover), `#eef1f7` (tło pod zdjęciem przed wczytaniem), `#E6ECF7` (tło chipa), `rgba(255,255,255,.5)` (ramka ghost w pasie).

Rzeczy w arkuszu, których nie wolno „poprawiać”:

- `.pdl h1,.pdl h2,.pdl h3,.pdl h4{color:#141414!important}` ma wagę (0,1,1) i przebija regułę motywu `div div div h3{color:…!important}` (0,0,4). Dlatego na stronach `.pdl` `<h3>` nie potrzebuje inline koloru, a `sprawdz_szkic.py --pdl` to akceptuje. Białe nagłówki w pasie i w karcie CTA (`.pdl-band .pdl-h2`, `.pdl-p--cta .pdl-h3`, waga 0,2,0) wygrywają z tą regułą.
- `.pdl-checks li::before{border:solid var(--pdl-green);border-width:0 0 2.5px 2.5px}`: dozwolone, bo to arkusz. Reguła o `border-width` z BRIEF.md dotyczy atrybutu `style`. Nie przenoś tego do inline.
- `content:"\2212"` w FAQ zostaje jako escape. Dosłowny znak minus w pliku to błąd sprawdzarki `pauza`.
- `.pdl` dziedziczy z motywu `font-size:24px`. Każdy element z tekstem musi mieć klasę rozmiaru (`.pdl-txt`, `.pdl-txt-sm`, `.pdl-h*`, `.pdl-btn`…), inaczej wyjdzie 24 px (tak jest z linkiem w karcie CTA, U8).

### 2.3 Kontrast: wszystkie pary tekst/tło

WCAG 2.x, luminancja względna, próg 4,5:1 dla tekstu poniżej 24 px (i poniżej 18,66 px pogrubionego), 3:1 dla większego.
Liczone wzorem w Pythonie i niezależnie zmierzone w przeglądarce (`wzorzec-*-pomiar.json`, klucz `pary`); wyniki zgodne.

| tekst | tło | gdzie | rozmiar/waga | wynik | |
|---|---|---|---|---|---|
| `#141414` ink | `#fff` | h1-h4, lead, przycisk ghost, pytania FAQ | 15,5-58 px | 18,42 | OK |
| `#141414` | `#F5F5F5` | h2, h3 w sekcjach wash | 19-38 px | 16,90 | OK |
| `#5f5f5f` mute | `#fff` | `.pdl-txt`, `.pdl-txt-sm`, listy | 14,5-16,5/300 | 6,39 | OK |
| `#5f5f5f` | `#F5F5F5` | `.pdl-txt` w nagłówkach sekcji wash, `.pdl-checks` w K7 `--rev` | 15,5-16,5/300 | 5,86 | OK |
| **`#9a9aa6` grey** | `#fff` | podpis liczby w hero `.pdl-stat span` | 12,5/300 | **2,78** | BŁĄD |
| (`#9a9aa6`) | (`#F5F5F5`) | gdyby stat trafił na wash | | 2,55 | BŁĄD |
| `#12388C` navy | `#fff` | eyebrow, liczba w stat, linki kart, numery kroków | 13-16/600-800 | 10,66 | OK |
| `#12388C` | `#F5F5F5` | eyebrow w sekcjach wash | 13/600 | 9,78 | OK |
| `#12388C` | `#E6ECF7` | `.pdl-chip` | 11/600 | 8,99 | OK |
| `#fff` | `#12388C` | przycisk główny, karta CTA, h2 pasa | 15-38 px | 10,66 | OK |
| `#fff` z `opacity:.86` = `#dee3ef` | `#12388C` | tekst w pasie `.pdl-band .pdl-txt` | 16,5/300 | 8,29 | OK |
| `#12388C` | `#fff` | przycisk główny w pasie (odwrócony) | 15,5/700 | 10,66 | OK |
| **`#fff`** | **`#DE6B24` rust** | plakietka „Przed” | 11/700 | **3,37** | BŁĄD |
| **`#DE6B24` rust** | `#fff` | numery branż `.pdl-branza-num` 01-06 | 12,5/800 | **3,37** | BŁĄD |
| (`#DE6B24`) | (`#F5F5F5`) | gdyby numer trafił na wash | | 3,09 | BŁĄD |
| `#fff` | `#175C43` green | plakietka „Po” | 11/700 | 7,93 | OK |
| ptaszek `#175C43` (grafika) | `#fff` / `#F5F5F5` | `.pdl-checks` | | 7,93 / 7,27 | OK (próg 3:1) |
| ramka `#d9d9d9` (nie tekst) | `#fff` | przycisk ghost | | 1,41 | informacyjnie, U19 |
| ramka `rgba(255,255,255,.5)` | `#12388C` | ghost w pasie | | 3,87 | OK |

Trzy błędy, z czego dwa wymienia BRIEF-marketing.md (grey w hero, biały na rust), a trzeci wyszedł w pomiarze: numery branż w kolorze rust na białym (6 sztuk na stronę).

### 2.4 Dopisek do arkusza (plik `wzorzec-pdl-dopisek.css`)

Wklej na końcu arkusza, po linii `@media (prefers-reduced-motion…)`, przed `</style>`. Wszystko zawężone do `.pdl`.
Część A jest obowiązkowa (kontrast). Część B naprawia układ sióstr (U7-U9) i jest zalecana; po jej dodaniu strona marketingowa będzie miała odstępy, które siostry miały mieć według własnego arkusza, ale dziś nie mają.

```css
/* ===== Dopisek do arkusza .pdl (strona Uslugi dla marketingu, 13.10.2026) ===== */
/* A. Kontrast WCAG AA (OBOWIAZKOWY). Tekst do 18,66 px pogrubionego i do 24 px zwyklego: min. 4,5:1.
   --pdl-grey: podpisy liczb w hero (.pdl-stat span, 12,5 px/300). Bylo #9a9aa6 = 2,78:1 na bialym.
               Teraz #6b6b76 = 5,26:1 na #fff i 4,83:1 na #F5F5F5.
   --pdl-rust: plakietka Przed (bialy 11 px/700 na tle rust) i numery branz (.pdl-branza-num, 12,5 px/800 na bialym).
               Bylo #DE6B24 = 3,37:1. Teraz #B55119 = 5,05:1 (bialy na nim i on na bialym), 4,64:1 na #F5F5F5.
   Oba tokeny sa uzyte tylko w tych miejscach, wiec podmiana tokenu nie zmienia niczego innego. */
.pdl{--pdl-grey:#6b6b76;--pdl-rust:#B55119;}

/* B. Uklad (ZALECANY). */
/* B1. .pdl p i .pdl h1..h4 {margin:0} maja wage (0,1,1), wyzsza niz .pdl-hero-copy>*+* i
       .pdl-detail-copy>*+* (0,1,0), a .pdl-checks{margin:0} stoi pozniej. Naglowek, lead, tekst
       i lista z ptaszkami stykaly sie bez odstepu (widac na zywej HoReCa i Przemysle). */
.pdl .pdl-hero-copy>.pdl-lead,.pdl .pdl-hero-copy>.pdl-txt{margin-top:14px;}
.pdl .pdl-detail-copy>.pdl-txt{margin-top:14px;}
.pdl .pdl-detail-copy>.pdl-checks{margin-top:18px;}
/* B2. Link w karcie CTA (.pdl-p--cta a) nie ma rozmiaru i dziedziczy 24 px z motywu. */
.pdl-p--cta a{font-size:15.5px;line-height:1.4;}
/* B3. Galeria na telefonie: 2 kolumny zamiast 8 duzych kwadratow jeden pod drugim (ok. 3200 px przewijania). */
@media (max-width:640px){.pdl-gal{grid-template-columns:1fr 1fr;gap:10px;}}
```

Wybór wartości (liczone dla obu teł, bo komponenty bywają na białym i na `#F5F5F5`):

| token | było | jest | na `#fff` | na `#F5F5F5` | biały tekst na nim |
|---|---|---|---|---|---|
| `--pdl-grey` | `#9a9aa6` (2,78) | `#6b6b76` | 5,26 | 4,83 | n/d |
| `--pdl-rust` | `#DE6B24` (3,37) | `#B55119` | 5,05 | 4,64 | 5,05 |

Odrzucone kandydatki: `#70707b` (4,89 na białym, ale 4,49 na wash), `#bf571b` (4,57, za mały zapas; 4,19 na wash), `#c45a1c` (4,35).
`#6b6b76` zachowuje niebieskawy odcień grey i jest wciąż jaśniejszy od `--pdl-mute` (#5f5f5f), więc hierarchia „liczba, pod nią podpis” zostaje.
`#B55119` to ten sam rdzawy odcień, ciemniejszy; obok zielonej plakietki „Po” (7,93) wygląda spójnie (zrzut `wzorzec-horeca-poprawiona-1440-s03.png`).
Pomiar po dopisku: 0 par poniżej progu w 1440 i 390 px na obu siostrach.

---

## 3. Komponenty

Konwencja: `[[…]]` = tekst, adres albo zdjęcie do podmiany. Sprawdzarka traktuje `[[` i `]]` jako pozostałość i zwraca błąd `slad`, więc niewypełniony slot nie przejdzie.
Fragmenty są już w wersji POPRAWIONEJ (p. 4). Przy każdym komponencie napisane, czym różni się od sióstr.
Zdjęcia: tylko adresy z `zrodla/media.json` (`https://grawerowanie-laserowe.pl/wp-content/uploads/…`). Przed napisaniem `alt` obejrzyj zdjęcie (`kontaktowka.py`, potem Read).
Poza hero każde `<img>` ma `loading="lazy" decoding="async"`.

### 3.1 Mapa sekcji obu sióstr

| s | tło | HoReCa 2283: eyebrow → komponent | Przemysł 2264: eyebrow → komponent | wys. 1440 px |
|---|---|---|---|---|
| s00 | białe (body, sekcja bez tła) | „Usługi dla HoReCa” → K1 hero | „Usługi dla przemysłu” → K1 | 612 |
| s01 | wash `#F5F5F5` | „Trzy światy” → K2 + K3 (3 karty) | „Zakres usług” → K2 + K3 (3 karty) | 897 |
| s02 | białe | „Zakres” → K2 + K4 (5 + karta CTA) | „Grawerowanie dla przemysłu” → K2 + K4 (5 + CTA) | 1032 / 997 |
| s03 | wash | „Zastawa, którą już masz” → K2 + K5 + K6 + przycisk | „Usługa wyjątkowa na rynku” → K2 + K5 + K6 + przycisk | 1285 / 1259 |
| s04 | białe | „Szkło” → K7 (zdjęcie z prawej) | „Cięcie laserowe” → K7 | 572 |
| s05 | wash | „Drewno” → K7 `--rev` (zdjęcie z lewej) | „Frezowanie CNC” → K7 `--rev` | 572 |
| s06 | białe | „Materiały” → K2 + K8 (6) | „Materiały” → K2 + K8 (6) | 1184 / 1235 |
| s07 | wash | „Realizacje” → K2 + K9 (8 zdjęć) | „Realizacje” → K2 + K9 (8) | 812 |
| s08 | białe | „Kto u nas zamawia” → K2 + K10 (6) | „Branże” → K2 + K10 (6) | 864 / 882 |
| s09 | wash | „FAQ” → K2 + K11 (7 pytań) | „FAQ” → K2 + K11 (7) | 874 |
| s10 | białe | K12 pas CTA | K12 pas CTA | 398 / 449 |
| po grupie | | brak | K14 JSON-LD `Service` | |

### 3.2 Naprzemienność teł

- Hero nie ma tła (widać białe `body` motywu). Od s01 sekcje idą na przemian: `pdl-sec pdl-sec--wash`, `pdl-sec`, `pdl-sec--wash`, … Pierwsza po hero jest zawsze szara, przedostatnia (FAQ) też szara, ostatnia (z pasem) biała.
- Między hero a pasem jest więc NIEPARZYSTA liczba sekcji (u sióstr 9), zaczyna i kończy wash. Jeśli składacz wyrzuca sekcję, wyrzuca parę albo przestawia klasy tak, żeby nigdy nie stały obok siebie dwie sekcje o tym samym tle i żeby sekcja przed pasem była wash.
- Karty (`.pdl-card`, `.pdl-p`, `.pdl-mat`, `.pdl-branza`, `.pdl-q`, `.pdl-step`, `.pdl-ba-item`) mają własne białe tło z ramką `#ededed`. Na wash odcinają się tłem, na białym tylko ramką, i tak ma być: siostry dają siatki kart na obu tłach.
- Para K7: wersja zwykła (zdjęcie z prawej) na białym, zaraz po niej `--rev` (zdjęcie z lewej) na wash. Przy jednym K7 wybierz wersję wg tła, które wypada w kolejności.
- Pas K12 (granat) stoi zawsze w białej sekcji `pdl-sec`, nie w wash.
- Granica między białym a wash nie ma linii ani cienia; odróżnia je sam kolor `#F5F5F5` (dlatego na zrzutach całostronicowych sekcje wyglądają jak pasy).

### 3.3 Siatki: ile kolumn i ile elementów

Szerokość treści = min(1220, szerokość okna) - 48 px.

| siatka | reguła | 1440 | 1024 | 390 | pełne rzędy przy 1440 |
|---|---|---|---|---|---|
| `.pdl-hero-grid` | auto-fit, min 360, gap 52 | 2 | 2 | 1 (poniżej 820 px) | - |
| `.pdl-cards` K3 | auto-fill, min 300, gap 22 | 3 | 3 | 1 | 3 |
| `.pdl-prod` K4 | auto-fill, min 330, gap 22 | 3 | 2 | 1 | 3 albo 6 (z kartą CTA) |
| `.pdl-ba` K5 | auto-fit, min 320, gap 22 | 2 (przy 2 elementach) | 2 | 1 | 2 |
| `.pdl-steps` K6 | auto-fit, min 240, gap 20 | 4 | 3 | 1 | 4 |
| `.pdl-detail` K7 | auto-fit, min 340, gap 52 | 2 | 2 | 1 (poniżej 780 px) | - |
| `.pdl-mats` K8 | auto-fill, min 260, gap 20 | 4 | 3 | 1 | 4 albo 8 (siostry mają 6: rząd 4 + 2) |
| `.pdl-gal` K9 | auto-fill, min 220, gap 14 | 5 | 4 | 1, po dopisku B3: 2 | 5 albo 10 (siostry 8: 5 + 3) |
| `.pdl-branze` K10 | auto-fill, min 300, gap 20 | 3 | 3 | 1 | 3 albo 6 |

---

### K1. Hero z liczbami i dwoma zdjęciami

Gdzie: s00 na obu stronach. Zrzuty: `wzorzec-horeca-1440-s00.png`, `wzorzec-przemysl-1440-s00.png`, telefon `-390-s00.png`.
Liczby w hero to `ul.pdl-stats > li.pdl-stat` (biała kafelka z ramką: pogrubiona liczba w granacie, pod nią szary podpis). To NIE jest `.pdl-chip`; chip to mała niebieska pigułka z K10.

```html
<section class="pdl-hero">
  <div class="pdl-wrap pdl-hero-grid">
    <div class="pdl-hero-copy">
      <span class="pdl-eyebrow">[[Usługi dla …]]</span>
      <h1 class="pdl-h1">[[H1, wiersz 1]]<br>[[H1, wiersz 2]]</h1>
      <p class="pdl-lead">[[lead: jedno zdanie, co i dla kogo]]</p>
      <p class="pdl-txt">[[1-2 zdania konkretu]]</p>
      <div class="pdl-btns"><a class="pdl-btn pdl-btn--main" href="/kontakt/">[[Wyceń …]]</a><a class="pdl-btn pdl-btn--ghost" href="#[[id-sekcji]]">[[Co robimy]]</a></div>
      <ul class="pdl-stats"><li class="pdl-stat"><b>[[liczba]]</b><span>[[podpis liczby]]</span></li></ul>
    </div>
    <div class="pdl-hero-media"><div class="pdl-shot"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik]].jpg" alt="[[co widać]]" loading="eager" fetchpriority="high" decoding="async" data-no-lazy="1"></div><div class="pdl-shot"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik]].jpg" alt="[[co widać]]" loading="eager" fetchpriority="high" decoding="async" data-no-lazy="1"></div></div>
  </div>
</section>
```

Powtórzenia: `li.pdl-stat` 3 razy (u obu sióstr 3, mieszczą się w jednym rzędzie przy 1440; na telefonie łamią się 1 + 2).

| slot | tekst do podmiany | wskazówka |
|---|---|---|
| eyebrow | „Usługi dla marketingu” | CSS robi wersaliki, pisz normalnie |
| H1 | 2 wiersze rozdzielone `<br>` | 58 px; ok. 18-20 znaków na wiersz, inaczej łamie się w 3 |
| lead | 1 zdanie | 22 px pogrubione, do ok. 70 znaków |
| txt | 1-2 zdania | |
| przyciski | główny do `/kontakt/`; ghost do `#id` sekcji na tej stronie | `id` musi istnieć (U2) |
| stat `b` / `span` | liczba i podpis | `b` do ok. 14 znaków, `span` do ok. 28 |
| 2 zdjęcia | kadr 3:4 (object-fit: cover) | wybieraj zdjęcia z przedmiotem w środku; drugie jest przesunięte 32 px w dół (20 px na telefonie) |

Różnice wobec sióstr: zdjęcia `loading="eager" fetchpriority="high" data-no-lazy="1"` zamiast `lazy` (U1); kotwica ghost ma cel (U2); po dopisku B1 między H1, leadem i tekstem jest 14 px odstępu (U7).
Liczby ze źródłem dla marketingu: „od 2002” / „na rynku obróbki laserowej” (`zrodla/pages-8-produkty.txt`: „od 2002 na rynku obróbki laserowej”), „od 100 zł” / najniższa cena realizacji (zleceniodawca, 13.10.2026), „2 dni” / grawer, od ręki za dopłatą (zleceniodawca, 13.10.2026; czy dotyczy serii: pytanie P04 w `pytania.md`, podpis nie może sugerować serii). Liczb sióstr („setki i tysiące”, „5-10 dni”, „±0,01 mm”, „24-72 h”) nie przenosimy.

### K2. Sekcja z nagłówkiem

Gdzie: obudowa każdej sekcji s01-s09; nagłówek `.pdl-head` w s01, s02, s03, s06, s07, s08, s09 (K7 ma własny układ tekstu, K12 nie ma nagłówka).

```html
<section class="pdl-sec pdl-sec--wash" id="[[id, tylko gdy prowadzi tu kotwica]]"><div class="pdl-wrap"><div class="pdl-head"><span class="pdl-eyebrow">[[EYEBROW]]</span><h2 class="pdl-h2">[[H2, wiersz 1]]<br>[[H2, wiersz 2]]</h2><p class="pdl-txt">[[1-2 zdania wstępu]]</p></div>
[[siatka komponentu: K3, K4, K5+K6, K8, K9, K10 albo K11]]
</div></section>
```

Wariant białego tła: `class="pdl-sec"`. `id` tylko na sekcjach, do których prowadzi `href="#…"`; same małe litery ASCII, bez polskich znaków (`zakres`, `uslugi`, `produkty`).
Nagłówek ma max 760 px szerokości i 40 px odstępu do siatki. H2 38 px; siostry łamią go `<br>` na dwa wiersze, jedno krótkie zdanie bez `<br>` też jest w porządku („Lokale, które grawerujemy.”).

### K3. Karty „trzy światy” ze zdjęciem i linkiem

Gdzie: s01 (wash). HoReCa: „Hotele / Restauracje / Bary i kawiarnie”, wszystkie trzy linki „Zobacz zakres →” do `#produkty` (martwa kotwica, U2, U12). Przemysł: „Grawerowanie laserowe / Wycinanie laserowe / Frezowanie CNC”, linki do `/grawerowanie-laserowe/`, `/wycinanie-laserowe/`, `/frezowanie-cnc/` (działają).
Zrzuty: `wzorzec-horeca-1440-s01.png`, `wzorzec-przemysl-1440-s01.png`.

```html
<div class="pdl-cards"><article class="pdl-card">
      <div class="pdl-card-img"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik]].jpg" alt="[[co widać]]" loading="lazy" decoding="async"></div>
      <div class="pdl-card-body">
        <h3 class="pdl-h3">[[Nazwa świata]]</h3>
        <p class="pdl-txt-sm">[[2 zdania: co konkretnie robimy dla tej grupy]]</p>
        <a class="pdl-card-link" href="[[/opublikowany-adres/ albo #id]]">[[Zobacz …]] &rarr;</a>
      </div></article></div>
```

Powtórzenia: `article.pdl-card` 3 razy (jeden rząd przy 1440 i 1024).
Sloty: zdjęcie (kadr 4:3), tytuł (19 px, 1 wiersz), tekst (3-4 wiersze), etykieta i adres linku. Link jest przyklejony do dołu karty (`margin-top:auto`), więc linki trzech kart stoją w jednej linii nawet przy tekstach różnej długości.
Dla marketingu: każda karta prowadzi w INNE miejsce (opublikowana strona usługi albo `#id` sekcji na tej stronie), nie trzy razy do tego samego.

### K4. Siatka zakresu z kartą CTA

Gdzie: s02 (białe). HoReCa „Zakres”: 5 grup produktów + karta „Otwierasz nowy lokal?”. Przemysł „Grawerowanie dla przemysłu”: 5 + „Niestandardowe zlecenie?”.
Zrzuty: `wzorzec-horeca-1440-s02.png` (stan obecny, link CTA 24 px), `wzorzec-horeca-poprawiona-1440-s02.png` (po B2).

```html
<div class="pdl-prod"><article class="pdl-p">
          <h3 class="pdl-h3">[[Grupa produktów]]</h3>
          <p class="pdl-txt-sm">[[1-2 zdania: co i z czego]]</p>
          <ul><li>[[cecha]]</li><li>[[cecha]]</li><li>[[cecha]]</li></ul></article><article class="pdl-p pdl-p--cta">
          <h3 class="pdl-h3">[[Pytanie, np. Masz nietypowy pomysł?]]</h3>
          <p class="pdl-txt-sm">[[1-2 zdania zachęty]]</p>
          <a href="/kontakt/">[[Omów …]] &rarr;</a></article></div>
```

Powtórzenia: `article.pdl-p` 5 razy, karta CTA raz, zawsze ostatnia (6 = dwa pełne rzędy po 3 przy 1440, trzy po 2 przy 1024). Lista 3-4 punkty, znacznik to granatowy kwadracik z CSS.
Sloty: tytuł grupy, opis, punkty listy, w karcie CTA pytanie, zachęta, etykieta linku (cel `/kontakt/`).
Różnica wobec sióstr: po dopisku B2 link w karcie CTA ma 15,5 px zamiast odziedziczonych 24 px (U8).

### K5. Przed / po

Gdzie: s03 (wash), nad K6. HoReCa: kieliszek „Przed” i karafka Mercure „Po”; Przemysł: tłok z błędną strzałką i ten sam tłok po poprawce.
Zrzut: `wzorzec-horeca-1440-s03.png`, po poprawce plakietki: `wzorzec-horeca-poprawiona-1440-s03.png`.

```html
<div class="pdl-ba"><div class="pdl-ba-item"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik przed]].jpg" alt="[[co widać]]" loading="lazy" decoding="async">
          <div class="pdl-ba-body"><span class="pdl-tag pdl-tag--before">Przed</span>
          <h3 class="pdl-h4">[[stan przed]]</h3><p class="pdl-txt-sm">[[opis]]</p></div></div><div class="pdl-ba-item"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik po]].jpg" alt="[[co widać]]" loading="lazy" decoding="async">
          <div class="pdl-ba-body"><span class="pdl-tag pdl-tag--after">Po</span>
          <h3 class="pdl-h4">[[stan po]]</h3><p class="pdl-txt-sm">[[opis]]</p></div></div></div>
```

Dokładnie 2 elementy. Zdjęcia w kadrze 16:10.
Różnice wobec sióstr: `<h3 class="pdl-h4">` zamiast `<h4 class="pdl-h4">` (U11; wygląd bez zmian, 16,5 px); plakietka „Przed” po dopisku A ma tło `#B55119` (U5).
Warunek treści: tylko prawdziwa para zdjęć TEGO SAMEGO przedmiotu. Para HoReCa tego warunku nie spełnia (U13). Dla marketingu pary nie ma w źródłach, więc K5 pomijamy, chyba że klient ją przyśle (pytanie W01 w `pytania.md`). Sam K6 może stać bez K5.

### K6. Kroki „Jak to działa”

Gdzie: s03 pod K5 na obu stronach (4 kroki, potem przycisk).

```html
<h3 class="pdl-h3" style="margin-bottom:20px">Jak to działa</h3>
<ol class="pdl-steps"><li class="pdl-step"><p class="pdl-txt-sm">[[Nazwa kroku. Jedno-dwa zdania, co się dzieje.]]</p></li></ol>
<div class="pdl-btns" style="margin-top:32px"><a class="pdl-btn pdl-btn--main" href="/kontakt/">[[Wyślij … do wyceny]]</a></div>
```

Powtórzenia: `li.pdl-step` 4 razy (jeden rząd przy 1440). Numery 01-04 robi licznik CSS, nie wpisuj ich.
Oba atrybuty `style` zawierają tylko marginesy, więc są bezpieczne (reguła 3 z BRIEF.md dotyczy ramek).
Gdy K6 stoi sam w sekcji, zamiast `<h3>` „Jak to działa” użyj nagłówka K2.
Treść kroków sióstr („Wycena w 24 godziny”, „50 cykli zmywarki”, „±0,05 mm”) nie jest źródłem dla marketingu.

### K7. Zdjęcie + tekst + lista z ptaszkami + przycisk

Gdzie: s04 (białe, zdjęcie z prawej) i s05 (wash, `--rev`, zdjęcie z lewej). HoReCa „Szkło” i „Drewno”, Przemysł „Cięcie laserowe” i „Frezowanie CNC” (w tym ostatnim przycisk prowadzi do `/frezowanie-cnc/` zamiast do `/kontakt/`).
Zrzuty: `wzorzec-horeca-1440-s04.png` (stan obecny, tekst sklejony z nagłówkiem), `wzorzec-horeca-poprawiona-1440-s04.png` (po B1), telefon `wzorzec-horeca-390-s04.png` i `-s05.png`.

```html
<section class="pdl-sec"><div class="pdl-wrap">
      <div class="pdl-detail">
        <div class="pdl-detail-copy">
          <span class="pdl-eyebrow">[[EYEBROW]]</span>
          <h2 class="pdl-h2">[[H2, wiersz 1]]<br>[[H2, wiersz 2]]</h2>
          <p class="pdl-txt">[[2-3 zdania]]</p>
          <ul class="pdl-checks"><li>[[cecha]]</li><li>[[cecha]]</li><li>[[cecha]]</li></ul>
          <div class="pdl-btns"><a class="pdl-btn pdl-btn--main" href="/kontakt/">[[Wyceń …]]</a></div>
        </div>
        <div class="pdl-detail-media"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik]].jpg" alt="[[co widać]]" loading="lazy" decoding="async"></div>
      </div></div></section>
```

Wariant: `<div class="pdl-detail pdl-detail--rev">` i `<section class="pdl-sec pdl-sec--wash">` dla drugiej sekcji z pary.
Powtórzenia: `li` 3 razy. Zdjęcie w kadrze 4:3 (ok. 560 × 420 px przy 1440).
Sloty: eyebrow, H2, tekst, punkty z ptaszkiem (zielony ptaszek z CSS), etykieta i cel przycisku, zdjęcie.
Różnica wobec sióstr: dopisek B1 przywraca odstępy 14 px (H2 → tekst) i 18 px (tekst → lista), U7.

### K8. Siatka materiałów

Gdzie: s06 (białe), 6 kart na obu stronach. Zrzut: `wzorzec-horeca-1440-s06.png`.

```html
<div class="pdl-mats"><article class="pdl-mat"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik]].jpg" alt="[[co widać]]" loading="lazy" decoding="async">
      <div class="pdl-mat-body"><h3 class="pdl-h4">[[Materiał albo rodzaj przedmiotu]]</h3>
      <p class="pdl-txt-sm">[[1-2 zdania: co z niego robimy]]</p></div></article></div>
```

Powtórzenia: `article.pdl-mat` 4 albo 8 dla pełnych rzędów przy 1440 (siostry: 6, rząd 4 + 2). Zdjęcie w kadrze 16:10.
Różnica wobec sióstr: `<h3 class="pdl-h4">` zamiast `<h4>` (U11).
Zdjęcie musi pokazywać ten materiał (U13).

### K9. Galeria realizacji (sekcja klientów)

Gdzie: s07 (wash), 8 zdjęć bez podpisów na obu stronach. Zrzuty: `wzorzec-horeca-1440-s07.png`, telefon przed i po B3: `wzorzec-horeca-390-s07.png` (8 kwadratów jeden pod drugim, ok. 3200 px), `wzorzec-horeca-poprawiona-390-s07.png` (2 kolumny), desktop z przyciskiem: `wzorzec-horeca-poprawiona-1440-s07.png`.

```html
<div class="pdl-gal"><img src="https://grawerowanie-laserowe.pl/wp-content/uploads/[[plik]]-768x512.jpg" alt="[[co widać, kto jest klientem tylko jeśli jest w galerii realizacji]]" loading="lazy" decoding="async"></div>
<div class="pdl-btns" style="margin-top:32px"><a class="pdl-btn pdl-btn--ghost" href="/przykladkowe-realizacje/">Zobacz wszystkie realizacje</a></div>
```

Powtórzenia: `img` 5 albo 10 dla pełnych rzędów przy 1440 (siostry 8: 5 + 3; 8 daje pełne rzędy przy 1024 i na telefonie po B3).
Zdjęcia w kadrze 1:1, zaokrąglone, bez podpisu, nieklikalne, bez lightboxa (w przeciwieństwie do `.pdw`).
Różnice wobec sióstr: przycisk „Zobacz wszystkie realizacje” pod siatką, bo tekst sekcji obiecuje „pełną galerię na osobnej podstronie”, a linku nie ma (U10); 2 kolumny na telefonie (B3, U9); miniatury `-768x…` z `media.json` (`url_medium`) zamiast pełnych plików (U17; sprawdzarka akceptuje rozmiary pośrednie).
Kandydatki z `zrodla/realizacje-karty.json` pasujące do marketingu (OBEJRZYJ przed podpisaniem): Statuetka z plexi; Statuetka jubileuszowa „INSOFT”; Napis przestrzenny „Tea” i „Team” (lustrzana plexi na sklejce, CIĘTE LASEREM wg zleceniodawcy, w galerii błędnie „Frezowanie”); Logo przestrzenne „BOKO”; Ekspozytor „Guerlain”; Ścianka fotograficzna „Bondi Sands”; Podświetlana litera „R”; Kubek termiczny padir; MacBook „The Last Dance”; Grawer „WOW!” na owocach; Ładowarka „enel X”. Nazwy klientów tylko w kontekście realizacji, tak jak na `/przykladkowe-realizacje/`.

### K10. Kto zamawia / branże z chipami

Gdzie: s08 (białe). HoReCa „Kto u nas zamawia” i Przemysł „Branże”, po 6 kart. Zrzut: `wzorzec-horeca-1440-s08.png`.

```html
<ul class="pdl-branze"><li class="pdl-branza"><span class="pdl-branza-num">01</span>
          <h3 class="pdl-h3">[[Segment klienta]]</h3><p class="pdl-txt-sm">[[1 zdanie: co dla niego robimy]]</p>
          <div class="pdl-chips"><span class="pdl-chip">[[słowo]]</span><span class="pdl-chip">[[słowo]]</span><span class="pdl-chip">[[słowo]]</span></div></li></ul>
```

Powtórzenia: `li.pdl-branza` 3 albo 6; numer `01`, `02`… wpisujesz ręcznie (to nie licznik CSS). Chipy po 3, 1-2 słowa każdy (11 px).
Dla marketingu segmenty z BRIEF-marketing.md: działy marketingu firm, agencje reklamowe, agencje eventowe, organizatorzy konkursów, gal i firmowych wydarzeń. Chip nie może być twierdzeniem bez źródła (normy, certyfikaty, nakłady).
Różnica wobec sióstr: numer w kolorze `#B55119` po dopisku A (U6).

### K11. FAQ na `<details>`

Gdzie: s09 (wash), 7 pytań na obu stronach. Zrzut: `wzorzec-horeca-1440-s09.png`.

```html
<div class="pdl-faq"><details class="pdl-q"><summary>[[Pytanie klienta?]]</summary>
      <div class="pdl-q-a"><p class="pdl-txt-sm">[[Odpowiedź, 2-4 zdania]]</p></div></details></div>
```

Powtórzenia: `details.pdl-q` 5-7. Domyślnie zamknięte; znak plus (zamknięte) i minus (otwarte) rysuje CSS. Lista ma max 900 px szerokości.
Odpowiedzi tylko z faktami ze źródeł. Fakty pewne dla marketingu: najniższa cena realizacji 100 zł; grawer w ciągu 2 dni albo od ręki za dodatkową opłatą; odbiór Matuszewska 14, Warszawa (`zrodla/pages-20-kontakt.txt`). Bez progu 12 sztuk.

### K12. Pas `.pdl-band`

Gdzie: s10, ostatnia sekcja, białe tło, na obu stronach. Zrzuty: `wzorzec-horeca-1440-s10.png`, `-390-s10.png`.

```html
<section class="pdl-sec"><div class="pdl-wrap"><div class="pdl-band">
      <div><h2 class="pdl-h2">[[Wezwanie w jednym zdaniu]]</h2><p class="pdl-txt">[[1-2 zdania: co wysłać i co odpowiemy]]</p></div>
      <div class="pdl-btns"><a class="pdl-btn pdl-btn--main" href="/kontakt/">[[Wyceń …]]</a><a class="pdl-btn pdl-btn--ghost" href="/przykladkowe-realizacje/">Zobacz realizacje</a></div></div></div></section>
```

Granatowy blok z zaokrągleniem 44/12/44/44 px; przyciski w nim odwrócone (główny biały z granatowym tekstem, ghost z białą ramką). Na telefonie przyciski schodzą pod tekst.
To jedyne miejsce kontaktu na dole strony: stron branżowych nie zamykamy formularzem CF7.

### K13. Przyciski i drobne klasy (atomy)

```html
<div class="pdl-btns"><a class="pdl-btn pdl-btn--main" href="/kontakt/">[[Akcja główna]]</a><a class="pdl-btn pdl-btn--ghost" href="[[adres albo #id]]">[[Akcja druga]]</a></div>
```

- `.pdl-btn--main`: granat, biały tekst; `.pdl-btn--ghost`: obrys `#d9d9d9`, tekst `#141414`, na hover granat. Zaokrąglenie 16/4/16/16. W pasie K12 kolory odwrócone.
- Pod siatką przycisk dostaje `style="margin-top:32px"` na `.pdl-btns` (jak w K6 i K9).
- Typografia: `.pdl-eyebrow` 13 px wersaliki granat; `.pdl-h1` 36-58 px; `.pdl-h2` 26-38 px; `.pdl-h3` 19 px; `.pdl-h4` 16,5 px; `.pdl-lead` 18-22 px pogrubione; `.pdl-txt` 16,5 px/300; `.pdl-txt-sm` 15 px/300. Tekst bez żadnej z tych klas dostaje 24 px z motywu.
- Strzałka w linkach: encja `&rarr;`.

### K14. Dane strukturalne JSON-LD (opcjonalnie)

Gdzie: tylko 2264, drugi blok `wp:html` ZA grupą. HoReCa go nie ma (U18).

```html

<!-- wp:html -->
<script type="application/ld+json" data-no-optimize="1">{"@context":"https://schema.org","@type":"Service","@id":"https://grawerowanie-laserowe.pl/[[slug]]/#service","name":"[[nazwa usługi]]","serviceType":"[[nazwa usługi]]","description":"[[1-2 zdania, tylko fakty ze źródeł]]","url":"https://grawerowanie-laserowe.pl/[[slug]]/","provider":{"@id":"https://grawerowanie-laserowe.pl/#organization"},"areaServed":{"@type":"Country","name":"Polska"},"hasOfferCatalog":{"@type":"OfferCatalog","name":"Zakres usługi","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":"[[usługa]]"}}]},"audience":{"@type":"BusinessAudience","name":"[[odbiorcy]]"}}</script>
<!-- /wp:html -->
```

2264 ma dodatkowo `availableChannel` z `"servicePhone":"+48227413655"` (numer jest na `/kontakt/`: „+48 227 413 655”), `mainEntityOfPage` i `image` z identyfikatorami Yoasta. `itemListElement` powtarzaj dla każdej usługi z K4. W JSON nie może być `&&`.

---

## 4. Usterki szablonu

Na obu siostrach sprawdzarka zwraca kod 1:

```
2283: BŁĘDY 7: 6 × [hero-ladowanie] (karafka Mercure, szklanka Binkowski: brak loading="eager", fetchpriority="high", data-no-lazy="1"), 1 × [kotwica] #produkty; ostrzeżenia 0
2264: BŁĘDY 7: 6 × [hero-ladowanie] (tlok-1.jpeg, IMG_0060.jpg), 1 × [kotwica] #uslugi; ostrzeżenia 1: [styl-tekstu] „kompleksow”
```

Po poprawkach U1, U2, U4-U11 (`wzorzec-*-poprawiona.html`): `sprawdz_szkic.py --pdl` kod 0 na obu, pomiar kontrastu 0 błędów w 1440 i 390 px (zostaje tylko ostrzeżenie U3 w tekście 2264, który do nowej strony nie trafia).

**U1. Zdjęcia w hero ładowane leniwie** (BRIEF-marketing p. 1, sprawdzarka `hero-ladowanie`, obie strony).
Jest: `loading="lazy" decoding="async"`; na żywej stronie LiteSpeed dokłada jeszcze `data-lazyloaded="1"` i podmienia `src`. Hero, czyli pierwsze, co widać, ładuje się na końcu.
Poprawka (K1): `<img … loading="eager" fetchpriority="high" decoding="async" data-no-lazy="1">`.

**U2. Martwe kotwice** (BRIEF-marketing p. 2, sprawdzarka `kotwica`).
2283: `href="#produkty"` 4 razy (ghost w hero + 3 linki „Zobacz zakres” w K3), `id="produkty"` nie ma. 2264: `href="#uslugi"` (ghost w hero), `id="uslugi"` nie ma.
Poprawka: `id` na sekcji docelowej, np. `<section id="produkty" class="pdl-sec">` na „Zakres” (s02 HoReCa), `<section id="uslugi" class="pdl-sec pdl-sec--wash">` na „Zakres usług” (s01 Przemysł). Na nowej stronie każde `href="#x"` ma `id="x"`.

**U3. Zwrot z listy „śladów AI”** (sprawdzarka `styl-tekstu`, 2264): „Grawerowanie laserowe, wycinanie laserowe i frezowanie CNC kompleksowo, w jednej pracowni”.
Poprawka: bez „kompleksow*”, np. „Grawerujemy, tniemy laserem i frezujemy w jednej pracowni.” Na nowej stronie sprawdzarka ma nie dawać żadnych ostrzeżeń `styl-tekstu`.

**U4. Szary podpis liczb w hero: 2,78:1** (BRIEF-marketing p. 3; `--pdl-grey:#9a9aa6`, 12,5 px/300 na białym kafelku).
Poprawka: dopisek A, `--pdl-grey:#6b6b76` (5,26:1; 4,83:1 na wash).

**U5. Biały tekst na rdzawej plakietce „Przed”: 3,37:1** (BRIEF-marketing p. 3; 11 px/700 na `#DE6B24`).
Poprawka: dopisek A, `--pdl-rust:#B55119` (5,05:1).

**U6. Rdzawe numery branż na białym: 3,37:1** (poza listą z briefu, znalezione w pomiarze; `.pdl-branza-num` 12,5 px/800, 6 razy na stronę).
Poprawka: ten sam token co U5 (5,05:1; 4,64:1 na wash).

**U7. Zapadnięte odstępy w hero i w K7** (zrzuty `-s00`, `-s04`, `-s05`; zmierzone `getComputedStyle`: `margin-top` 0 px u H1, leada, tekstu i listy).
Przyczyna: `.pdl p{margin:0}` i `.pdl h1..h4{margin:0}` mają wagę (0,1,1), a `.pdl-hero-copy>*+*{margin-top:20px}` i `.pdl-detail-copy>*+*{margin-top:18px}` tylko (0,1,0); `.pdl-checks{margin:0}` stoi w arkuszu później. Działa tylko odstęp przed `.pdl-btns` i `.pdl-stats`. Efekt: H1 dotyka leada, nagłówek K7 dotyka tekstu, tekst dotyka listy.
Poprawka: dopisek B1 (14 px przed leadem i tekstem w hero, 14 px przed tekstem i 18 px przed listą w K7). Zrzuty po: `wzorzec-horeca-poprawiona-1440-s00.png`, `-s04.png`.

**U8. Link w karcie CTA ma 24 px** (zrzut `wzorzec-horeca-1440-s02.png`, „Omów koncept →” większe od nagłówka karty).
Przyczyna: `.pdl-p--cta a` nie ma rozmiaru, dziedziczy 24 px z motywu.
Poprawka: dopisek B2 (`font-size:15.5px`).

**U9. Galeria na telefonie w jednej kolumnie** (zrzut `wzorzec-horeca-390-s07.png`: 8 kwadratów po 342 px, sekcja 3192 px).
Poprawka: dopisek B3, 2 kolumny poniżej 640 px (sekcja 1131 px, zrzut `wzorzec-horeca-poprawiona-390-s07.png`).

**U10. Galeria obiecuje link, którego nie ma.** Tekst: „Pełną galerię wszystkich projektów znajdziesz na osobnej podstronie.”, a w sekcji nie ma odnośnika; zdjęcia też nie są klikalne. Jedyny link do realizacji jest w pasie na samym dole.
Poprawka (K9): pod siatką `<div class="pdl-btns" style="margin-top:32px"><a class="pdl-btn pdl-btn--ghost" href="/przykladkowe-realizacje/">Zobacz wszystkie realizacje</a></div>`.

**U11. Przeskok poziomu nagłówków h2 → h4** (K5 i K8: 8 razy `<h4>` bezpośrednio pod `<h2>`; w s03 po `<h4>` przychodzi jeszcze `<h3>` „Jak to działa”).
Poprawka: `<h3 class="pdl-h4">…</h3>`. Wygląd bez zmian (klasa daje 16,5 px, kolor daje reguła `.pdl h3`), zmierzone: 18,42:1, 16,5 px/700.

**U12. Trzy identyczne linki w K3 HoReCa.** Wszystkie „Zobacz zakres →” prowadzą do tej samej (martwej) kotwicy, więc trzy karty nie różnią się celem.
Poprawka: każda karta do innego, istniejącego celu (opublikowana strona usługi albo `#id` innej sekcji), jak na Przemyśle.

**U13. Zdjęcia powtarzane i niepasujące do podpisu.**
2283: 12 unikalnych plików na 23 `<img>` (karafka Mercure, szklanka Binkowski i kieliszek padir po 3 razy; noże, sztućce, oznakowanie, ażurowe drzewo, kubek po 2 razy). 2264: 13 na 23 (`tlok-1.jpeg` 4 razy, `wbet-ds18.jpg` 3 razy).
Niezgodności: para przed/po HoReCa to dwa różne przedmioty, a zdjęcie „Przed” („Kieliszek bez sygnatury lokalu”) pokazuje kieliszek z wygrawerowanym logo padir; sekcja „Karty menu z drewna” ma zdjęcie ażurowego drzewa z sowami; Przemysł „Tworzywa techniczne” ma zdjęcie logo przestrzennego BOKO z lustrzanej plexi (realizacja reklamowa).
Poprawka: każde zdjęcie najwyżej raz w treści (dopuszczalne powtórzenie: hero i galeria), zdjęcie pokazuje to, co mówi nagłówek, alt opisuje to, co widać (po obejrzeniu w `kontaktowka.py`); K5 tylko z prawdziwą parą.

**U14. Liczby sióstr nie są źródłem, część jest sprzeczna.**
HoReCa: „5-10 dni” typowego czasu realizacji, a obowiązuje (zleceniodawca 13.10.2026) „grawer w ciągu 2 dni albo od ręki za dodatkową opłatą”; „od 12 sztuk” (BRIEF-marketing: nie pisać, w trakcie wyjaśniania).
Przemysł: „±0,01 mm” w hero, „±0,1 mm” w K3 i „±0,05 mm” w K6 na tej samej stronie; „Pole robocze 1680 × 2510 mm”, gdy reszta serwisu podaje „2510 × 1680 mm” (`zrodla/pages-8-produkty.txt`).
Poprawka: na nowej stronie tylko fakty z cytatem w `zrodla/` albo od zleceniodawcy; reszta jako pytanie w `pytania.md`.

**U15. Różna kolejność zdjęcia i tekstu w K7 na telefonie** (zrzuty `-390-s04` i `-390-s05`): w wersji zwykłej zdjęcie jest pod tekstem, w `--rev` nad nim (bo `order:-1` działa też w jednej kolumnie).
Poprawka (opcjonalna, poza dopiskiem): `@media (max-width:779px){.pdl-detail .pdl-detail-media{order:-1;}}`, wtedy zawsze zdjęcie nad tekstem.

**U16. Karta K3 unosi się na hover, choć klikalny jest tylko link na dole.**
Poprawka (opcjonalna): zostawić jak u sióstr dla spójności albo `.pdl-card:hover{transform:none;box-shadow:none;}`.

**U17. Pełnowymiarowe pliki w małych kaflach** (galeria 220 px, karty 300-380 px, pliki ok. 1000 px i więcej).
Poprawka: tam, gdzie `media.json` ma `url_medium` (np. `…-768x512.jpg`), używaj go w K8 i K9. Sprawdzarka akceptuje rozmiary pośrednie tego samego pliku.

**U18. JSON-LD tylko na jednej siostrze.** 2264 ma `Service`, 2283 nie ma nic.
Poprawka (opcjonalna): K14 na nowej stronie, wyłącznie z faktami ze źródeł.

**U19. Ramka przycisku ghost 1,41:1** (informacyjnie). WCAG 1.4.11 tego nie wymaga, bo przycisk rozpoznaje się po tekście (18,42:1). Zostawiamy jak u sióstr.

---

## 5. Lista kontrolna składacza

1. `cd S && python3 -I sprawdz_szkic.py praca/marketing/strona.html --pdl` → kod 0, BEZ `--szkic`, bez ostrzeżeń `styl-tekstu`.
2. Podgląd: `python3 -I praca/marketing/wzorzec-podglad.py praca/marketing/strona.html praca/marketing/podglad --sekcje`; w `podglad-pomiar.json`: `zly_kontrast` puste, `przewijanie_w_bok` 0, `niezaladowane` puste. Obejrzyj zrzuty sekcji.
3. Arkusz z p. 2.1 dosłownie + dopisek z p. 2.4 na końcu.
4. Hero: zdjęcia `eager` / `fetchpriority="high"` / `data-no-lazy="1"`; wszystkie inne `lazy`.
5. Każde `href="#x"` ma `id="x"`. Linki wewnętrzne tylko do opublikowanych adresów z `SPIS.json`. Przydatne dla marketingu: `/kontakt/`, `/przykladkowe-realizacje/`, `/grawerowanie-laserowe/`, `/wycinanie-laserowe/`, `/frezowanie-cnc/`, `/grawerowanie-laserowe/prezenty/`, `/blog/firmowe-prezenty-z-grawerem/`, `/blog/tworzenie-ekspozycji-dla-marek-kosmetycznych/`, `/case-study/`, `/materialy-do-grawerowania/`, `/uslugi-dla-horeca/`, `/uslugi-dla-przemyslu/`. NIE linkować: `/?page_id=1731` (najczęściej grawerowane przedmioty, szkic) ani wpisu 1841 (szkic o długopisach).
6. Tła: hero, potem wash i białe na przemian, sekcja przed pasem wash, pas w białej.
7. Zero żółtych ramek i „Wersja robocza”; brak źródła = brak zdania, pytanie do `pytania.md` (dopisywać).
8. Tylko dywiz `-`, bez `&&`, bez `border-width` / `border-color` w atrybutach `style`.
9. Jeden `<h1>`; pod `<h2>` tylko `<h3>` (także `<h3 class="pdl-h4">`).
10. Strona `/uslugi-dla-marketingu/` będzie szkicem, więc dopóki nie zostanie opublikowana, inne strony nie mogą do niej linkować (sprawdzarka, reguła `link`: adres spoza `SPIS.json`). Dotyczy to sekcji „Branże, w których grawerujemy” na stronie grawerowania, gdzie marketing ma być trzecią branżą obok HoReCa i przemysłu: link dodać przy publikacji.
