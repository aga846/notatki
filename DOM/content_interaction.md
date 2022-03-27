# Interakcja z treścią strony  
  
## Zmiana tekstu - treści i właściwości 
Do zmiany treści: wybieram element i przypisuję go do zmiennej.  
Potem do atrybutu textContent tego elementu przypisuję wybraną wartość (tekst):  
```
var p = document.querySelector("p")
p.textContent = "new text"
``` 
  
Do zmiany właściwości: potrzebuję atrybutu innerHTML. Do atrybutu innerHTML wybranego elementu przypisuję kod HTML:  
```
p.innerHTML = "<strong>I'm bold</strong>";
```  
  
## Zmmiana atrybtutu  
Potrzebne są metody:  
- getAttribute() - dostanie się do atrybutu danego elementu,  
- setAttribute() - zmiana atrybutu. Przyjmuje dwa argumenty - nazwa atrybutu, którego wartość chcemy zmienić oraz wartość, na którą chcemy zmienić.  
```
var special = document.querySelector("#special")
special1 = special.querySelector("a")
specialA.getAttribute("href")          # adres URL - wartość atrybutu href
specialA.setAttribute("href", "https://www.amazon.com")   
```
