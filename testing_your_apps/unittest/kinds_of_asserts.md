## assertEqual(x,y)  
assertEqual sprawdza, czy funkcja od podanego argumentu/argumentów jest równa podanemu wyrażeniu:  
  
```
def eat(food, is_healty):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"
    

class MyFileTests(unittest.TestCase):
    def test_eat(self):
        self.assertEqual(eat("broccoli", is_healthy=True),
        "I'm eating broccoli, because my body is a temple")
        self.assertEqual(eat("pizza", is_healthy=False),
        "I'm eating pizza, because YOLO!")
```
  
W powyższym przykładzie funkcja eat zwraca jeden z dwóch stringów, zależnie od tego, czy wprowadzone jedzenie jest zdrowe czy nie.
  
W assertEqual jako argumenty podaję:   
- wywołanie funkcji testowanej (tutaj: eat()) od argumentów, które chcę przetestować - tutaj podaję przykładowe jedzenie i boolean, czy jest ono zdrowe,  
- spodziewany/zamierzony wynik tej funkcji od podanych argumentów.  
  
  
## assertNotEqual(x, y)  
assertNotEqual sprawdza, czy funkcja od podanego argumentu/argumentów nie jest równa podanemu wyrażeniu:  
  
```
class MyFileTests(unittest.TestCase):
    def test_eat(self):
        self.assertNotEqual(eat("broccoli", is_healthy=False),
        "I'm eating broccoli, because my body is a temple")
        self.assertNotEqual(eat("pizza", is_healthy=True),
        "I'm eating pizza, because YOLO!")
```
  
## assertTrue(x) i assertFalse(x)   
assertTrue sprawdza, czy wynik funkcji od podanego argumentu/argumentów jest True, a assertFalse sprawdza, czy wynik jest Falsey (nie False, bo chodzi również o None, 0, puste obiekty).  
  
```
def is_funny(person):
    if person is "tim": return False
    return True  
    
class MyFileTests(unittest.TestCase):
    def test_is_funny(self):
        self.assertTrue(is_funny("john"), "john should be funny")
    
    def test_is_funny(self):
        self.assertFalse(is_funny("tim"), "tim shouldn't be funny")
```
  
W powyższym przykładzie funkcja is_funny powinna zwracać False tylko dla argumentu "tim", dla każdego innego - True.  
      
W assertTrue i assertFalse jako argumenty podaję:  
- wywołanie funkcji testowanej (tutaj: is_funny()) od argumentów, które chcę przetestować (tutaj: "john" i "tim"),  
- opcjonalnie: wiadomość, która się wyświetli, jeśli wynik podanej funkcji od podanego argumentu nie będzie True (przy assertTrue) lub Falsey (przy assertFalse).  
  
To ważne, że metoda assertFalse sprawdza nie tylko False, ale też inne Falsey, dlatego, że gdyby w powyższym przykładzie funkcja is_funny() wyglądała tak:  

```
def is_funny(person):
    if person != "tim": return True
```
to jej wynikiem dla "tim" byłoby "None", a nie "False".  
Dlatego, jeśli chcemy sprawdzić, czy wynikiem funkcji jest konkretnie False, a nie Falsey, lepiej użyć metody assertEqual i jako drugi argument podać False.  

## assertIsNone(x) i assertIsNotNone(x)  
assertNone sprawdza, czy wynik funkcji od podanego argumentu/argumentów jest None, a assertIsNotNone sprawdza, czy wynik funkcji od podanego argumentu/argumentów nie jest None.  

```
def is_funny(person):
    if person != "tim": return True

class MyFileTests(unittest.TestCase):
    def test_is_funny(self):
        self.assertIsNone(is_funny("tim"), "tim should equal None")
    
    def test_is_funny(self):
        self.assertIsNotNone(is_funny("jonh"), "john should be funny")
```
  
## assertIn(x, y) i assertNotIn(x, y)  
Zamiast pisać assertEqual, mogę sprawdzić, czy x jest w podanej krotce.  
  
```
from random import choice

def laugh():
    return choice(("lol", "hahaha", "tehehe")))

class MyFileTests(unittest.TestCase):
    def test_laugh(self):
        self.assertIn(laugh(), ("lol", "hahaha", "tehehe"))
        
    def test_laugh(self):
        self.assertNotIn(laugh(), ("pfff", "grrrr", "wtf"))
```

## assertRaises(error)  
assertRaises sprawdza, czy błąd został wywołany w podanym przypadku.  
NALEŻY UŻYĆ INNEJ SKŁADNI:

```
def eat(food, is_healty):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"
    

class MyFileTests(unittest.TestCase):
    def test_eat(self):
    """is_healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")
```
Gdyby w funkcji eat() nie został podniesiony błąd ValueError, to test by nie przeszedł - "ValueError not raised".
