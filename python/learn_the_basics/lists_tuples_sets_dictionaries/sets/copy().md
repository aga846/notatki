# Co robi metoda copy   
Metoda copy robi kopię seta. Oba sety mają te same wartości, ale "set1 is set2" zwróci False.  
## TO CO INNEGO, NIŻ FUNKCJA COPY() Z MODUŁU COPY  
  
```
my_set = {1, 2, 3, 4, 5}
set2 = my_set.copy()
print(set2)           # {1, 2, 3, 4, 5}
print(set is set2)    # False
```
