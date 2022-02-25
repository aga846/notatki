# Czym jest nonlocal  
Nonlocal to znaczące słowo w pythonie.  
Jeśli w funkcji wewnętrznej chcę zrobić coś ze zmienną, która została zdefiniowana w funkcji zewnętrznej, a nie do globalnej zmiennej ani do lokalnej zmiennej, potrzebuję użyć słowa "nonlocal". W innym przypadku zmienna będzie zmienną lokalną, do której możliwe odniesienie się będzie tylko w tej funkcji wewnętrznej.  
Za pomocą słowa "nonlocal" dajemy znać pythonowi o tym, że dana zmienna jest zdefiniowana w funkcji zewnętrznej (funkcji "matce").  
Nie wystarczy także użyć słowa "nonlocal" przed zmienną podczas robienia coś z tą zmienną. Trzeba ją najpierw "zimportować".  

W pierwszym przykładzie nie odnoszę się do zmiennej z funkcji matki (nonlocal), tylko tworzę nową zmienną, tylko na potrzeby funkcji f_inside: 

```
total = 0

def F_outside():
    total = 5

    def f_inside():
        total = 10
        print(total)
        total += 1
        print(total)
    f_inside()
    return total

print(f_outside())
print(total)


#
10    <- linijka 8 kodu; printuje lokalne (z f_inside) total
11    <- linijka 10 kodu; printuje zmienione lokalne (z f_inside) total
5     <- linijka 12 kodu; printuje lokalne (ale z f_outside) total
0     <- linijka 15 kodu; printuje globalne total.
```

Poniżej taki sam przykład, ale z zaznaczeniem w funkcji wewnętrznej, że chodzi mi o total z funkcji "matki":
```
total = 0

def f_ouside():
    total = 5

    def f_inside():
        nonlocal total
        total = 10
        print(total)
        total += 1
        print(total)
    f_inside()
    return total

print(f_outside())
print(total)


#
10
11
11    <- total z funkcji f_outside zostało zmienione w f_inside najpierw poprzez zmianę na 10, potem przez dodanie do niego 1, dlatego jest równe 11.
0
```

## Ważne  
Nie mogę w funkcji wewnętrznej najpierw zdefiniować zmiennej lokalnej, a potem odnieść się do zmiennej nonlocal.
