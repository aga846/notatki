# Czym jest MRO  
MRO to skrót od "Method Resolution Order" i oznacza hierarchę klas przy mnogim dziedziczenu.  

## Jak odwołać się do MRO?  

1. penguin.__mro__      -> otrzymam krotkę z kolejnością klas
2. penguin.mro()        -> otrzymam listę z kolejnością klas
3. help(penguin)        -> najbardziej czytelne
