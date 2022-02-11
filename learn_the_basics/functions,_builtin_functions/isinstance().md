# Do czego służy funkcja isinstance  
Funkcja isinstance sprawdza, czy podana zmienna jest instancją podanej klasy.  
Składnia:  
isinstance(x, class)  

## Przykład z typem zmiennych 

```
x = "word"
print(isinstance(x, str))     # True
print(isinstance(x, int))     # False
```

## Przykład z obiektem klasy  
```
class Animal:
      pass
      
blue = Animal()

print(isinstance(blue, Animal))       # True
```
