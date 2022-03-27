# Co robi funkcja index 
Funkcja index() pokazuje, na którym indeksie jest pierwszy znaleziony element o podanej nazwie/wartości.  
```
friends = ["Kasia", "Ania", "Asia", "Kasia", "Basia", "Ania"]
print(friends.index("Ania"))    # 1
```
  
## Można też podać argumenty, które funkcjonują w poniższy sposób:   
Na którym indeksie, zaczynając od podanego indeksu, znajduje się pierwszy znaleziony element o podanej nazwie/wartości.  
```
friends = ["Kasia", "Ania", "Asia", "Ania", "Kasia", "Basia", "Ania"]
print(friends.index("Ania", 3))    # 3
print(friends.index("Ania", 2))    # 3
```
Na którym indeksie, między podanymi indeksami, znajduje się pierwszy znaleziony element o podanej nazwie/wartości.   
WAŻNE: druga podana wartość traktowana jest wyłącznie (patrz: 2 ostatnie przykłady poniżej).  
```
friends = ["Kasia", "Ania", "Asia", "Ania", "Kasia", "Basia", "Ania"]
print(friends.index("Ania", 1, 5))    # 1
print(friends.index("Ania", 2, 4))    # 3
print(friends.index("Ania", 2, 3))    # "Ania" is not in list
print(friends.index("Ania", 4, 6))    # "Ania" is not in list
```
dlatego jeśli chcę przeszukać listę włącznie z ostatnim elementem, muszę napisać index o numerze o 1 większym niż pozycja ostatniego elementu, tj. w ostatnim przykładzie: 4, 7.
