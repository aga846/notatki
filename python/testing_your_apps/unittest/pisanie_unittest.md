# Jak pisze się unittesty?   
Najpierw muszę zaimportować funkcje, które chcę przetestować, z pliku, w którym się znajdują, oraz moduł unittest:  
  
```
import unittest
from "my_file.py" import function, function2
```
  
Żeby testować za pomocą unittestów, w nowym pliku do testowania tworzę klasę testującą, która dziedziczy z wbudowanej klasy TestCase (zawartej w module unittest, który muszę importować):  
  
```
import unittest
from "my_file.py" import function, function2

class MyFileTests(unittest.TestCase):
```
  
Jako kolejne funkcje w klasie dodaję kolejne testy. Mogę dodać w jednej funkcji różne testy do testowanej funkcji, ale lepiej jest testy rozdzielić na różne funkcje - wtedy będę widziała, ile testów przeszło.  
  
```
import unittest
from "my_file.py" import function, function2

class MyFileTests(unittest.TestCase):
    def test_eat(self):
        self.assertEqual(eat("broccoli", is_healthy=True),
        "I'm eating broccoli, because my body is a temple")
        self.assertEqual(eat("pizza", is_healthy=False),
        "I'm eating pizza, because YOLO!")
```  
  
W powyższym przykładzie funkcja eat zwracała jeden z dwóch stringów, zależnie od tego, czy wprowadzone jedzenie jest zdrowe czy nie:  
  
```
def eat(food, is_healty):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"
```
  
W pliku testowym najpierw zdefiniowałam funkcję "test_eat", która będzie testować funkcję eat().  
Potem stosuję metody, które mają za zadanie sprawdzić daną rzecz. W podanym przykładzie metodą jest assertEqual, w której jako argumenty podaję:   
- wywołanie funkcji testowanej (tutaj: eat()) od argumentów, które chcę przetestować - tutaj podaję przykładowe jedzenie i boolean, czy jest ono zdrowe,  
- spodziewany/zamierzony wynik tej funkcji od podanych argumentów.  
  
Opis innych metod -> unittest/kinds_of_asserts.md.  
  
  
## __name__, __main__  
  
Na końcu pliku testowego dodaję:  
```
if __name__ == "__main__":
    unittest.main()
```
^ chodzi o to, żeby uruchamiał sę dobry plik.
