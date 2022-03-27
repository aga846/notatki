# Do czego służą **  
Dzięki **, możemy podać słownik jako argument do funkcji, która jako parametr ma **kwargs. Dzięki temu podany słownik nie będzie jednym z elementów na krotce args, ale faktycznie słownikiem.  
  
```
def hey(*args, **kwargs):
    return kwargs


print(hey(**{"wife": "Aga", "husband": "Damian"})) 
# {'wife': 'Aga', 'husband': 'Damian'}
```
  
  
Przy podawaniu słownika możliwe jest podanie go również jako jeden argument i rozpakowanie z jedną * (jeśli parametrem jest *args): wtedy elementami na krotce args będą tylko keys.  
  
```
def hey(*args, **kwargs):
    return args


print(hey(*{"wife": "Aga", "husband": "Damian"}))     # ("wife", "husband")
print(hey({"wife": "Aga", "husband": "Damian"}))      # ({"wife": "Aga", "husband": "Damian"})
```
