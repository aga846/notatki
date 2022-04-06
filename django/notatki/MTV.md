# Czym jest MTV  
Django operuje na paradygmacie Models-Templates-Views, czyli MTV. Chodzi o to, jak połączyć wszystko ze sobą - modele, template'y, views:  
1. W pliku views.py importujemy modele, których chcemy użyć  
2. Używamy view żeby zapytać model o dane, których potrzebujemy  
3. Wstawiamy rezultat z modelu to template'u  
4. Edytujemy template, żeby był gotowy na zaakceptowanie i wyświetlenie danych z modelu  
5. Mapujemy URL do view.  
  
Ad 1  
```
from first_app.models import Topic, Webpage, AccessRecord
```
  
Ad 2  
```
def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}
    return render(request, "first_app/index.html", context=date_dict)
```  
Robię listę webpages_list, w której znajdują się obiekty klasy AccessRecord, przesortowane wg daty (metoda order_by).  
Robię słownik date_dict, w którym key będzie "access_records", a value lista webpages_list (value to to, co chcemy wyświetlić na stronie).  
Potem renderuję request, plik HTML, którego chcę użyć oraz stworzony słownik.  
  
Ad 3, Ad 4   
To edytowanie pliku HTML.  
Wstawiam w nim div, a w nim:  
```
{% if access_records %}    <- sprawdzam, czy jest jakieś access record 
```
Potem tworzę tabelę, która ma nagłówki: Site Name i Date Accessed.  
Potem muszę stworzyć rzędy - w tym celu muszę stworzyć pętlę, która będzie przechodziła przez wszystkie rzędy w bazie Access Records, czyli przez wszystko to, co mam w kluczu access_records w słowniku date_dict, a więc w liście webpages_list.  
Więc dla każdego elementu tej listy (czyli każdego obiektu klasy AccessRecord, mającego atrybuty date i name - atrybuty, czyli po prostu komórki po odpowiednią kolumną) tworzę rząd, w którym umieszczam w pierwszej komórce name, a w drugiej date. Ponieważ każdy ten element na liście jest obiektem klasy AccessRecord, to do jego atrybutu dostaję się po kropce:   
```
<table>
  <thead>
    <th>Site Name</th>
    <th>Date Accessed</th>
  </thead>
  
  {% for acc in access_records %}
  <tr>
    <td>{{ acc.name }}</td>
    <td>{{ acc.date }}</td>
  </tr>
  {% endfor %}      <- tak zakańcza się pętlę w tagach template
</table>
```  
  
Skoro wcześniej miałam if, potrzebuję else, i cały blok if-else muszę także zakończyć:  
```
{% else %}
  <p>NO ACCESS RECORDS FOUND!</p>
{% endif %}
```
  
Ad 5  
Trzeba sprawdzić, czy jesteśmy zmapowani w urls.py do właściwego view.
