# Tworzenie całego projektu  
## Podstawy  
1. Tworzę projekt dzięki django-admin startproject.  
2. Tworzę aplikację dzięki django-admin startapp.  
3. W pliku settings.py w liście zainstalowanych aplikacji wpisuję nową aplikację.  
4. Tworzę w folderze aplikacji pliki urls i forms.  
5. Robię migracje (python manage.py migrate i makemigrations).  
  
## Tworzenie modeli  
1. Importuję timezone z django.utils i reverse z django.urls.  
2. Tworzę klasę Post; przy author jest ForeignKey z podanym 'auth.User' - odnosi się do tego, że w projekcie nie będzie wielu użytkowników, tylko jedna osoba, która będzie dodawała, edytowała posty - superuser.   
Timezone - w settings.py jest TIME_ZONE - można to zmieniać.  
Przy published_date - blank=True, bo mogę w ogóle nie wstawiać posta (będzie tylko create_date), null=True, bo to pole może być puste.  
W get_absolute_url - po dodaniu posta przekieruje mnie na stronę post_detail, gdzie w słowniku kwargs PK będzie równe PK aktualnego posta.  
3. Tworzę klasę Comment.  
  
## Tworzenie formularzy + ustawianie widgetów korespondujących z klasami CSS  
Ad. widgety - chodzi o to, żeby niektórym elementom formularza (np. button, text area, text input) nadawać różne style. Do tego celu wystarczy tylko dodać atrybut widgets do klasy Meta. Ten atrybut to słownik, któremu dostarczam argumenty, które łączą dany widget z klasą. Potem, jak z pliku CSS odniosę się do tej klasy, wpłynie to na konkretny widget. Jako key tego słownika - nazwa fielda, jako value - nazwa widgetu z podanymi argumentami: attrs={'class': 'nazwa_klasy_dla_CSS'} - patrz: mysite/blog/forms.py.  
1. W pliku forms.py importuję forms z django oraz modele z models.py.  
2. Tworzę klasę PostForm oraz CommentForm. Tam zamieszczam również widgety.  
3. Tworzę folder static wewnątrz aplikacji. Wewnątrz folderu static tworzę 2 foldery - css i js. W folderze css tworzę plik blog.css.  
4. W settings.py ustawić static (STATIC_ROOT).  
5. Tworzę folder templates wewnątrz folderu aplikacji. W folderze templates tworzę foldery z nazwą aplikacji oraz folder registration. Ustawiam to w settings.py.  
6. W settings.py tworzę również LOGIN_REDIRECT_URL i ustawiam na stronę główną ('/').  
  
## Views, templates, urls  
1. Tworzę bazowy plik html.  
2. Tworzę views w view.py. Importuję z django.views.generic TemplateView, ListView oraz modele z blog.models.  
Najpierw tworzę view dla strony about (AboutView) oraz strony głównej, gdzie będą wylistowane wszystkie posty (PostListView). W AboutView ustawiam połączenie do template'u, który tworzę. Ustawiam połączenie z urls.py - najpierw w urls.py aplikacji include('blog.urls') do każdej strony, która nie jest adminem, potem do samego view połączenie ustawiam w urls.py aplikacji. To samo będę robić dla każdego kolejnego view, który stworzę.  
### Funkcja get_queryset  
W view PostListView, w funkcji get_queryset zwracam
```
Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
```
Ta metoda to jest pythonowy sposób na zrobienie zapytania SQL. Ona zwraca: model Post, wszystkie obiekty z niego, przefiltrowane po podanych warunkach: published_date__lte to specjalny sposób pisania właściwy dla field queries. Oznacza: weź datę opublilkowania__i tutaj dopiero warunki. LTE oznacza less then or equal to. Czyli wszystkie posty, które zostały opublikowane teraz lub przed teraz. Uszereguj je według published_date. Ta kreska przed published_date oznacza odniesienie się do tego, czy ma być rosnąco czy malejąco. Bez tej kreski wyświetlałby się najpierw najstarszy post. To znaczy to samo co:  
```
SELECT * FROM blog_post WHERE published_date <= '2020-01-01'
```
chociaż nie wiem, jak w SQL napisać 'now'.  
  
Oprócz metody query_set - filter, są jeszcze exclude i get.  
Sposób wyszukiwania (to, co w nawiasach): nazwafieldu__typwyszukiwania=wartość.  
Oprócz typu wyszukiwania lte są jeszcze exact (w SQL: =), iexact (case-insensitive matching), contains (w SQL: WHERE name_field LIKE).
  
Po stworzeniu view, pamiętać o dodaniu do go urls.py.  
  
Przy tworzeniu klasy CreatePostView - chcę, żeby do tej strony miał dostęp tylko ktoś, kto tworzy posty (superuser). Przy function based views używałam do tego dekoratora login_required, natomiast przy CBV będe używać mixins: from django.contrib.auth.mixins import LoginRequiredMixin. Te mixins to są klasy, które wrzucamy tam, gdzie klasy, z których dziedziczymy - czyli w nawiasie po nazwie klasy. Teraz w klasie tworzę zmienną 'login_url' (gdzie ma przekierować użytkownika, jeśli nie jest zalogowany), redirect_field_name (gdzie ma przekierować po zalogowaniu/jeśli jest zalogowany), form_class (równy formularzowi - więc trzeba go też zimportować).  
  
## Templates  
Tworzę pliki HTML pod każdy stworzony view.  
  
## Authentication system  
Sprawienie, żeby każdy, kto chce stworzyć post, musiał być superuserem.  
W pliku urls.py projektu importuję views z django.contrib.auth.  
Tworzę przekierowania na login (pod registration mam taki plik html) i na logout, przy czym przy logout daję kwargs, w którym daję key 'next_page', które za value będzie miało '/', czyli stronę główną (po wylogowaniu przekieruje na stronę główną).  
  
W login.html tworzę formularz, który przekieruje na stronę login. Nie muszę pisać blog:login, bo mam template'y tylko w aplikacji blog.  
