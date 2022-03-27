# Self jako parametr w każdej metodzie obiektów klasy  
W każdej funkcji zamieszczonej w klasie, pierwszym parametrem musi być self. Jeśli chcę w tej funkcji odwoływać się do atrybutów konkretnego obiektu, nie mogę po prostu podać "atrybut", tylko "self.atrybut".  
Podając "self" jako parametr danej funkcji przy jej definiowaniu, ma ona dostęp do wszystkich argumentów danego obiektu.  
  
```
class User:
    def __init__(self, first, last, age=20):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"


user1 = User("Damian", "Jaskolski", 26)
print(user1.full_name())          # Damian Jaskolski
```
  
## Nadpisywanie funkcji w klasie  
Jeśli dana metoda/funkcja już istnieje i jest "special dunder method" (jak np. __init__()), a chcę dla obietów danej klasy zmienić tę funkcję, muszę dodać "__" na początku i końcu nazwy danej metody.  
Jeśli natomiast tworzę własną metodę (jak powyżej - full_name), nie jest konieczne dodawanie "__".  
  
  
## Kolejność metod obiektu   
Najpierw umieszczamy wszystkie dunder methods, potem wszystkie inne.  
   
  
# Parametry w metodzie  
Ponieważ funkcja obiektu zdefiniowana w klasie poprzez zamieszczenie w niej parametru "self" ma dostęp do wszystkich atrybutów obiektu, nie umieszczamy tych atrybutów jako kolejne parametry funkcji.  
Można natomiast zamieścić kolejne parametry - są to takie parametry, który nie są atrybutami podanymi w __init__. Argument do takiej funkcji podaje się przy jej wywoływaniu.  
Podsumowując, jeśli w funkcji używam tylko atrybutów danego obiektu, nie podaję ich w parametrach funkcji (metody) tego obiektu.  
   
```
class User:
    def __init__(self, first, last, age=20):
        self.first = first
        self.last = last
        self.age = age

    def likes(self, thing):
        return f"{self.first} likes {thing}"


user1 = User("Damian", "Jaskolski", 26)
print(user1.likes("Ice Cream"))       # Damian likes Ice Cream
```
