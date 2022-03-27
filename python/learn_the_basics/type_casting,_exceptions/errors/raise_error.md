# Do czego służy raise  
Raise wywołuje podany przez nas błąd. Można napisać:  
```
raise ValueError("VALUE ERROR RAISED!!!")
```
Wtedy po prostu pojawi się błąd ValueError, z wiadomością podaną w nawiasach.  
Można też użyć po prostu "raise Exception", tylko to trochę zbyt ogólne.    
  
Bez sensu jednak używać tego w ten sposób. Można za to np. zapobiec podawaniu przez użytkownika innych wartości, niż były zamierzone, np.  

```
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "red")
    if type(text) is not str:
        raise TypeError("text must be a string!")
    if type(color) is not str:
        raise TypeError("color must be a string!")
    if color not in colors:
        raise ValueError("color is invalid color")
        
    print(f"Printed {text} in {color}")
    
colorize("hello", "yellow")    # Printed hello in yellow
colorize("3, "cyan")           # TypeError: text must be a string!
```
