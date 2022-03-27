## Otwieranie i zamykanie pliku - open, close  
Jeśli chcę cokolwiek zrobić z plikiem - czytać, pisać - muszę go najpierw otworzyć, a jak skończę - zamknąć.  
1. Gorszy sposób: zwykłe otworzenie z koniecznością zamknięcia  
  
```
file = open("story.txt")
```  
Do zmiennej "file" przypisany jest cały plik.  
   
Konieczne jest potem zamknięcie pliku:  
  
```
file.close()
```
   
2. Lepszy sposób: bez konieczności zamykania    
  
```
with open("story.txt") as file:
    pass
```
Tu również do zmiennej "file" zostaje przypisany cały plik.  
   
Plik zostanie automatycznie zamknięty po wykonaniu wszystkiego, co znajdzie się w zakresie "with open ... as ...".  
   
   
## Czytanie pliku - read  
  
```
file.read()
```
   
Ta funkcja sprawia, że python czyta cały plik. Jeśli po wywołaniu funkcji wywołamy ją jeszcze raz, nie przeczyta pliku jeszcze raz, bo kursor przejechał do końca pliku po pierwszym przeczytaniu.  
Jeśli dopiszę coś do pliku, mając go otwartego w pythonie, i potem wywołam  read() jeszcze raz, to będzie czytał dalej - od momentu, w którym skończył ostatnio.  
   
Można przypisać zmienną do file.read(), np.   
```
data = file.read()
```
   
   
## Przesuwanie kursora - seek  
  
```
file.seek(0)
```
  
Przesuwa kursor na początek pliku. Dzięki temu możliwe jest przeczytanie pliku ponownie od wybranego momentu.   
0 - przesuwa kursor na początek pliku.  
1 - przesuwa kursor do znaku na indeksie 1, itd.  
Działa tylko na otwartym pliku.  
  
  
## Czytanie linijki - readline  
  
```
file.readline()
```
   
Czyta kolejną linijkę pliku.   
   
  
## Zwracanie linijek jako listy - readlines   
  
```
file.readlines()
```
   
Zwraca wszystkie linijki pliku jako elementy listy, np.   
["This is a short story.\n", "Now it's a little longer.\n", "The end."\]   
   
   
## Atrybut closed   
  
```
file.closed()
```
   
Zwraca informację, czy plik jest zamknięty (True lub False) - to nie funkcja, tylko atrybut.   
   
   
## Argumenty funkcji open - file modes: "r", "w", "a", "r+"   
To argumenty funkcji open().   
  
### "r" - read  
Domyślnym argumentem jest "r", dlatego nie trzeba go pisać, jeśli chce się tylko przeczytać plik.  
  
### "w" - write   
NADPISUJE to, co wpiszemy, czyli usuwa to, co dotychczas było w pliku i zastępuje to podaną przez nas zawartością.  
  
```
with open("story.txt", "w") as file:
    file.write("Writing files is great!\n")
    file.write("Here's another line of text.")
```
  
Jeśli jako parametr w open() podam niestniejący plik, UTWORZY GO.  
  
### "a" - append  
Dodaje to, co wpiszemy, na koniec pliku (jak "w", ale nie nadpisuje, więc nie usuwa dotychczasowej zawartości).  
  
```
with open("story.txt", "a") as file:
    file.write("Writing files is great!\n")
    file.write("Here's another line of text.")
```
  
Podobnie jak "w", UTWORZY PLIK, jeśli podam w open() nieistniejący plik.  
  
### "r+" - read+  
"+" oznacza updatowanie, więc read+ działa tylko z istniejącymi plikami = NIE UTWORZY NOWEGO PLIKU.  
Dodaje zawartość na początku pliku, nadpisując - ale nie jak "w", bo zostawia istniejący tekst, którego nie nadpisał, np.  
- było "123456"  
- napisałam "abc" przy użyciu r+  
- mam "abc456".  
  
Jeśli chcę napisać coś na konkretnej pozycji (np. 10), mogę najpierw przesunąć kursor na tę pozycję przy pomocy seek(10) i potem napisać coś przy pomocy r+:  
  
```
with open("story.txt, "r+") as file:
    file.seek(10)
    file.write("hello")
```
^ spowoduje to dodanie "hello" na pozycji 10, 11, 12, 13, 14.  
  
### Zmniejszenie rozmiaru pliku - truncate   

```
file.truncate()
```
lub
```
file.truncate(20)
```
  
Zmniejsza rozmiar pliku do liczby podanych bajtów.
