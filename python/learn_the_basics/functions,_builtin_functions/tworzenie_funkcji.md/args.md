# Do czego służą *args  
Dzięki *args możemy stworzyć funkcję, która pozwoli na wprowadzenie dowolnej liczby argumentów. Z podanych argumentów robi krotkę.  
Jeśli są argumenty poza args, które zostały oznaczone jako parametry, nie będą zawarte w krotce ORAZ oznaczenie ich poza args nakłada przymus podania przynajmniej tylu argumentów, ile podaliśmy parametrów (nie licząc args).  
  
```
def my_func(*args):
    return args
    
print(my_func("Aga", "Damian", "Kasia", "Mati"))
# ("Aga", "Damian", "Kasia", "Mati")
```
```
def my_func(name, *args):
    return args
    
print(my_func("Aga", "Damian", "Kasia", "Mati"))
# ("Damian", "Kasia", "Mati")
```
  
W pierwszym przykładzie mogłam nie podawać ani jednego argumentu, ale też mogłam podać ile argumentów chcę, w drugim przykładzie musiałam podać przynajmniej jeden argument.  
  
Nazwa args nie ma znaczenia, może to być cokolwiek, znaczenie ma *.
