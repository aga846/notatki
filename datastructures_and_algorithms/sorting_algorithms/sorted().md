# Co robi funkcja sorted()  
Funkcja sorted() zwraca wartości w podanym zbiorze (liście, krotce, słowniku) posortowane alfabetycznie lub od najmniejszego do największego.  
Kolejność elementów w danym zbiorze pozostaje niezmienna (inaczej niż przy .sort()).  

## Przykłady   
### sorted() ze słownikiem:
```
damian = {"name": "Damian", "age": 26}
print(sorted(damian.items()))   # [('age', 26), ('name', 'Damian')]
```
ale jeśli nie podam items():  
```
damian = {"name": "Damian", "name": "Aga", "name": "Kasia",
          "age": "26", "last_name": "Jaskolski", "pet": "no"}
print(sorted(damian))   # ['age', 'last_name', 'name', 'pet']
```
### sorted() z listą:
```
aga = ["Aga", "Jask", "Czesc"]
print(sorted(aga))   # ['Aga', 'Czesc', 'Jask']

numbers = [5, 2, 6, 7, 3]
print(sorted(numbers))   # [2, 3, 5, 6, 7]
```


## Ważne!  
Najpierw idą wielkie litery, tj. w powyższym przykładzie z listą - gdyby "czesc" było napisane z małej litery, lista pozostałaby niezmieniona.  

# Sortowanie z podaniem klucza  
Przy sortowaniu można podać, wg jakiego klucza elementy mają być posortowane:  
```
sorted(damian, key=)  
```
Kluczem f może być inna funkcja, np. len():

```
users = [
    {"username": "Damian", "tweets": ["Hello"]},
    {"username": "Aga", "age": 26, "pet": "no"},
    {"username": "Kasia"}
]
sorted(users, key=len)   # [{'username': 'Kasia'}, {'username': 'Damian', 'tweets': ['Hello']},
{'username': 'Aga', 'age': 26, 'pet': 'no'}]
```
Kluczem może być również funkcja lambda:  
```
sorted(users, key=lambda user: user["username"])   # [{'username': 'Aga', 'age': 26, 'pet': 'no'}, {'username': 'Damian', 'tweets': ['Hello']}, {'username': 'Kasia'}]
```
w powyższym przykładzie kluczem jest funkcja lambda zastosowana dla każdego elementu w słowniku users. Oznacza to, że słownik zostanie posortowany wg "username", tj. elementy będą sortowane alfabetycznie wg wartości podanych w kluczu "username".  
  
  
Kluczem może być także długość elementów:  
```
sorted(users, key=lambda user: len(user["username"]))   # [{'username': 'Aga', 'age': 26, 'pet': 'no'}, {'username': 'Kasia'},

{'username': 'Damian', 'tweets': ['Hello']}]
```  
  
albo wielkość liczby:  
```
songs = [
    {"title": "happy", "playcount": 1},
    {"title": "baby", "playcount": 33},
    {"title": "hello", "playcount": 23}
]

sorted(songs, key=lambda song: song["playcount"])
# [{'title': 'happy', 'playcount': 1}, {'title': 'hello', 'playcount': 23}, {'title': 'baby', 'playcount': 33}]
