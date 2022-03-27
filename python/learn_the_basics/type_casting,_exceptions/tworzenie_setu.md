# Tworzenie setu  
Set można stworzyć albo za pomocą funkcji set() albo za pomocą {}.  
### W secie nie ma powtórzonych wartości. Jeśli jako argument podajemy listę z powtórzonymi wartościami, tworząc z niej set usuniemy powtarzające się elementy.  
### Wartości w secie są pomieszane, nie mają indeksów.  
  
## Przykład z set()   
set() przyjmuje tylko jeden argument - może to być lista, set. Nie mogą to być po prostu wartości.  
```
s = set([1, 2, 3])
s2 = set({4, 5, 6})
print(s)     # {1, 2, 3}
print(s2)    # {4, 5, 6}
```
  
## Przykład z {}   
```
s = {1, 2, 3}
```
  
## Zmiana listy z powtórzającymi się elementami w listę z unikalnymi elementami za pomocą seta   

```
my_list = [1, 4, 4, 3, 2, 15, 15, 4, 6]
my_unique_list = list(set(my_list))
print(my_unique_list)  # [1, 2, 3, 4, 6, 15]
```
Wartości są w innej kolejności niż w pierwotnej liście, dlatego że na secie nie miały indeksów, zostały przemieszane.
