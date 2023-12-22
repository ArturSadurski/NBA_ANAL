# NBA_ANAL

# NBA Data Analysis Project

## Źródło Danych

Dane zostały pobrane z [nba_api](https://pypi.org/project/nba_api/), które jest oficjalnym źródłem statystyk i informacji związanych z NBA.

## Zakres Danych

Analiza obejmuje sezony od 2000 do 2023. Zawiera kompleksowe statystyki dotyczące meczów, drużyn, zawodników oraz wyników.



# Opis Danych

## Dane Unikalne
Są to identyfikatory, które są unikatowe dla każdego wpisu i zazwyczaj nie powtarzają się.
- **Index**: Unikalny identyfikator dla każdego wpisu.
- **GAME_ID**: Unikalny identyfikator dla każdej gry.
- **GAME_EVENT_ID**: Unikalny identyfikator dla każdego wydarzenia w grze.
- **PLAYER_ID**: Unikalny identyfikator dla każdego gracza.
- **TEAM_ID**: Unikalny identyfikator dla każdego zespołu.

## Dane Kategoryczne
Są to dane, które przyjmują ograniczoną liczbę kategorii. Mogą być tekstowe lub numeryczne, ale reprezentują grupy lub kategorie.
- **GRID_TYPE**: Typ siatki lub układu użytego do reprezentacji danych.
- **PLAYER_NAME**: Nazwa gracza.
- **TEAM_NAME**: Nazwa zespołu.
- **EVENT_TYPE**: Typ wydarzenia (np. rzut, faul).
- **ACTION_TYPE**: Konkretna akcja w ramach wydarzenia.
- **SHOT_TYPE**: Typ wykonanego rzutu.
- **SHOT_ZONE_BASIC**: Ogólna strefa, z której wykonano rzut.
- **SHOT_ZONE_AREA**: Szczegółowy opis miejsca, z którego wykonano rzut.
- **SHOT_ZONE_RANGE**: Zakres odległości rzutu.
- **SHOT_ATTEMPTED_FLAG**: Wskazuje, czy podjęto próbę rzutu.
- **SHOT_MADE_FLAG**: Wskazuje, czy rzut zakończył się sukcesem czy niepowodzeniem.
- **HTM**: Oznaczenie drużyny gospodarzy.
- **VTM**: Oznaczenie drużyny gości.

## Dane Ciągłe
Są to dane numeryczne, które mogą przyjmować dowolną wartość w określonym zakresie.
- **MINUTES_REMAINING**: Minuty pozostałe w bieżącym okresie.
- **SECONDS_REMAINING**: Sekundy pozostałe w bieżącym okresie.
- **SHOT_DISTANCE**: Dokładna odległość, z której wykonano rzut.
- **LOC_X**: Współrzędna x (pozioma) na boisku, z której wykonano rzut.
- **LOC_Y**: Współrzędna y (pionowa) na boisku, z której wykonano rzut.

## Dane Inne
Są to dane, które nie pasują dokładnie do powyższych kategorii, ale są ważne w kontekście zestawu danych.
- **PERIOD**: Okres gry (numeryczny, ale określający specyficzne etapy gry, więc jest raczej traktowany jako dyskretny).
- **GAME_DATE**: Data rozegrania gry (format daty, traktowany jako ciągły w kontekście czasu).


## Planowane Analizy Statystyczne

W ramach projektu planujemy rozważyć przeprowadzenie niektórych z następujących analiz statystyczne:
- Analiza efektywności poszczególnych zawodników.
- Porównanie drużyn pod względem różnych statystyk.
- Trendy i zmiany w statystykach na przestrzeni lat.
- Prognozowanie wyników na podstawie zgromadzonych danych.
- Jak kontekst gry (mecz u siebie vs na wyjeździe, różnica punktów) wpływa na wydajność graczy.
- Wpływ sytuacji presji (ostatnie 5 minut, playoffs vs sezon zasadniczy) na decyzje i efektywność zawodników.
- Klasterowanie zawodników na podstawie statystyk do identyfikacji typów jak "strzelcy", "obrońcy", "wszechstronni gracze".
- Analiza skuteczności rzutów w zależności od odległości.
- Porównanie skuteczności rzutów wolnych, za 2 punkty i za 3 punkty.
- Wpływ zmęczenia na skuteczność rzutów w trakcie gry.
- Predykowanie wyników gier

## Cele Projektu

Celem projektu jest zrozumienie dynamiki i trendów w NBA, identyfikacja kluczowych czynników sukcesu oraz stworzenie modeli predykcyjnych, które pomogą w prognozowaniu przyszłych wyników.

## Jakość Danych

Pobrane dane były kompletnie i nie zawierały brakujących wartości. W celu symulacji rzeczywistych warunków, wprowadziliśmy losowo wartości NaN do niektórych kolumn, aby zademonstrować, jak można radzić sobie z brakującymi danymi.

## Metody Radzenia Sobie z Brakującymi Danymi

Podczas przetwarzania danych zastosowaliśmy kilka podstawowych technik radzenia sobie z brakującymi danymi:
- Usunięcie wierszy lub kolumn zawierających brakujące wartości.
- Wypełnienie brakujących wartości stałą wartością, średnią, medianą, lub najczęstszym wynikiem.
- Użycie algorytmów, które mogą obsługiwać brakujące dane.

## Zakończenie

Projekt jest w toku, a wyniki zostaną zaktualizowane w miarę postępu prac. Zachęcamy do śledzenia repozytorium i udziału w dyskusji.

