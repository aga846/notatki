# Co to są media queries?  
Media queries dotyczą zmian, które dokonują się na stronie w zależności od wielkości okna przeglądarki. Dotyczy to zarówno samego zmniejszania/zwiększania okna na komputerze, jak i wyświetlania strony na różnych urządzeniach (komputerach, telefonach, tabletach).  
  
Składnia:  
\@media (warunek) {opis}  
  
W warunku można dać np.  
### width
"width 800px" - oznacza to, że opis (np. ustawienie koloru h1 na fioletowy) będzie działał tylko wtedy, gdy szerokość okna będzie 800px. Okna, tzn. tego, co jest aktualnie widoczne.   
Bardziej popularne jest używanie min-width i max-width (min-width = od ustawionej szerokości wyświetlaj dany opis; max-width = do ustawionej wielkości wyświetlaj dany opis).  
  
Można mieszać ze sobą min i max, np.  
```
@media (min-width: 600px) and (max-width: 800px){
  h1 {color: blue}
}
```
  
Można również dodawać kolejne warunki, np. od 500px kolor czerwony, od 700px kolor żółty, ale wtedy:  
- albo trzeba ustawić kolor domyślny i potem dodawać od mniejszej do większej wartości,  
- albo trzeba wstawiać \@media od większej do mniejszej wartości.  
  
  
### orientation  
Odnosi się do orientacji pionowej lub poziomej (landscape).  
  
  
W dokumentacji jest opisanych wiele różnych warunków.
