# Czym są transitions?  
Transitions odnoszą się do zmian elementów na stronie, jeśli element jest w danym stanie. Najprostszy przykład - jeśli ustawię dany element, żeby był różowym kwadratem i po najechaniu myszką zmienił się w niebieskie koło, to ustawiając atrybut transition na 3s sprawię, że element po najechaniu zmieni się w koło dopiero po 3 sekundach (stopniowo).  
  
```
#dividv {height: 100px;
         width: 100px;
         background-color: magenta;
         transistion: 3s}
         
#divdiv:hover {background-color: cyan;
               border-radius: 50%}
```  
  
## Właściwości transistion  
### property name  
Mogę odnieść się tylko do jednego atrybutu (jednej właściwości), który chcę zmienić, np. podając "transition: background-color 3s" sprawię, że jedynie kolor zmieni się po 3s. Kształ zmieni się natychmiastowo. Kolejne atrybuty piszę po przecinku. Chcąc ustawić wszystkie atrybuty, piszę "all". Lepiej tego nie robić.  
```
transition: background-color 3s, corder-radus 1s
```
  
### delay  
Oznacza opóźnienie - zanim przemiana się zacznie, strona odczeka podaną ilość sekund. Delay podaje się po property name:  
```
transistion: background-color 3s 1s;
```
  
### timing function  
Odnosi się do tego, w jaki sposób ma się dokonać przemiana - czy ma się zrobić w równomiernym tempie, czy najpierw szybko, potem zwalniać, itd.  
Dla transition-timing-function istnieją różne wartości, np:  
- linear - równomierne tempo,  
- ease-in - coraz szybciej,    
- steps(6, end) - skokowo,  
- cubic-bezier(.29, 1.01, 1, -0.68) - są różne style, z których można sobie wybierać (jak np. podskakiwanie 2 razy i dopiero skoczenie do końca).  
  
Można podać timing-function od razu w "transition" - np.  
```
 "transistion: background-color 3s 1s ease-in"  
```  

Jeśli robię oddzielnie dla różnych elementów, podaje się to jako "transition-timing-function".
  
"Transform" to również element, który mogę zmienić po np. najechaniu na jakiś element, dlatego "transform" również może być "property name" w transition.
