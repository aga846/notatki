# Args i kwargs we wrapperze  
Umieszczenie jako parametry w funkcji wrapper *args i **kwargs sprawia, że funkcja, wokół której owinięta jest shout(fn) - w naszym przypadku funkcja greet() oraz order() - może przyjmować dowolną liczbę argumentów, również 0.  
  
```
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper
    
@shout
def greet(name):
    return f"Hi, I'm {name}"
    
@shout
def order(main, side):
    return f"Hi, I would like to order {main} with {side}"
    

print(greet("damian"))            # HI, I'M DAMIAN
print(order("burger", "fries"))   # HI, I WOULD LIKE TO ORDER BURGER WITH FIRES
```
