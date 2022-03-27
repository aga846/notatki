# Absolute units  
- px,  
- pt,  
- cm,  
- in,  
- mm.
  
  
# Relative units  
- em,  
- rem,  
- vh,  
- vw,  
- %.  
  
## % percentages  
Mogą odnosić się do:  
  
### elementu-rodzica  
Np. mam <section>, który ustawiam na określoną wysokość i szerokość. Wewnątrz tego <section> umieszczam <div> i ustawiam go na 50% wysokości i 50% szerokości <section>:  
```
section {background-color: blue;
         width: 800px;
         height: 800px;}

div {background-color: pink;
     width: 70%;
     height: 20%}
```
  
### samego elementu  
Np. ustawiam czcionkę danego <h1> na ileś px i ustawiam wysokość na jakiś %. Ten procent będzie odnosił się do czcionki:  
```
h1 {font-size: 40px;
    border: 1px solid black;
    line-height: 200%}
```  
  
Przy % może przydać się opcja calc() - jesli np. chcę umieścić na stronie obok siebie 3 obrazki, których szerokość ustawiłam na 30% (w tym przypadku to 30% elementu-rodzica, tj. body) i chcę, żeby marginesy między nimi oraz na zewnątrz lewego i prawego obrazka były równe, mogę napisać:  
```
img {width: 30%;
     margin calc(10%/6);}
```
Dzięki temu nie muszę liczyć.  
  
  
## em  
### Czcionka  
Ems w przypadku czcionki odnoszą się do czcionki elementu-rodzica, tj. jeśli mam <article> i w nim <h1> i dla <article> ustawiam czcionkę o wielkości 40px, to ustawiając dla <h1> czcionkę o wielkości 2em, będzie ona 2 razy większa niż w <article>, czyli będzie miała w tym przypadku 80px. Czcionka w <h1> zmienia się w zależności od zmian czcionki <article>.    
```
article {font-size: 30px}
h1 {font-size: 2em}
```  
Jeśli żadnemu elementowi nie ustawię rozmiaru czcionki, to domyślnym rozmiarem jest 16px (tj. 1em = 16px).  
  
### Padding, margin, border-radius   
Tutaj ems będą odnosiły się do czcionki danego elementu, tj. jeśli w <h2> mam ustawioną czcionkę na 40px (która może być wyrażona za pomocą ems - tak jak w przypadku na górze), to ustawiając margin-left na 1em, będzie on miał 40px.
  
  
## rem - root em  
Rozwiązują problem bardzo szybkiego zwiększania się lub zmniejszania się czcionek w elementach zagnieżdżonych (problem z czcionkami list: listy zagnieżdżonej w liście zagnieżdżonej w liście, zamieszczonych w artykule; czcionki odnoszą się do czcionki artykułu, do czcionki listy, do czcionki listy - poprzez ems).  
Używając rems, jako źródłowy rozmiar czcionki jest rozmiar czcionki całego dokumentu (podaje się na samym początku przy <html lang> lub sam się ustawia jak nic nie napiszemy). Dzięki temu ustawiając czcionkę na coraz bardziej zagnieżdżonych elementach, nie odnoszę się do czcionki elementu-rodzica, tylko przy każdym z tych elementów odnoszę się do jednej czcionki, tj. 0.5rem w <div> będzie takie samo, jak 0.5rem zagnieżdzonego w niej <li>.
