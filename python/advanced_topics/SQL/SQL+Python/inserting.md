# Wstawianie danych do tabeli  
## Wstawianie pojedynczych danych  
### Wstawienie wartości w kodzie SQL  
Można przypisać do zmiennej kod SQLowy, w którym wstawimy wartości, i potem tę zmienną wstawić do metody execute():  
```
insert_query = '''INSERT INTO friends 
                  VALUES ("Merry", "Lewis", 7)'''
c.execute(insert_query)
```
Dzięki użyciu potrójnego pojedycznego cudzysłowia zamiast zwykłych cudzysłowiów, można łamać linię.  
   
### Słaby sposób - wstawienie za pomocą f-stringa  
Można przypisać zmienną do jakiejś wartości, którą chcemy wstawić.  
Następnie przypisać zmienną do f-stringa (kodu SQLowego), w którym zawrzemy wartość, którą chcemy wstawić (powyżej przypisaną do zmiennej).  
Wstawić zmienną do metody execute().  
```
form_first = "Dana"
query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
c.execute(query)
```
  
### Dobry sposób - wstawienie za pomocą ?  
W kodzie SQL w miejscu na wartości do wstawienia piszemy znak zapytania. Następnie metodzie execute() podajemy nie tylko zmienną, która jest przypisana do tego kodu SQL, ale też krotkę zmiennych, do których przypisane są wartości, które chcemy wstawić (jak nie damy krotki, będzie iterować przez każdy znak tej wartości):  
```
form_first = "Mary-Todd"
query = f"INSERT INTO friends (first_name) VALUES (?)
c.execute(query, (form_first,))
```
Żeby wstawić wiele wartości, dobrze jest do zmiennej z wartościami przypisać te wartości naraz, w krotce. Wtedy w VALUES podaje się znaki zapytanie po przcinku, a metodzie execute() podaje się nie krotkę, w której jest zmienna, tylko po prostu zmienną (tutaj dobrze będzie, jak będzie iterować przez te wartości):  
```
data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
```  
  
## Wstawianie wielu danych (bulk inserts)  
Mam listę krotek, w których zawarte są dane, która chcę wstawić - każda krotka to kolejny rząd.  
```
people = [
  ("Kasia", "Pal", 10),
  ("Ania", "Piet", 8),
  ("Asia", "Roz", 7),
  ("Dorota", "Woj", 7)
]  
```
  
Mogę:  
1. iterować przez tę listę (pętla for, dla każdej krotki w tej liście robię wstawienie za pomocą ?):  
```
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
```
Przydaje się wtedy, kiedy chcę te dane wstawić w wiele miejsc lub chcę np. robić jakieś działania z niektórymi wartościami, które będę wstawiać (jak np. przechowywanie średniej jakichś wartości), np.  
```
average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]
print(average/len(people))
```
    
2. lub mogę użyć metody executeMany(). Tej metodzie dostarczam query (kod SQL) oraz listę, którą chcę wstawić: 
```
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
```
Mogę podać inną kolejność, po friends dając w nawiasie tę kolejność (INSERT INTO friends (last_name, first_name, closeness)). Dopóki daję po kolei - tak, jak mam nazwy kolumn, to nie podaję w nawiasie nic. 
