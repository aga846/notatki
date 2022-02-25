# Range  
Range to jedna z możliwych wartości atrybutu "type" tagu "input".  
Pojawia się "suwak", który można ustawić na dowolną wartość z podanego zakresu.  
  
```
<label for="cheese">Amout on Cheese</label>
<input type="range" id="cheese">
```

## Wartość minimalna i maksymalna  
Można ustawić minimalną i maksymalną wartość:  
```
<label for="cheese">Amout on Cheese</label>
<input type="range" id="cheese" min="1" max="10" name="cheese_level">
```
Do strony prześle się "cheese_level=8".  
  
## Step  
Można ustawić, co ile wartości możliwy jest wybór (np. od 1 do 100, co 2 - tj. 1, 3, 5 ... 99):  
```
<label for="cheese">Amout on Cheese</label>
<input type="range" id="cheese" min="1" max="10" step="2" name="cheese_level">
``` 
  
## Value  
Można dodać domyślną, startową wartość:  
```
<label for="cheese">Amout on Cheese</label>
<input type="range" id="cheese" min="1" max="10" step="2" value="5" name="cheese_level">
```
  
  
# Text area  
Pojawia się okienko do wpisania tekstu. To nie to samo, co input (tj. nie wpisuje się tego w inpucie).  
  
```
<label for ="requests"Any special Requests?</label>
<textarea id="requests"></textarea>
```
  
Można kontrolować wyświetlaną na początku ilość rzędów, tj. wysokość okienka (domyślnie: 2 rzędy) - jako atrybut textarea daje się "rows". To wpływa tylko na początkowy wygląd (jak wysokie będzie okienko do pisania), ale linijek wciąż można dać, ile się chce.  
Można też kontrolować szerokość: "cols"  
  
Można ustawić name i placeholder.
