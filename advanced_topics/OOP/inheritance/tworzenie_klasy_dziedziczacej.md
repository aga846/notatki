# Jak tworzy się klasę dziedziczącą?  
Klasę dziedziczącą tworzy się poprzez zamieszczenie w nawiasie, jako argumentu klasy-dziecka, nazwy klasy-matki, z której dana klasa-dziecko będzie dziedziczyć.  

```
class Animal:
    def make_sound(self, sound):
        print(f"This animal says {sound}")
        
class Cat(Animal):
    pass
    
blue = Cat()
blue.make_sound("MEOW")      # This animal says MEOW
```

## Klasa może dziedziczyć również z wbudowanej klasy, np. dict  

```
class grumpy_dict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
        
data = grumpy_dict({"first": "Tom", "animal": "cat"})
print(data)
#
NONE OF YOUR BUSINESS
{"first": "Tom", "animal": "cat"}
```

można zmieniać istniejące w tej klasie metody, tutaj np. __missing__, __setitem__, __contains__...
