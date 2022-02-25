# Jak połączyć plik CSS z plikiem HTML?  
Są 3 sposoby:  
  
## Kod CSS w osobnym pliku  
To najlepszy sposób. Piszemy kod CSS opisujący kod w HTMLu w osobnym pliku i potem łączymy go z plikiem HTML:  
W <head> w pliku HTML piszemy:  
```
<link rel="stylesheet" href="app.css">
```
"app.css" to plik, w którym zawarty jest kod CSS. Jeśli jest w innym folderze, niż plik HTML, należy to napisać poprzez "folder/app.css".  
  
## Kod CSS w <head> HTMLa  
Kod CSS zawarty jest w <head> w pliku HTML.  
  
## Kod CSS od razu opisuje elementy HTMLa  
Najgorszy sposób. Od razu po napisaniu jakiegoś elementu opisujemy go, np.:  
```
<button style="background-color: palegreen">I AM BUTTON</button>
```
Bez sensu pisać w ten sposób, bo trzeba się powtarzać wiele razy, w jeśli chcę zmienić jakąś cechę wszystkich np. buttonów czy h2, muszę zmieniać kod wielokrotnie.
