# Czym jest higher order function?  
Higher order function to:  
- funkcja, która wywołuje inną funkcję lub w argumencie ma inną funkcję, np. funkcja sumująca kwadraty liczb wywoła funkcję liczącą te kwadraty,  
- funkcja, która zawiera w sobie inną funkcję (definiuje ją); wtedy funkcja inner ma dostęp do argumentu podanego w funkcji outer.
  
```
def hello(name="Damian"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    
    def greet():
        return "I AM INSIDE GREET()"
      
    def welcome():
        return "I AM INSIDE WELCOME()"
        
    if name == "Damian":
        return greet            <- Ważne, bez nawiasów!
    else:
        return welcome
        
        
x = hello()
print(x())          # THE HELLO() FUNCTION HAS BEEN RUN!
                    # I AM INSIDE GREET()
```
Do zmiennej x przypisałam wywołanie funkcji hello().  
W funkcji hello() zamieściłam warunek, od którego zależy, która funkcja wewnętrzna zostanie wywołana.  
Następnie wywołałam funkcję od x (czyli od wywołanej funkcji) i sprintowałam to wszystko. W efekcie: 
- najpierw zostało sprintowane "THE HELLO() FUNCTION HAS BEEN RUN!", który to string był printowany na samym początku funkcji hello(),  
- następnie funkcja przeszła do bloku "if/else" i wybrała, co zrobi,  
- na koniec, kiedy została wywołana funkcja od tej wywołanej funkcji, został sprintowany wynik funkcji greet().
