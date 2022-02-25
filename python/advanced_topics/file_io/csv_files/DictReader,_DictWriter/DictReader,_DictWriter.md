DictReader i DictWriter traktują każdy rząd w pliku jako jakby-słownik, z uporządkowanymi wartościami.  
  
# Czytanie pliku csv - DictReader  
Przy plikach csv, żeby python przeczytał taki plik, zamiast funkcji file.read(), stosuje się funkcję DictReader(file):  

```
with open("slowka.csv") as file:
    csv_reader = DictReader(file)
```  

Skoro DictReader traktuje każdy rząd jako jakby-słownik, to poniższy for zwróci rzędy zawarte w pliku csv, jako coś w rodzaju słownika - z header jako key i wartością z kolejnego rzędu jako value:  

```
with open("slowka.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row)
        
# 
OrderedDict([("ang", "overhaul"), ("pl", "wyremontowac")])
OrderedDict([("ang", "seek"), ("pl", "szukac")])
``` 

Do konkretnych wartości mogę dostać się używając keys - dla powyższej pętli:
  
```
print(row["ang"])

#
overhaul
seek
```

## DictReader to iterator  
W powyższej pętli każdy z rzędów to uporządkowany słownik, bo pętla ITERUJE po rzędach, ale DictReader(file) daje iterator, lecz NIE LISTĘ. Można zrobić z niego listę:  
```
data = list(csv_reader)
```  
  
## Delimiter - argument DictReadera  
Delimiter oznacza znak, którym przedzielone są wartości. Domyślnie jest to przecinek (","), ale przy niektórych plikach jest to np. ";" lub "|". Wtedy, żeby dało się przeczytać plik, w DictReader() oprócz pliku należy dać także argument "delimiter=";"":  

```
csv_reader = DictReader(file, delimiter=";")
```

# Pisanie w pliku csv - DictWriter, writeheader, writerow  
Podobnie jak w innych plikach, żeby móc pisać w pliku, dodawać coś na koniec pliku lub updatować plik, potrzebuję najpierw podać konkretny argument w open(). Przy pisaniu jest to "w". Przy appendowaniu jest to "a".  
W celu napisania czegoś w pliku, potrzebuję użyć funkcji DictWriter, writeheader oraz writerow - inaczej niż przy zwykłych plikach, w których po prostu do pliku przypisanego do zmiennej file (w "with open ... as file") stosuje się funkcję write - tutaj po przypisaniu pliku do zmiennej file muszę przypisać do kolejnej zmiennej (np. "csv_writer") "DictWriter(file)" i dopiero do tej zmiennej muszę zastosować funkcję writeheader oraz writerow:  

```
with open("slowka.csv", "w") as file:
    headers = ["First_name", "Last_name", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({"First_name": "Damian", "Last_name": "Jaskolski", "Age": 26})
    csv_writer.writerow({"First_name": "Aga", "Last_name": Jaskolska, "Age": 26})
```
Najpierw tworzę listę lub krotkę headers, w której umieszczam nagłówki. Headers to kwargs dla obiektu DictWriter. Za jego pomocą nazywa się headers (nagłówki, fieldnames).  
Potem tworzę obiekt klasy DictWriter, który nazywam csv_writer. Jako jego atrybuty podaję plik oraz fieldnames - czyli nasze wczesniej utworzone headers. Fieldnames to keyword argument, więc trzeba napisać "fieldnames=".  
Następnie do obiektu tej klasy stosuję funkcję writeheader(), która dodaje rząd headers: bierze podane jako atrybut fieldnames i dodaje za nas.  
Potem, stosując writerow(), dodaję kolejne rzędy, podając je jako słownik. Key to nagłówek, header, a value to wartość, która ma być w danej komórce.  
  
Writer nadpisuje plik oraz tworzy nowy, jeśli nie istnieje taki, jaki podałam w open().
