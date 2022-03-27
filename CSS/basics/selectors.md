## *  
Gwiazdka symbolizuje wszystko (np. * {color: cyan;} zrobi każdy tekst na stronie w kolorze cyjanowym). Raczej się nie używa.  
  
## Element selector  
Pisze się nazwę danego elementu, np. h1, div, img - wtedy wszystkie elementy nazywające się w ten sposób będą zmienione w podany sposób.  
  
## Selector list  
Podaje się listę elementów: h1, h2 {color: blue;} - wszystkie h1 i h2 na stronie będą niebieskie.  
  
## id selector  
Można nadać id każdemu elementowi (nie tylko po to, żeby powiązać go z label), żeby móc zmieniać nie wszystkie elementy, tylko jeden konkretny.  
Odwoływanie się do elementu z nadanym id (podawanie go jako selector) odbywa się przy pomocy #:  
```
#singup {background-color: darkblue;}
```
Pisze się tylko #id, bez nazwy danego elementu.  
Najlepiej nie mieć za dużo id w dokumencie.  
  
## class selector  
Dzięki class mogę odwołać się do grupy elementów. Klasę nadaję dokładnie tak jak id: class="tag". Klasa nie musi dotyczyć tylko takich samych elementów.  
Odwoływanie się do elementów z nadaną klasą (podawanie ich jako selector) odbywa się przy pomocy .:  
```
.tag {background-color: yellow;
      color: red;}
```
  
## Descendant selector  
Wybiera wszystkie elementy, które są zagnieżdżone w podanym elemencie, np. li a {color: teal;} wybierze wszystkie tagi <a>, które są zagnieżdżone w <li>. Ale z samym <li> nic nie zrobi.  
Można łączyć klasę z zagnieżdżonymi selectorami - wtedy wszystkie elementy zagnieżdżone wewnątrz elementów o danej klasie będą ulegały wskazanym zmianom.  
```
.post a {color: #457b9d;}
```  
  
## Sąsiadujące elementy  
Wybiera wszystkie elementy, które występują bezpośrednio po podanym elemencie, np. h2 + p {color: yellow;} wybierze wszystkie tagi <p>, które występują bezpośrednio po <h2>, ale nie są zagnieżdżone w tym elemencie - są równorzędne.  
```
h2 + p {color: yellow;}
```
  
## Direct child  
Wybiera wszystkie elementy, które są bezpośrednim dziedziczącym (dzieckiem) podanego elementu, np. div > li {color: white;} wybierze wszystkie tagi <li>, które są bezpośrednim dzieckiem <div>. Nie chodzi o jakiekolwiek dziecko zagnieżdżone w <div>, tylko o bezpośrednie dziecko. Nie liczy się tutaj kolejność elementów (tj. nawet jeśli dane <li> będzie na samym końcu, pod innym tagiem, który zawiera w sobie inne zagnieżdżone elementy, to i tak jest ono bezpośrednim dzieckiem).  
  
## Attribute selector  
Odnoszenie się do elementu po jego atrybucie, np. do inputów, które mają type="text":  
```
input[type="text"] {width: 300px;}
```
  
### Klasa i id  
Klasa i id również są atrybutami, dlatego odwoływanie się do elementu, któremu została nadana jakaś klasa, może też wyglądać tak:  
```
section[class="post"] {}
```
Powyższy przykład można przedstawić także tak:  
```
section.post {}
```  
  
### *=, $=, ~=  
Oznaczanie wartości atrybutu przy odnoszeniu się do elementu, któremu ten atrybut został nadany, nie musi być tylko za pomocą znaku =. Może użyć też w/w znaków:  
- *= oznacza, że gdziekolwiek wśród wartości danego atrybutu pojawia się dane słowo, tj. jeśli atrybut danego elementu ma wartość "www.google.pl", to napisanie *="google", wybierze go, ponieważ "www.google.pl" zawiera w sobie słowo "google",  
- $= oznacza odniesienie się do elementu, którego wartość atrybutu kończy się na dane słowo.  
  
  
## Pseudo classes  
Odnoszenie się do elementu na podstawie jego stanu (np. wszystkie checkboxy, które zostały zaznaczone lub linki, na które najechaliśmy myszką).  
Służą do tego dwukropki.  

### hover  
Stan oznaczenia myszką to ":hover":  
```
button:hover {background-color: red;}
```
Można to łączyć z klasami, bezpośrednim dziedziczącym, itd. Np. w poniższym przykładzie, w przypadku najechania kursorem na link znajdujący się wewnątrz elementu z klasy post, link będzie podkreślony.    
```
.post a:hover {text-decoration: underline;}
```

### active  
Stan, w którym dany element jest aktywny, kliknięty, np. kiedy naciskamy na przycisk lub link.  
  
### checked  
Stan, w którym dany element został oznaczony (np. radio input, checkbox input).  
  
### nth-of-type()  
1. Oznacza któryś element z kolei, np. trzeci element o klasie post:  
```
.post:nth-of-type(3) {background-color: #dfe8dc;}
```

2. Z dodaniem "n" do liczby - oznacza co któryś, np. co trzeci:  
```
.post:nth-of-type(3n) {background-color: #dfe8dc;}
```
  
  
## Pseudo elements  
Służą do zmiany tylko części wybranego elementu - np. zmiana tylko pierwszej litery każdego paragrafu.  
Służą do tego dwa dwukropki.  
  
```
h2::first-letter {font-size: 50px;}
```
Na większości przeglądarek będzie działał również pojedynczy dwukropek, ale powinny być 2.  
Inne pseudo elementu: first-line (zmienia pierwszą linię elementu), selection (zmienia element, który został zaznaczony przez użytkownika kursorem).  
Jeśli chcę odnieść się do całego dokumentu, piszę po prostu ::selection {}, bez precyzowania elementu przed dwukropkami.  
