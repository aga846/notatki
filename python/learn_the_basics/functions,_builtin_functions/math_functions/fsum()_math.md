# KONIECZNE ZAIMPORTOWANIE MODUŁU MATH  
  
## Co robi funkcja sum  
Funkcja sum zwraca sumę wszystkich wartości z listy, z tym że stosuje się dla liczb float.  
W przeciwieństwie do sum, nie przyjmuje argumentu "start".  
  
```
nums = [4, 6, 2, 4, 12]
print(math.fsum(nums))         # 28.0

print(math.fsum(range(10)))    # 45.0
``
