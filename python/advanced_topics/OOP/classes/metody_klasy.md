# Co to jest metoda klasy?  
Metoda klasy to metoda, która odnosi się do całej klasy, a nie do samych obiektów tej klasy.  
Przed zdefiniowaniem metody klasy należy zamieścić dekorator "@classmethod".  
Tak jak metoda obiektu ma "self" jako pierwszy parametr, tak metoda klasy ma "cls".  
  
```
class User:
    @classmethod
    def display_active_users(cls):
```
  
W celu dostania się do metody klasy należy napisać jedno z poniższych:  
  
```
User.display_active_users()
user1.display_active_users()
```
  
W celu dostania się do atrybutu klasy, można napisać: cls.active_users (a nie Klasa.active_users), ale jedynie w obrębie klasy, nie poza nią.  
  
## Metoda klasy tworząca nowy obiekt z podanego stringa   
  
```
class User:
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(", ")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


d = User.from_string("Damian, Jaskolski, 26")
print(d.first)
```
Parametrem w funkcji klasy from_string jest:  
- cls, bo to metoda klasy,  
- podany string.  
W tej funkcji do wartości "first", "last" i "age" przypisywane są elementy z listy stworzonej z podanego stringa (lista została stworzona dzięki split()).  
(Nie piszę w tej funkcji "self.first, self.last, self.age = ...", dlatego że first, last i age to będą argumenty, z których potem utworzę obiekt. To tak, jakbym je po prostu podstawiła przy tworzeniu obiektu: User("Aga", "Jaskolska", 26).)  
Następnie zostaje utworzony obiekt z argumentami first, last, age (do których przypisane są teraz wartości z podanego stringa). To dokładnie to samo, co User(first, last, age), dlatego automatycznie jest wywoływana funkcja __init__().  
  
## Kiedy tworzymy metody klasy?   
Metody klasy tworzymy tylko wtedy, kiedy nie potrzebujemy mieć dostępu do konkretnego obiektu przy użyciu jej. Innymi słowy - wtedy, kiedy robimy coś na poziomie całej klasy.
