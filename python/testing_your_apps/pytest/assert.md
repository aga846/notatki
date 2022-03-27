# Czym jest assert  
Assert to rodzaj testu, który umieszcza się w funkcji, pod samym zdefiniowaniem jej. Assert musi być wyrażeniem boolean.  
Jeśli odpowiedź asserta jest False -> wtedy przy egzekwowaniu wyskakuje "AssertionError: mój opis tego błędu".  
Jeśli odpowiedź asserta jest True -> wykonuje funkcję.  
Assert nie jest funkcją, tylko "statement", tak jak return, raise, yield, dlatego nie potrzebujemy nawiasów.  
  
Składnia:  
def fn():  
    assert WARUNEK, WIADOMOŚĆ  
    reszta funkcji  
  
```
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y
    
add_positive_numbers(1, 1)    # 2
add_positive_numbers(1, -1)   # AssertionError: Both numbers must be positive!
```

```
def eat_jun(food):
    assert food in ["pizza", "ice cream", "candy"], "food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"
```
