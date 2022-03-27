# $  
Znak dolara służy do wyboru danego elementu.  
- $("h1") -- wybór wszystkich tagów h1 jako lista obiektów; dostawanie się do konkretnego elementu na liście:  
```
listItems = $("li")
list.Items.eq(0)      # w nawiasie numer indeksu
```      
- $(".container") -- wybór klasy,  
- $("#special") -- wybór po ID.  
  
## Edytowanie właściwości CSS  
1. Przypisuję dany element do zmiennej.  
2. Do tej zmiennej stosuję css(property, value).  
```
var x = $("h1")
x.css("color", "red")
x.css("background", "blue")
```  
  
Mogę edytować wiele właściwości naraz, tworząc słownik (JS object) z własnościami jako keys i wartościami jako values:  
```
newCSS = {
  "color": "white",
  "background": "blue",
  "border": "20px solid red"
}

x.css(newCSS)
```  
  
## Dostawanie się do zawartości taga i zmienianie jej  
Obie te rzeczy robię metodą text():  
```
$("h1").text()              # wyświetli zawartość tagu h1
$("h1").text("New Text")    # zmieni zawartość na podaną w nawiasach
```
  
## Zmiana kodu HTML  
Kod HTML zmienia się metodą html():  
```
$("h1").html                    # dostanę tylko zawartość tagu
$("h1").html("<em>new</em>)     # wstawi do tagu h1 to, co w nawiasie
```
  
## Zmiana wartości atrybutu  
Za pomocą metody attr, której dostarczam nazwę atrybutu i wartość, na jaką chcę go zmienić.  
```
$("input").eq(1).attr("type", "checkbox")
```
Mogę zmienić wartość np. textboxu inputu:  
```
$("input").eq(0).val("new value")    # w nawiasie, na jaką wartość chcę zmienić
```  
  
## Dodawanie i usuwanie klasy z tagu  
Wybieram tag i stosuję metodę addClass/removeClass, którym dostarczam nazwę klasy którą chcę przypisać/usunąć temu tagowi.  
```
$("h1").addClass("turnRed")
$("h1").removeClass("turnRed")
```
Mogę też przełączać - dodawać i usuwać klasę, bez martwienia się o to, czy dany tag akurat ma czy nie ma tej klasy. Stosuję metodę toggleClass(). Jeśli element ma daną klasę - toggle usunie ją. Jeśli nie ma - toggle doda ją.  
```
$("h1").toggleClass("turnBlue")
```
