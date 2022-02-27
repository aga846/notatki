# Checkbox  
Checkbox to jedna z możliwych wartości atrybutu "type" tagu "input".  
Pojawia się okienko do kliknięcia "tika", "ptaszka". Wystarczy kliknąć na label, żeby okienko się kliknęło.  
  
Jeśli daję checkbox jako wartość atrybutu "type" w inpucie, to mogę do tego inputu dodać również atrybut "checked" - to sprawi, że strona otworzy się z zaznaczonym checkboxem (zaznaczenie będzie stanem domyślnym). Bez tego atrybutu strona otwiera się z niezaznaczonym checkboxem.  

```
<label for="agree">I agree to everything</label>
<input type="checkbox" name="agree_tos" id="agree" checked>
```
  
Jeśli zasubmitujemy, czyli przeniesie nas na stronę podaną w action (przy form), i checkbox będzie zaznaczony, w linku pojawi się "agree_tos=on". Jeśli checkbox nie będzie zaznaczony, w linku nie pojawi się nic (żadne name=).
  
# Radio buttons  
Radio buttons to właściwie to samo, co checkboxy, tylko pośród kilku boxów do kliknięcia można wybrać tylko jeden.  
  
Jako wartość atrybutu "type" w inpucie podajemy "radio". Ilekolwiek inputów z tą wartością byśmy nie napisali, wszystkie będą ze sobą niepołączone. W celu połączenia należy nadać im dokładnie takie samo "name".  
Każdy input będzie miał swój własny label:    
```
<label for="xs">XS:</label>
<input type="radio" name="size" id="xs">
<label for="s">S:</label>
<input type="radio" name="size" id="s">
<label for="l">L:</label>
<input type="radio" name="size" id="l">
```
W powyższej sytuacji do strony (action w \<form\>) prześle się "size=on". Żeby przesyłała się także informacja, który radio button został wybrany, należ w inpucie dodać atrybut "value", dla każdego radio buttona inny:  
```
<label for="xs">XS:</label>
<input type="radio" name="size" id="xs" value="xs">
<label for="s">S:</label>
<input type="radio" name="size" id="s" value="s">
<label for="l">L:</label>
<input type="radio" name=";" is="l" value="l">
```
  
# Select  
Dzięki select tworzy się rozwijana lista, z której możemy wybrać jedną opcję. Tworzymy jeden label dla całej listy.  
```
<label for="meal">Please select an entree</label>
  <select name="meal" id="meal">
    <option value="fish">Fish</option>
    <option value="vege">Vegetarian</option>
    <option value="steak">Steak</steak>
  </select>
```
  
Możliwa do wyboru jest tylko jedna opcja. Do strony prześle się "meal=steak".  
Można ustawić domyślną wartość poprzez dodanie atrybutu "selected" do wybranej opcji:  
```
<option value="vege" selected>Vegetarian</option>
```
