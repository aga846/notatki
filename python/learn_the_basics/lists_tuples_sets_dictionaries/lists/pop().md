# Co robi metoda pop  
Metoda pop() usuwa podany element z listy. Domyślnym argumentem jest -1, czyli ostatni element.  
  
```
nums = [1, 2, 3, 4]
nums.pop()
print(nums)     # [1, 2, 3]
nums(pop(1))    # [1, 3]
```  
  
Do nums.pop() można przypisać zmienną. Wtedy ta zmienna będzie usuwanym elementem, mimo że na liście nums już go nie będzie:   
```
nums = [1, 2, 3, 4]
x = nums.pop(2)
print(x)       # 3
print(nums)    # [1, 2, 4]
```
