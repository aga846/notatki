# Jak dostać się do konkretnego atrybutu danego obiektu klasy?  
Mając klasę User z parametrami (self, first, last, age), żeby dostać się do konkretnego atrybutu danego obiektu, należy napisać:  
user1.atrybut

```
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("Damian", "Jaskolski", 26)
print(user1.age)         
```

## Zmiana atrybutu obiektu  
Możliwa jest zmiana atrybutu obiektu.  

```
class User:
    def __init__(self, first, last, age=20):
        self.first = first
        self.last = last
        self.age = age

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


user1 = User("Damian", "Jaskolski", 26)
print(user1.age)                # 26
user1.birthday()         
print(user1.age)                # 27
print(user1.birthday())         # Happy 28th, Damian
```

## Prywatne atrybuty  
W Pythonie nie ma czegoś takiego, jak "prywatne" i "publiczne" atrybuty. Jeśli tworzymy atrybut prywatny, tj. taki, który nie jest zamierzony do używania poza klasą, należy napisać "_" przed jego nazwą. Jest możliwy dostęp do niego poza klasą, ale chodzi o konwencję - jeśli czytam czyjś kod i widzę atrybut prywatny, to wiem, że mam go nie używać poza klasą, bo developer tego nie chciał.  

```
self._secret = "hi"
```

## Atrybuty z __  
Można dodać atrybut poprzedzając jego nazwę __. Wtedy nie można się do niego dostać tak, jak do zwykłego atrybutu, ale w poniższy sposób:  
```
class User:
    def __init__(self, first, last, age=20):
        self.first = first
        self.last = last
        self.age = age
        self.__msg = "I like you"
        
user1 = User("Damian", "Jaskolski", 26)
print(user1._User__msg)
```
Umieszczanie takich atrybutów ma na celu rozróżnienie danego atrybutu pomiędzy klasą matką, a klasą dziedziczącą.
