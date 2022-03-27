# Czym jest pickling?  
Pickling, czyli zamrażanie, marynowanie.  
Mogę "zamrozić" obiekt/dane w pliku jako kod binarny (stąd "wb" i "rb") i potem go odmrozić. Mam do niego dostęp dzięki pickle.load().  
  
```
import pickle

blue = Cat("Blue", "Scottish Fold", "String")
rusty = Cat("Rusty", "Persian", "Ball")

with open(pets.pickle", "wb") as file:
    pickle.dump((blue, rusty), file)
    
with open("pets.pickle", "rb") as file:
    zobmie_blue, zombie_rusty = pickle.load(file)
    print(zombie_blue)
    print(zombie_rusty.play())
```
   
Plik, który utworzyłam (za pomocą "with open", używając trybu write) musi mieć rozszerzenie .pickle. Wtedy zamienia kod, który napisałam, na kod binarny, i w tym pliku "pets.pickle" będzie utworzony obiekt, który zamroziłam dzięki pickle.dump, napisany w kodzie binarnym.  
Następnie obiekty (blue i rusty), które były napisane jako kod binarny, nazywam jak chcę (tu: "zombie_blue", "zombie_rusty") i je wyświetlam/stosuję metodę z klasy Cat.  
Do tego nie potrzebuję już teraz pierwszego "with open", mogę go skomentować, bo plik został już utworzony i w nim obiekty zostały już zapisane w kodzie binarnym. Teraz je tylko "odmrażam".  
  
Pickle używa się wtedy, kiedy chce się używać danego kodu potem w Pythonie. Jeśli chcę tych danych używać potem w innym języku, lepiej nie używać pickle.  
  
  
## JSON    
Używa się tego w celu zamiany kodu napisanego w Pythonie na język JSON (JavaScript Object Notation) lub odwrotnie - z JSON na Python.  
  
```
import json

j - json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
charles = Cat("Charles", "Tabby")
c = json.dumps(c.__dict__)

print(j)    # ["foo", {"bar": ["bazz", null, 1.0, 2]}]
print(c)    # {"name": "Charles", "breed": "Tabby"}
```

Kod napisany w pythonie zostanie zamieniony na kod w JSON:  
- j: podwójne cudzysłowy, nie będzie krotki, None zostanie zamienione na null,  
- c: słownik w JSON wygląda tak samo, więc wyświetla dokładnie tak, jak w Pythonie.  
  
  
### JSON pickling  
Możliwe jest picklowanie, które będzie działało w JSON.   
Należy zainstalować moduł jsonpickle (python -m pip install jsonpickle).  
Sprawdzać wszystko w dokumentacji, poniżej przykład spisany z filmiku z kursu.  
```
import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
c = Cat("Charles", "Tabby")
frozen = jsonpickle.encode(c)
print(frozen)         # {"py/object": "__main__.Cat", "breed": "Tabby", "name": "Charles"}
```
  
Mogę również zapisać to samo w nowym pliku:  

```
with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)
```
Utworzył się nowy plik i został w nim "zamrożony" obiekt c. Potem mogę go odmrozić i dostanę obiekt "zrekonstruowany z umarłych", rzeczywisty pythonowy obiekt klasy Cat:  

```
with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)     # <__main__.Cat object at xxx>
```
