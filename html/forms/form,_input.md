# Formularze  
Chodzi o wypełnianie jakiegoś formularza, jak np. logowanie się gdzieś na stronę, wpisywanie danych do dostawy, wyszukiwanie czegoś na stronie.  
  
## \<form\> \</form\>  
Formularz tworzy się przy użyciu \<form\>.  
  
### action  
Action to atrybut form, w którym wpisuje się adres URL, do którego dany formularz na być wysłany. To taki "adres dostawy" naszego formularza (danych wpisanych w formularzu).    
```
<form action="/search">
```  
W powyższym przykładzie formularz jest wysyłany do linka danej strony z rozszerzeniem go o /search.  
Kiedy wpisze się coś w formularzu, link rozszerzy się również o wpisany input:  
```
/search/?q=tocowpisalam
```
  
### method  
Method to atrybut form, w którym wpisuje się "get" lub "post" (w zależności od tego, jakiego typu http request to jest).  
  
  
  
## \<input\>  
Tag input nie ma tagu zamknięcia. Tworzy okienko, w którym można coś wpisać.  
  
### type  
Input przyjmuje atrybut type. Type może mieć różne wartości, np.:    
- text (domyślny),  
- password (pojawiają się czarne kółka zamiast liter - jak przy wpisywaniu hasła),  
- color (można wybrać kolor z pojawiającej się palety),  
- month (wybór miesiąca),  
- number (wybór liczby); można dać też atrybut min, max i step (tak jak w range),  
- time (wybór godziny),  
- checkbox (okienko do zaznaczenia) -\> zobacz plik "checkboxes,_radio_buttons.md",  
- range (wartość do wyboru z danego zakresu) -\> zobacz plik "range,_text_area".    
  
### placeholder  
Input przyjmuje atrybut placeholder. W nim wpisuje się to, co w danym okienku ma być napisane, dopóki nie wpiszemy własnej wartości (np. username):  
```
<input type="text" placeholder="username">
```  
Zamiast placeholder można dać atrybut "value", wtedy, jeśli użytkownik nie wpisze nic w danym okienku, to wartość atrybutu "value" będzie przesłana.  
Nie działa dla wszystkich typów. Działa np. dla password, number.  
  
### name  
Wartość atrybutu name to nazwa, która będzie używana przy wysyłaniu danych z formularza. To np. to "q" z przykładu z action. Jeśli podam w inpucie atrybut name="blablabla", a w formularzu w tym inpucie wpiszę "koty", to link będzie "/search/?blablabla=koty".  
```
<input type="text" placeholder="name" name="myname">
```
Atrybuty "name" różnych inputów w tym samym formularzu będą miały następujące odzwierciedlenie w linku:  
```
/search/?username=aga&passwword=1234&num=78
```
^ są połączone znakiem "&".
