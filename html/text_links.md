# Wstawianie linka, który przekierowuje do innej strony  
Używa się tagu "a" i "/a". Wszystko, co jest pomiędzy "a" i "/a" jest częścią linka.  
W tagu "a" pisze się atrybut href (HyperText Reference), gdzie wpisuje się adres URL.  
Po nim można napisać również atrybut target, który wskazuje, gdzie nowa strona zostanie otwarta (nowe czy to samo okno).
```
<a href = "http://www.google.com" target = "_self">Tutorials Point</a>
```  
Muszę dać znać, że chcę się połączyć z http i dlatego piszę http:// przed adresem. Jeśli napiszę tylko "google.com", przeglądarka będzie myślała, że ma dodać /google.com do aktualnego linka.  
Mogę w ten sposób przejść też do innego swojego pliku, w href wpisując "about.html" (about to nazwa pliku).
  
Atrybut target może przyjmować różne wartości:  
- _blank - otwiera link w nowym oknie lub karcie  
- _self - otwiera link w tej samej karcie  
- _parent - otwiera link w karcie nadrzędnej (?)  
- _top  
- targetframe
