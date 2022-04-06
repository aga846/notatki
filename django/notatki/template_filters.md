# Template filters and custom filters  
Przykład: mamy pewne informacje z modelu, które chcę użyć wewnątrz różnych views (podstron/rozszerzeń stron). Ale wcześniej mogę chcieć edytować te informacje przed ich wstawieniem w inne miejsce, jak np. zrobić jakieś operacje na stringach lub operacje arytmetyczne.  
Składnia wygląda tak:  
```
{{ value|filter:"parameter" }}
```
Czyli:  
wstawiana_wartość | nazwa_filtra:"parametr_filtra"  
  
Ważne - nie wszystkie filtry przyjmują parametry.  
Wiele filtrów bazuje na wbudowanych pythonowych funkcjach.  
Przykład - kapitalizowanie każdego słowa w stringu:  
```
{{ django|title }}
gdzie context = {'django': 'the web framework for perfectionists with deadlines'}
```
Powyższe wyświetli "The Web Framework For Perfectionists With Deadlines".  
  
Przykład filtrów z parametrami:  
```
{{ my_date|date:"Y-m-d" }} 
{{ number:add:"99"}}   <- doda podaną jako string liczbę do zmiennej "number"
```
    
## Wbudowane filtry  
W dokumentacji - https://docs.djangoproject.com/en/4.0/topics/templates/#filters (czyli "django templates" w google), zakładka "Filters".  
  
## Własne filtry  
Trzeba stowrzyć funkcję, która będzie pracować z filtrem.   
Do tego potrzebuję najpierw w folderze danej aplikacji stworzyć nowy folder "templatetag", wewnątrz którego muszę stworzyć plik "__init__.py" (on będzie kompletnie pusty; dzięki niemu Python będzie traktował ten folder jako moduł, żeby można go było przywoływać).  
W kolejnym pliku w tym folderze będę tworzyć swoje filtry (np. "my_extras.py").  
  
W pliku z filtrami muszę zimportować z django template. Tworzę obiekt "register", który będzie równy template.Library(). Następnie tworzę funkcję, która będzie opisywała mój filter.  
Jako argument ma:  
- value - czyli wartość/zmienną z kontekstowego słownika, który wstawię (do którego zastosuję tę funkcję/filtr),  
- arg - czyli dodatkowy argument.  
  
Następnie trzeba zarejestrować ten filtr przez register.filter, dostarczając jako string nazwę, którą mu nadaję oraz nazwę funkcji.    
  
```
from django import template

register = template.Library()

def cut(value, arg):
  """
  This cuts out all values of "arg" from the string!
  """
  return value.replace(arg, '')
  
register.filter('cut', cut)
``` 
  
Można też inaczej zarejestrować filtr - poprzez dekorator (wtedy niepotrzebna mi ostatnia linijka powyższego przykładu).  
```
@register.filter(name='cut')
def cut(value, arg):
  return value.replace(arg, '')
```
  
W pliku HTML trzeba załadować dany filtr, zaraz pod DOCTYPE piszę:  
```
{% load my_extras %}
```
