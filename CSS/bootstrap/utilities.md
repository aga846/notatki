# Utilities  
Jest samodzielną dużą sekcją - na równi z "content", "forms" itd.  
W utilities są takie własności, jak tło, granice, kolory, flex, opacity, position itd.  
Nie są to samodzielne elementy - dodaje się je do czegoś.  
  
  
## Color  
### Tekst  
Daje się klasę: "text-primary" (lub inna nazwa koloru):  
```
<h1 class="display-1 text-center text-primary">
```
  
### Tło  
Daje się klasę: "bg-primary" (lub inna nazwa koloru).  
  
  
## Border  
Daje się klasę:  
- "border",  
- "border-top",  
- "border-right",  
- "border-bottom",  
- "border-left".  
  
### Usuwanie granic  
Do powyższych klas dodaje się "-0", np. "class="border-top-0".  
  
### Kolor granicy  
Dodaje się klasę "border-primary", np. "class=border border-primary".  
  
### Border-radius  
Daje się klasę np. "rounded-circle", "rounded-bottom".  
Można zmienić zaokrąglenia granic (w "Sizes").  
  
  
## Shadows  
Można dodać cień. Nie mamy za dużej kontroli nad jego rozmiarem, są do wyboru tylko:  
- "shadow-none",  
- "shadow-sm",  
- "shadow",  
- "shadow-lg".  
  
  
## Spacing - margin & padding  
"m" odpowiada za margin, "p" za padding.  
Potem podaje się strony, do których dodajemy margin lub padding - t (top), b (bottom), l (left), r (right), x (left i right), y (top i bottom), blank (wszystkie 4 strony).  
Następnie podaje się rozmiar margin lub padding. Jest 7 opcji: od 0 do 5 (0 to żaden margin i padding, 5 to najwięcej) oraz auto.  
Przykłady:  
```
class="btn btn-primary p-0"       # w ogóle bez padding
class="btn btn-primary p-0 pt-5"  # padding rozmiar 5 na górze
class="btn btn-primary px-4"      # padding rozmiar 4 po bokach

class="mt-2"
class="my-5"
```
  
Można dodać breakpoint - jeszcze przed podaniem rozmiaru:  
```
class="btn btn-primary p-0 p-sm-1 p-md-2 pt-lg-3 p-xl-5"
```
  
  
## Display property  
Można zmieniać na block/inline/flex, ale można też np. sprawić, że dany element będzie ukryty na danym breakpoincie:  
```
.d-none .d-sm-block         # będzie się pokazywało dopiero od rozmiaru small
```



 
