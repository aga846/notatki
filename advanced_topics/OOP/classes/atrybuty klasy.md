# Co to są atrybuty klasy?  
Atrybuty klasy są takie same dla każdego obiektu.  

## Jak odwołać się do atrybutu klasy?  
Odwołujemy się do nich poprzez: "Klasa.atrybut",  
ale można dostać się także poprzez: obiekt.atrybut.  


W poniższym przykładzie tworzymy atrybut klasy o nazwie active_users, któremu nadajemy wartość 0. Przy tworzeniu każdego nowego obiektu, ponieważ z automatu jest wywoływana funkcja __init__, atrybut klasy active_users powiększa się o 1.  

```
class User:
    active_users = 0
    
    def__init__(self):
        User.active_users += 1
        
user1 = User()
print(User.active_users)        # 1
user2 = User()
print(user1.active_users)       # 2
```

Jeśli do atrybutu klasy odwołujemy się również w innych funkcjach, a nie tylko w __init__, najlepiej używać atrybutu klasy poza funkcją __init__.  
Jeśli do atrybutu klasy odwołujemy się tylko w danej funkcji, lepiej umieścić go w tej funkcji.
