# Class based views (CBV)  
Najpierw trzeba zimportować klasę View z Django do pliku views.py:  
```
from django.views.generic import View 
```   
  
Trzeba będzie też zmienić to, jak wywołujemy view w pliku urls.py. Trzeba będzie dodać wywołanie klasy poprzez metodę ".as_view()" - to metoda odziedziczona z klasy View.  
  
## Bardziej manualny sposób tworzenia CBV - HttpResponse   
Importuję HttpResponse z django.http.  
Tworzę klasę, która dziedziczy z klasy View.  
Wewnątrz klasy tworzę metodę get, której dostarczam self i request.  
Zwracam jakąś wiadomość, używając HttpResponse.  
```
from django.http import HttpResponse

class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")
```
  
W pliku urls.py dokonuję zmian w wywołaniu tego view (ale poza tym, tak jak wcześniej, muszę zaimportować views z basic_app). Zamiast "views.index" muszę przywołać klasę. Używam do tego metody ".as_view":  
```
path('', views.CBView.as_view())
```  
Powyższe mówi Django: weź tę klasę i pokaż ją jako view.  
  
  
## Template views - zwracanie template'u w CBV  
Zamiast podawać plik w funkcji render, robię klasę jako view, która dziedziczy ze zimportowanej klasy TemplateView (z django.views.generic, razem z klasą View). Potem do atrybutu obiektu klasy Templateview, template_name, przypisuję nazwę pliku HTML będącego templatem.  
```
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
```  
  
### Używanie context dictionary  
Dużą częścią używania template'ów jest wstawianie zawartości do danego template'u.  
To, co chcę wstawić w pliku HTML wewnątrz tagów template, w pliku views.py opisuję w następujący sposób:  
W klasie będącej view tworzę funkcję get_context_data, której dostarczam self oraz kwargs. W tej funkcji przypisuję do zmiennej context "super().get_context_data(kwargs)".  
Następnie ustawiam dany klucz (którym będę się posługiwać w pliku HTML) na dowolną wartość i zwracam context.  
```
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context
```
Key 'injectme' będę używać w index.html (w tagach template). To będzie się odwoływać do ustalonej wartości.
  
  
## List Views and Detail Views - listowanie wszystkich obiektów modelu lub szczegółów danego obiektu  
To dotyczy konkretnie modeli - wyżej dotyczyło tylko wyświetlenia template dzięki CBV. Ta sekcja odnosi się do wylistowania obiektów modelu lub wyświetlenia szczegółów konkretnego obiektu tego modelu.  
Wcześniej, żeby zrobić listę wszystkich obiektów modelu, używałam metody all() w danym view, co potem wykorzystywałam w pliku HTML (sprawdź: ProTwo: app_two/views.py oraz templates/app_two/users.html):  
```
users_list = User.objects.all()
```
Dzięki temu tworzyłam połączenie między templatem a wywołaniem modelu, żeby pokazać informacje z bazy danych.  
Dzięki CBV i jego generic view classes, z których mogę dziedziczyć, można szybko wyświetlić informacje z modelu.  
Tutaj powszechne jest inne lokalizowanie template'ów - zrobienie folderu templates WEWNĄTRZ folderu danej aplikacji i wewnątrz tego folderu jeszcze jeden folder z nazwą tej aplikacji (czyli: basic_app/templates/basic_app).  
  
### 1. Tworzenie modeli w pliku models.py      
Najpierw tworzę modele.  
```
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
        

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    schools = models.ForeignKey(School, related_name='students')
    
    def __str__(self):
        return self.name
```
  
### 2. Rejestracja modeli w pliku admin.py  
Potem w pliku admin.py danej aplikacji importuję te modele i rejestruję je (dzięki temu będę mogła jako admin dodawać obiekty tych modeli).  
  
### 3. Stworzenie plików HTML  
Wewnątrz folderu basic_app/templates/basic_app tworzę pliki: basic_app_base.html, school_detail.html, school_list.html.  
Teraz będę je edytować i upewniać się, że wszystko jest ustawione dla CBV. W tym celu muszę stworzyć te CBV.  
  
