# Łączenie funkcji map i filter  
Dzięki funkcji filter() można zrobić listę elementów, które będą drugim argumentem (iteratorem) dla funkcji map().  

```
my_list = [1, 2, 3, 4, 5, 15, 18, 21, 32, 46, 34, 55]
y = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_list))
print(list(y))       # [4, 16, 324, 1024, 2116, 1156]
```

W powyższym przykładzie:  
- najpierw zrobiłam "listę" (iterator, bo <filter object> nie jest listą, ale nie muszę go zamieniać na listę, żeby móc przez niego iterować) za pomocą funkcji filter:  
filter(lambda x: x % 2 == 0, my_list))  <-  każde x, którego wynik z warunku x % 2 == 0 jest True, dodałam na "listę" filter  
z tego działania uzyskałam "listę" samych wartości parzystych z my_list.  
- następnie tę "listę" podstawiłam jako argument do funkcji map(), która zrobiła funkcję lambda x: x ** 2 dla każdego elementu z tej "listy".  

### Przykład z tworzeniem listy imion użytkowników, którzy nie podali imienia zwierzęcia  

```
users = [{"name": "Aga", "last_name": "Jaskolska", "pet_name": "Oscar"},
         {"name": "Damian", "last_name": "Jaskolski", "pet_name": ""},
         {"name": "Kasia", "last_name": "Palyz", "pet_name": ""},
         {"name": "Mati", "last_name": "Palyz", "pet_name": "Kropka"}]
no_pet_name = map(lambda user: user["name"], filter(lambda u: not u["pet_name"], users))
print(list(no_pet_name))     # ["Damian", "Kasia"]
```
