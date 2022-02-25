# Content box  
Zawiera treść. Ma wysokość (height) i szerokość (width). Można je zmieniać:  
```
h1 {height: 200px;
    width: 100px;
    background-color: blue}
```
Element h1, który został zmieniony, wciąż rozciąga się na całą linię, ale sama zawartość tego elementu się zmieniła, dlatego tło będzie niebieskie jedynie w podanych wysokości i szerokości.  
Te własności można podawać w różnych jednostkach.  
  
# Border  
Do border można zastosować następujące właściwości:  
- border-width (szerokość granicy, podaje się np. w px),  
- border-color (kolor granicy),  
- border-style (styl, np. solid, dotted, inset, dashed; można podawać inną granicę dla każdej strony, np. dashed solid oznacza górę i dół dashed, prawo i lewo solid. Można też dać 4 własności, w kolejności góra, prawo, dół, lewo),  
- box-sizing (np. border-box -> będzie oznaczało, że szerokość i wysokość całego elementu nie zwiększy się o szerokość granicy. Jeśli tego nie ustawimy, element będzie wyższy i szerszy o dwukrotną szerokość granicy,  
- odnoszenie się do konkretnej strony granicy: np. border-left-width.  
  
Można odnieść się do wszystkich trzech właściwości naraz, w kolejności: width, style, color:  
```
border: medium dashed green
```

## Border-radius  
Zaokrąglenie krawędzi granicy. Podaje się w px, %. Można dzięki temu robić kółka.  
```
border-radius: 50%
```
Można też ustawiać konkretne rogi indywidualnie:  
```
border-top-left-radius: 300px
```
