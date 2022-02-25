# Do czego służy funkcja max  
Funkcja max zwraca największy z podanych elementów - zarówno liczb, jak i liter i wyrazów.  
Składnia:  
max(x, y, z)
Ważne - elementy mogą być podane jako pojedyncze elementy, ale również na krotce czy liście.

``` 
print(max(2, 4, 3, 2, 5, 18, 4))                  # 18

print(max("a", "d", "e", "b", "r", "a"))          # r

print(max("a", "D", "e", "F"))                    # e

print(max("Damian", "Aga", "Kasia", "Mati"))      # Mati
```
Odnośnie liter - w pierwszej kolejności są litery wielkie, potem małe, dlatego w przykładzie nr 3 została zwrócona litera "e", a nie "F".

## Podawanie klucza w funkcji max  
Do funkcji max() oprócz samego zbioru elementów można podać również klucz, wg którego funkcja będzie zwracać wartość maksymalną.  

1. Zwracanie najdłuższego stringa z listy  
Bez podania klucza zostałby zwrócony element "Ola", bo jest ostatni w alfabecie.  
W przykładzie podajemy klucz, który jest funkcją lambda, która dla każdego elementu w names zwraca długość tego elementu, dlatego funkcja max() mając podane długości elementów, zwróci element najdłuższy.
```
names = ["Damian", "Aga", "Mati", "Bartek", "J",
         "Kasia", "Mati", "Marcelina", "Jagoda", "Ola"]
print(max(names, key=lambda n: len(n)))                     # Marcelina
```

2. Zwracanie tytułu piosenki, która była odtwarzana najwięcej razy  
W poniższym przykładzie bez podania klucza wywaliłoby błąd "TypeError", ponieważ nie da się zwrócić max() porównując słowniki.  
Tutaj:  
- podajemy listę słowników "songs",  
- jako drugi argument podajemy klucz, który jest funkcją lambda, która dla każdego elementu w songs (tj. dla każdego słownika) zwróci value od "count", tj. liczbę. Tym samym funkcja max() dostaje podane cztery liczby: 10, 2, 30, 3 i spośród nich szuka największego elementu. Znajduje 30 i zwraca cały słownik, dla którego value od key "count" była 30,  
- dodatkowo, w drugim princie po zamknięciu funkcji max() dodajemy ["title"], żeby została zwrócona sama value od key "title" dla tego słownika, który został wyszukany przez funkcję max().

```
songs = [{"title": "Hey", "artist": "John", "count": 10},
         {"title": "Rock Time", "artist": "Robots", "count": 2},
         {"title": "Euro", "artist": "Mom", "count": 30},
         {"title": "Love", "artist": "D", "count": 3}
         ]

print(max(songs, key=lambda s: s["count"]))
# {"title": "Euro", "artist": "Mom", "count": 30}
print(max(songs, key=lambda s: s["count"])["title"])   # Euro
```
