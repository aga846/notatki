# Do czego służy pbd  
PDB = Python Debugger  
Pdb to po prostu moduł, który należy zaimportować.  
Służy do zatrzymania się w trakcie egzekwowania kodu. Po prostu się zatrzymuje - nie wyłącza program, przeskakuje kolejne linijki, tylko się zatrzymuje.  
Przy napotkaniu pdb program się zatrzymuje i potem z terminala możemy "nawiązać interakcję".  
Pdb pokazuje następną linijkę, która będzie egzekwowana po pdb.   
  
```
import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(restult)
pdb.set_trace()
```
  
Program najpierw zrobi 2 pierwsze linijki, napotka pdb.set_trace() i zatrzyma się.  
  
```
# result = first + second
  (Pdb) 
``` 
  
Mogę teraz nawiązywać interakcję z pythonem poprzez:   
- l (list) - pokazuje cały kod oraz wskazuje na linijkę, przed którą się zatrzymał  
- n (next_line) - egzekwuje kolejną linijkę kodu  
- p (print) - jeśli mam zmienną o nazwie takiej, jak komenda (np. l, n, c), to jak napiszę "p c", python wyświetla zmienną, a nie robi komendę  
- c (continue) - wychodzi, wyświetlając program do końca  
- napisanie zmiennej - wyświetli mi jej zawartość - np. first -> # "First"; jeśli w tym momencie, na którym się zatrzymałam w powyższym przykładzie spróbuję dostać się do zmiennej result lub third, wyskoczy NameError, ponieważ program jeszcze nie dotarł do momentu, w którym ta zmienna jest zdefiniowana.  
  
Pdb jest egzekwowane tylko wtedy, kiedy kod jest egzekwowany (np. jak pbd jest w funkcji, to egzekwowane jest dopiero wtedy, kiedy ta funkcja jest wywołana).
