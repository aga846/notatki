## align-content  
Odnosi się do ustawienia elementów względem drugiej (nie głównej) osi. Ma zastosowanie tylko, gdy mamy wartość "wrap" lub "wrap-reverse" przy atrybucie flex-wrap.  
  
Np. jeśli mam:  
```
display: flex;
flex-direction: column;    # oś główna: pionowa od góry do dołu
justify-content: center;   # ustawienie wyśrodkowania względem głównej osi (czyli wyśrodkowanie w pionie)
align-items: flex-end      # wyjustowanie elementów w osi poziomej do prawej strony
flex-wrap: wrap            # sprawienie, że elementy się "zawijają" wg głównej osi - robią się kolumny
```
to align-content ustawione na flex-start sprawi, że kolumny będą ustawiały się od lewej strony.  
  
Align-content może mieć też wartości:  
- space-between;  
- space-around;
- flex-end.  
  
## align-self  
Tą własność dajemy poszczególnym elementom, a nie całemu elementowi-rodzicowi.  
Ustawia to dany element w jakimś ustawieniu względem drugiej osi (nie głównej). Dodaje się to w opisie samego elementu, np.  
```
dev:nth-of-type(3) {align-self: center;}
``` 
Tutaj tylko pojedynczy element (trzeci) będzie wycentrowany względem osi y (ponieważ główna jest x - flex-direction: row).  
Align-self może mieć też wartości:  
- flex-start;  
- flex-end.  
Ale jeśli mam:  
```
display: flex;
flex-direction: column;
justify-content: center;
align-items: flex-end;
flex-wrap: wrap
```
to align-self: flex-start nie przesunie ostatniego elementu do samego początku osi x (czyli do krawędzi z lewej strony), tylko do środkowego elementu - tj. będzie się poruszać tylko wewnątrz "swojej" przestrzeni.
