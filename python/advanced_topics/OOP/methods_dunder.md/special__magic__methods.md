# Czym są special__magic__methods?  
Special_magic_methods to zawsze dunder methods!!!  

To metody, które działają dla obiektów różnych klas, tj. ta sama nazwa metody, operacja, działa dla obiektów różnych klas. W dokumentacji dostępny jest spis tych metod. Są to np.  
- len działa inaczej na listach, krotkach, stringach,  
- dodawanie działa inaczej na stringach i na integerach:  

```
8 + 2           # 10
"8" + "2"       # "82"
```

Operator "+" jest skrótem dla specjalnej metody __add__(), która jest wywoływana dla pierwszego operanda.  
Jeśli pierwszy operand to int, metoda __add__() robi dodawnie.  
Jeśli pierwszy operand to string, metoda __add__() robi łączenie.

## Własne definiowane special__magic__methods  
Mogę na potrzeby swojej klasy zmieniać special__magic__methods. Wtedy nadpisują się dla obiektów danej klasy. Mogę również odwoływać się (również w tych nowych special__magic__methods) do pierwotnej metody, np.  

```
class GrumpyDict(dict):
      def __repr__(self):
          print("NONE OF YOU BUSINESS")
          return super().__repr__()
```

### Własne definiowanie len()   
Jeśli stworzę klasę Human i chcę, żeby długość (len) obiektu tej klasy oznaczała wysokość danego obiektu (człowieka), mogę zdefiniować metodę len() w tej klasie, używając "__" na początku i na końcu nazwy tej metody. Jeśli nie dodam podwójnego pokreślnika, wywali błąd: "object of type Human" has no len()".  
Do wyniku tej metody mogę dostać się zarówno używając len(obiekt), jak i tak jak do każdej innej metody obiektu: obiekt.__len__().

```
class Human:
    def __init__(self, height):
        self.height = height

    def __len__(self):
        return self.height


Aga = Human(170)
print(len(Aga))           # 170
print(Aga.__len__())      # 170
```
  
### Własne definiowanie add()  
Na potrzeby klasy Human chcę stworzyć funkcję, która będzie dodawała jeden obiekt do drugiego (jednego człowieka do drugiego) i tworzyła nowy obiekt (człowieka) o konkretnym imieniu ("Newborn"), nazwisku (równym nazwisku pierwszego obiektu) i wieku (0).  

W metodzie __add__ jako parametry podaję self (czyli obiekt klasy) oraz other, który będzie odnosił się do drugiego obiektu, który chcę dodać do pierwszego obiektu.  
W tej funkcji najpierw sprawdzam, czy drugi argument (other) jest obiektem tej klasy. Jeśli jest - wynikiem tej funkcji będzie nowy obiekt klasy o podanych atrybutach. Jeśli nie jest - wynikiem będzie string "You can't add that!".  

Żeby wywołać tę funkcję, tak jak w przypadku metody len(), mogę albo użyć skrótu metody add(), czyli "+", albo mogę ją wywołać tak jak każdą inną metodę obiektu klasy (obiekt.__add__()).
```
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.special__magic__methods

    def __add__(self, other):
        if isinstance(other, Human):
            return Human("Newborn", self.last, 0)
        return "You can't add that!"


aga = Human("Aga", "Jaskolska", 26)
damian = Human("Damian", "Kleska", 26)
child = aga.__add__(damian)
child1 = aga + damian
print(child)      # Human named Newborn Jaskolska
print(child1)     # Human named Newborn Jaskolska
print(aga + 2)    # You can't add that!
```
    
### Własne definiowanie mul()  
Na potrzeby funkcji Human chcę stworzyć funkcję, która będzie mnożyła obiekty klasy.  
Wywołanie tej funkcji - albo tak jak każdą inną metodę klasy, albo poprzez "*" - skrót dla metody __mul__().  
Jeśli będę chciała pomnożyć obiekt razy cokolwiek innego, będzie to działało. Ale jeśli będę chciała pomnożyć cokolwiek innego razy obiekt, wywali błąd, ponieważ python będzie stosował metodę mul() dla pierwszego podanego operanda (tj. aga * 2 będzie ok, ale 2 * aga nie będzie ok).  

Najpierw sprawdzam, czy drugi parametr (other) jest integerem. Jeśli tak:  
- mogę zwrócić listę dzięki list comprehension: [self for i in range(other)], wtedy otrzymam listę składającą się z elementów "Human named .. .." w takiej ilości, przez którą pomnożyłam. Problemem jest to, że tutaj nie robię nowych obietów, tylko tworzę listę reprezentacji obiektu "aga". Jeśli w takim przypadku chciałabym zmienić imię (self.first) tylko elementu na indeksie 1 w tej liście, to zmieniłabym imię dla każdego elementu tej listy.  
- mogę użyć funkcji copy z modułu copy i zrobić listę kopii obiektu: [copy(self) for i in range(other)]
```
from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.special__magic__methods

    def __add__(self, other):
        if isinstance(other, Human):
            return Human("Newborn", self.last, 0)
        return "You can't add that!"
    
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
          return "Can't multiply"
        
aga = Human("Aga", "Jaskolska", 26)
damian = Human("Damian", "Kleska", 26)   
print(aga * 3)
# [Human named Aga Jaskolska, Human named Aga Jaskolska, Human named Aga Jaskolska]
```

### Łączenie stworzonych add() i mul()  
Mogę stworzyć "trojaczki" dla agi i damiana:  
print((aga + damian) * 3)
