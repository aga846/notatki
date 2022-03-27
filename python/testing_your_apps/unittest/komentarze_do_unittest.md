# Jak dodawać komentarze do unittestów?  
Po def test_eat(self) należy dodać:  
  
```
def test_eat(self):
    """testing a thing"""
```  
  
W komentarzach pisze się, co testowana funkcja powinna robić (np. "eat shoulg have a postive message for healthy eating").  
  
  
## Jak dostać się do komentarzy?  
Przy otwieraniu pliku z testami należy napisać:  
  
```
python test_file.py -v
```
  
-v od "verbose".
