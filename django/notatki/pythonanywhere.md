# Pythonanywhere  
https://www.pythonanywhere.com/ na tej stronie tworzę konto.  
Mam dostępnych kilka zakładek:  
- consoles - pozwala na tworzenie i wzajemnie oddziaływanie Pythona i bash console,  
- files - pozwala na ładowanie i organizowanie plików wewnątrz disk quota,  
- web - pozwala na konfigurowanie ustawień dla moich postawionych aplikacji,  
- schedule - pozwala na tworzenie zadań i ustawianie ich egzekwowania na konkretną datę,  
- databases - pozwala na konfigurowanie bazy danych MySQL (pozwala też robić postgrads jeśli mam płatne konto).  
  
## Ustawianie wirtualnego środowiska  
W zakładce Consoles pod "Other" znajdę "Bash". Klikam, otworzy mi się konsola. W niej piszę:  
```
mkvirtualenv --python=python3.10 nazwa_projektu
```
Co oznacza: zrób wirtualne środowisko, w którym Python będzie równy wskazanej wersji Pythona i nazwij je "nazwa_projektu".  
Po stworzeniu wirtualnego środowiska, kiedy będę w nim, będę miała jego nazwę pokazaną w nawiasach.  
  
Sprawdzenie, jakie paczki są już zainstalowane:  
```
pip list
```
  
Zainstalowanie Django (w konkretnej wersji):  
```
pip install -U django==4.0.3
```  
Sprawdzenie, czy zostało zainstalowane:  
```
which django-admin.py
```  
  
## Załączanie linka do repozytorium  
Na GitHubie na stronie repozytorium znajdę Code/HTTPS i kopiuję stamtąd linka.  
Następnie w konsoli:  
```
git clone skopiowany-link
```  
  
Czyszczenie konsoli,  
Listowanie zawartości  
Zmienianie folderu 
```
clear
ls
cd
```  
  
Zazwyczaj będę miała modele, które potrzebuję zmigrować i ustawić.  
```
python manage.py migrate
python manage.py makemigrations basic_app
python manage.py migrate
```  
Tworzenie superusera:  
```
python manage.py createsuperuser
```  
  
Teraz wszystko jest gotowe, żeby ustawić aplikację webową, z czym wiąże się ustawienie ustawień WSGI. To oznacza powiedzenie Pythonowi anywhere żeby "zaserwował" moją aplikację, jeśli ktoś odwiedzi moją stronę.  
  
W prawym górnym rogu - Dashboard - wrócę do zakładek, które były na początku. Wchodzę w "Web" i dodaję nową aplikację webową. Pojawi się okienko i trzeba podążać za instrukcjami - trzeba wybrać Django i wersję Pythona. Potem trzeba wrócić, żeby wybrać Manual configuration, wybrać wersję Pythona; konfiguracja manualna będzie się wiązała z edytowaniem pliku wsgi.py.  
Storzy się plik WSGI.  
Teraz mogę kliknąć na podany link i zobaczę tam coś w stylu "Hello World" - coś, co chwilowo utworzyło się dla mnie. Jeśli chcę skonfigurować swoją własną aplikację webową, klikam na podany link do web.app.setup. Tam mam instrukcje:  
Na dole znajduje się "Virtualenv" i w nim "Enter path to a wirtualenv, if desired", klikam w to i piszę ścieżkę:  
```
/home/nazwa_użytkownika/.virtualenvs/nazwa_wirtualnego_środowiska
```
Kliknąć tik, pojawi się ścieżka.  
Następnie klikam "Start a console in the virtualenv".  
Trzeba ustawić link do folderu projektu.  
W konsoli trzeba wejść w projekt i wpisać komendę pwd (print working directory). Wyświetli ścieżkę, kopiuję ją.  
   
Wracam do Dashboard/Web, na dole znajduje się "Code" i tam w "Source code" wklejam tę ścieżkę, klikam tik.  
Potem muszę ustawić plik WSGI. Zaraz pod "Source code" jest link do WSGI configuration file, klikam w niego - przeniesie mnie w miejsce, gdzie mogę edytować ten plik.  
Od "HELLO WORLD" aż do mniej więcej 47 linijki jest samo wyświetlenie Hello World (to, co wyświetlało się po stworzeniu pliku WSGI). To już nie jest mi potrzebne, usuwam. Chcę powiedzieć temu programowi, żeby poszedł zamiast tego na moją stronę.  
Niżej w tym pliku jest sekcja DJANGO, tam są napisane jako komentarz niektóre linijki (1-5), które muszę napisać:  
```
import os
import sys 
path = '/home/nazwa_użytkownika/nazwa_repozytorium/nazwa_projektu'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nazwa_projektu.settings")

import django 
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
os.environ -> muszę powiedzieć Django, gdzie settings.py jest zlokalizowany.  
Zapisuję powyższe.  
   
Wracam do Dashboard/Web, klikam na link, który zaprowadzi mnie do mojej strony.  
Niektóre podstrony wyglądają gorzej niż wyglądały jak odpalałam je u siebie z serwera. Żeby to naprawić:  
Dashboard/Web, na samym dole mam Static files. Muszę tu się połączyć ze static files dla strony admin oraz moimi własnymi plikami static.  
Klikam w "Enter URL" pod "URL" i tam łączę ze static files dla admin:  
```
/static/admin
```
Potem w Directory:  
```
/home/nazwa_użytkownika/.virtualenvs/nazwa_wirtualnego_środowiska/lib/python3.10/site-packages/django/contrib/admin/static/admin
```
  
Jak cokolwiek zmieniam w Static files, muszę przeładować aplikację webową - na górze w Web mam "Reload" i przycisk do przeładowania.  
Potem trzeba wyłączyć tryb debug i upewnić się, że pozwoliłam pythonanywhere być hostem: idę do Files, klikam na repozytorium i potem na projekt, potem folder z nazwą projektu, tam idę do pliku settings.py.  
Tam w liście ALLOWED_HOSTS wpisuję 'nazwę_użytkownika.pythonanywhere.com'.  
Wracam do głównego folderu projektu. Tam tworzę nowy folder 'static' (tutaj później mogę załadowywać static files). Póki co trzeba ustawić link do niego.  
Wracam do Web i przeładowuję stronę - teraz już wszystko będzie wyglądać normalnie.  
Jeśli wpiszę jakieś nieistniejące rozszerzenie strony, wyskoczy błąd i komunikat, że DEBUG=True (co oznacza, że tryb debug jest ciągle włączony). Wracam do Files, wchodzę do pliku settings.py i tam ustawiam DEBUG=False.  
Idę do Web i teraz muszę połączyć się z moimi własnymi plikami static.  
W URL wpisuję:  
```
/static/
```
w Enter path wpisuję:   
```
/home/nazwa_użytkownika/nazwa_repozytorium/nazwa_projektu/static 
```  
Przeładowuję stronę. Teraz przy wpisaniu rozszerzenia strony, które nie istnieje, będzie po prostu "Not Found", bez ujawniania nic z mojego kodu.
