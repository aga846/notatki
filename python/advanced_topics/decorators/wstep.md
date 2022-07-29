# Czym są dekoratory?  
Dekoratory to funkcje, które "owijają się" wokół innej funkcji.  
  
## Przykład owijania się bez dekoratora   
  
```
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day!")
    return wrapper
    
def greet():
    print("My name is Aga")
    
greeting = be_polite(greet)
greeting()
```
  
Greeting równa się wynikowi funkcji be_polite od argumentu greet, który też jest funkcją.  
Następnie został wywołany greeting(), dlatego zaczęło się egzekwowanie funkcji be_polite. Funkcja ta ma w sobie zdefiniowaną funkcje wrapper, którą egzekwuje w linijce 6 kodu.  
Tym samym teraz została wywołana funkcja wrapper, która printuje pierwsze zdanie, potem wywołuje funkcję greet, która printuje swoje zdanie, a potem printuje drugie zdanie.  
  
Inny przykład:  
```
def hello(name="Damian"):
    return "Hello" + name
    
  mynewgreet = hello    <-- ważne, bez nawiasów!
  print(mynewgreet()) # wynik funkcji hello() - "Hello Damian"
```  
   
## Przykład owijania się z dekoratorem    
  
```
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day!")
    return wrapper
    
@be_polite
def greet():
    print("My name is Aga")
```
  
Dzięki zawarciu dekoratora @be_polite, za każdym razem, kiedy wywołam funkcję greet(), będzie wokół niej owinięta funkcja be_polite -> nie ma potrzeby już wywoływania be_polite od argumentu greet.
