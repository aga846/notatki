# Co to są events  
Zazwyczaj nie chcemy zmieniać na stronie całego elementu, tylko np. dostać się do atrybutu hover (zmienić tylko to, co będzie się działo przy najechaniu myszką).  
Żeby to osiągnąć, trzeba dodać "Event Listener". JS będzie nasłuchiwał, kiedy event się pojawi i jak się pojawi, wtedy egzekwował funkcję.  
  
Należy do zmiennej (do której przypisany jest element, który wyciągnęliśmy z DOM poprzez metodę np. querySelector) zastosować atrybut "addEventListener", który przyjmuje argumenty event oraz func (nasza funkcja lub wbudowana).  
```
var head = document.querySelector("h1");
head.addEventListener("click", changeColor);
```
Ważne - nazwa funkcji nie jest w cudzysłowiu.  
  
Przykładowe events:  
- click - event nazywa się "click",  
- hover - event nazywa się "mouseover"; do przestania najeżdżania: "mouseout",  
- double click, - event nazywa się "dblclick",  
- drag.  
Jest ogromna ilość events - w dokumentacji.  
  
```
headOne.addEventListener("mouseover", function() {
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = "red";
  })
```
W powyższym przykładzie po najechaniu, napis zmieni się na zawsze (aż do odświeżenia strony). Żeby wracał do poprzedniego stanu po przestaniu najeżdżania na niego, trzeba dodać kolejny eventListener, z eventem "mouseout":  
```
headOne.addEventListener("mouseout", function() {
  headOne.textContent = "HOVER OVER ME!";
  headOne.style.color = "black";
  })
