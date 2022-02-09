# Co robi funkcja map  
Funkcja map() podstawia każdy element z podanego iteratora i (listy, krotki) pod podaną funkcję fn.  
Składnia:  
map(fn, i)  
  
Przy map() często używa się lambdy. 
  
Wynikiem funkcji map() jest <map object at ...>, dlatego można z jej wyniku zrobić listę. 

```
my_list = ["Damian", "Aga", "Blablabla"]
x = map(len, my_list)
print(list(x))              # [6, 3, 9]
```


Przykład z użyciem lambdy:
```
my_list = [2, 3, 5, 18, 20]
x = map(lambda x: x*2, my_list)
print(list(x))              # [4, 6, 10, 36, 40]
```
