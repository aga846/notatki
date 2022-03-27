# Wybieranie danych z tabeli przy pomocy Pythona  
## Wszystkie dane z tabeli  
Mogę chcieć wybrać wszystkie dane z tabeli i wyświetlić je.  
Mogę to zrobić za pomocą pętli iterując przez resultaty kursora:  
```
c.execute("SELECT * FROM friends")
for result in c:
    print(result)
```  
  
Zamiast tego mogę użyć metody fetchall(), która zwróci listę zawierającą wszystkie resultaty (czyli to samo co wyżej, tylko w liście).  
```
c.execute("SELECT * FROM friends")
print(c.fetchall())
```
  
## Tylko niektóre dane z tabeli  
Mogę chcieć wybrać tylko jedną daną z tabeli, o określonej cesze, np. wybieram wszystkich przyjaciół o imieniu "Ania" i potem chcę wyświetlić tylko jedną Anię (pierwszą):  
```
c.execute("SELECT * FROM friends WHERE first_name IS 'Ania'")
print(c.fetchone())
```
