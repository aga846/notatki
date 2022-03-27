# Metody stosowane do list   
  
## pop  
Pop() działa tak samo, jak w Pythonie - usuwa ostatni element i zwraca ten element.  
  
## push  
Push() działa jak append().  
Zwraca długość listy po dodaniu danego elementu.  
  
## indexOf  
Zwraca indeks danego elementu na podanej liście:  
```
lista.indexOf(element)
```  
  
## splice  
Usuwa z listy element na podanym indeksie:  
```
lista.splice(index, 1)
```
Drugi argument to liczba elementów, które chcemy usunąć z listy, zaczynając od wskazanego indeksu.  
  
## Zagnieżdżanie list w listach  
Jeśli zagnieżdżę listy w liście:  
```
matrix = [[1,2,3], [4,5,6],[7,8,9]]
```
to jeśli wpiszę "matrix", wyświetli się:  
```
[Array[3], Array[3], Array[3]]
```
- w nawiasach długość danego elementu (listy).  
