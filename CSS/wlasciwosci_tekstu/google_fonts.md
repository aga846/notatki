Na fonts.google.com znajduje się wiele czcionek dostępnych za darmo online (ustawienie takiej czcionki rozwiązuje problem braku danej czcionki na urządzeniu użytkownika).  
  
Na tej stronie wybieram sobie interesującą mnie czcionkę (klikam w nią i tam znajdują się różne jej grubości - najlepiej wybrać tylko takie, których będę używać, a nie całą rodzinę czcionek; cała ta czcionka ma swoją nazwę, a poszczególne wielkości - podnazwy). Po prawej stronie wyskoczy mi link do danych czcionek (do całej ich paczki, pakietu). Ten link wklejam w pliku html:  
```
<link href="link_z_czcionkami" rel="stylesheet">
```
Powyższe wstawiam oprócz, niezależnie od \<link\>, w którym znajduje się połączenie z plikiem CSS.  
  
  
W pliku CSS piszę:  
```
font-family: Roboto, sans-serif; #nazwa czcionki ze strony i podnazwa
```  
  
Jeśli całe \<body\> mam napisane jakąś rodziną czcionki, którą sprowadziłam z Google, to jeśli w danym elemencie (np. h1) znajdującym się w tym \<body\>, zmienię rozmiar czcionki na większy niż rozmiar największej sprowadzonej z Google czcionki, to ustawi się największy sprowadzony rozmiar.  
  
  
Osadzać czcionki (sprowadzać je) można również ze strony fontlibrary.org, ale tam nie wszystkie są darmowe.  
