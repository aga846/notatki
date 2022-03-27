# Jak połączyć DB z plikiem .py  
Najpierw trzeba zaimportować moduł sqlite3, a następnie stworzyć połączenie dzięki metodzie connect():  
```
import sqlite3
conn = sqlite3.connect("example.db")
```
Jeśli mam już istniejącą bazę danych, łączę ją w powyższy sposób.  
Jeśli nie mam bazy danych (pliku bazodanowego - .db), powyższa komenda utworzy bazę danych. Jeśli natomiast odpalę plik .py kolejny raz, już po utworzeniu bazy danych, nie stworzy nowej, tylko połączy się z już istniejącą.    
  
Następnie będziemy interaktować z tą bazą danych poprzez utworzone połączenie.  
  
  
## Kursor  
Żeby robić coś z bazą danych poprzez plik pythonowy, musimy:  
1. Utworzyć kursor  
```
c = conn.cursor()
```
Potem cokolwiek będziemy robić z bazą danych, będziemy robić to za pomocą kursora (będzie c.execute()).  
   
2. Wyegzekwować kod SQL  
Za pomocą kursora - wklejamy do metody execute kod SQL:  
```
c.execute("CREATE TABLE friends(first_name TEXT, last_name TEXT, closeness INTEGER);")
```
  
3. Zatwierdzić zmiany  
Po dokonaniu zmian musimy je zatwierdzić - zatwierdzamy połączenie:  
```
conn.commit()
```  
  
  
## Zamykanie połączenia  
Na sam koniec trzeba zamknąć połączenie (tak jak zamykanie pliku po pracy z nim):  
```
conn.close()
```
