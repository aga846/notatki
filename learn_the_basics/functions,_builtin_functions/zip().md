# Do czego służy funkcja zip  
Funkcja zip() łączy:  
- pierwszy element z list1 z pierwszym elementem z list2,  
- drugi element z list1 z drugim elementem z list2,  
itd.  
Może być podane więcej niż tylko 2 listy.
Pary (ciągi) elementów są zwracane w krotkach, jednak jest to <zip object at ...>.  
Jeśli z wyniku funkcji zip() chcemy zzrobić listę lub słownik, należy użyć funkcji list() lub dict(), przy czym słownik można zrobić tylko wtedy, jeśli spinamy ze sobą dwie listy, nie więcej.  
Podane listy muszą być takiej samej długości. Jeśli nie są - zip() spina razem tylko tyle elementów, ile jest na krótszej liście.  
  
```
list1 = [3, 4, 2]
list2 = [15, 18, 2]
list3 = ["A", "B", "C"]

print(list(zip(list1, list2, list3)))
# [(3, 15, 'A'), (4, 18, 'B'), (2, 2, 'C')]

print(list(zip(list1, list2)))    {3: 15, 4: 18, 2: 2}
```

## Rozpakowanie listy do funkcji zip  
Jeśli podana lista jest listą krotek, można użyć gwiazdki (*) w celu rozpakowania tej listy. Wtedy zip() połączy ze sobą pierwsze elementy krotek, drugie elementy krotek, itd.

```
my_list = [(0, 1), (4, 8), (12, 14)]
print(list(zip(*my_list)))      # [(0, 4, 12), (1, 8, 14)]
```
