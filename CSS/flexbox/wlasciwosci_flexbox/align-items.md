## align-items  
Align odnosi się do drugiej osi (nie głównej) - tj. jeśli główna oś to pozioma, to "align-items" będzie odnosiło się do pionowej, która jest domyślnie od góry do dołu. Domyślna wartość to flex-start.  
Mogę zmienić align-items na:  
- flex-end: elementy będą w pionie ustawione na dole (nie domyślnie na górze),  
- center: elementy będą w pionie ustawione pośrodku,  
- baseline: elementy będą ustawione zgodnie z napisem w nich zawartym, tj. jeśli mam 5 elementów, z których każdy ma jakiś napis, a 4 element ma większą czcionkę niż reszta, to elementy będą ustawione od góry, przy czym tylko 4 element będzie dotykał górnej granicy, a pozostałe elementy będą wyrównane z tym 4 elementem (będą niżej, tak, żeby cały napis był w równej linii). Baseline = na podstawie hipotetycznej linii podkreślającej całe słowo/słowa we wszystki elementach (divach) w danym section.  
