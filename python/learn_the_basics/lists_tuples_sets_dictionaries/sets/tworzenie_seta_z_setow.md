# Jak można utworzyć seta z dwóch innych setów  
Istnieje metoda | oraz metoda &  

## Metoda |  
Tworzy set z dwóch setów, dodaje wartości z obu setów i tworzy nowy set z tych wartości (unikalnych, bez powtórzeń).  
```
set1 = {1, 2, 3}
set2 = {3, 4, 5}
combo = set1 | set2
print(combo)    # {1, 2, 3, 4, 5}
```

## Metoda &  
Tworzy set z elementów, które są zarówno na pierwszym, jak i drugim secie.  
```
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 7}
combo = set1 & set2
print(combo)    # {2, 4}
```
