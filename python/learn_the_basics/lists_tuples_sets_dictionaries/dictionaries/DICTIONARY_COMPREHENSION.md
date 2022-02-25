# Do czego służy dictionary comprehension  
Dictionary comprehension służy do tworzenia nowego słownika z podanego słownika lub samych tylko wartości, pozwalając na dowolną zmanę każdego key i value (i te zmienione key i values dodaje do nowego słownika).

## Przykłady  
### 1. Tworzenie słownika za słownika  
Tworzy słownik składający się z takich samych keys, jak podany słownik, z values podniesionymi do kwadratu.

```
numbers = {"first": 1, "second": 2, "third": 3}
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)
# {'first': 1, 'second': 4, 'third': 9}
```

### 2. Tworzenie słownika z listy  
Tworzy słownik składający się z podanych numerów jako keys i ich drugiej potęgi jako values.  

```
dict_from_list = {num: num ** 2 for num in [1, 2, 3, 4]}
print(dict_from_list)
# {1: 1, 2: 4, 3: 9, 4: 16}
```

### 3. Tworzenie słownika z dwóch stringów  
Tworzy słownik składający się z liter pierwszego stringa jako keys i z liter drugiego stringa jako values.  

```
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)
# {'A': '1', 'B': '2', 'C': '3'}
```
