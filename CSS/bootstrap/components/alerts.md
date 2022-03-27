# Alerts  
Alert zapewnia rodzaj feedbacku dla użytkownika.  
Np. kiedy stronie się ładuje albo kiedy została zrobiona jakaś akcja, pojawia się informacja, że zostało zapisane (np. "Dziękujemy za wypełnienie testu", "Nie masz pozwolenia, żeby to zrobić", "Witamy ponownie", "Wylogowywanie").  
  
W elemencie, w którym będzie zawarta dana informacja, daje się klasę "alert" oraz podklasę ze wskazaniem koloru:  
```
<div class="alert alert-primary"
  Check it out!
</div>
```

Można dodać nagłówek do alertu:  
```
<div class="alert alert-primary"
  <h4 class="alert heading">Alert heading</h4>
  Check it out!
</div>
```

## Dismissing  
Można dodać do alertu przycisk "x", który wyłączy dany alert.  
Jest tu trochę JavaScriptu.  
  
Nie dodaje się raczej litery "x", tylko entity codes (\&times to x).  
Dodaje się span:  
```
<span aria-hidden="true">&times;</span>
```  
To "aria-hidden" jest dla screan readers.  
Ten span umieszcza się wewnątrz buttona.  
W buttonie natomiast dodaje się aria-label="Close" (też dla screan readers - po to, żeby przeczytało "Close" a nie czytało spana; wszystkie aria są dla screan readres).  
Oprócz tego w buttonie dodaje się klasę "close" - przesuwa przycisk "x" na prawo całego alertu - ale nie w prawy górny róg.  
Żeby działało - tj. żeby rzeczywiście alert się zamykał po kliknięciu na "x", trzeba dać jeszcze w buttonie "data-dismiss="alert" - już poza klasą.  
```
<button aria-label="Close" class="close" data-dismiss="alert">
  <span aria-hidden="true">&times;>/span>
</button>
```  
  
Dodatkowo można jeszcze przesunąć "x" w prawy górny róg i sprawić, żeby cały alert zniknął trochę wolniej, a nie nagle. W tym celu do elementu, wewnątrz którego jest cały alert (czyli w naszym przypadku - do diva), trzeba dodać w klasie jeszcze "alert-dismissible fade show". Całość będzie wyglądać tak:  
```
<div class="alert alert-primary alert-dismissible fade show">
  <h4 class="alert heading">Alert heading</h4>
  Check it out!
  <button aria-label="Close" class="close" data-dismiss="alert">
    <span aria-hidden="true">&times;>/span>
  </button>
```
  
W samym divie można dodać jeszcze role="alert" - dla screan readers - wskazuje, że to jest istotna informacja.  
  
Żeby wszystko działało, trzeba dodać skrypty - skopiować ze strony bootstrapa - to skrypty JavaScript.
