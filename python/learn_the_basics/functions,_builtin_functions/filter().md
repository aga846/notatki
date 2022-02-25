# Co robi funkcja filter  
Funkcja filter() podstawia każdy element z podanego iteratora i (listy, krotki) pod podaną funkcję fn. Warunkiem koniecznym jest to, żeby wynikiem podawanej funkcji był boolean.   
Składnia:  
filter(fn, i)  
  
Przy filter() często używa się lambdy. 
  
Wynikiem funkcji filter() jest <filter object at ...>, dlatego można z jej wyniku zrobić listę. 

```
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, my_list))
print(evens)           # [2, 4, 6, 8]
```
