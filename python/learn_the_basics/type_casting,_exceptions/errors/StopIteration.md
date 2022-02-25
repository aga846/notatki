# Czym jest StopIteration  
StopIteration nie jest do końca błędem, ale wyjątkiem, który pojawia się, kiedy nie ma już elementów danego obiektu, które można iterować.  
Pętla automatycznie kończy się, kiedy pojawia się ten wyjątek, dlatego go nie widzimy.  
Jeśli jednak używalibyśmy metody next() dla iteratora, który by się już skończył, wyskoczyłoby "StopIteration" i program nie będzie szedł dalej.  

```
my_list = [1, 2, 3]
i = iter(my_list)
print(next(i))    # 1
print(next(i))    # 2
print(next(i))    # 3
print(next(i))    # StopIteration, koniec programu

print("Hello")
```
