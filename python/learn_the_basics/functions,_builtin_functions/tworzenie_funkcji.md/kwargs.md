# Do czego służą kwargs  
Dzięki **kwargs możemy stworzyć funkcję, która pozwoli na wprowadzenie dowolnej liczby argumentów z kluczem (KeyWord Arguments). Z kluczów oraz z podanych argumentów robi słownik.  
Jeśli są argumenty poza kwargs, które zostały oznaczone jako parametry, nie będą zawarte w słowniku ORAZ oznaczenie ich poza kwargs nakłada przymus podania przynajmniej tylu argumentów, ile podaliśmy parametrów (nie licząc kwargs).  
  
```
def my_func(**kwargs):
    return kwargs
    
print(my_func(name1="Aga", name2="Damian", name3="Kasia", name4="Mati"))
# {'name1': 'Aga', 'name2': 'Damian', 'name3': 'Kasia', 'name4': 'Mati'}
```
```
def my_func(name, **kwargs):
    return kwargs
    
print(my_func(name="Aga", name2="Damian", name3="Kasia", name4="Mati"))
# {'name2': 'Damian', 'name3': 'Kasia', 'name4': 'Mati'}
```
  
W pierwszym przykładzie mogłam nie podawać ani jednego argumentu, ale też mogłam podać ile argumentów chcę, w drugim przykładzie musiałam podać przynajmniej jeden argument, przy czym mogłam nie podawać jego klucza, tylko podać po prostu "Aga".  
  
Jeśli byłoby więcej keyword arguments, kolejność podawania argumentów do funkcji miałaby znaczenie (chyba że używałabym przy tym keywords -> patrz "kolejnosc_argumentow").  
  
Nazwa kwargs nie ma znaczenia, może to być cokolwiek, znaczenie mają **.
