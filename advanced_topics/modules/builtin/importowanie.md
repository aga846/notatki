# Importowanie modułów  

Moduły można importować na różne sposoby:  

## Importowanie całego modułu  
1. Importuje cały moduł. Przy używaniu funkcji z tego modułu, konieczne jest pisanie "random.randint()":
```
import random
```

2. Importuje cały moduł, który w danym programie będzie rozumiany jako "r". Przy używaniu funkcji z tego modułu, należy pisać "r.randint()":
```
import random as r
```

3. Z modułu random importuje wszystko, z tym, że przy wywoływaniu funkcji nie trzeba pisać nazwy modułu, wystarczy sama funkcja:
```
from random import *
```

4. Z modułu random importuje konkretną funkcję lub konkretne funkcje, pisane po przecinku. Przy ich używaniu nie trzeba pisać nazwy modułu:
```
from random import randint
```
