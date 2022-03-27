## Porównywanie zmiennych  
\>, \<, =, ==, \>=, \<=, != działa jak w Pythonie, z wyjątkiem porównywania stringa do number - JS przeczyta, że "2" jest równe 2. Żeby zapobiec tej sytuacji, należy użyć trzech ===.  
```
"2" == 2    #true
"2" === 2   #false
```
To działa również przy "nie jest równe", tj.  
```
"5" != 5    #false
"5" !== 5   #true
```  
  
To działa tak dlatego, że JS "does his best", żeby skonwertować najpierw obie zmienne, a potem je porównać. Tj. porównuje same wartości, bez typów danych.  
  
## AND  
"and" w JS to &&.  
```
1 === 1 && 2 === 2    #true
```
  
## OR  
"or" w JS to ||.  
```
1 === 1 || 2 === 1    #true
```
  
## NOT  
"not" w JS to ! (zwraca odwrotność wyniku danego warunku).  
```
!(1===1)    #false
```
