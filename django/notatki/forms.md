# Dlaczego używać Django Forms?  
1. Mogę szybko wygenerować kod HTML z widgetów  
2. Mogę zwalidować dane i przetworzyć do pythonowej bazy danych; mogę też tworzyć własne reguły walidacji    
3. Mogę tworzyć formularzowe wersje modeli i szybko aktualizować modele z formularzy  
  
## Tworzenie formularza  
1. Plik forms.py   
Najpierw trzeba stworzyć plik forms.py wewnątrz aplikacji.  
Następnie wywołuję wbudowane w Django klasy formularzy (podobnie do tworzenia modeli - klas).  
```
from django import forms 

class FormName(forms.Form): 
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
```
Każdy input to atrybut klasy.  
Żeby sprawdzić inne widgety, trzeba udać się do dokumentacji Django. Tutaj to widget, który odpowiada za pole tekstowe.  
  
2. Plik views.py  
Teraz należy pokazać formularz używając view:  
Wewnątrz view.py w aplikacji muszę zimportować forms - są 2 sposoby:  
```
from . import forms                 <- z aktualnego folderu zimportuj forms
from forms import FormName          <- z forms zimportuj klasę FormName
```  
Następnie tworzę view:  
```
def form_name_view(request):
    form = forms.FormName()
    return render(request, "form_name.html", {"form": form})
``` 
Plik HTML będzie przechowywał formularz.  
  
Notka odnośnie ModelForm - jeśli nie używam bezpośrednio modelu w pliku views.py (tylko forms.py), nie muszę importować modeli.  
Notka odnośnie save: żeby zapisać formularz (informacje z niego) w bazie danych, należy w if form.is_valid() napisać "form.save(commit=True)": jeśli ktoś wypełni formularz i dane są prawidłowe, zapisujemy ten formularz. W return można zamiast render, dać inny view z pliku views.py, np.   
```
if form.is_valid():
        form.save(commit=True)
        return index(request)
```
  
  
3. Plik urls.py  
W pliku urls.py znajdującym się wewnątrz aplikacji (bezpośrednio lub za pomocą include()).  
Bezpośrednio:  
```
from basicapp import views
urlpatterns = [
  path('formpage', views.form_name_view, name='form_name'),
]
```  
  
4. Templates  
Potem tworzymy folder templates i wewnątrz niego podfolder dla danej aplikacji, w którym będzie znajdował się plik HTML, który będzie przechowywał tagi template dla formularza.  
Trzeba pamiętać, żeby views ozdwierciedlały podfoldery wewnątrz templates: w returnie funkcji, która tworzy view (wewnątrz views.py), jest wskazanie do pliku HTML, który znajduje się w konkretnym podfolderze; ważne: nie piszemy tam templates/first_app/index.html, tylko samo first_app/index.html.
  
5. Plik settings.py  
Trzeba pamiętać o zmiennej TEMPLATE_DIR wewnątrz pliku settings.py.  
  
6. Plik HTML  
Jest kilka sposobów na wstawienie formularza używając tagów template.  
Mogę po prostu dodać key ze słownika stanowiącego context w views:  
```
{{ form }}
```
Zasadniczo będzie to wyglądać tak (z zastosowaniem klas z Bootstrapa):  
```
<div class="container">
  <form method="POST">
    {{ form.as_p }} 
    {% csrf_token %}
    <input type="submit" class="btn btn-primary" value="Submit">
  </form>
</div>
```
{{ form.as_p }} oznacza, że jest używany tag \<p\> (żeby był ładniejszy layout); czyli automatycznie, dzięki "as_p", zostanie to zwrócone wewnątrz tagów \<p\> -\> będzie ustawione od góry do dołu, a nie od lewej do prawej.  
Można sprawdzić w dokumentacji Django, jak zrobić, żeby formularz był zwrócony np. jako tabela.  
  
{% csrf_token %} = Cross-Site Request Forgery token, który ochrania akcję HTTP POST zainicjowaną przy późniejszym zasubmitowaniu formularza (chroni przed dostaniem złych danych lub przed wysłaniem ich gdzieś indziej niż było to zamierzone). Django wymaga, żeby zawrzeć token CSRF - bez niego formularz może nie zadziałać. Ten token działa przez używanie "ukytego inputu", który jest randomowym kodem i sprawdza, czy pasuje do lokalnej strony użytkownika. Może być zawarty przed lub po {{ form }}.   
    
7. Plik views.py  
Jeśli teraz zasubmitujemy, nic się nie wydarzy. Należy więc poinformować view, że jeśli dostaniemy z powrotem POST, trzeba sprawdzić czy dane są ważne i jeśli tak, wziąć je.  
Na razie zakładamy, że są ważne (poprawne).  
Możemy mieć dostęp do słownika-jak-atrybut tych danych, który nazywa się "cleaned_data". Trzeba w następujący sposób edytować view:  
```
def form_name_view(request):
    form = forms.FormName()
      
    if request.method == "POST":
        form = forms.FormName(request.POST)
      
        if form.is_valid():
            print("Form Validation Success. Prints in console.")
            print("Name" + form.cleaned_data['name'])
            print("Email" + form.cleaned_data['email'])
            print("Text" + form.cleaned_data['text'])
        
    return render(request, "form_name.html", {"form": form})
```
a) sprawdzamy, czy mamy z powrotem POST (czyli user zasubmitował i jego request to post)  
b) jeśli tak, chcemy wprowadzić ten request - do klasy (formularza) FormName wprowadzamy ten request  
c) potem sprawdzamy, czy te dane są poprawne (ważne) - jeśli tak, mamy dostęp do danych poprzez key od słownika, do którego mamy dostęp poprzez form.cleaned_data.  
  
