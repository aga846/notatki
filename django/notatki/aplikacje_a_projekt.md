# Czym jest projekt Django?  
Projekt Django jest zbiorem różnych aplikacji i konfiguracji, które wspólnie tworzą pełną aplikację internetową (czyli pełną, działającą stronę internetową).  
  
APLIKACJA WEBOWA != APLIKACJA DJANGO  
  
Aplikacja Django jest stworzona, żeby przedstawiać konkretną funkcjonalność zawierającą się w pełnej stronie internetowej.  
Aplikacja webowa to inaczej strona internetowa, czyli projekt Django. Wewnątrz tego projektu znajdują się aplikacje Django.  
  
Aplikacje Django można łączyć z innymi projektami Django (tak jak używać aplikacji stworzonych przez innych ludzi).  
  
## Tworzenie aplikacji Django  
Żeby stworzyć aplikację Django, muszę być w folderze, w którym znajduje się plik manage.py. Tam wpisują komendę:  
```
python manage.py startapp first_app
```
Ta komenda stworzy w głównym folderze mojego projektu (w tym, w którym znajduje się plik manage.py oraz kolejny folder z nazwą projektu) folder o nazwie aplikacji, którą wpisałam.  
W tym folderze znajdują się:  
- plik __init__.py - tak jak w projekcie: pusty plik; dzięki nazwie z dwoma podkreślnikami przed i po, Python będzie wiedział, że ten folder ma traktować jak paczkę  
- plik admin.py - w tym pliku mogę rejestrować swoje modele, których Django potem użyje z interfejsem administratora  
- plik apps.py - zapewnia miejsce dla jakichkolwiek specyficznych konfiguracji aplikacji  
- plik models.py - dane o modelach aplikacji; mogę to specyfikować podmioty i relacje między danymi  
- plik tests.py - tutaj piszę testy dla kodu mojej aplikacji  
- plik views.py - tutaj znajdują się funkcje, które obsługują żądania i odpowiedzi na nie  
- folder migrations - przechowuje specyficzne informacje o bazie danych w odniesieniu do modeli (w tym folderze znajduje się plik __init__.py).  
Plików views.py i models.py będę używać dla każdej aplikacji.  
  
Po stworzeniu aplikacji muszę dać znać Django, że ją utworzyłam - w pliku settings.py znajduje się lista "INSTALLED_APPS" zawierająca domyślne aplikacje, i tam jako string podaję nazwę mojej aplikacji.  
  
### Tworzenie view  
Najpierw w pliku views.py trzeba zimportować obiekt HttpResponse z modułu django.http.  
Następnie, każdy view dla danej aplikacji będzie istniał w środku pliku views.py jako osobna funkcja.   
Nazwa funkcji = nazwa view.  
Każda funkcja będzie przyjmowała przynajmniej jeden argument. Zazwyczaj nazywamy go "request" (umownie).  
Funkcja zwraca obiekt HttpResponse, któremu coś dostarczamy, np. HttpResponse("Hello World!"). Każda funkcja musi zwrócić ten obiekt.  
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
```  
Tym, co dostarczamy HttpResponse, może być także kod html, np. "<em>Hello World!</em>". Wtedy to, co później (po kolejnym kroku) zobaczymy w przeglądarce, będzie w tym przypadku napisane kursywą.  
   
#### Mapowanie do pliku urls.py  
Żeby zobaczyć stworzony view przy odpaleniu serwera (w przeglądarce), musimy zmapować ten view do pliku urls.py:  
1. Muszę zimportować tam views z danej aplikacji  
2. W pliku urls.py znajduje się lista urlpatterns, do której dodaję pusty string jako pierwszy argument, funkcję z pliku views jako drugi argument oraz nazwę jako trzeci argument:  
```
from first_app import views

urlspatterns = [
path('', views.index, name='index')]
```

Pierwszy argument to ścieżka - to, co znajduje się po głównym adresie (po http://127.0.0.1:8000/).  
W ścieżce mogę dawać różne zmienne poprzez użycie nawiasów <>, w którym określam typ zmiennej oraz jej nazwę, np.  
```
path("<str:name>", views.greet, name=greet)
```  
Powyższe oznacza, że zmienną (string) "name" dostarczę jako parametr funkcji greet znajdującej się w views.py - która np. zwraca "HttpResponse(f"Hello {name.capitalize()}!")".  
    
Ogólnie lepiej jest utrzymywać główny plik urls.py (ten stworzony automatycznie przy tworzeniu projektu) jak najczystszym; w tym celu najlepiej zawierać potrzebne URL w samych aplikacjach - tam stworzyć plik urls.py i używać funkcji include().  
  
#### Mapowanie przy pomocy include()  
W aplikacji tworzymy plik urls.py.  
W ogólnym pliku urls.py (tym projektowym) importujemy z modułu django.conf.urls funkcję include.  
W liście urlspatterns, zawieramy path('adres_strony', include('first_app.urls.')). To oznacza: szukaj tej strony, którą podałam, i wtedy wywołaj plik urls.py z first_app.  
```
urlpatterns = [
  ...
  path("first_app/", include("first_app.urls")),
  ...
]
```
To, w co w powyższym przykładzie jest nazwane "first_app", może nazywać się jakkolwiek chcemy - np. "mynewextenstion".  
  
Następnie, w pliku urls.py w aplikacji (nie tym projektowym), importujemy path z django.urls oraz views z first_app, tworzymy tam listę urlspatterns, której dostarczamy path('', konkretne_view, nazwa_view):  
```
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
