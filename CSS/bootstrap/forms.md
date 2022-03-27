## form-control  
To klasa, którą zamieszcza się w inpucie. Robi input bardziej przyjaznym dla oka.  
Jeśli mam select, to umieszczam w select.  
  
## form-group  
Służy do grupowania label i inputu. Daje się ją w tagu (np. divie), w którym będzie zamieszczony label i input.  
  
## form-check  
Dla checkboxów. Umieszcza się w tagu (np. w divie), w którym będzie zamieszczony label i input.  
Zmiana wyglądu checkboxów nie jest łatwa.  
W input i label umieszcza się odpowiednio klasy "form-check-input" i "form-check-label".  
  
Zwykły, domyślny checkbox (samo okienko, które się zaznacza/odznacza) wygląda dosyć słabo; ale istnieje custom checkbox, który wygląda lepiej. Żeby go użyć, należy w klasie tagu, w którym będzie zamieszczony checkbox, dać "custom-control custom-checkbox", a w inpucie i labelu odpowiedznio klasy "custom-control-input" i "custom-control-label".  
```
<div class="custom-control custom-checkbox">
  <input type="checkbox" class="custom-control-input" id="customCheck1">
  <label class="custom-control-label" for="customCheck1">Check this custom checkbox</label>
</div>
```
  
Zamiast checkboxów można użyć switches - więcej o tym w dokumentacji.  
  
## form-row  
Można dać kolejne inputy i labele jako "col" w "row", ale można zamiast tego dać "form-row" - wyjdzie na to samo, ale będą inne odległości między okienkami - specjalne dla formularza.  
  
## small  
Mała informacja, którą najczęściej umieszcza się pod okienkiem inputu, np. "We'll never share your email with anyone else.".    
```
<small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
```
  
## multiple select  
Umożliwia wybór wielu opcji, w odróżnieniu od zwykłego select.  
```
<select multiple class="form-control" id="exampleFormControlSelect2">
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
  <option>5</option>
</select>
```  
  
