# Do czego służy __dict__  
Dzięki __dict__ możemy dostać się do atrybutów obiektu zwróconych jako słownik:

```
print(jane.__dict__)
# {"first": "Jane", "last": "Goodall", "_age": 20}
```

Nie wyświetlają się tutaj @properties, tylko same atrybuty - dlatego age jest z "_".
