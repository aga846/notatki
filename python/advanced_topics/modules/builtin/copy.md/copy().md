# Co robi funkcja copy   
Funkcja copy() kopiuje podany obiekt.  
Elementy będą miały te same wartości, jednak "x is y" zwróci False (chyba x to string) <- patrz basic_syntax -> "==_oraz_is"

```
from copy import copy
x = [1, 2, 3]
y = copy(x)
print(y)   # [1, 2, 3]
```
