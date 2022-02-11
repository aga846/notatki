# Co robi funkcja colored  
Funkcja colored zmienia podany tekst tak, że ma on określony przez nas kolor, tło oraz atrybuty (np. mruga).  
Dostępne kolory, kolory tła oraz atrybuty można znaleźć w dokumentacji lub poprzez help().  

```
import termcolor

x = termcolor.colored("Damian", color="yellow", on_color="on_cyan", attrs=["blink"])
print(x)       # słowo "Damian" napisane na żółto na cyjanowym tle, murgające
```
