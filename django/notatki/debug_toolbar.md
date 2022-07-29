# Instalacja  
```
pipenv django-debug-toolbar
```
  
## Plik settings.py  
W liście zainstalowanych aplikacji dodajemy 'debug_toolbar'. Ważne - musi być po staticfiles i po wszystkich innych defaultowych i wbudowanych rzeczach.  
  
W liście MIDDLEWARE dodaję:  
```
'debug_toolbar.middleware.DebugTollbarMiddleware'
```  
  
Na dole pliku tworzę zmienną:  
```
INTERNAL_IPS = ['127.0.0.1']
```    
Dzięki temu debug toolbar będzie dostępny tylko, jak lokalnie uruchomię stronę.   
     
## Plik urls.py projektu  
Najpierw importuję settings from django.conf.  
Potem pod listą urlpatterns:
```
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', inlude(debug_toolbar.urls))
    ] + urlpatterns
```  
  
## Na stronie  
Na stronie pojawia się pasek z wieloma panelami:  
### 1. Versions  
Wersje, których używam.  
### 2. Time  
Całkowity czas, który zajęło załadowanie strony.  
### 3. Settings  
Wszystkie ustawienia z pliku settings.py.  
### 4. Headers  
Pokazuje nagłówki requestów i odpowiedzi HTTP oraz wartości z WSGI environ. 
### 5. Request  
Pokazuje requesty GET lub POST oraz cookies.  
### 6. SQL  
Pokazuje SQL queries, włącznie z czasem egzekucji i linkami, które mają wytłumaczyć każdy query (pokazuje zapytanie SQL, które zostało wykreowane).  
### 7. Static files  
Informacje o static files.  
### 8. Templates  
Template, z którym dana strona jest połączona.  
### 9. Cache  
Cache queries.  
### 10. Signals  
Lista sygnałów do argumentów i odbiorców (?).  
### 11. Logging  
Użyteczne w przypadku używania wbudowanego modułu Pythona do logowania np. error messages.
