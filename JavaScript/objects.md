# Objects  
Objects to słowniki w JS. Nie mają uporządkowanych elementów.    
Składnia:  
```
{key1: "value one", key2: "value two"}
```
Keys nie są wpisywane jako stringi:  
```
var carInfo = {make: "Toyota", year: 1990, model: "Camry"}
```
  
## Dostawanie się do obiektu  
Tak jak w Pythonie - poprzez []. W tych nawiasach key podajemy już w cudzysłowiu:  
```
carInfo["make"]
```  
  
## Zmiana wartości  
Działa jak w Pythonie:   
```
carInfo["year"] = 2006
carInfo["year"] += 2006
```  
  
## Pętla  
Dostawanie się do keys:  
```
for (k in carInfo) {
  console.log(k)
}
```
  
Dostawanie się do wartości:  
```
for (k in carInfo) {
  console.log(carInfo[k])
```  
  
# Meteody w objects  
Wartością danego key w object może być funkcja.  
```
var carInfo = {
  make: "Toyota",
  carAlert: function() {
    alert("We've got a car here!")
  }
}
```
Jeśli wewnątrz takiej funkcji odwołuję się do wartości znajdującej się w tym słowniku, potrzebuję słowa "this", natomiast jeśli chcę się dostać do tej funkcji, wywołuję nazwę objectu i po kropce piszę funkcję (której nazwa jest key):  
```
var myObj = {
  prop: 37,
  reportProp: function() {
    return this.prop;
  }
};
console.log(myObj.reportProp());
```  
  
```
var myObj {
  name: "Damian",
  greet: function() {
    console.log("Hello " + this.name)
  }
};
console.log(myObj.greet());
```
