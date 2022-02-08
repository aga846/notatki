# Co robi funkcja insert  
Funkcja insert() wstawia na listę podany element na podanej pozycji.  

```
friends = ["Kasia", "Dorota", "Asia", "Ania1"]
friends.insert(2, "Ania2")  
# wstawi "Ania2" na pozycję nr 2: ['Kasia', 'Dorota', 'Ania2', 'Asia', 'Ania1']

friends.insert(-1, "Marta")
# to działa nieintuicyjnie. Wstawia element PRZED elementem -1, czyli na przedostatniej pozycji:
['Kasia', 'Dorota', 'Ania2', 'Asia', 'Marta', 'Ania1']
```
