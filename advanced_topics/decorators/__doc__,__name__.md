Jeśli nie zastosujemy @wraps(fn), przy wywoływaniu __doc__ i __name__ (patrz -> learn_the basics/functions,_builtin_functions/tworzenie_funkcji/__doc__ oraz __name__) wyświetlą się informacje na temat funkcji owijającej. Żeby temu zapobiec, i wyświetlać informacje funkcji głównej (w poniższym przykładzie funkcji greet()), należy zaimportować funkcję wraps z modułu functools i dodać @wraps tuż przed zdefiniowaniem funkcji wrapper:  

```
from functools import wraps

def shout(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper
    
@shout
def greet(name):
    return f"Hi, I'm {name}"
```
