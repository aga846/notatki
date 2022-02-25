## Wyrównanie tekstu  
Chodzi o wyrównanie do lewej/do środka/do prawej wewnątrz danego elementu (nie wewnątrz linijki lub całego dokumentu):  
```
h1 {
    text-align: right;  
}
```
  
## Szerokość czcionki  
Chodzi o to, jak szerokie będą litery, jak bardzo będą pogrubione (bold). 
```
h1 {
    font-weight: 500;
}
```
400 to normalny rozmiar.  
Nie każdy rodzaj czcionki może przyjmować wszystkie wartości. Np. przy h1 niemożliwe jest danie wartości 100, więc przyjmuje najniższą możliwą dla tego elementu.  
Szerokość czcionki można wyrażać numerycznie (100-900) lub słowami (normal, bold, lighter, bolder).  
  
## Text decoration  
Dodatki do tekstu, np. podkreślenie, kreska nad tekstem, przekreślenie:  
```
h1 {
    text-decoration: underline;
}
```
  
Można również wstawić te dodatki w kolorze:  
```
h1 {
    text-decoration: blue overline; (lub #024f50 overline)
}
```  
Można również wybrać styl dodatków, np. falowana linia, kropkowana, podwójna:  
``h1 {
    text-decoration: red underline wavy;
}
```
  
Można usunąć domyślną linię (przy <a> link jest domyślnie z linią podkreślającą), pisząc "text-decoration: none;".  
  
## Wysokość linii tekstowych  
Można ją wyrazić albo słownie (np. normal), albo poprzez liczbę (np. 2.5) albo przez procent (150%) lub pixele (32px) albo w innej jednostce (3em). Nie chodzi o wysokość tekstu (nie zmienia rozmiaru tekstu), tylko linijki (robi mniejsze/większe odległości między wierszami tekstu).  
```
p {line-height: 150%}
```
  
## Odległość między literami  
```
p {letter-spacing: 15px}
```  
  
## Wielkość liter  
Można zmieniać litery na wielkie/małe/pierwsza litera każdego słowa wielka:  
```
h1 {text-transform: uppercase}
```
