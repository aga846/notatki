## Typy danych w SQLite  
Jest 5 typów danych:  
- NULL (wartość None),  
- INTEGER (wartość integer),  
- REAL (liczba zmiennoprzecinkowa),  
- TEXT (tekst),  
- BLOB (dokładnie to, co wpsaliśmy).  
  
W SQLite nie ma booleanów. Wartości booleanowe są przechowywane jako 0 lub 1.  
W SQLite nie ma również typów daty ani czasu.  
  
## Definiowanie tabeli  
Tworzę plik o rozszerzeniu sql. Ale mogę również to wszystko zrobić w konsoli.  
Piszę "CREATE TABLE nazwa_tabeli(nazwy_kolumn_po_przecinku TYP_ZMIENNEJ);":  
```
CREATE TABLE dogs(
    name TEXT,
    breed TEXT,
    age INTEGER
  );
```
Jeśli utworzę tabelę z poziomu konsoli, to po wyjściu z SQLite, tabela nie będzie zapisana. Jeśli chcę ją zapisać, muszę utworzyć nowy plik poprzez ".open nazwa_pliku.db" i w tym pliku utworzyć tabelę, wpisując powyższą komendę. Jeśli wyjdę z sqlite i następnie wejdę w ten plik (poprzez komendę sqlite3 dog_db.db"), zadziała ".tables" - wyświetli się nazwa tabeli, którą utworzyłam.  
Zamiast ".open" mogę utworzyć plik wpisując "sqlite3 cats_db.db", i utworzyć tabelę - efekt będzie taki sam.  
  
## Wstawianie danych do tabeli  
W pliku lub w konsoli.  
Piszę "INSERT INTO nazwa_tabeli (nazwy_kolumn_po_przecinku) VALUES (wartości_w_tej_samej_kolejności_co_kolumny);":  
```
INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold" 3);
```
  
Mogę mieć w pliku wartości, które chcę wstawić do tabeli (już istniejącej w innym pliku). Załóżmy, że plik, w którym mam wartości do wstawienia, nazywa się "basics.sql".  
W konsoli otwieram plik (bazę danych), do którego chcę wstawić te wartości ("sqlite3 dog_db.db"), otwieram tabelę, która jest w tym pliku (".tables"), wpisuję komendę ".read basics.sql". Dzięki temu do tabeli dogs dopiszą się dane (wartości) zawarte w pliku "basics.sql".  
```
sqlite3 dog_db.db
.tables                 # dogs
.read basics.sql 
SELECT * FROM dogs;     # dane z pliku basics.sql   
```
  
  
## SELECT  
### Wszystko  
SELECT * FROM cats; - pokaże całą zawartość tabeli.  
"*" oznacza "wszystkie kolumny".  
  
### Określone kolumny  
Mogę też wyświetlić tylko kolumnę "name": SELECT name FROM dogs;.  
Mogę wyświetlić dwie różne kolumny: SELECT name, age FROM dogs;.  
  
### Określone wiersze  
Mogę wyświetlić tylko konkretny wiersz (wszystko w nim zawarte): SELECT * FROM dogs WHERE name IS "Piggy";.  
Jeśli któreś wiersze mają wspólną wartość dla jakiejś kolumny, zastosowanie powyższego wyświetli wszystkie te wiersze (np. (..) WHERE breed IS "Husky" - wyświetli wszystkie wiersze (psy), których rasa to "Husky").  
Mogę wyspecyfikować i chcieć tylko names tych psów (SELECT name FROM dogs WHERE breed IS "Husky").  
Mogę też użyć NOT - (...) WHERE breed IS NOT "Husky" - wyświetli wszystkie psy, których rasa jest inna niż "Husky".  
  
### Logic  
Można używać:  
- IS (również =),  
- IS NOT,  
- AND,  
- OR,  
- <,  
- >,  
- LIKE (WHERE name LIKE "%gg%" - gdzie w imieniu występują dwie litery g koło siebie),  
- ORDER BY (WHERE closeness > 5 ORDER BY closeness" - w sposób uporządkowany według closeness).
