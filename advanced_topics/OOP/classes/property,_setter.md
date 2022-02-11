# Czym jest @property w klasie?  
Dzięki @property można dostać się do atrybutu, który był przewidziany jako prywatny (bo z _), bez konieczności pisania metody np. get_age(self) i set_age(self, new_age), które dla przykładu napiszę poniżej:  

## Przykład get_age i set_age  
```
def get_age(self):
    return self._age

def set_age(self, new_age):
    if new_age >= 0:
        self._age = new_age
    else:
        self._age = 0
```

służyłyby one do:  
- dostania się,  
- zmiany  
atrybutu _age, który był przewidziany jako prywatny.  

Nie jest konieczne jednak pisanie takich funkcji, jeśli skorzystamy z @property.  


## Przykład property

Polega na napisaniu funkcji o nazwie takiej, jak atrybut, zwrócenie w niej tego atrybutu oraz poprzedzenie jej "@property".  

```
@property
def age(self):
    return self.get_age
```

Ustalamy tutaj property, który nazywa się "age" i zwracamy prywatny atrybut.  
Kiedy odwołujemy się do neigo, nie musimy wywoływać tej metody/funkcji, piszą nawiasy - do property można dostać się tak, jak do zwykłego atrybutu, tak, jakby to był atrybut:  

```
print(jane.age)
```
    
Można dodać także jeszcze nieistniejący property.  


# Czym jest setter?  
Setter zapobiega zmianie atrybutu na wartość, której nie chcemy - w tym przypadku zmiany age na negatywną wartość. Inaczej niż przy zwykłej metodzie set_age, dzięki dekoratorowi @setter niemożliwa będzie zmiana age na negatywną wartość, bo zostanie wyrzucony błąd.  

## Przykład setter  

Polega na:  
- napisaniu funkcji o nazwie takiej, jak atrybut,  
- przypisanie jej parametru self oraz nowej_wartości,  
- zawarcie w niej warunku oraz ewentualnie wywołanie błędu,  
- poprzedzenie jej "@atrybut.setter".  

```
@age.setter
def age(self, value):
    if value >= 0:
        self._age = value
    else:
        raise ValueError("age can't be negative!")
```

teraz, żeby ustawić nową wartość dla danego atrybutu (tutaj: dla age), wystarczy zmienić go tak, jakby to był zwykły atrybut, nie trzeba wywoływać funkcji age(self, value):  

```
jane.age = 20
```


## Uwagi wspólne dla property i setter  
Jeśli chcę nazwać property inaczej, wtedy setter też musi być nazwany inaczej, tak jak property - np. "rage". Wtedy ten "rage" będzie manipulował atrybutem _age.  

### Przykład z full_name  
Mogę stworzyć property o nazwie full_name, wykorzystującej inne atrybuty danego obiektu, ale nie jest wskazane tworzenie wtedy również settera:  

```
@property
def full_name(self):
    return f"{self.first} {self.last}"
```

Stworzenie settera jest możliwe, ale wtedy zmieniamy więcej atrybutów za jego pomocą:  

```
@full_name.setter
def full_name(self, name):
    self.first, self.last = name.split(" ")
```

wtedy, jeśli napiszę:
```
jane.full_name = "Tim Minchin"
```
atrybuty first i last zostaną zmienione. Dlatego nie jest to wskazane.
