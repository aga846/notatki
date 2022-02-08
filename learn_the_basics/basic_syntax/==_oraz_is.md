# Porównanie == oraz "is"
== porównuje wartości
is odnosi się do miejsca w pamięci.  

Na stringach oba powyższe działają tak samo, jednak na listach nie.  

## Stringi:
```
word = "hello"
word2 = "hello2"
print(word == word2)    # True
print(word is word2)    # True
```

## Listy:
```
from copy import copy

word = [1, 2, 3]
word2 = [1, 2, 3]
word3 = copy(word)
print(word == word2)   # True
print(word is word2)   # False
print(word is word3)   # False
```
