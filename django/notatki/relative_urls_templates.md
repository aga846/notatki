# O co chodzi  
Chodzi o to, żeby stworzyć template, którego będę mogła używać w wielu "rozszerzeniach" swojej strony głównej, taki bazowy kod HTML, który będzie podstawą dla kolejnych zakładek - nie tylko strony głównej, ale też np. help page, users page, sing up page itp.  
Główne użycie - przy projekcie, w którym znajduje się wiele aplikacji.  
Najpierw trzeba dodać linki do rozszerzeń strony (dodawanie linków do strony głównej czy do strony admin).  
  
## Dodawanie linków do rozszerzeń strony  
Dotychczas używałam tagów \<a\>, w którym zamieszczałam ścieżkę hardcoded do pliku. To zła praktyka, jeśli chcę, żeby mój projekt Django działał na każdym systemie - potrzebuję ścieżek relatywnych (relative paths).  
  
Dzięki relative urls w template'ach mogę tworzyć ścieżki relatywne. Są różne metody na osiągnięcie tego.  
Zamiast wklejania do tagu \<a\> hrefu "first_app/thankyou", mogę użyć tagów template:  
### Odniesienie się do "name" w pliku urls.py  
```
<a href="{% url 'thanku' %}">Thanks</a>
```
name="thanku" jest w pliku urls.py.   
  
### Odniesienie się bezpośrednio do view (nie w Django 4.0):  
```
<a href="{% url 'first_app.views.thankyou' %}">Thanks</a>
``` 
Kliknięcie na "Thanks" zabierze nas do tego konkretnego view.  
  
### Zrobienie wszystkiego w pliku urls.py - najlepsza metoda  
Dodaję w tym pliku zmienną "app_name" i ustawiam ją na string, który jest nazwą mojej aplikacji.  
```
app_name = 'first_app'
```
następnie wewnątrz tagu \<a\> w pliku HTML piszę 'nazwa aplikacji: nazwa view'.
```
<a href="{% url 'first_app:thankyou' %}">Thanks</a>
```  
  
Żeby zawrzeć linka do strony admin, trzeba użyć zmiennej app_name, która we wbudowanej aplikacji admin jest przypisana do słowa "admin":  
```
<a href="{% url 'admin:index' %}">Link to admin page</a>
```
  
Żeby zawrzeć linka do strony głównej, trzeba po prostu wpisać "index":  
```
<a href="{% url 'index' %}">LINK TO INDEX</a>
```
  
## Template inheritance (aka template extending)  
Pozwala na kreowanie bazowego template'u. Np. chcę mieć navbar na każdej podstronie, nie tylko na stronie głównej. Dzięki template inheritance mogę go napisać tylko raz i w kolejnych rozszerzeniach strony używać tego navbaru.  
Ważne - dziedziczenie template'ów nie musi się ograniczać do jednego bazowego pliku!  
  
Kroki do dziedziczenia:  
1. Znaleźć powtarzające się części projektu  
2. Stworzyć bazowy template  
3. Ustawić konkretne tagi w bazowym templacie  
4. Wstawiać te tagi gdzie tylko chcę  
  
### Tagi  
Plik bazowy:    
```
<linki do JS, CSS, Bootstrapa>
<powtarzające się części projektu, które będę chciała dziedziczyć w innych plikach> 
  <body>
    {% block body_block %}
    {% endblock %}
  </body>
```
Wszystko, co jest pomiędzy "block body_block" oraz "endblock", będzie zawarte tylko w pliku bazowym.  
  
Plik dziedziczący:  
```
<!DOCTYPE html>
{% extends "basic_app/base.html" %}   <- zawarcie pliku bazowego
{% block body_block %}
<kod HTML właściwy tylko dla tego konkretnego pliku>
{% endblock %}
```  
W pliku dziedziczącym z boilerplate'a muszę wpisać tylko DOCTYPE - nie potrzebuję tagów html, head, body, linków do CSS itd. - jeśli to wszystko dziedziczę w pliku bazowego.  
