# Do czego służy *  
Dzięki *, przy podaniu jako argument listy lub krotki do funkcji, która jako parametr ma *args, elementem na krotce args będą elementy z tej listy lub krotki, a nie ta lista lub krotka.  

```
def hey(*args):
    return args
    
print(hey(*[1, 2, 3]))     # (1, 2, 3)
print(hey([1, 2, 3]))      # ([1, 2, 3])
```
