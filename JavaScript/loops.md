## While loop  
Składnia:  
```
while (condition){
  execute some code while this condition is true
}
```  
Przykład:  
```
var x = 0;

while (x < 5) {
  console.log("x is currently: " + x);
  console.log("x is still less than 5, adding 1 to x");
  
  x = x + 1;
}
```  
  
### Break  
Działa jak w Pythonie.  
  
  
## For loop  
Składnia:  
```
for (statement1;statement2;statement3) {
  execute some code
}
```
- statement1 - egzekwowany jeszcze zanim pętla się zacznie - warunek wyjściowy, tak jak przypisanie na początku do zmiennej x liczby 0 w przykładzie z while loop powyżej,   
- statement2 - zwykły warunek, tak jak w while loop - np. x < 5,  
- statement3 - egzekwowany po każdym cyklu pętli - np. x++.  
  
### For of  
For of działa jak zwykły for w Pythonie, tyle że zamiast "in" jest "of":  
```
arr = [1, 2, 3, 4]
for (num of arr) {
  console.log(num);
}
```  
  
### ForEach  
forEach pozwala na zastosowanie danej funkcji do każdego elementu danego iteratora:  
```
arr = ["A", "B", "C"]
arr.forEach(alert)
```
Powyższy kod wyświetli w kolejnych komunikatach litery A, B i C.  
Ważne - nie pisze się nawiasów po nazwie funkcji, tylko samą jej nazwę.  
