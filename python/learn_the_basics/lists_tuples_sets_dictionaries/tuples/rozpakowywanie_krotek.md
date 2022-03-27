# Jak rozpakować krotkę  
Mając listę:  
```
my_pairs = [(1, 2), (3, 4), (5, 6)]
```
mogę rozpakować krotki będące jej elementami w następujący sposób:  
```
for (t1, t2) in my_pairs:
  print(t1)
  print(t2)
```
    
Można też pominąć nawiasy:  
```
for t1, t2 in my_pairs:
  print(t1)
  print(t2)
```
