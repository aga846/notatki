# Co to jest slice method  
Slice method to metoda pozwalająca na zwrócenie kawałka listy lub stringa.  
[start:stopWYŁĄCZNIE:co_ile_kroków]  
## Listy

```
friends = ["Kasia", "Dorota", "Asia", "AniaB", "AniaZ", "Marta", "Dominika"]
print(friends[1:5])
# ['Dorota', 'Asia', 'AniaB', 'AniaZ'] <- bez 5!
```
```
friends = ["Kasia", "Dorota", "Asia", "AniaB", "AniaZ", "Marta", "Dominika"]
print(friends[1:5:2])
# ["Dorota", "AniaB"]
```
```
friends = ["Kasia", "Dorota", "Asia", "AniaB", "AniaZ", "Marta", "Dominika"]
print(friends[5:1:-1])
# ['Marta', 'AniaZ', 'AniaB', 'Asia'] <- bez 1!
```
```
friends = ["Kasia", "Dorota", "Asia", "AniaB", "AniaZ", "Marta", "Dominika"]
friends[1:3] = ["MatiP", "Michał", "Maciek"]
print(friends)
# ['Kasia', 'MatiP', 'Michał', 'Maciek', 'AniaB', 'AniaZ', 'Marta', 'Dominika
']
```
w powyższym przykładzie nastąpiła zamiana elementów na indeksach 1 i 2 (bez 3!) na podane elementy.

## Stringi
```
print("helloiamaga"[2:10:2])
# loaa
```
```
print("agaidamian"[::-1])
# naimadiaga
```
