# Co robi funkcja any  
Funkcja any() sprawdza, czy jakikolwiek element w podanym iteratorze jest True.  
Funkcja any() zwraca True lub False.  
  
```
my_list = [0, "Damian", "Kasia", False, None, "Aga"]
print(any(my_list))         # True

my_list = [2, "Damian", "Kasia", True, ["hey"], "Aga"]
print(any(my_list))         # True

my_list = [[], None, 0, False, {}]
  print(any(my_list))
  ```
