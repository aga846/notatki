# Wstawianie statycznych plików do strony  
Tak jak wstawiamy tekst za pomocą templates, tak możemy też wstawić inne elementy, jak np. zdjęcie lub inne statyczne elementy (te, które się nie zmienią, np. plik CSS, JS).  
  
Należy w głównym folderze projektu stworzyć folder o nazwie static (tak jak tworzyliśmy templates).  
Potem dodajemy ścieżkę tego folderu do pliku settings.py (tak jak z templates) - dodajemy zmienną STATIC_DIR, w której podajemy ścieżkę do folderu static: 
```
STATIC_DIR = os.path.join(BASE_DIR, "static")
```  
    
Dodajemy również listę STATICFILES_DIRS (na samym dole settings.py), w której jako element wstawiamy zmienną STATIC_DIR.   
  
Teraz potrzebujemy miejsca, żeby przechowywać zdjęcia (statyczne pliki graficzne): tworzymy podfolder o nazwie images wewnątrz folderu static. Wewnątrz tego projektu umieszczamy zdjęcie.  
  
Żeby sprawdzić, czy wszystko działa, należy udać się pod adres:  
http://127.0.0.1:8000/static/images/pict.jpg  
  
Dalej będziemy tworzyć tag template, żeby osiągnąć to wszystko.  
  
## Tagi template  
Na samej górzej pliku HTML (zaraz po DOCTYPE) trzeba wstawić specyficzny tag:  
```
{% load static %}
```
  
Następnie wstawiamy zdjęcie za pomocą tagu HTML "img src=":  
```
<img src={%static "images/pict.jpg" %} />
```
  
### Różnica między {{ }} a {% %}  
{{ }} jest używane do prostego wstawienia tekstu,  
{% %} jest używane do bardziej złożony wstawień oraz logiki.  
  
### Wstawianie pliku CSS  
W folderze static tworzę nowy folder "css". W tym folderze tworzę plik CSS (np. "mystyle.css").  
W pliku HTML łączę się (poprzez tag "link") z moim plikiem CSS, jako href wpisując tag template:  
```
link rel="stylesheet" href="{% ststic "css/mystyle.css" %}"
```
