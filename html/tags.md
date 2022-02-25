## <!DOCTYPE html>  
Tag używany po to, żeby przeglądarka zrozumiała, która wersja HTMLa jest użyta w dokumencie.  
  
## <html> </html>  
Cała zawartość dokumentu (pliku) jest między <html> a </html>, łącznie z <head>.  
  
## <head> </head>  
To tytuł dokumentu/strony. Jeśli otworzę stronę, to to, co jest zawarte pomiędzy <head> i </head>, będzie widoczne w tytule strony (jak mam otwarte kilka kart, to widzę tytuł każej z nich).  
  
## <body> </body>  
Pomiędzy <body> a </body> znajduje się wszystko, co będzie wyświetlone na stronie.  

## <h1> </h1>  
Wielkość czcionki, jaką napisany będzie tekst pomiędzy <h1> a </h1>. Jest 6 dostępnych wielkości w HTMLu.  
  
## <p> </p>  
Zawarcie tekstu pomiędzy <p> a </p> robi z tego tekstu kolejny paragraf (kolejne paragrafy są automatycznie oddzielone enterami, nie trzeba pisać np. \n, jak w pythonie).  
  
## <br>  
Break. Wszystko, co jest poprzedzone <br />, zaczyna się do nowej linijki. Nie musi mieć tagów otwierających i zamykających, bo nic nie będzie umieszczone pomiędzy nimi.  
  
## <center> </center>  
To, co znajdzie się między <center> a </center>, zostanie wyśrodkowane.  
  
## <hr>  
Horizontal rule. Służy do zrobienia poziomej linii od aktualnej pozycji w dokumencie, do prawego marginesu (przedzielenie linijek poziomą linią).  
  
## <pre> </pre>  
Dzięki <pre>, napisany tekst będzie wyświetlał się w takim formatowaniu, jak napisane w dokumencie (z enterami).  
  
## &nbsp;  
Dzięki &nbsp; (nonbreaking space), dane słowa zostaną przedzielone twardą spacją (słowa te będą utrzymane razem, nie zrobi się między nimi enter).  
  
## <i> </i>  
Tekst zawarty między <i> a </i> będzie napisany kursywą.  
  
## <u> </u>  
Tekst zawarty między <u> a </u> będzie podkreślony. 
  
## <b> </B>
Tekst zawarty między <b> a </b> będzie pogrubiony.  
  
## <strike> </strike>  
Tekst zawarty między <strike> a </strike> będzie przekreślony linią.  
  
## <tt> </tt>  
Tekst zawarty między <tt> a </tt> będzie napisany czcionką o jednakowej szerokości liter.  
  
## <sup> </sup>  
Tekst zawarty między <sup> a </sup> (od superscript text) będzie wyświetlony o połowę wysokości wyżej niż otaczające go słowa (tak jak np. przypis, potęga).  
  
## <sub> </sub>
Tekst zawarty między <sup> a </sup> (od subscript text) będzie wyświetlony o połowę wysokości niżej niż otaczające go słowa.  
  
## <ins> </ins>  
Tekst zawarty między <ins> a </ins> jest wyświatlany jako wstawiony tekst. Przykład przy poniższym tagu <del>.  
  
## <del> </del>  
Tekst zawarty między <del> a </del> jest wyświetlany jako usunięty tekst.  
```
<p>I want to drink <del>cola</del> <ins>wine</ins></p>
```
"cola" będzie przekreślone, a "wine" podkreślone.  
  
## <big> </big>  
Tekst zawarty między <big> a </big> będzie napisany czcionką o jeden rozmiar większą niż czcionka reszty tekstu.  
  
## <small> </small>  
Tekst zawarty między <small> a </small> będzie napisany czcionką o jeden rozmiar mniejszą niż czcionka reszty tekstu. 
  
## <div> </div>  
Div służy do grupowania elementów, tworzenia sekcji i podsekcji na stronie, np. wszystkie przypisy chcę mieć w jednym miejscu i w jednym stylu na dole, i dzięki <div> wskazuję, że wszystkie elementy w <div> odnoszą się do przypisów. Podobnie np. z jaką tabelą lub obrazkiem i jego opisem pod nim. Dzięki <div> wskazuję, że cała treść zawarta w <div> należy do jednej grupy.   
```
<body>
  <div id = "menu" align = "middle">
    <a href = "/index.htm">HOME</a> |
    <a href = "/about/contact_us.htm">CONTACT</a> |
    <a href = "/about/index.htm">ABOUT</a>
  </div>
  
  <div id = "content" align = "left">
    <h5>Content Articles</h5>
    <p>Actual content goes here...</p>
</body>
```
  
<div> robi osobny blok, w odróżnieniu od np. <a>.
  
## <span> </span>  
Span służy do grupowania elementów wewnątrz linijki. Jeśli mam część zdania lub paragrafu, którą chcę zgrupować razem i użyc wspólnego dla niej stylu (innego niż reszty zdania), wstawiam ją pomiędzy <span> a </span>.  
```
<p>This is the example of <span style = "color:green">span tag</span></p>
```
  
Przyda się bardziej w połączeniu z CSS.
  
## <em> </em>  
Em - emphasized text - tekst będzie pokreślony (zazwyczaj napisany kursywą).  
  
## <mark> </mark>  
Mark służy do zaznaczenia tekstu kolorem żółtym (na żółtym tle, tak jakbym pisakiem podkreśliła).  

## <strong> </strong>  
Napisanie "silnym naciskiem" - będzie pogrubione (różnica między bold: strong to stan logiczny, a bold to stan fizyczny).  
  
## <abbr> </abbr>  
Reprezentuje skrót. Jeśli jest atrybut title, może stanowić rozwinięcie lub opis skrótu (ale nic więcej).  

## <acronym> </acronym>  
Wskazuje, że tekst pomiędzy <acronym> a </acronym> jest akronimem. Nie wyświetla się w żaden innym sposób niż reszta tekstu.  
  
## <bdo> </bdo>  
Bi-Directional Override. Czyta tekst od drugiej strony (i wyświetla się taki odwrócony tekst).  
  
## <dfn> </dfn>  
Definition element. Używa się go, kiedy wprowadza się jakiś nowy termin. Wyświetla się jako napisane kursywą.  
  
## <blockquote> </blockquote>  
Używa się go, jeśli chce się zacytować jakiś tekst. Zazwyczaj wyświetla cytat od akapitu z lewej i prawej strony, czasami napisany kursywą.  
  
## <q> </q>  
Używa się, jeśli chce się dodać podwójny cudzysłów w środku zdania.  
  
## <cite> </cite>  
Cytaty - wyświetlane jako napisane kursywą.  
  
## <code> </code>  
Służy do zapisywania kodu programistycznego. Zazwyczaj tekst pomiędzy <code> a </code> jest wyświetlany czcionką o jednakowej szerokości liter.  
  
## <kbd> </kbd>  
Podobny rezultat, co <code>.

## <var> </var>  
Używa się w połączeniu z <pre> i <code>. <var> wskazuje, że jest to zmienna.  
  
## <samp> </samp>  
Używane przy dokumentacjach programistycznych. Stosuje się do wyświetlania outputu (co zrobi print).  
  
## <address> </address>  
Używa się do zawarcia adresu. Napisze przechyloną czcionką.  
  



  
# Notatki  
- Tag to nie to samo co element. Tag to samo np. <h1>, a element to <h1>Kocham Damiana</h1>.  
- Można zamieszczać elementy w elementach, jak np.  
```
<h1>This is<i>italic</i> heading</h1>
```
- 
  
