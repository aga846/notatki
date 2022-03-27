# Atrybuty DOM  
Wpisujemy w konsoli.  
- document.URL - zwróci bieżący URL strony,  
- document.body - zwróci całe body,  
- document.head - wszystko, co jest w head,  
- document.links - wszystie linki, jakie są na stronie.  
  
## Metody dostania się do elementów DOM  
Wpisujemy w konsoli.  
- document.getElementById(),  
- document.getElementsByClassName() - zwraca listę,  
- document.getElementsByTagName(),  
- document.querySelector() - pierwszy obiekt, który pasuje do podanego selektora CSS,  
- document.querySelectorAll() - wszystkie obiekty pasujące do podanego selektora CSS; jako lista.  
  
W nawiasach wpisujemy w cudzysłowiu nazwę ID/klasy/tagu.  
W metodach query dodatkowo przy ID również "#", przy klasie "." - jak przy selektorach CSS.  
  
Można wielokrotnie stosować powyższe metody:  
```
var special = document.querySelector("#special")
special1 = special.querySelector("a")
```
Powyższe special1 to będzie tag a znajdujący się wewnątrz elementu z ID "special".  
  
## Zmiany elementów - na przykładzie zmiany koloru  
1. Wybieramy element i przypisujemy go do zmiennej.  
```
myheader = document.querySelector("h1")
```
2. Wybieramy atrybut elementu (po wpisaniu "myheader" pojawia się rozwijana lista z atrybutami tego elementu) i właściwość tego atrybutu, np.  
```
myheader.style.color
```
"style" odnosi się do tego, że chcemy zmienić styl elementu (może być też np. textContent), a "color" to że konkretnie kolor (może być też np. border, align, font, margin - wszystko, co było w CSS).  
Do tego atrybutu i właściwości przypisujemy wybraną wartość:
```
myheader.style.color = "red";
```
