# Co robi funkcja split()  
Funkcja split zamienia string na listę, tj. zamienia zawarte w stringu elementy na listę.  
Elementami listy będą elementy ze stringa (litery lub wyrazy), które były rozdzielone podanym znakiem/wartością.  
  
```
word1 = "Cześć jestem Aga i bardzo Cię kocham"
word2 = "Cześć, jestem Aga, bardzo Cię kocham"
word3 = "Cześć, jestem Aga"

print(word1.split())
# tutaj domyślnym argumentem funkcji split() jest " ", więc to będzie to samo, co poniższy przykład:
print(word1.split(" "))
# ['Cześć', 'jestem', 'Aga', 'i', 'bardzo', 'Cię', 'kocham']
print(word2.split(", "))
# ['Cześć", " jestem Aga', ' bardzo Cię kocham']
print(word3.split("e"))
# ["Cz", "ść, j", "st", "m Aga"]

```
