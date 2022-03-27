# Do czego odnosi się position  
Atrybut position odnosi się do położenia danego elementu na stronie.  
  
## static
Domyślna pozycja to static.  
  
## relative  
Dzięki wykorzystaniu relative, mogę podać, o ile chcę przesunąć element w górę/w dół/w prawo/w lewo. Przy czy, podając "top: 50px", przesuwam w dół, bo przesuwam od góry o 50px.   
  
```
#relative {position: relative;
           top: 50px;
           left: 50px;}
```
  
## absolute  
Podając absolute jako wartość atrybutu position spowoduje, że dla danego elementu nie będzie zarezerwowane żadne nowe miejsce - będzie on na miejscu poprzedzającego go elementu.  
Jeśli podam np. top, left, to będą się one odnosić do najbliższego przodka tego elementu, który został spozycjonowany. Jeśli nie został - do body (czy do samego początku strony).  
  
## fixed  
Działa jak absolute - nie będzie zarezerwowane miejsce dla danego elementu, ale przy podaniu top, left, będzie się odnosić do samej góry strony, i, co ważne, będzie się przesuwał razem z przesuwaniem przez nas strony w dół, tj. będzie odnosił się do góry każdej pozycji strony, na której aktualnie będziemy.  
  
## sticky  
Na początku, przy otwarciu strony jest na normalnym, swoim miejscu, ale wraz z przesuwaniem strony, działa jak fixed.  
