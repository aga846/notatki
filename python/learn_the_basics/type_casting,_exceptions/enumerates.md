# Czym jest enumerate  
Enumerate jest listą, obiektem, iteratorem (nie wyświetlającym się), który z listy tworzy "jakby kopię" listy, w której każdy element skopiowanej listy jest unikatowy. Nawet jeśli w oryginalnej liście są powtórzenia, to w enumerate każdy element jest traktowany jako oddzielny, zależny od indeksu.  

```
l = [3, 4, 5, 4, 2, 7, 4]

for x in enumerate(l):
    print(x)
# 
(0, 3)
(1, 4)
(2, 5)
(3, 4)
(4, 2)
(5, 7)
(6, 4)
```

W enumerate można iterować również przez indeks i wartość, tj.

```
l = [3, 4, 5, 4, 2, 7, 4]

for x, y in enumerate(l):
    print(x, y)
    
#
1 4
2 5
3 4
4 2
5 7
6 4
```
Domyślnie x jest tutaj indeksem, a y wartością.
