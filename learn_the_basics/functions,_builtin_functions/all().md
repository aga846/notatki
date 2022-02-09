# Co robi funkcja all  
Funkcja all() sprawdza, czy wszystkie wyrażenia/elementy w podanym iteratorze są True.  
Wynikiem funkcji all() jest True lub False.

```
my_list = [0, "Damian", "Kasia", False, None, "Aga"]
print(all(my_list))         # False

my_list = [2, "Damian", "Kasia", True, ["hey"], "Aga"]
print(all(my_list))         # True
```
