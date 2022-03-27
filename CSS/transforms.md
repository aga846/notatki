# Czym są transforms?  
Transforms odnoszą się do różnych "dekoracji", zmian elementów - obracanie, skalowanie, przesuwanie, przekrzywianie. Wszystkie te transformacje odnoszą się do całego elementu, również do elementów w nim zawartych (np. jeśli obracam cały div, to button zamieszczony w środku niego również się obróci).    
  
### rotate  
Obrót elementu. Podawany w różnych jednostkach - degrees (0-360), radients, gradients, turns (0-1). Wartość podaje się inaczej niż w przypadku innych atrybutów - używamy nawiasów:  
```
transform: rotate(45deg);
```
Domyślnie obraca się względem środka. Można ustawić inny początek (np. obracanie względem prawego dolnego wierzchołka) poprzez użycie atrybutu "transform-origin":  
```
transform-origin: bottom right;
transform: rotate(45deg)
```  
  
Istnieje również możliwość obracania względem różnych osi, np. x, y - wszystko jest w dokumentacji (np. rotate3d, rotateX).  
  
### scale  
Skalowanie. Zmniejszanie lub zwiększanie elementu:  
```
transform: scale(0.5);
```
Można podawać dwie wartości - jedna odnosi się do szerokości, druga do wysokości (np. "scale(2, 1)" spowoduje dwukrotne powiększenie w poziomie, przy zachowanym takim samym jak pierwotnie pionie).  
Istnieje też coś takiego jak scaleX, scaleY - skalowanie tylko w szerokości lub wysokości (wg osi x lub y).  
  
### translate  
Służy do przesuwania elementów. Można podawać w różnych jednostkach (px, %, cm).  
TranslateX przesunie w poziomie, translateY w pionie.  
```
transform: translateX(200px)
```
Można też podać dwie wartości w "translate()" - będą się odnosiły do obu osi.  
Przesuwanie w lewo lub do góry - można używać negatywnych wartości.  
  
### scew  
Przekrzywia element - nie obraca tylko zostawia poziome brzegi równe, przekrzywia tylko boczne. Można podawać w różnych jednostkach (np. deg).  
Jeśli podamy dwie wartości, przekrzywia również poziome brzegi.  
    
## Łączenie zmian  
Można łączyć różne zmiany ze sobą - np. obrócić element i zmienić jego wielkość:  
``` transform: rotate(90deg) scale(1.2)
```
