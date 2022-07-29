# O co chodzi z model forms?  
Chodzi o to, żeby nie tylko wyświetlać dane z formularza w konsoli, ale zachowywać je jako model, np. mamy użytkownika, który rejestruje się na stronę i chcemy zapisać jego informacje do modelu lub ktoś pisze komentarz, który chcemy żeby zawsze się wyświetlał na stronie.  
Trzeba skorzystać (dziedziczyć) z forms.ModelForm w pliku forms.py. Ta klasa pozwoli na stworzenie formularza z istniejącego już modelu.  
Następnie dodajemy klasę inline "Meta", która zapewnia informacje, łącząc model z formularzem (klasa inline - to klasa wewnątrz klasy).  
  
Jestem w pliku forms.py.
Muszę zimportować forms z django.  
Potem z mojego pliku models.py znajdującego się wewnątrz aplikacji, importuję konkretny model.  
Tworzę klasę, która dziedziczy z forms.ModelForm - będzie to nasz formularz.  
Wewnątrz klasy tworzę fieldy oraz klasę Meta - ona połączy model z fieldami z formularza. Można ją zapisać zarówno tak jak poniżej w przykładzie, jak i "class Meta():".  
Wewnątrz klasy Meta tworzę model (ZAWSZE MUSI NAZYWAĆ SIĘ "model"!!!), który jest obiektem klasy, którą zimportowałam z models.py oraz fields, które zrobią bardzo wiele, jeśli chodzi o połączenie z modelem.  
```
from django import forms 
form first_app.models import MyModel

class MyNewForm(forms.ModelForm):
    # FORM FIELDS 
    class Meta:
        model = MyModel
        fields = ###
```  
## Fields w klasie Meta  
Jest dużo sposobów, żeby stworzyć połączenie między model a formularzem.  
Ale w pierwszej kolejności muszę pomyśleć o bezpieczeństwie fieldów - sprawdzić w dokumentacji.  
Jeśli chcę, żeby formularz pasował idealnie do modelu, nie muszę określać fieldów w klasie MyNewForm - okreslam je wtedy tylko w klasie Meta, którą tworzę OD RAZU w klasie MyNewForm. Wtedy formularz tworzy się dokładnie z modelu. Jednak, jeśli chcę stworzyć własne walidatory, potrzebuję stworzyć te fieldy, żeby dać im parametr validators. Natomiast automatyczne czyszczenie i walidacja będzie zrobiona bezpośrednio z modelu (który w atrybutach ma swoje ograniczenia, jak np. max_length, które będą szły automatycznie do formularza jako walidatory, jeśli mam klasę Meta).   
  
### fields = wszystkie_pola_z_modelu  
```
fields = "__all__" 
```
To po prostu bierze wszystkie fields z modelu i umieszcza je w formularzu.  
  
### fields = [lista_wyłączonych_fields]  
```
fields = ["field1", "field2"]
```
Wklejam nazwy fields, które chcę WYŁĄCZYĆ z formularza, tj. nie zawierać ich w formularzu.  
  
### fields = (krotka_fields)  
```
fields = ("field1", "field2")
```
Wklejam nazwy fields, które chcę zawrzeć w formularzu.  
  
Więcej sposobów na łączenie fields z modeli z formularzem - w dokumentacji.  
