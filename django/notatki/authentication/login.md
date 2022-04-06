# Logowanie się użytkowników  
Kiedy użytkownik jest już zarejestrowany, chcemy sprawić, żeby mógł logować się na stronę.  
1. Stworzenie views do logowania + użycie wbudowanych dekoratorów do dostępu (upewnienie się, że dany view wymaga loginu załatwia się dzięki dekoratorom)  
2. Dodanie LOGIN_URL w pliku settings.py  
3. Stworzenie pliku login.html  
4. Edytowanie plików urls.py (mapowanie)  
  
  
## Ad 1 - Stworzenie views do logowania + dekoratory   
Dużo importów - bo będziemy korzystać dużo z wbudowanych funkcjonalności.  
```
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
```
Jeśli kiedykolwiek chcę, żeby view wymagał od usera, żeby był zalogowany, mogę użyć dekoratora login_required.

### View login    
Nie nazywać funkcji login (bo importuję już login wyżej z django.contrib.auth - nie chcę go nadpisać; nie nazywać też tak, jak jakakolwiek funkcja, którą zimportowałam).  
W funkcji user_login sprawdzam, czy metoda request jest równa POST. Jeśli tak, przypisuję do zmiennej username to, co wpisał użytkownik w username - do tego używać request.POST.get('username') - to get odnosi się do name, który nadałam inputowi. To samo robię z password.  
  
Teraz używam wbudowanych w Django dekoratorów. Dzięki temu całe uwierzytelnienie zrobi się za mnie (jedna linijka kodu).  
Potem sprawdzam, czy user=True (user to jest ten uwierzytelniony user z podanym username i password).  
Jeśli tak - chcę sprawdzić, czy konto jest aktywne.  
Jeśli jest - chcę zalogować użytkownika (znowu jedna wbudowana funkcja).  
I teraz, jak już jest zalogowany, chcę go gdzieś wysłać - np. na stronę jego profilu czy home page. Do tego celu używać HttpResponseRedirect. I to przekieruje go z powrotem na podaną przeze mnie stronę, np. index.  
Else - jeśli konto nie jest aktywne, użyję HttpResponse z jakimś komunikatem, np. Konto nieaktywne.  
Drugie, zewnętrzne else - jeśli user=False, printuję coś w konsoli tylko dla mojej informacji - np. że ktoś próbował się zalogować i się nie udało oraz opcjonalnie nazwę użytkownika i hasło, których próbował użyć (tych danych nie ma w naszej bazie danych), a użytkownikowi wyświetlam np. komunikat, że nieważne dane logowania.  
Trzecie, najbardziej zewnętrzne else - jeśli metoda requesta nie była POST - zwracam stronę logowania.  
```
def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
                
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login details supplied!")
    
    else:
        return render(request, 'basic_app/login.html')
```  
  
### View logout  
Wbudowanej funkcji logout dostarczam request - to automatycznie wyloguje użytkownika.  
Zwracam HttpResponseRedirect, która przekieruje na stronę główną.
Do tego jeszcze trzeba dołożyć sprawdzenie, czy user jest zalogowany - możemy pozwolić wylogować się tylko userowi, który jest zalogowany. Do tego używam dekoratora login_required, którego używam do KAŻDEGO view, który wymaga bycia zalogowanym.  
```
@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
```
  
### View special  
Przykład innej funkcji, która wyświetla komunikat tylko dla zalogowanych użytkowników:  
```
@login_required
def special(request):
    return HttpResponse("You are logged in!")
```

## Ad 2 - Dodanie LOGIN_URL w pliku settings.py  
W pliku urls.py całego projektu tworzę zmienną LOGIN_URL równą 'basic_app/user_login'.  

## Ad 3 - Stworzenie pliku login.html   
Najpierw w bazowym pliku html tworzę w navbarze kolejny link - albo LOGIN albo LOGOUT, w zależności od tego, czy użytkownik jest zalogowany czy nie. Do tego potrzebuję pewnej logiki - będę używać tagów template.  
  
Sprawdzam, czy user.is_authenticated. Jesli jest, dodaję kolejny link w navbarze. Href będzie równy przekierowaniu do strony logout (wpisanie 'logout' wskazuje na name nadany temu przekierowaniu w pliku urls.py). Jeśli nie jest - tworzę link w navbarze, który przekieruje do strony logowania.
  
  
W pliku login.html: extenduję z basic_app/base.html. Potem umieszczam body block i endblock. Między nimi robię div o klasie jumbotron (opcjonalnie) - w tym divie będzie całe logowanie się przez użytkownika (formularz zrobiony przez tagi HTML, a nie tagi templates).  
Tworzę nagłówek (h1) oraz formularz:  
Przy tagu form w atrybucie action daję odniesienie do strony user_login (zdefiniowany view w views.py).  
Tworzę inputy z labelami (na username, password i submit).  
```
{% extends 'basic_app/base.html' %}
{% block body-block %}

<div class="jumbotron">
  <h1>Please Login</h1>
  <form action="{% url 'basic_app:user_login' %}" method="post">
    {% csrf_token %}
    <label for="username">Username:</label>
    <input type="text" name="username" placeholder="Enter Username">
    
    <label for="password">Password:</label>
    <input type="password" name="password">
    
    <input type="submit" name="" value="Login">
  </form>
</div>
{% endblock %}
```  
  
## Ad 4 - Edytowanie plików urls.py (mapowanie)  
Tworzę przekierowanie do stworzonych views - dwa pierwsze w pliku urls.py projektu, trzeci w pliku urls.py aplikacji:  
```
  path('logout/', views.user_logout, name='logout'),
  path('special/', views.special, name='special'),
  
  path('user_login', views.user_login, name='user_login'),
```
