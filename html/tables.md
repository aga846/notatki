## \<table\> \</table\>  
Tworzy tabelę.  
  
## \<td\> \</td\>  
Table data - reprezentuje pojedynczą komórkę. Komórki tworzą się w tym samym rzędzie.  
  
## \<tr\> \</tr\>  
Table row - robi nowy rząd.  
  
## \<th\> \</th\>  
Definiuje header (headers też trzeba ująć w osobny \<tr\>; tym osobnym tr'em jest thead).  
  
  
## \<thead\> \</thead\>  
Wskazuje, gdzie są nagłówki. To nie tylko zrobienie nowego rzędu, ale można użyć także, jeśli jakiś nagłówek ma podnagłówki.  
  
## \<tbody\> \</tbody\>  
Wskazuje, gdzie znajduje się właściwa tabela.  
  
## \<tfoot\> \</tfoot\>  
Koniec tabeli, ostatni rząd. Używany, gdy np. podaje się sumę wszystkich elementów.  
  
  
# Komórka obejmuje wiele kolumn lub rzędów  
## rowspan  
Używany do wskazania, że komórka zajmuje dwa rzędy (rozciąga się w pionie). Podaje się jako atrybut przy tworzeniu danej komórki, poniżej przykład z header, który ma zajmować 2 rzędy:  
```
<th rowspan="2">Animal</th>
```
  
## colspan  
Używany do wskazania, że komórka zajmuje dwie kolumny (rozciąga się w poziomie). Podaje się jako atrybut przy tworzeniu danej komórki, poniżej przykład z header, który ma zajmować 2 kolumny:  
```
<th colspan="2">Animal</th>
```
  
