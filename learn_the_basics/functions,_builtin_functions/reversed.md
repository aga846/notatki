# Co robi funkcja reversed()  
Funkcja reversed() zwraca odwrócony iterator.  
Działa nie tylko na listach.  
Nie zmienia pierwotnie podanego elementu.  
  
## Przykłady  
```
print("".join(list(reversed("hello"))))

# olleh
```

Przy próbie sprintowania po prostu reversed(cos), zwraca "iterator object". Oznacza to, że nie można tego wyświetlić, ale można iterować po elementach podanego iteratora, np.  
```
for char in reversed("hello"):
    print(char)

#
o
l
l
e
h
```
W odniesieniu do stringów: reversed("hello") to to samo, co  
```
"hello"[::-1]
```
