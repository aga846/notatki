# Sprawdzanie, czy dana para key, value jest w słowniku  
key, value in dict.items(); zwraca True lub False.   
  
```
husband = {"name": "Damian", "last_name": "Jaskolski", "age": 26, "is_handsome": True}
print(("is_handsome", True) in husband.items())     # True
print(("wife", "Aga") in husband.items())           # False
``` 
  
# Sprawdzanie przy użyciu metody .get()   
To samo można osiągnąć (sprawdzić, czy dana para jest w słowniku) przy użyciu metody .get():   
slownik.get(key) == value; zwraca True lub False.  
  
```
husband = {"name": "Damian", "last_name": "Jaskolski", "age": 26, "is_handsome": True}
print(husband.get("last_name") == "Jaskolski")     # True
print(husband.get("name") == "Michal")             # False
print(husband.get("wife") == "Aga")                # False
```
