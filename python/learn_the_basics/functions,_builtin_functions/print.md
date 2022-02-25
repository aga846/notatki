# Argument "sep" w funkcji print  
Oprócz wartości, które chcemy wyświetlić, w princie można również podać, czym te wartości mają być przedzielone.  
```
aga = "Aga"
damian = "Damian"

print(aga, damian)   # tutaj domyślnie jest " " --> Aga Damian
print(aga, damian, sep=", ")   # Aga, Damian
print(aga, damian, sep="*")   # Aga*damian
```
