Funkcja może być parametrem w innej funkcji.  
  
```
def power(x, y):
    return x ** y
    
def sum_of_number_and_its_power(x, y, fn=power):
    return x + power(x, y)
    

output = sum_of_numbers_and_its_power(2, 4, power)
print(output)     # 18
```
W powyższym przykładzie funkcja power jest podana jako domyślna w funkcji sum_of_number_and_its_power, dlatego w ogóle nie trzeba jej podawać jako argument.  
Jeśli chcę podać inną funkcję, mogę to zrobić, np.:  

```
import math

def subtract_3(x):
    return x - 3

def sum_of_number_and_function(x, fn=power):
    return x + fn(x)

b = sum_of_number_and_function(18, math.sqrt)
print(b)     # 22.242640687119284
```
