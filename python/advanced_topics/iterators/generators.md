# Co to są generatory  
patrz -> learn_the_basics\lists_tuples_sets_dictionaries\generator_expressions  
  
## Generator functions  
Jeśli chcę, żeby funkcja zwróciła generator, to zamiast "return" piszę "yield". Funkcja zwraca to, co jest napisane po "yield" i zatrzymuje się, jednak po ponownym wystartowaniu (tj. next()) zaczyna od tego, co jest po "yield" (może yieldować wiele razy, a nie tak jak return - tylko raz).  
  
Yield zwraca generator expressions = <generator object ...>.  
  
Tak jak generator expressions, yield pamięta tylko ostatnią wartość, nie robi jakiejś listy/krotki, dzięki czemu nie zabiera tyle pamięci.  
  
```
def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1
        
counter = current_beat()
print(next(counter))      # 1
print(next(counter))      # 2
```

   
## Kiedy używać?  
Dobrze używać yield wtedy, gdy nie chcę zapamiętywać żadnych wartości, tylko zwracać jedną wartość w kółko (tj. kilka wartości w kółko).
