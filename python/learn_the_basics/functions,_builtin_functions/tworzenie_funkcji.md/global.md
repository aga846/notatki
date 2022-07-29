# Czym jest global  
Global to znaczące słowo w pythonie.  
Jeśli w funkcji chcę zrobić coś ze zmienną, która została zdefiniowana poza funkcją, potrzebuję użyć słowa "global". W innym przypadku wywali błąd: "local variable 'total' referenced before assignment".  
Za pomocą słowa "global" dajemy znać pythonowi o tym, że dana zmienna jest zdefiniowana poza funkcją.  
Nie wystarczy także użyć słowa "global" przed zmienną podczas robienia coś z tą zmienną. Trzeba ją najpierw "zimportować":  
  
```
total = 0

def adding_to_x(x):
    global total
    total += 1
    x += total
    return x

print(adding_to_x(2))    # 3
```   
Ważne jest również to, że jeśli robimy coś z globalną zmienną wewnątrz funkcji, ona zmienia się globalnie. Gdybyśmy w powyższym przykładzie wywołali print(total), zwróciłoby 1, a nie 0.  
  
## Używanie globalnej zmiennej w zagnieżdżonej funkcji  
W funkcji zawsze python szuka lokalnej zmiennej, a nie globalnej. Dlatego, jeśli zdefiniowałam zmienną (lokalną) w funkcji zewnętrznej, to a funkcji wewnętrznej python będzie odwoływał się do tej właśnie zmiennej, nawet jeśli w funkcji wewnętrznej zdefiniowałam zmienną globalną. Natomiast już poza zewnętrzną funkcją zmienna globalna będzie taka, jak zdefiniowana w funkcji wewnętrznej.  
  
```
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)  


# 
Before calling bar: 20
Calling bar now
After calling bar: 20
x in main: 25
```
  
W powyższym przykładzie najpierw zdefiniowałam zmienną lokalną x w funkcji zewnętrznej. Potem w funkcji wewnętrznej zaznaczyłam, że x, do którego się teraz odnoszę, jest globalną zmienną i zmieniłam ją na 25. Mimo to jednak wewnętrz funkcji foo() (a więc również w funkcji bar()) python zwraca wartość 20 dla x. Dopiero po wyjściu z całej funkcji x jest 25.
