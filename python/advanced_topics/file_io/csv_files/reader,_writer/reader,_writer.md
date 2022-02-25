Reader i writer traktują każdy rząd w pliku csv jako listę - również rząd z nagłowkami (headers).  
  
# Czytanie pliku csv - reader  
Przy plikach csv, żeby python przeczytał taki plik, zamiast funkcji file.read(), stosuje się funkcję reader(file):  

```
with open("slowka.csv") as file:
    csv_reader = reader(file)
```  

Skoro reader traktuje każdy rząd jako listę, to poniższy for zwróci rzędy zawarte w pliku csv, jako listy:  

```
with open("slowka.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
        
# 
["ang", "pl"]
["overhaul", "wyremontowac"]
["seek", "szukac"]
```
  
## Reader jako iterator  
W powyższej pętli każdy z rzędów to lista, bo pętla ITERUJE po rzędach, a reader(file) daje iterator, lecz NIE LISTĘ. Można zrobić z niego listę:  
```
data = list(csv_reader)
```
    
  
## Delimiter - argument readera  
Delimiter oznacza znak, którym przedzielone są wartości. Domyślnie jest to przecinek (","), ale przy niektórych plikach jest to np. ";". Wtedy, żeby dało się przeczytać plik, w reader() oprócz pliku należy dać także argument "delimiter=";"":  

```
csv_reader = reader(file, delimiter=";")
```
  
    
# Przejście do kolejnego rzędu - next  
Reader(file) jest jak generator - przy wywołaniu funkcji next(), python przechodzi do kolejnego rzędu i nie będzie mógł przejść z powrotem do pierwszego.  

```
with open("slowka.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
```
Dzięki powyższemu kodowi, jeśli teraz napisałabym pętlę, wyświetliłby kolejne rzędy, bez pierwszego (nagłówków). 
  
  
# Pisanie w pliku csv - writer, writerow  
Podobnie jak w innych plikach, żeby móc pisać w pliku, dodawać coś na koniec pliku lub updatować plik, potrzebuję najpierw podać konkretny argument w open(). Przy pisaniu jest to "w". Przy appendowaniu jest to "a".  
W celu napisania czegoś w pliku, potrzebuję użyć funkcji writer oraz writerow - inaczej niż przy zwykłych plikach, w których po prostu do pliku przypisanego do zmiennej file (w "with open ... as file") stosuje się funkcję write - tutaj po przypisaniu pliku do zmiennej file muszę przypisać do kolejnej zmiennej (np. "csv_writer") "writer(file)" i dopiero do tej zmiennej muszę zastosować funkcję writerow:  

```
with open("slowka.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Damian", 26])
    csv_writer.writerow(["Aga", 26])
```
Najpierw dodaję nagłówki (headers) jako listę, a potem kolejne rzędy, również jako listę - bo writer traktuje rzędy jako listy.  
  
Writer nadpisuje plik oraz tworzy nowy, jeśli nie istnieje taki, jaki podałam w open().
