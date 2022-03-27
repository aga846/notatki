### justify content  
Dotyczy tego, jak elementy są porozkładane na głównej osi.  
Domyślna wartość attrybutu justify-content to "flex start" - elementy zaczynają się od samego początku głównej osi. Można to zmienić:  
- flex-end: elementy będą wyrównane do końca głównej osi (tj. przy flex-direction: main, przy flex-end będą szły od lewej do prawej, ale wyrównane do prawej strony),  
- center: elementy będą wyśrodkowane względem głównej osi,  
- space-between: pozostała przestrzeń (ta po zagospodarowaniu jej wszystkimi elementami) zostanie równo podzielona pomiędzy elementami, np.  
```
|x  x  x  x  x|
```

- space-around: pozostała przestrzeń zostanie podzielona równo na granicach każdego elementu, również od strony granicy głównego elementu, np.  
```
| x  x  x  x |
```
Powyżej każdy "x" ma jedną spację po lewej i prawej, a więc między samymi x-ami są po 2 spacje.  

- space-evenly: to samo co wyżej, tylko między samym elementem a granicą głównego elementu jest taka sama odległość, co między elementami (w powyższym przykładzie - 2 spacje).  
