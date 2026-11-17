# Padir, obsluga serwisu grawerowanie-laserowe.pl

Skrypty do pracy na serwisie przez REST API WordPressa.

## Start

- `CLAUDE.md`: najwazniejsze informacje o projekcie, zasady i stan prac (Claude Code wczytuje go sam).
- `URUCHOMIENIE-LOKALNE.md`: praca lokalna z Claude Code i Chrome.

## Poswiadczenia

`wordpress/wp.py` bierze je ze zmiennych srodowiskowych `PADIR_WP_USER`
i `PADIR_WP_APP_PASSWORD`, a gdy ich nie ma, z pliku
`wordpress/wp.creds.json` (uprawnienia 600, poza repozytorium):

    {"user": "<login>", "app_password": "<haslo aplikacji>"}

Haslo aplikacji generuje sie w panelu WordPressa: Uzytkownicy, profil,
Hasla aplikacji. Nie wklejaj go do repozytorium ani na czat.

## Zasady, ktore wynikly z pracy na tym serwisie

- **Kazdy skrypt ma probe na sucho.** Domyslnie nic nie zapisuje,
  dopiero `--wdroz` wysyla zmiany.
- **Kopia przed kazdym zapisem**, do pliku `backup-*.json` obok skryptu.
- **Sprawdzenie na SERWOWANEJ stronie**, nie na lokalnym podgladzie.
  Motyw i LiteSpeed potrafia zmienic wynik.
- **`data-no-optimize="1"` na kazdym `<style>` w tresci.** Bez tego
  LiteSpeed wciaga arkusz do pliku zbiorczego, a UCSS wycina z niego
  reguly. Raz skonczylo sie to zerem regul na stronie.
- **Nie uzywac zarezerwowanych parametrow zapytania** przy omijaniu
  pamieci podrecznej: `?p=`, `?w=`, `?cat=`, `?s=`, `?m=`. WordPress
  interpretuje je jako zapytanie i oddaje inna strone albo 404.
  Bezpieczny jest `?odswiez=`.
- **HTML parsowac parserem, nie wyrazeniem regularnym.** Kilka razy
  regex zlapal nazwe klasy wewnatrz `<style>` zamiast elementu.
- **Zadnych pauz (— –) w tresciach po polsku**, wylacznie dywiz.
