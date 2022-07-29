# Wstęp  
Istotą każdej strony jest to, żeby przyjmować informacje od użytkownika, wstawiać je do bazy danych i odzyskiwać informacje z tej bazy w celu generowania zawartości strony dla użytkownika.  
  
Używamy modeli, żeby włączyć bazę danych do projektu.  
Django korzysta z SQLite (oraz innych rodzajów/engine'ów SQL).  
  
W pliku settings.py mogę edytować parametr ENGINE używany pod DATABASES.  
Żeby stworzyć model, używamy struktury klas wewnątrz pliku models.py danej aplikacji. Klasa będzie dziedziczyć z wbudowanej w Django klasy django.db.models.Model.  
Każdy atrybut tej klasy (dziedziczącej) będzie reprezentować konkretne pole (field) - tak jak kolumna w SQLu.  
primary key = unikalny identyfikator pod każdy rząd w tabeli - kolumna z konkretnym indentyfikatorem (numerem), której nie tworzę; zawsze jest pierwsza w każdej tabeli; to ID każdego obiektu     
foreign key = wskazuje na to, że dana kolumna "zbiega się" z primary key innej tabeli.  
Fieldy ForeignKey oraz OneToOneField wymagają dodatkowo argumentu on_delete=models.CASCADE.  
  
## Tworzenie klas w pliku models.py  
Tworzę klasę, która dziedziczy z klasy models.Model. Każda klasa to model. Każdy model jest jak tabela.  
Każdy atrybut będzie oznaczony jako:  
models.RodzajPola(ograniczenia), np.  
```
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    
class Webpage(models.Model):
    category = models.ForeignKey(Topic) <- wskazanie na "zbieganie się" z primary key innej tabeli (Topic)
    name = models.CharField(max_length=264)
    url = models.URLField()
    
    def __str__(self):
      return self.name   <- przy printowaniu webpage pokaże się name
```  
Rodzaje pól są opisane w dokumentacji. Oprócz CharField, np. EmailField, PositiveIntegerField.    
Po utworzeniu modeli będziemy migrować bazę danych.  
  
## Migracja bazy danych  
Innymi słowy - stworzenie bazy danych SQL, która koresponduje z utworzonymi modelami. Wystarczy do tego komenda:  
```
python manage.py migrate
```    
Następnie trzeba zarejestrować zmiany do aplikacji (tutaj: app1):  
```
python manage.py makemigrations app1
```  
Potem migrujemy bazę danych jeszcze raz (pierwsza komenda).  
  
  
Żeby używać bardziej wygodnego interfejsu admina z modelami, trzeba zarejestrować je do pliku aplikacji admin.py:  
```
from django.contrib import admin
from app.models import Model1, Model2
admin.site.register(Model1)
admin.site.register(Model2)
```
Żeby w pełni używać bazy danych i admina, trzeba stworzyć "superusera":  
```
python manage.py createsuperuser
```
zapewaniając nazwę (imię), email i hasło.  
  
Teraz, po wpisaniu adresu strony + /admin, będę mogła się zalogować i zarządzać modelami z poziomu przeglądarki.  
  
## Sprawdzanie, czy zadziałało  
Żeby sprawdzić, czy stworzenie modeli zadziałało, można wykreować kilka testowych danych. Do tego celu muszę wejść w Interaktywną Konsolę poprzez komendę:  
```
python manage.py shell
```  
Teraz muszę zimportować któryś z utworzonych w pliku models.py modeli:  
```
from first_app.models import Topic 
```
Żeby wyświetlić wszystkie obiekty tej klasy:  
```
print(Topic.objects.all())      # <QuerySet []> <- bo na razie nie mam żadnego obiektu
```
Stworzenie obiektu:  
```
t = Topic(top_name="Social Network")
t.save()   <- metoda odziedziczona z klasy models.Model
```
Teraz przy sprintowaniu wszystkich obiektów pojawi się:  
```
<QuerySet [<Topic: Social Network>]>
```
  
Raczej nie będę w ten sposób tworzyć czegokolwiek, oglądać modelu ani dowiadywać się, co baza danych zawiera. Przyda się admin interfejs.
