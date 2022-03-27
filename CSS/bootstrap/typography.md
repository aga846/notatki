# Typography  
Nie jest to component, ale jest samodzielną sekcją (pod "Content").  
Odnosi się do globalnych zmian.  
  
## Display - rozmiar nagłówka  
Istnieją 4 "display", które odnoszą się do nagłówków. Można zrobić normalne h1-h4, ale dodając:
```
<h1 class="display-1"Display 1</h1>
```
wyświetli się większy napis niż zwykłe h1.  
 
## Lead class - rozmiar głównego tekstu   
Sprawia, że dany tekst się wyróżnia (nieco większa i grubsza czcionka). Tę klasę dodaje się zazwyczaj do głównego tekstu na stronie.  
  
## Blockquotes - cytaty
Blockquote to jeden z elementów htmla (block element, jak div).  
Dodając klasę blockquote, jest inny styl (specjalny dla cytatów).   
   
### Naming a source (footer) - źródło/autor cytatu    
Nazywanie źródła, autora cytatu - wystarczy do tagu "footer" dodać klasę "blockquote-footer":  
```
<footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
```
Będzie dodane pod cytatem, innym kolorem i rozmiarem czcionki, z kreską "-" na początku.  
  
### Margin class (mb) - margines  
Można zmienić margines dodając "class="mb-0" - tutaj usuwam margines.  
  
### Alignment - wyrównanie  
Chcąc wycentrować tekst, ddodaję do głównej klasy "text-center" czy "text-right", np. class="blockquote text-center" albo class="display-1 text-right".  
