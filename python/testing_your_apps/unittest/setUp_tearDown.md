# Do czego służy setUp?  
SetUp odpala się zawsze przed każdym testem, należy go umieścić w pierwszej funkcji w klasie testowej.  
Dzięki setUp robię jedną rzecz dla wszystkich testów opisanych jako funkcje w danej klasie, np. jeśli w setUp tworzę obiekt klasy, ten obiekt na nowo będzie stworzony w taki sposób, w jaki został stworzony w setUpie. Nawet jeśli w jednym teście dany atrybut, dany obiektowi w setUpe się zmieni, to w kolejnym teście ten atrybut nie będzie zmieniony, tylko będzie taki, jakiego utworzyłam go w setUpie.  
  
# Do czego służy tearDown?  
TearDown jest odwrotnością setUpa. Odpala się po każdym teście, należy go umieścić w ostatniej funkcji w klasie testowej.  
  
```
def setUp(self):
    self.mega_man = Robot("Mega Man", battery=50)

def tearDown(self):
    pass
```
potem przy odwoływaniu się do obiektu klasy Robot, czyli obiektu "self.mega_man", piszę nie "mega_man", tylko "self.mega_man".
