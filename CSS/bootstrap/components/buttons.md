## Klasa główna  
Buttons zawsze mają klasę "btn".  
  
## Rodzaje "podklas"  
Drugi rodzaj klasy, po "btn", tj. "btn-primary", "btn-secondary", "btn-success", itd. odnosi się do domyślnego koloru w bootstrapie. Oznacza to, że klasy innych elementów, jak np. alerts, również odnoszą się do tych nazw, np. "alert-primary". Ale mimo to, że są domyślne, to można zmienić te kolory.  
Te nazwy po prostu odnoszą się do domyślnych stanów na stronie:  
- primary - jako coś głównego, pierwszego,  
- secondary - coś pobocznego,  
- success - coś zakończone sukcesem,  
- danger - coś niebezpiecznego,  
- warning - ostrzeżenie,  
- info - informacje,  
- light,  
- dark,  
- link - nie wygląda jak button, ale jest buttonem.  
To jest po to, żeby sobie uprościć, bo każda strona prawdopodobnie będzie potrzebowała tego typu rodzajów klas. Ale nie oznacza to, że na wszystkich stronach primary to zawsze będzie niebieski, a warning żółty - można to sobie zmienić (i wtedy ustawia się to dla wszystkich elementów, nie tylko dla buttonów - to jakby wzór, szablon dla danej strony).  
    
## Zamieszczanie danego button na stronie  
Ze strony getbootstrap.com kopiujemy dany button (razem z typem i klasą) i wklejamy do pliku html.  
Można również użyć typu i klasy button na innych elementach (tagach), np. a, input. Wtedy one będą wyglądały jak buttony.  
  
## Outline buttons  
Mają inną podklasę: "btn-outline-primary" (lub inny kolor/styl).  
  
## Sizes  
Dodaje się kolejną podklasę - lg lub sm:  
```
<button type="button" class="btn btn-primary btn-sm">Small Button></button>
```
  
## Block buttons  
Button, który jest szeroki: dodaje się kolejną podklasę "btn-block".  
  
## Inne rodzaje  
- active state,  
- disabled state - dodaje się po prostu "disabled" (bez podklasy).
