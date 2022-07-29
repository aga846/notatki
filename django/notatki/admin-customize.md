## Templates  
Mogę nadpisać template zawarty w pliku HTML połączonym ze stroną admina.  
Tworzę folder templates w głównym folderze projektu, a potem w tym folderze tworzę folder admin. Do tego miejsca mogę wklejać pliki HTML połączone z adminem i nadpisywać je.  
   
Potrzebuję przejść do kodu źródłowego django. Na GitHubie - django/django. W nim trzeba znaleźć, gdzie znajdują się template'y admin: folder django/contrib/admin/templates. W zależności od tego, co chcę zmienić, wybieram folder admin lub registration. Dla admina - admin. Tam są wszystkie pliki HTML.  
Wchodzę w "base_site.html". Ten plik extenduje z "base.html", więc jeśli chcę zmienić np. kolory, to tam.  
Jeśli chcę zmienić stronę bazową (base_site) - kopiuję kod z tego pliku i wklejam go do nowo utworzonego pliku w w/w folderze (który to plik nazywam tak samo jak plik, który będzie nadpisywany). W tym pliku wklejam skopiowany kod i dokonuję zmian.  
  
## Ordering fields  
Domyślnie admin wyświetla fieldy w detail view w takiej kolejności, w jakiej są zdefiniowane w modelu (chodzi o wejście w konkretny obiekt modelu, np. w konkretnego customer'a).  
W pliku 'admin.py' pod aplikacją muszę stworzyć nową klasę, która nazywa się 'nazwamodeluAdmin' (np. MovieAdmin). Ta klasa dziedziczy z admin.ModelAdmin. W klasie dodaję atrybut fields, który będzie listą fieldów w takiej kolejności, jaką chcę.  
```
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
```  
Teraz muszę zarejestrować tę klasę, mogę to zrobić od razu po przecinku po głównym modelu.   
```
admin.site.register(models.Movie, MovieAdmin)
```
  
## Adding Search  
Chodzi o to, żeby łatwo wyszukać dane obiekty modeli.  
W utworzonej i zarejestrowanej wyżej klasie (MovieAdmin) dodaję atrybut search_fields, który będzie listą fieldów, po których chcę szukać. Jeśli dodam np. 2, będzie szukać w obu, np. wyszuka zarówno tytuł, jak i długość trwania (czyli zarówno jak wyszukam 'indiana', ale też jak wyszukam '120').  
  
## Adding Filters  
Będzie filtrować w zależności od typu danych. Nie każdy field będzie użyteczny jako field.  
W stworzonej wyżej klasie dodaję atrybut list_filter, który będzie listą rzeczy, po których chcę filtrować, np. po release_year, genre.  
Zazwyczaj dobrze filtorwać po czymś, co będzie pasowało do wielu rzeczy (nie np. po tytule, czymś, co jest unikalne/mało powtarzalne).  
  
## Adding Fields  
Chodzi o to, by w liście obiektów modelu pojawiało się więcej fieldów.  
W utworzonej wyżej klasie dodaję atrybut list_display, który będzie listą fieldów, które chcę, żeby się pojawiały w liście obiektów (po wejściu w dany model). Ważna jest kolejność podawania fieldów na tej liście.  
  
## Editable ListView  
Chodzi o edytowanie obiektu bez wchodzenia w jego DetailView.  
W stworzonej wyżej klasie tworzę atrybut list_editable, który będzie listą fieldów, które chcę, żeby były edytowalne z poziomu ListView (pamiętać - te fieldy muszą być najpierw wyświetlone, tj. podane w liście atrybutu list_display).
