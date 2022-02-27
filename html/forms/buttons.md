Button to przycisk. Buttony tworzy się wewnątrz formularza - inaczej nie robią nic. Wszystkie notatki poniżej dotyczą buttonów wewnątrz formularza.  
  
## \<button\> \</button\>  
Tworzy button.    
```
<button>Submit</button>
```
Po klinkięciu danego button, domyślnie przekierowuje nas do strony, którą podaliśmy w atrybucie action tagu form (przy tworzeniu formularza), przesyłając tam dane, które podaliśmy w formularzu. Ten sam efekt uzyskamy, klikając enter.  
  
## type jako atrybut button 
Atrybut type wskazuje na to, jakiego typu ma być dany button. Wartości typu:  
- "button" - zamieniamy button w formularzu (submitujący formularz) na zwykły button (nierobiący nic),  
- "submit" - domyślna wartość type - submituje formularz,  
Podanie wartości button nie jest tak popularne. Przy JavaScript bardziej.  
  
## Dodawanie submitującego button za pomocą input  
Mało używane podejście.  
W atrybucie "type" inputu mogę podać wartość "submit" i wtedy tworzy się przycisk "Submit". Jeśli chcę zmienić jego nazwę, należy podać kolejny atrybut, "value", i w nim napisać, co ma być napisane w buttonie:  
```
<input type="submit" value="Click me!">
```
