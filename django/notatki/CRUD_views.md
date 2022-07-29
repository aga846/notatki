# CRUD  
Create, Retrieve, Update, Delete.  
Jeśli pracuję z modelami i bazami danych, będę potrzebować wykonywania tych 4 akcji. CBV z Django ułatwiają ten proces.   
  
## CreateView  
W pliku views.py importuję CreateView, UpdateView, DeleteView.  
CreateView pozwoli łatwo stworzyć nową szkołę (nowy obiekt).  
Tworzę klasę SchoolCreateView, dziedziczę z CreateView, ustawiam model na models.School (obiekt klasy School z models.py, czyli po prostu nowy rząd w tabeli).  
```
class SchoolCreateView(CreateView):
    model = models.School
```  
W pliku urls.py aplikacji ustawiam przekierowanie na ten view, kiedy rozszerzenie strony będzie "create/".  
```
path('create/', views.SchoolCreateView.as_view(), name='create')
```  
Jeśli teraz przejdę do tej strony, będzie błąd "ImproperlyConfigured at /basic_app/create/. Using ModelFormMixin (base class of SchoolCreateView) without the 'fields' attribute is prohibited.". To oznacza: ej, chcesz stworzyć view, ale nie sprecyzowałaś, które fields są zabronione, a które są dostępne. Trzeba to naprawić poprzez przejście do pliku views.py i stworzyć fieldy - np. podaję w krotce wszystkie 3 istniejące w klasie School fieldy.  
```
fields = ('name', 'principal', 'location')
```  
Teraz po odświeżeniu strony mam kolejny błąd - TemplateDoesNotExist - bo nie zrobiłam pliku HTML (template dla School Creation Page). Wskazuje też, że szuka pod basic_app pliku o nazwie "school_form.html". To oznacza, że klasa CreateView automatycznie tworzy domyślny template HTML, którego oczekuje. A oczekuje, żeby była nazwa modelu małymi literami, podkreślnik, "form". Tworzę więc plik o takiej nazwie.  
W tym pliku robię formularz. Najpierw sprawdzam, czy dany PK istnieje, jeśli tak, nagłówek to "Update School", jeśli nie - "Create School".  
Potem tworzę formularz (po prostu z modelu, bez pliku forms).  
```
{% extends "basic_app/basic_app_base.html" %}
{% block body_block %}
<h1>
  {% if not form.instance.pk %}
  Create School 
  {% else %}
  Update School 
  {% endif %}
</h1>

  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" class="btn btn-primary" value="Submit">  
  </form>
{% endblock %}
```
Jeśli teraz zasubmituję, będzie błąd "ImproperlyConfigured. No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model." Będziemy wykorzystywać drugie rozwiązanie - definiować w modelu metodę get_absolute_url.  
Tu mamy dać znać, z jakim PK chcemy, żeby dana szkoła została stworzona. Trzeba zimportować reverse z django.urls. Tworzę metodę get_absolute_url i zwracam w niej reverse("basic_app:detail", kwargs={'pk':self.pk}); czyli view detail (to "detail" jest zdefiniowane w urls.py jako "name"), z PK tego obiektu jako PK. Oznacza to, że po wypełnieniu formularza Django ma przejść z powrotem (reverse) na podaną stronę - stronę detail obiektu o danym PK. Bo w formularzu nie podałam strony, na którą ma być przekierowanie - po to mi metoda get_absolute_url.  
```
def get_absolute_url(self):
      return reverse("basic_app:detail", kwargs={'pk':self.pk})
```
  
## UpdateView  
Tworzę klasę dziedziczącą z UpdateView. Ustalam, które fieldy chcę, żeby były dostępne do aktualizowania (tutaj trzeba się zastanowić - w przypadku szkoły raczej miejsce się nie zmieni, ale nazwa i dyrektor już mogą).  
Potem tworzę obiekt modelu School.  
```
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
```
Teraz wprowadzam zmiany w pliku urls.py: dodaję ścieżkę zawierającą "update/" oraz PK danej szkoły.  
```
path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update')
```  
Teraz muszę zedytować template - plik school_detail.html. Dodaję div, w nim paragraf, w nim tag \<a\>, w którym przekierowuję do strony update (opisane wyżej, w urls.py) oraz podaję argument pk=school_detail.pk.  
```
<div class="container">
  <p><a class='btn btn-warning' href="{% url 'basic_app:update' pk=school_detail/pk %}">Update</a></p>
</div>
```
UpdateView prawdopodobnie też szuka pliku school_form.html, bo właśnie na ten plik (na stronę tego HTMLa) przekierowuje.  
  
## DeleteView  
Tworzę klasę dziedziczącą z DeleteView. Tworzę obiekt modelu School.  
Muszę stworzyć atrybut success_url. Teraz trzeba użyć metody reverse_lazy (najpierw zimportować ją z django.urls) i wprowadzić do niej url, do którego przekieruje (czyli np. "basic_app:list" - czyli strona wylistowanych szkół) - to oznacza: jeśli powiedzie się usunięcie szkoły, wróć z powrotem na stronę z listą. Użycie reverse_lazy jest po to, żeby przekierowało tam dopiero wtedy, gdy usunięcie się powiedzie.  
```
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
```
W pliku urls.py dodaję ścieżkę zawierającą "delete" oraz PK danej szkoły.  
```
path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete')
```
Teraz muszę mieć jakiś plik HTML. Oczekiwany jest: school_confirm_delete.html. Ta strona się pokaże, jak ktoś będzie próbował manualnie usunąć szkołę. Tam używam contextu dla view SchoolDeleteView (który defaultowo to po prostu nazwa modelu małymi literami) i pytam, czy usunąć szkołę o danej nazwie.  
Potem robię formularz - tworzę 2 przyciski, jeden do potwierdzenia usunięcia, drugi do wyjścia, który przekieruje do strony detail danej szkoły (dlatego tam też zapewniam PK jako argument).  
```
{% extends "basic_app/basic_app_base.html" %}
{% block body_block %}
<h1>Delete {{  school.name }}?</h1>
<form method="post">
  {% csrf_token %}
  <input type="submit" class='btn btn-danger' value="Delete">
  <a href="{% url 'basic_app:detail' pk=school.pk %}">Cancel</a>
</form>
{% endblock %}
```
