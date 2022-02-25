# Do czego służy funkcja max  
Funkcja max zwraca najmniejszy z podanych elementów - zarówno liczb, jak i liter i wyrazów.  
Składnia:  
min(x, y, z)  
Ważne - elementy mogą być podane jako pojedyncze elementy, ale również na krotce czy liście.

``` 
print(min(2, 4, 3, 1, 2, 5, 18, 4))             # 1

print(min("d", "e", "b", "r", "a"))             # a

print(min("a", "D", "e", "F"))                  # D

print(min("Damian", "Aga", "Kasia", "Mati"))    # Aga
```
Odnośnie liter - w pierwszej kolejności są litery wielkie, potem małe, dlatego w przykładzie nr 3 została zwrócona litera "e", a nie "F".

## Podawanie klucza w funkcji min  
Do funkcji min() oprócz samego zbioru elementów można podać również klucz, wg którego funkcja będzie zwracać wartość minimalną.  

1. Zwracanie najkrótszego stringa z listy  
Bez podania klucza zostałby zwrócony element "Aga", bo jest pierwszy w alfabecie.  
W przykładzie podajemy klucz, który jest funkcją lambda, która dla każdego elementu w names zwraca długość tego elementu, dlatego funkcja min() mając podane długości elementów, zwróci element najkrótszy.
```
names = ["Damian", "Aga", "Mati", "Bartek", "J",
         "Kasia", "Mati", "Marcelina", "Jagoda", "Ola"]
print(min(names, key=lambda n: len(n)))                     # J
```

2. Zwracanie tytułu piosenki, która była odtwarzana najmniej razy  
W poniższym przykładzie bez podania klucza wywaliłoby błąd "TypeError", ponieważ nie da się zwrócić min() porównując słowniki.  
Tutaj:  
- podajemy listę słowników "songs",  
- jako drugi argument podajemy klucz, który jest funkcją lambda, która dla każdego elementu w songs (tj. dla każdego słownika) zwróci value od "count", tj. liczbę. Tym samym funkcja min() dostaje podane cztery liczby: 10, 2, 30, 3 i spośród nich szuka najmniejszego elementu. Znajduje 2 i zwraca cały słownik, dla którego value od key "count" była 2,  
- dodatkowo, w drugim princie po zamknięciu funkcji min() dodajemy ["title"], żeby została zwrócona sama value od key "title" dla tego słownika, który został wyszukany przez funkcję min().

```
songs = [{"title": "Hey", "artist": "John", "count": 10},
         {"title": "Rock Time", "artist": "Robots", "count": 2},
         {"title": "Euro", "artist": "Mom", "count": 30},
         {"title": "Love", "artist": "D", "count": 3}
         ]

print(min(songs, key=lambda s: s["count"]))
# {"title": "Rock Time", "artist": "Robots", "count": 2}
print(min(songs, key=lambda s: s["count"])["title"])   # Rock Time
```
