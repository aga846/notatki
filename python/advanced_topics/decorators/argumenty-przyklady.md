Dzięki dekoratorom można wiele zrobić z argumentami funkcji "owijanej", np.  
- zapewnić, że nie zostaną wprowadzone określone typy zmiennych jako argumenty do funkcji owijanej,  
- zapewnić, że konkretny argument funkcji owijanej będzie jakimś wybranym przez nas (np. że pierwszym argumentem w funkcji owijanej zawsze będzie "pomidor"),  
- zmienić typ argumentu funkcji owijanej (np. zmienić string na integer).   
  
## Zapewnienie, że nie będzie określonych typów zmiennych jako argumenty   
Tutaj: nie będzie żadnych keyword arguments w funkcji owijanej.    
  
```
from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def f_owijana(*args, **kwargs):
    return args


print(f_owijana("Aga", "Damian", "Wiktoria", "Radek", last_name="Jaskolscy"))
# ValueError: No kwargs allowed

print(f_owijana("Aga", "Damian", "Wiktoria", "Radek"))
# ('Aga', 'Damian', 'Wiktoria', 'Radek')
```

## Zapewnienie, że któryś argument będzie jakiś  
Tutaj: pierwszy argument musi być argumentem (słowem) podanym przez nas jako argument w funkcji owijającej (tu: ensure_first_arg_is).  
  
```
from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg must be {val}!"
            return fn(*args, **kwargs)
        return wrapper
    return inner
    
@ensure_first_arg_is("pomidor")
def fav_foods(*foods):
    return foods
    
print(fav_foods("pomidor", "jablko"))    # ("pomidor", "jablko")
print(fav_foods("bataty", "pierogi"))    # First arg must be pomidor!
```

Funkcja ensure_first_arg_is akceptuje 1 argument, który będziemy sprawdzać (on wyznacza, jak ma brzmieć pierwszy argument funkcji fav_foods). Dopiero funkcja inner jest tą funkcją, która przyjmuje jako argument funkcję owijaną i dopiero w inner jest wrapper, który rzeczywiście sprawdza to, co chcemy (czy pierwszy argument w args funkcji fav_foods jest równy argumentowi podanemu funkcji ensure_first_arg_is).  
  
## Zmiana typu argumentu dzięki dekoratorowi   

```
def enforce(*types):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)
        return wrapper
    return decorator
    
@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)
        
print(repeat_msg("Miśku", "3"))
# Miśku
  Miśku
  Miśku
  None
```
Funkcja wrapper najpierw tworzy nową, pustą listę dla nowych argumentów, które zostaną podane jako argumenty do funkcji repeat_msg, która będzie za chwilę egzekwowana we wrapperze.  
Dla każdej pary: a - argument funkcji repeat_msg i t - typ podan w funkcji enforce, zepnij je w krotki (argument, typ) i dodaj do nowo utworzonej listy newargs argument (a) zamieniony na typ (t) -> stąd mamy t(a).  
Pary tworzą się przez zip() tak, że spina się pierwszy argument funkcji repeat_msg (msg) z pierwszym argumentem funkcji enforce (str) i drugi argument funkcji repeat_msg (times) z drugim argumentem funkcji enforce (int), stąd dodajemy do listy msg zamienione na string i times zamienione na integer.   
Po dodaniu na listę wszystkich argumentów zamienionych na typy (czyli np. "("message", 3)"), wywołujemy funkcję repeat_msg od listy nowych args - potrzebujemy tu * przed newargs, bo jest to lista, którą musimy rozpakować.
