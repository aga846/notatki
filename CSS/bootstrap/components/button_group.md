# Button group  
Grupuje wiele buttonów razem.  
Np. grupa radio buttons.  
W elemencie, w którym znajdują się buttony, które chcę zgrupować, dodaje się klasę "btn-group":  
```
<div class="btn-group">
  <button type="button" class="btn btn-secondary">Left</button>
  <button type="button" class="btn btn-secondary">Middle</button>
  <button type="button" class="btn btn-secondary">Right</button>
</div>
```
Teraz buttony są w grupie - nie ma marginesów między nimi; radius sąsiadujących buttonów się zmienił.  
  
Jeśli mam buttony, spośród których ma być wybrany tylko jeden, czy te buttony stanową różne opcje - można dać podklasę role="group".  
  
Można zmienić rozmiar - dodając podklasę "btn-group-lg" lub "btn-group-sm".
  
