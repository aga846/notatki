# Do czego służy list comprehension  
List comprehension służy do tworzenia nowej listy z podanej listy/range, pozwalając na dowolną zmianę każdej wartości (i tą zmienioną wartość dodaje do nowej listy).

## Przykłady  
1. Tworzy listę składającą się z podwojonej wartości (x**2) każdego x (for x) z listy nums (in nums).
```
nums = [1, 2, 3, 4]
squared_nums = [x**2 for x in nums]
print(squared_nums)
# [1, 4, 9, 16]
```

2. Tworzy listę składającą się z podwojonej wartości (x**2) każdego x (for x) z range od 0 do 4 (in range(5)).
```
squared = [x**2 for x in range(5)]
print(squared)
# [0, 1, 4, 9, 16]
```

3. Tworzy listę składającą się ze skonwertowanego na wartość boolean (bool(val)) każdego val (for val) z listy some_list (in some_list).
```
some_list = [24, 0, False, "Aga", None, 5.4]
bool_list = [bool(val) for val in some_list]
print(bool_list)
# [True, False, False, True, False, True]
```

4. Tworzy listę składającą się ze skonwertowanej na string (str(num)) każdego num (for num) z listy numbers (in numers).
```
numbers = [1, 2, 3]
str_numbers = [str(num) for num in numbers]
print(str_numbers)
# ['1', '2', '3']
```

5. Tworzy listę składającą się ze:
- skonwertowanej na string (str(num)) każdego num (for num)
- oraz dodanego do każdego skonwertowanego num słowa "HELLO" (+ "HELLO")
z listy numbers (in numbers).
```
numbers = [1, 2, 3]
str_numbers = [str(num) + "HELLO" for num in numbers]
print(str_numbers)
# ['1HELLO', '2HELLO', '3HELLO']
```

## Dodawanie warunków w list comprehension  
Wartość dla Każdej_Wartości w Liście !!!JEŚLI!!! WARUNEK
Przykład: tworzy listę składającą się z wartości dla każdej wartości w numbers, JEŚLI ten number jest podzielny przez 2.
```
numbers = [1, 3, 4, 6, 13, 15, 3, 4]
evens = [x for x in numbers if x % 2 == 0]
print(evens)
# [4, 6, 4]
```

### Warunki z else  
Wartość(+zmiana) !!!JEŚLI!!! WARUNEK ELSE WARUNEK2 dla Każdej_Wartości w Liście.  
Przykład: tworzy listę składającą się z:  
- x*2 jeśli x na pierwotnej_liście jest podzielny przez 2,
- x/2 jeśli x na pierwotnej_liście nie jest podzielny przez 2
dla każdej wartości z pierwotnej_listy.
```
pierwotna_lista = [2, 3, 6, 5, 15, 4, 12, 18, 21]
druga_lista = [x*2 if x % 2 == 0 else x/2 for x in pierwotna_lista]
print(druga_lista)
# [4, 1.5, 12, 2.5, 7.5, 8, 24, 36, 10.5]
```

# List comprehension zagnieżdżone w list comprehension  
Można tworzyć listę (przy użyciu list comprehension) z list powstałej przy użyciu list comprehension.  

```
my_list = [[num for num in range(1, 4)] for val in range(1,4)]
print(my_list)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```
W powyższym przykładzie:
zaczynamy czytanie od najbardziej zewnętrznej listy, tj.  
- "for val in range(1, 4)" <- dla każdej wartości w range 1, 2, 3 zrobiłam:  
wewnętrzna lista:  
- Wartość dla Każdej_Wartości w Range(1, 4) <- zrobiłam listę z każdej wartości w range 1, 2, 3.  
  
Inaczej:
for val in range(1, 4) zrobiłam [num for num in range(1,4)]:
for 1 zrobiłam 1, 2, 3
for 2 zrobiłam 1, 2, 3
for 3 zrobiłam 1, 2, 3
