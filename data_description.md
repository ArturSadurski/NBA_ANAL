# Opis Danych

## Pierwsze 5 wierszy danych
|    |   index | GRID_TYPE         |   GAME_ID |   GAME_EVENT_ID |   PLAYER_ID | PLAYER_NAME   |    TEAM_ID | TEAM_NAME          |   PERIOD |   MINUTES_REMAINING |   SECONDS_REMAINING | EVENT_TYPE   | ACTION_TYPE                     | SHOT_TYPE      | SHOT_ZONE_BASIC       | SHOT_ZONE_AREA   | SHOT_ZONE_RANGE   |   SHOT_DISTANCE |   LOC_X |   LOC_Y |   SHOT_ATTEMPTED_FLAG |   SHOT_MADE_FLAG |   GAME_DATE | HTM   | VTM   |
|---:|--------:|:------------------|----------:|----------------:|------------:|:--------------|-----------:|:-------------------|---------:|--------------------:|--------------------:|:-------------|:--------------------------------|:---------------|:----------------------|:-----------------|:------------------|----------------:|--------:|--------:|----------------------:|-----------------:|------------:|:------|:------|
|  0 |       0 | Shot Chart Detail |  22200001 |               7 |      203954 | Joel Embiid   | 1610612755 | Philadelphia 76ers |        1 |                  11 |                  38 | Missed Shot  | Turnaround Fadeaway shot        | 2PT Field Goal | Mid-Range             | Left Side(L)     | 8-16 ft.          |              12 |    -118 |      50 |                     1 |                0 |    20221018 | BOS   | PHI   |
|  1 |       1 | Shot Chart Detail |  22200001 |              11 |      203935 | Marcus Smart  | 1610612738 | Boston Celtics     |        1 |                  11 |                  15 | Made Shot    | Driving Floating Bank Jump Shot | 2PT Field Goal | Mid-Range             | Right Side(R)    | 8-16 ft.          |              13 |     120 |      55 |                     1 |                1 |    20221018 | BOS   | PHI   |
|  2 |       2 | Shot Chart Detail |  22200001 |              12 |      202699 | Tobias Harris | 1610612755 | Philadelphia 76ers |        1 |                  11 |                   5 | Missed Shot  | Driving Floating Jump Shot      | 2PT Field Goal | In The Paint (Non-RA) | Center(C)        | 8-16 ft.          |              14 |      50 |     135 |                     1 |                0 |    20221018 | BOS   | PHI   |
|  3 |       3 | Shot Chart Detail |  22200001 |              14 |      202699 | Tobias Harris | 1610612755 | Philadelphia 76ers |        1 |                  11 |                   3 | Made Shot    | Tip Layup Shot                  | 2PT Field Goal | Restricted Area       | Center(C)        | Less Than 8 ft.   |               0 |       0 |       0 |                     1 |                1 |    20221018 | BOS   | PHI   |
|  4 |       4 | Shot Chart Detail |  22200001 |              15 |     1628369 | Jayson Tatum  | 1610612738 | Boston Celtics     |        1 |                  10 |                  46 | Made Shot    | Jump Shot                       | 3PT Field Goal | Left Corner 3         | Left Side(L)     | 24+ ft.           |              23 |    -232 |      49 |                     1 |                1 |    20221018 | BOS   | PHI   |

## Informacje o danych
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4589583 entries, 0 to 4589582
Data columns (total 25 columns):
 #   Column               Dtype  
---  ------               -----  
 0   index                int64  
 1   GRID_TYPE            object 
 2   GAME_ID              int64  
 3   GAME_EVENT_ID        int64  
 4   PLAYER_ID            int64  
 5   PLAYER_NAME          object 
 6   TEAM_ID              int64  
 7   TEAM_NAME            object 
 8   PERIOD               int64  
 9   MINUTES_REMAINING    float64
 10  SECONDS_REMAINING    float64
 11  EVENT_TYPE           object 
 12  ACTION_TYPE          object 
 13  SHOT_TYPE            object 
 14  SHOT_ZONE_BASIC      object 
 15  SHOT_ZONE_AREA       object 
 16  SHOT_ZONE_RANGE      object 
 17  SHOT_DISTANCE        int64  
 18  LOC_X                int64  
 19  LOC_Y                int64  
 20  SHOT_ATTEMPTED_FLAG  int64  
 21  SHOT_MADE_FLAG       int64  
 22  GAME_DATE            int64  
 23  HTM                  object 
 24  VTM                  object 
dtypes: float64(2), int64(12), object(11)
memory usage: 875.4+ MB
```
## Informacja o braku danych (liczba brakujących wartości)
|                     |   0 |
|:--------------------|----:|
| index               |   0 |
| GRID_TYPE           |   0 |
| GAME_ID             |   0 |
| GAME_EVENT_ID       |   0 |
| PLAYER_ID           |   0 |
| PLAYER_NAME         |   0 |
| TEAM_ID             |   0 |
| TEAM_NAME           |   0 |
| PERIOD              |   0 |
| MINUTES_REMAINING   |  10 |
| SECONDS_REMAINING   |  10 |
| EVENT_TYPE          |   0 |
| ACTION_TYPE         |   0 |
| SHOT_TYPE           |   0 |
| SHOT_ZONE_BASIC     |   0 |
| SHOT_ZONE_AREA      |   0 |
| SHOT_ZONE_RANGE     |   0 |
| SHOT_DISTANCE       |   0 |
| LOC_X               |   0 |
| LOC_Y               |   0 |
| SHOT_ATTEMPTED_FLAG |   0 |
| SHOT_MADE_FLAG      |   0 |
| GAME_DATE           |   0 |
| HTM                 |   0 |
| VTM                 |   0 |
