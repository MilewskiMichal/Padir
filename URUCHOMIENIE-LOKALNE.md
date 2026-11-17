# Uruchomienie lokalne z Chrome

Cel: Claude Code na Twoim komputerze, w tym repozytorium, z dostępem do Twojego Chrome (WhitePress, Webpozycja, Senuto, panel WordPressa i wszystko, na co jesteś zalogowany). Najważniejsze informacje o projekcie Claude wczyta sam z `CLAUDE.md`.

## Czego potrzebujesz

- macOS, Windows albo Linux. **Nie WSL**: tam integracja z Chrome nie działa.
- Google Chrome (albo Edge) z rozszerzeniem [Claude in Chrome](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) w wersji 1.0.36 lub nowszej. Rozszerzenie musi być zalogowane na **to samo konto i tę samą organizację** claude.ai co Claude Code.
- [Claude Code](https://code.claude.com/docs/en/quickstart) zalogowany przez `/login` kontem claude.ai. Logowanie kluczem API wyłącza Chrome.
- git i Python 3.10 lub nowszy.

## 1. Repozytorium

```bash
git clone https://github.com/MilewskiMichal/Padir.git
cd Padir
git checkout claude/padir-wordpress-integration-labd7q
```

## 2. Python

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install python-docx pillow playwright openpyxl
python -m playwright install chromium
```

Do czego to służy:

- `python-docx` i `playwright` budują artykuły WhitePress (docx i infografiki).
- `pillow` składa kontaktówki zdjęć.
- `openpyxl` eksportuje zgłoszenia z formularza.
- Same skrypty do WordPressa działają na czystym Pythonie.

## 3. Hasło do WordPressa

Przy okazji zrób rotację, bo stare hasło aplikacji kiedyś wyciekło:

1. W panelu WordPressa otwórz Użytkownicy, potem profil konta, którego używa Claude, i sekcję Hasła aplikacji.
2. Unieważnij stare hasło i wygeneruj nowe.
3. Zapisz je w zmiennych środowiskowych. Nigdy nie wklejaj go w czacie z Claude ani do repozytorium.

macOS i Linux (dopisz do `~/.zshrc` albo `~/.bashrc`, potem otwórz nowy terminal):

```bash
export PADIR_WP_USER="login-konta"
export PADIR_WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"
```

Windows (PowerShell, potem nowe okno terminala):

```powershell
setx PADIR_WP_USER "login-konta"
setx PADIR_WP_APP_PASSWORD "xxxx xxxx xxxx xxxx xxxx xxxx"
```

Zamiast zmiennych możesz utworzyć `wordpress/wp.creds.json` z treścią `{"user": "...", "app_password": "..."}`. Plik jest w `.gitignore`; na macOS i Linuksie nadaj mu `chmod 600`.

Test, który tylko czyta i przy okazji odświeża spis stron dla sprawdzarki:

```bash
python3 wordpress/narzedzia/odswiez_zrodla.py
```

Powinien wypisać liczbę stron, wpisów i plików w bibliotece mediów.

## 4. Chrome

1. Zainstaluj rozszerzenie i zaloguj się w nim.
2. W katalogu repozytorium uruchom `claude --chrome`. Za pierwszym razem pojawi się okno o integracji z Chrome; zatwierdź Enterem.
3. Wpisz `/chrome` i wybierz **Enabled by default**. Od teraz Chrome łączy się sam, bez flagi.
4. Panel `/chrome` powinien pokazywać „Status: Enabled” i „Extension: Installed”.
5. Wyjdź z Claude Code (`/exit`).

## 5. Start pracy

**Wariant A, kontynuacja rozmowy z chmury** (ta sama historia, gałąź i ustalenia):

```bash
claude --teleport session_01MTxcc6Zm7EqVd3RvtaSbGk
```

Uruchom to w katalogu repozytorium, bez niezacommitowanych zmian. Claude pobierze gałąź i wczyta rozmowę w wersji skróconej, bo w chmurze była już kompaktowana. Sesja w chmurze zostaje bez zmian, a dalsza praca toczy się już lokalnie.

**Wariant B, świeża sesja**:

```bash
claude --chrome
```

Wszystko, co potrzebne, Claude wczyta z `CLAUDE.md`.

Pierwsze zadanie do wklejenia:

```
Sprawdź w WhitePress przez Chrome, dlaczego odrzucono artykuły nr 1 i 6 (powód i komentarz wydawcy przy każdym zleceniu). Tylko czytaj, niczego nie klikaj poza otwieraniem stron. Potem zaproponuj poprawki i przebuduj paczki.
```

## Gdy coś nie działa

- **„Browser extension is not connected” albo „No browsers are connected”**:
  1. Sprawdź, czy rozszerzenie jest zalogowane na to samo konto i tę samą organizację co Claude Code (`/status`, wiersz Organization).
  2. Zrestartuj Chrome i Claude Code.
  3. Wpisz `/chrome` i wybierz Reconnect extension.
- **Rozszerzenie niewykryte przy pierwszym uruchomieniu**: zrestartuj Chrome, bo musi wczytać nową konfigurację połączenia.
- **Połączenie zrywa się po dłuższej przerwie**: wpisz `/chrome` i wybierz Reconnect extension.
- **Skrypt mówi „Brak poświadczeń WordPressa”**: zmienne z punktu 3 nie są widoczne w tym terminalu. Otwórz nowe okno albo sprawdź plik `wordpress/wp.creds.json`.

Dokumentacja: [Claude Code z Chrome](https://code.claude.com/docs/en/chrome), [przenoszenie sesji z chmury](https://code.claude.com/docs/en/claude-code-on-the-web#continue-a-cloud-session-in-your-terminal).
