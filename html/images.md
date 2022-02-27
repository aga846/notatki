\<img\> to tag, który się nie zamyka.  
  
\<img\> musi mieć atrybut (tak jak \<a\> musi mieć href). Nazywa się "source":  
\<img src = ""\>  
  
Można zmieniać rozmiar obrazka używając html, ale lepiej to robić za pomocą CSS.
  
  
## Wklejanie obrazka, który mam u siebie lokalnie  

```
<img src = "steve.jpg">
```  
  
Wystarczy napisać nazwę pliku (obrazka) wraz z rozszerzeniem, jeśli znajduje się w tym samym folderze, co mój plik.  
  
### Obrazek jest w innym folderze  
Należy dopisać nazwę folderu:  
```
<img src = "pictures/steve.jpg">
```
  
  
## Wklejanie obrazka z internetu  
Kopiuję adres obrazka i wklejam go jako src:  

```
<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Laced_Polish_chicken.jpg/330px-Laced_Polish_chicken.jpg">
```
  
### Adres obrazka się zmienił  
Można użyć atrybutu alt. Dzięki niemu będzie przechowywany tekstowy opis obrazka (tj. to, co napiszę w atrybucie "alt"). Nie będzie dzięki temu symbolu niezaładowanego obrazka.    
```
<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Laced_Polish_chicken.jpg/330px-Laced_Polish_chicken.jpg" alt = "My lovely chicken Steve">
``` 
Tutaj - jeśli będzie wadliwy adres URL, to pojawi się napis "My lovely chicken Steve".
