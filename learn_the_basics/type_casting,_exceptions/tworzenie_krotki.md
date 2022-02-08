# Tworzenie listy  
Krotkę można stworzyć albo za pomocą funkcji tuple() albo za pomocą ().  

## Przykłady z tuple()  
Funkcja tuple() przyjmuje co najwyżej jeden argument, dlatego jeśli na krotce ma być więcej elementów niż jeden, należy podać je jako zbiór, np. listę.  

```
damian = tuple(["Damian", "Jaskolski", 26])
numbers = tuple(range(10))

set1 = {1, 2, 3}
tuple1 = tuple(set1)
```

## Przykład z ()   
```
damian = ("Damian", "Jaskolski", 26)
aga = ("Aga",)
```
W powyższym, ostatnim przykładzie, po "Aga" jest przecinek, dlatego że jest to jedyny element na krotce.
