# Czym jest __repr__  
__repr__() to specjalny rodzaj funkcji. Funkcja ta jest wywoływana za każdym razem, gdy chcemy sprintować obiekt klasy. W tej funkcji ustala się, jaka będzie reprezentacja danego obiektu.  
Innymi słowy, dzięki __repr__() obiekt "zamienia się" w stringa. Za każdym razem, kiedy będę odwoływać się do tego obiektu, będzie on stringiem, a nie <__main__.User object at ...>.  
  
```
class User:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first} is {self.age} years old."


d = User("Damian", "Jaskolski", 26)
print(d)        Damian is 26 years old.
```
