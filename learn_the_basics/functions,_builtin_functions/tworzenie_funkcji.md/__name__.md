# Czym jest __name__  
Każdy plik ma zmienną __name__. Jeśli egzekwujemy dany plik, to ta zmienna jest równa __main__.  
Jeśli jednak mamy dwa pliki - A i B, przy czym A to plik główny, a B to plik, w którym jest kod, który importujemy - to jeśli w pliku A przywołamy zmienną __name__ pliku B, to to __name__ B nie będzie równe __main__, tylko będzie nazwą pliku B.  

__name__ = __main__ tylko przy bezpośrednim egzekwowaniu pliku.  

Przy importowaniu pliku B do pliku A zimportowany plik B od razu będzie egzekwowany w pliku A. Żeby tego uniknąć, należy w pliku B napisać:  

```
if __name__ == "__main__"
```
