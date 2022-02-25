# Czym jest funkcja __doc__  
Za pomocą funkcji __doc__ można dostać się do wytłumaczenia, co robi dana funkcja. Nie jest to zwykły komentarz, bo można mieć do niego dostęp tylko poprzez __doc__.  
DZIAŁA TEŻ NA WBUDOWANYCH FUNKCJACH.  

Wytłumaczenie działania tworzonej przez nas funkcji dodajemy za pomocą trzech podwójnych cudzysłowiów:
""" komentarz """  

```
def say_hello():
    """A function that returns hello"""
    return "hello"
    
print(say_hello.__doc__)

# A function that returns say_hello
```  

Nie dawać spacji po ani przed """ """, bo wtedy wyświetla z niepotrzebnymi spacjami.