### 4. Tworzenie views w pliku view.py  
Idę do views.py i importuję tam klasy ListView i DetailView.  
Tworzę klasę, która dziedziczy z ListView. Tworzę zmienną "model", która jest równa obiektowi danej klasy (danego zimportowanego modelu). I to wystarczy, żeby mieć listę obiektów - ListView robi to wszystko za mnie.  
Łączę ten model z danym templatem - podobnie jak klasa TemplateView, klasy ListView i DetailView również mają atrybut template_name, który podobnie jak wcześniej, ustawiam na nazwę pliku HTML będącego templatem.  
```
class SchoolListView(ListView):
    model = models.School
    
class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
```
  
### 5. Tworzenie template'ów - cd. 3  
Tworzę plik bazowy.  
W pliku school_list.html extenduję o ten plik bazowy. Potem dodaję pętlę for, żeby wyświetlić nazwę każdej szkoły. Używam zmiennej school_list (for school in school_list), ona pochodzi z views. Klasa ListView tworzy context dictionary i zwraca go za mnie - dzięki linijke "model = models.School": bierze nazwę danego modelu (tu: School), daje go małymi literami i dodaje "_list" i dzięki temu powstaje lista school_list.  
Zazwyczaj chcemy sami zdefiniować tę listę (na frontendzie i na backendzie pracują inne osoby/zespoły) - w tym przykładzie - nazwać ją schools. Trzeba dokonać zmian w pliku views.py żeby wywołać obiekt (w sensie zmienną) context, który zwraca to, co chcemy:  
Używamy do tego atrybutu obiektu klasy 'context_object_name' i ustawiamy go na dowolną nazwę. I ten atrybut zwróci po prostu listę obiektów modelu Schools. Właśnie zwrócenie tego atrybutu to jest to domyślne "school_list".   
  
```{% extends 'basic_app/basic_app_base.html' %}

{% block body_block %}
<h1>Welcome to a list of all the schools!</h1>
<ol>
  {% for school in schools %}
  <h2><li>{{ school.name }}</li></h2>
  {% endfor %}
</ol>

{% endblock %}
```  
  
Dygresja - skoro ListView zwraca school_list jako domyślna wartość atrybutu context, to co zwraca DetailView? On zwraca po prostu nazwę modelu małymi literami.  
  
W drugim pliku, school_detail.html wyświetlam szczegóły szkoły poprzez odniesienie się do contextu (który w views.py ustawiłam na nazwę "school_detail") i atrybutu danego obiektu.  
```
{% extends "basic_app/basic_app_base" %}
{% block body-block %}
<div class="jumbotron">
  <h1>Welcome to the School Detail Page</h1>
  <h2>School details:</h2>
  <p>Name: {{ school_detail }}</p>
  <p>Principal: {{ school_detail.principal }}</p>
  <p>Location: {{ school_detail.location }}</p>
  
</div>
{% endblock %}
```  
  
### 6. Tworzenie połączeń - pliki urls.py  
W głównym pliku urls.py importuję include (z django.urls) i zawieram plik urls.py z aplikacji basic_app do każdej strony zaczynającej się rozszerzeniem "basic_app".  
Mogę w funkcji include zawrzeć również drugi argument - namespace i ustawić na nazwę aplikacji. To "namespace" odnosi się do tego, co wpiszę w pliku HTML (basic_app:list).    
```
path('basic_app/', include('basic_app.urls', namespace='basic_app'))
```  
  
W pliku urls.py dla aplikacji importuję co trzeba, ustawiam nazwę app_name (używana w HTML, w navbarze) i tworzę połączenie url do view.  
```
from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list')]
```
  
### 7. Kolejne funkcjonalności - dodawanie linków do konkretnych stron (do school details), wyświetlanie uczniów  
W pliku school_list - stworzona wcześniej lista ze school.name teraz będzie miała wewnątrz każdego itemu tag \<a\>. Jako href wpisuję tam primary key danego obiektu (szkoły), czyli jego id. Będę tego używać w urls.py. Będzie to odniesienie do konkretnej szkoły (jej details).  
Dalej edytuję plik school_detail: dodaję pętlę do każdego studenta i wyświetlam jego imię i wiek. Odnoszę się do tego dzięki "for student in school_detail.students.all". "school_detail" to context, który sworzyłam w view. "students.all" jest dzięki temu, że przy tworzeniu modelu Student stworzyłam odniesienie do primary key modelu School w atrybucie "school" studenta, podając jako related_name własnie "students".
