Kolejność parametrów funkcji jest ważna:  

1. zwykłe parametry (to również keyword arguments)  
2. *args
3. default_parameters (parametry domyślne, tj. np. age=26: w tym przypadku, jeśli nie zostanie podany argument age przy wywoływaniu funkcji, automatycznie do age zostanie dopisana wartość 26. Jeśli zostanie podany ten argument, wartością age będzie podana wartość)  
4. **kwargs