## Walidowanie formularzy  
Po to, żeby dane były prawidłowe i żeby boty nie mogły ich wypełniać.  
Mogę to zrobić:  
- poprzez funkcję clean_  
- używając wbudowanych walidatorów  
- tworząc własne walidatory  
- dodając metodę clean_ do całego formularza  
  
### Walidowanie poprzez funkcję clean  
1. Dodawanie pustych pól - fields (puste pola - istnieją w HTMLu, ale są ukryte przed użytkownikiem)  
2. Dodawanie sprawdzenia dla botów - metoda clean_   
  
  
W pliku forms.py tworzę kolejny atrybut:  
```
botcatcher = forms.CharField(required=False,
                             widget=forms.HiddenInput)
```
- required=False, bo jak mamy ten field, to on się nie pokaże na stronie dla użytkownika, ale będzie w HTMLu (więc żeby dowiedzieć się, czy istnieje taki field, trzeba zbadać stronę)  
- widget=forms.HiddenInput pozwoli ukryć to pole przed typowym ludzkim użytkownikiem  
Jeśli jakieś boty odwiedzą moją stronę, nie patrzą na stronę, ale idą do kodu HTML i będą starały się automatycznie wypełniać pola (value attributes) na podstawie kodu - do danego inputu doda atrybut "value" i przypisze mu jakąś wartość.  
Jeśli dodadzą atrybut value do inputu botcatcher, nic się nie zmieni w formularzu ani w otrzymywanych z niego danych.  
Chcemy więc zwalidować ten konkretny input (botcatcher) - używamy metody clean (w forms.py):  
```
def clean_botcatcher(self):
    botchatcher = self.cleaned_data["botcatcher"]
    if len(botcatcher) > 0:
        raise forms.ValidationError("GOTCHA BOT!")
    return botcatcher
```
Tej metodzie daję nazwę clean i po podkreślniku nazwę pola, które chcę walidować.  
Ustawiam botcatcher równy cleaned_data od key [nazwa_fieldu] (to, co zwraca botcatcher zdefiniowany powyżej, w forms.py).  
Potem sprawdzam, czy długość tego botcatchera jest dłuższa niż 0 (mogę też wpisać po prostu "if botcatcher") - jeśli tak, tzn. że jakiś bot przyszedł na stronę - podnoszę wtedy błąd (wbudowany) i zwracam botcatcher.  
Jeśli bot wypełni formularz, nic nie zostanie zwrócone w konsoli, ale na stronie wyświetli się "(Hidden field botcatcher) GOTCHA BOT!".  
  
### Walidowanie poprzez walidatory z django.core  
Do pliku forms.py z django.core importuję validators.  
W fieldzie będę wprowadzała parametr walidacyjny - jako listę. Kolejnymi elementami będą wbudowane walidatory z django.core (np. sprawdzanie maksymalnej długości) - przy botcatcherze ma być 0 znaków, więc w nawiasie wpisuję 0. 
```
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=validators.MaxLengthValidator(0)])
```
  
Teraz jeśli zasubmituję taki formularz, na stronie wyświetli się: "(Hidden field botcatcher) Ensure this value has at most 0 characters (it has 8)", a w konsoli nic. To automatyczny djangowy komunikat z walidatora.  
  
### Tworzenie własnych walidatorów   
Przykład - chcę sprawdzić, czy imię zaczyna się od litery Z.  
Tworzę funkcję poza klasą, daję jej nazwę (np. "check_for_z"). Trzeba jej dodać parametr value. Wtedy Django wie, że ta funkcja będzie się zachowywała jak walidator.  
```
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")
```
sprawdzam, czy pierwsza litera (value[0]) jest równa 'z'. Jeśli nie - podnoszę błąd i wyświetlam zamieszczony w nawiasach komunikat.  
Potem muszę ten błąd wstawić do konkretnego atrybutu klasy - fielda. W powyższym przypadku wstawiam to do atrybutu name:  
```
name = forms.CharField(validators=[check_for_z])
```
Dzięki temu, że funkcja ma parametr value, Django wie, że jest to walidator.  
Teraz, jeśli imię nie zaczyna się na z, wyświetla się komunikat, który wstawiłam przy podnoszeniu błędu, a w konsoli nie wyświetla się nic.    
  
### Metoda clean_ dla całego formularza  
Przykład - podawanie adresu email drugi raz, żeby upewnić się, że podałam prawidłowy (że nie zrobiłam literówki).  
W klasie FormName dodaję kolejny field, któremu daję label:  
```
verify_email = forms.EmailField(label="Enter your email again:")
```  
Potem dodaję metodę clean - jeśli chcę, żeby dotyczyła całego formularza, piszę po prostu clean(self).  
```
def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data["email"]
    vmail = all_clean_data["verify_email"]
    
    if email != vmail:
        raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
```
all_clean_data zwróci wyczyszczone dane z całego formularza.  
Poza tym mogę robić coś z konkretnymi fieldami - do email przypisuję wartość z fieldu email, do vmail wartość z verify_email. Potem sprawdzam, czy są takie same - jeśli nie, podnoszę błąd i wyświetlam zamieszczoną w nawiasach wiadomość na stronie.  
