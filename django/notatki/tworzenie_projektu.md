# Tworzenie wirtualnego środowiska  
W folderze, w którym chcę mieć swój project, tworzę wirtualne środowisko, wpisując w wierszu poleceń:  
```
pipenv install  
```
Zainicjalizuje to wirtualne środowisko.  
  
W tym środowisku mogę instalować moduły lub narzędzia za pomocą komendy (poniżej - instalacja Django):  
```
pipenv install django
```  
Moduł lub narzędzie mogę zainstalować w konkretnej wersji:  
```
pipenv install django==2.1
```
  
## Wejście do wirtualnego środowiska  
```
pipenv shell
```
  
## Wyjście z wirtualnego środowiska  
```
exit
```  
  
  
# Tworzenie projektu  
Będąc w folderze, w którym utworzyłam środowisko, tworzę nowy projekt Django:  
```
django-admin startproject nazwa_projektu
```
  
Powyższa komenda stworzy folder o zadeklarowanej nazwie projektu. W tym folderze znajduje się:  
- kolejny folder o nazwie projektu, zawierający pliki:  
    a) __init__.py - pusty plik; dzięki nazwie z dwoma podkreślnikami przed i po, Python będzie wiedział, że ten folder ma traktować jak paczkę
    b) asgi.py  
    c) settings.py - ustawienia dotyczące całego projektu  
    d) urls.py - strony URL, których moja strona (projekt) będzie używać  
    e) wsgi.py - skrpyt Pythonowy, który zachowuje się jak "Web Server Gateway Interface"; będzie potrzebny, żeby wdrożyć aplikację webową do produkcji
- plik manage.py - będzie powiązany z wieloma poleceniami, gdy będę budować moją aplikację webową.    
  
## Uruchomienie aplikacji na serwerze  
Żeby móc otworzyć swój projekt w przeglądarce, będąc w folderze, w którym znajduje się plik manage.py, wpisuję komendę:  
```
python manage.py runserver
```  
W wierszu poleceń wyświetli się sporo informacji, m.in. "Starting development server at http://127.0.0.1:8000/". Idąc pod ten adres, zobaczę swój projekt w przeglądarce.  
  
## DEBUG = True  
W pliku settings.py DEBUG mam ustawione na True, ale jeśli dam coś do produkcji, muszę ustawić DEBUG na False (wtedy, jeśli pojawi się błąd, user nie będzie miał dostępu do naszych narzędzi debuggowych).  
  
  
## Ostrzeżenie o migracjach  
Jest to związane z bazami danych oraz z tym, jak połączyć je z Django.  
Migracja pozwala na przeniesienie bazy danych z jednego projektu do drugiego; jest to odwracalne.
