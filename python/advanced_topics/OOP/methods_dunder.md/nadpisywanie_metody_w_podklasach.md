# Definiowanie metody o takiej samej nazwie w różnych klasach lub w podklasach (nadpisywanie)  
W podklasach mogę definiować metody, które mają tą samą nazwę, co inne metody w klasie-rodzicu lub innych podklasach, ale robią coś innego.  

```
class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")
        
class Dog(Animal):
    def speak(self):
        return "woof"
        
class Cat(Animal):
    def speak(self):
        return "meow"
```
