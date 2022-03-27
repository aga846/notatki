# Dokonywanie zmian w pliku csv przy pomocy DictReader i DictWriter  
  
```
from csv import DictReader, DictWriter

def cm_to_in(cm):
    return float(cm) * 0.393701
    
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)
    
with open("inches_fighters.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({"Name": f["Name"], "Country": f["Country"], "Height": cm_to_in(f["Height_cm"])})
```
  
Najpierw napisałam funkcję, którą będę stosować do elementów, które w nowym pliku mają zostać zmienione: tutaj napisałam funkcję, która zmienia wysokość podaną w centymetrach na wartość w calach (zwraca wysokość podaną w cm na podaną w calach).  
   
Następnie otwieram plik do odczytu, przypisuję odczyt pliku do zmiennej csv_reader oraz z tej zmiennej robię listę, która nazywa się "fighters".  
  
W kolejnym "with open" otwieram nowy plik, w trybie do pisania - "w" (lub tworzę go w ten sposób).  
Przypisuję headers, podane w krotce.  
Potem tworzę obiekt klasy DictWriter, który nazywam csv_writer. Jako jego atrybuty podaję plik oraz fieldnames - czyli wyżej utworzone headers.  
Za pomocą funkcji writeheader() zastosowanej do obiektu csv_writer, tworzę rząd headers.  
Dla każdego elementu w liście fighters (która jest krotką list zawierających krotki - czyli czymś w rodzaju listy słowników:  
  ([("Name": "Arthur"), ("Country": "USA"), ("Height_cm": 175)],  
   [("Name": "Jake"), ("Country": "Japan"), ("Height_cm": 175)]  
   )  
), robię nowy rząd w nowym pliku inches_fighters.csv i w argumentach do writerow podaję:  
header: value od key w fighters (dla każdego fightera - f) -> "Name": f["Name"],  
dodatkowo do wartości, którą chcę zmienić, stosuję funkcję cm_to_in.
