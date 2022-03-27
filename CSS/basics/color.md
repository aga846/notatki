# color  
Są różne możliwości przedstawienia koloru (np. nazwa, rgb, hsl, #00ff00 - hexadecimal, w każdym razie za pomocą tekstu).  
"color" odnosi się do koloru tekstu (nie tła).  
Istnieje 140 kolorów, które mają swoją nazwę. Reszta kolorów musi być wyrażana w inny sposób, np. RGB lub hexadecimal:  
  
## RGB  
Kolor można wyrazić w systemie RGB:  
```
color: rgb(255, 0 255)
```
Natężenie każdego z kolorów to maksymalnie 255. Wszystkie trzy kolory w natężęniu 255 dają kolor biały, natomiast wszystkie w natężeniu 0 dają kolor czarny. Można wybierać kolor z palety kolorów (np. w google "color picker") i spisać natężenie każdego z kolorów.  
  
## Hexadecimal  
Kolor można wyrazić też w systemie szesnastkowym, który zawiera znaki: 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f. Największy znak to f.  
W tym systemie kolor jest wyrażony przez  # oraz 3 pary znaków, np. żółty to:  
```
#ffff00
```
(pierwsza para ff odpowiada za "red", kolejna para ff odpowiada za "green", a ostatnia para 00 odpowiada za "blue")  
Każda para odpowiada więc za natężenie koloru czerwonego, zielonego i niebieskiego. Innymi słowy, każda para to wyrażenie w systemie szesnastkowym liczby od 0 do 255 w systemie RGB.  
Jeśli mamy pary kolorów, w których jest ten sam symbol, można skrócić te pary, np. "#000000" można skrócić do "#000".  
    
# background-color  
Kolor tła można przedstawiać na takie same sposoby, jak kolor tekstu. Przykład opisania koloru czcionki i koloru tła buttona:  
```
button {
        color: teal;
        background-color: plum;
}
```  
  
Background-color to nie to samo, co background. Background może zrobić dużo więcej (np. ustawić obrazek w tle).
