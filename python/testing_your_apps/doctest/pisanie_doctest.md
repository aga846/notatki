# Jak pisze się doctesty?  
Doctesty pisze się w funkcji, zaraz po jej zdefiniowaniu, poprzedzając i kończąc je trzema podwójnymi cudzysłowami ("""). Poszczególne doctesty pisze się poprzedzając je ">>>". Składnia:  
```
"""
>>> doctest
spodziewany wynik doctestu
"""
```

Przykład:

```
def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    return a * b
```

Powyżej nie printuje niczego, po prostu odpalam program w takiej wersji, jak napisana w przykładzie, i python sprawdza, czy wszystkie napisane doctesty przechodzą. W podanym przykładzie nie przejdą, bo w returnie jest a * b, a nie a + b.  
Jest specjalna komenda do wywołania programu w taki sposób, żeby przeprowadził napisane testy. Powiedzmy, że powyższy przykład jest zapisany w pliku o nazwie "my_test.py":

```
python -m doctest -v my_test.py
```

## Problem z doctestami  
W opisywaniu oczekiwanego rezultatu należy być BARDZO DOKŁADNYM, np.:  
- jeśli spodziewamy się, że wywali błąd (np. w przykładzie z funkcją add() podałabym False i True jako argumenty -> a nie da się dodać booleanów), to trzeba napisać dokładnie to, co python by napisał przy wywaleniu błędu (tj. np. "Traceback (most recent call last): ... TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'),  
- jeśli napiszemy, że spodziewamy się stringa "hi", a wynikiem działania pythona będzie 'hi', to test nie przejdzie,
- jeśli napiszemy przypadkiem spację po spodziewanym wyniku, której w wyniku działania pythona nie będzie, to test nie przejdzie,
- jeśli napiszemy inną kolejność par w słowniku niż python przy egzekwowaniu kodu, to test nie przejdzie.
