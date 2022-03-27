# Dokonywanie zmian w pliku csv przy pomocy reader i writer  
Są 2 sposoby:  
- za pomocą dwóch "with open",  
- w obrębie jednego "with open".  
  
## Dwa "with open"  
  
```
from csv import reader, writer

with open("fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    
with open("screaming_fighters.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)
```
Pierwsze "with open":  
Najpierw otwieram plik "fighters.csv" tylko do odczytu.  
Do zmiennej csv_reader przypisuję odczyt pliku (czyli cały ten plik).  
Tworzę nową listę "fighters", która zawiera [[powiększone słowo dla każdego słowa w rzędzie] dla każdego rzędu w csv_reader] - czyli listę list, w której są te wartości, co w pliku fighters.csv, tylko pisane WIELKIMI LITERAMI.  
  
Drugie "with open":  
Otwieram do pisania (nie do appendowania) plik screaming_fighters.csv.  
Do zmiennej csv_writer przypisuję pisanie w pliku (writer(file)).  
Dla każdego rzędu/listy w liście fighters dopisuję kolejny rząd w csv_writer.  
  
  
## Jedno "with open"  

```
from csv import reader, writerow

with open("fighters.csv") as file:
    csv_reader = reader(file)
    with open("screaming_fighters.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_wrtier.writerow([s.upper() for s in fighter])
```

Drugie "with open" musi być zagnieżdżone w pierwszym, dlatego że "with open" zamyka od razu plik i nie miałabym wtedy dostępu do zmiennej csv_reader.  
Nie zrobiłam tu żadnej nowej listy fighters, tylko wykorzystałam csv_reader w forze zawartym w drugim "with open".  
Csv_reader jest połączony z plikiem który zostałby zamknięty, gdybym nie zagnieździła drugiego "with open" z pierwszym.
