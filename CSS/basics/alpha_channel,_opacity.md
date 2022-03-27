# Alpha channel  
Alpha channel odnosi się do przezroczystości. Mogę dać kolor tła, potem nadać jemu albo jego części inny kolor i zaznaczyć przezroczystość. Atrybut "alpha" ma wartości od 0 do 1. 0 oznacza zupełnie nieprzezroczysty, 1 oznacza zupełnie przezroczysty. Oznacza się do przy podawaniu koloru za pomocą rgb().  
W poniższym przykładzie dałam temu divovi id "rgba" (dlatego do niego odnosi się #rgba):    
  
```
div {width: 500px;
     height: 500px;
     background-color: magenta;}
     
#rgba {width: 50%;
       height: 50%;
       background-color: rgba(255, 255, 255, 0.7)}
```
Powyższe odnosi się tylko do koloru tła, kolor tekstu jest niezmieniony.  
Można oznaczać również w systemie hexadecimal - 00 jako zupełna nieprzezroczystość, FF jako zupełna przezroczystość.
  
  
# Opacity  
Opacity to przezroczystość. Również ma wartości od 0 do 1. Opacity odnosi się do całego elementu, nie tylko do tła.  
  
```
div {width: 500px;
     height: 500px;
     background-color: magenta;}
     
#opacity {width: 50%;
       height: 50%;
       background-color: yellow;
       opacity: 0.3;}
```
