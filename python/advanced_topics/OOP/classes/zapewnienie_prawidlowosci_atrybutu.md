# Jak można zapewnić, że dany atrybut nie będzie nieprawidłowy?  
  
```
class Human:
    def __init__(self, first, age):
        self.first = first
        if age >= 0:
            self._age = age
        else:
            self._age = 0
```
ewentualnie można użyć funkcji max() -> self.age = max(age, 0).  
  
## Problem tego rozwiązania  
Problemem tego rozwiązania jest to, że mimo że przy wprowadzaniu atrybutu rzeczywiście będzie zapewnione, że ten atrybut będzie miał określoną wartość (tutaj: nie będzie ujemny), to już po stworzeniu obiektu można go łatwo zmienić:   
  
```
self.age = -50
```

## Rozwiązanie problemu  
patrz -> @property, @setter
