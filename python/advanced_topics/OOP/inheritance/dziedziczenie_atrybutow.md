# O co chodzi w dziedziczeniu atrybutów  
W dziedziczeniu atrybutów chodzi o to, żeby się nie powtarzać, tj. nie przepisywać kilka razy tego samego, np. "self.name = name". Skoro klasa-rodzic już ma to zawarte w swoim __init__, to nie ma potrzeby pisać tego samego drugi raz w klasie-dziecku - o ile atrybuty w tej klasie są takie same, co w klasie-rodzicu.

## Dłuższa droga do dziedziczenia atrybutów klasy-rodzica  
W funkcji __init__() klasy-dziecka wpisuję jako parametry wszystkie atrybuty, a potem zamiast się powtarzać i pisać "self.name = name" i "self.species = species", daję znać, że atrybuty, które są już zawarte w __init__ konkretnej, wskazanej klasy-rodzica, dotyczą też obiektu klasy-dziecka. Następnie wpisuję "self.breed = breed" oraz "self.toy = toy" - dla atrybutów, których obiekt klasy-rodzica nie posiada.  
Innymi słowy - niektóre atrybuty są zdefiniowane w klasie-rodzicu, a niektóre w klasie-dziecku.  

Składnia:  
nazwa_klasy-rodzica.__init__(self, atrybuty_obiektow_klasy-rodzica)

```
class Animal:
    def__init__(self, name, species):
        self.name = name
        self.species = species
        
class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        Animal.__init(self, name, species)
        self.breed = breed
        self.toy = toy
```

## Krótsza droga do dziedziczenia atrybutów klasy-rodzica - super()  
Dokładnie to, co jest przy dłuższej drodze, dotyczy krótszej drogi, różnicą jest jedynie to, że zamiast podawać nazwę_klasy-rodzica, piszę "super()" oraz nie zamieszczam "self" potem w nawiasach, w których wymieniam atrybuty.  
Super() samo wywoła klasę Animal oraz jego self.
Super() odnosi się do klasy "bazowej", aktualnej klasy bazowej, która może się zmieniać w zależności od kontekstu (gdy dziedziczenie z większej ilości klas).

Składnia:  
super().__init__(atrybuty_obiektow_klasy-rodzica)

```
class Animal:
    def__init__(self, name, species):
        self.name = name
        self.species = species
        
class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        super().__init(name, species)
        self.breed = breed
        self.toy = toy
```

### Domyślna wartość atrybutu klasy-dziecka  
Mogę również, podczas wymieniania atrybutów w super(), ustalić domyślną wartość dla danego atrybutu klasy-dziecka. Wtedy usuwam ten atrybut z parametrów funkcji __init__ klasy-dziecka:  

```
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
        
class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy
```

### Wywoływanie __init__ klasy-rodzica  
Jeśli zarówno w klasie-rodzicu, jak i w klasie-dziecku mam zdefiniowaną metodę __init__, to tylko wywołanie wprost __init__ klasy-rodzica w klasie-dziecku rzeczywiście wywołuje tę metodę. Jeśli w __init__ klasy-rodzica mam zawarty jakiś kod, np. zwiększanie atrybutu klasy przy każdym utworzeniu nowego obiektu klasy, to bez wywołania __init__ klasy-rodzica w klasie-dziecku, ten kod nie będzie egzekwowany, np. jeśli w klasie-rodzicu User w funkcji __init__ dodaję użytkowników przy każdym tworzeniu nowego użytkownika (do zmiennej active_users), to jeśli w klasie-dziecku Moderator(User) nie wywołam tego __init__, to przy utworzeniu obiektu klasy-dziecka nie zostanie dodany nowy użytkownik do zmiennej User.active_users.  

Inaczej jest, jeśli klasa-dziecko nie ma zdefiniowanej metody __init__. Wtedy przy tworzeniu obiektu klasy-dziecka jest wywoływane __init__ klasy-rodzica.

### Wywoływanie innych metod z klasy-rodzica za pomocą super  
W super() mogę zawrzeć jakąkolwiek metodę z klasy-rodzica, np.  

```
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("I am making sound")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def meow(self):
        super().make_sound()


blue = Cat("Blue", "Scottish", "String")
blue.meow()    # I am making sound
```

to samo z podaniem argumentu:

```
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def meow(self, sound):
        super().make_sound(sound)


blue = Cat("Blue", "Scottish", "String")
blue.meow("meow")
```
