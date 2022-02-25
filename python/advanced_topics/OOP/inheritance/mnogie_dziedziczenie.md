# Jak działa mnogie dziedziczenie?  
W mnogim dziedziczeniu jako argumenty klasy-dziecka podaję nazwy klas, z których dziedziczy. W pierwszej kolejności klasa-dziecko będzie dziedziczyć w klas podanych w nawiasie jako pierwsze.  
Przy super() wywoła pierwszą w nawiasie klasę.

```
class Penguin(Ambulatory, Aquatic):
```
