# Events w jQuery  
Na code.jquery.com są wypisane wszystkie events.  
  
Składnia:  
```
$("h1").click(function() {
  console.log("There was a click!");
  })
```  
Jeśli jest wiele elementów o podanym tagu, to powyższa składnia będzie zastosowana do każdego z nich (jeśli wybrałabym wszystkie li, to na którekolwiek li będę klikać, będą się pojawiać kolejne komunikaty "There was a click!").  
  
Jeśli wewnątrz funkcji chcę coś zrobić z elementem, potrzebuję słowa "this":  
```
$("h1").click(function() {
  $(this).text("I WAS CHANGED");
})
```  
  
## Key press  
Oprócz takich events, jak hover, click, doubleclick, są też takie, które są inicjowane poprzez naciśnięcie jakiegoś klawisza.  
Przykład - jak tylko napiszę cokolwiek (jedną literę) w danym inpucie, nagłówek h3 przełącza klasę turnBlue (włącza się i wyłącza przy wpisywaniu kolejnych liter):  
```
$("input").eq(0).keypress(function() {
  $("h3").toggleClass("turnBlue");
})
```  
  
Jeśli funkcji dam parametr event i wyświetlę w konsoli ten event, to dostanę wielki obiekt event, w którym jest m.in informacja ("key", bo to obiekt, czyli słownik) "which", która za value ma kod ASCII litery, którą wpisałam (np. dla a będzie 97).  
```
$("input").eq(0).keypress(function(event) {
  console.log(event);
})
```
Czyli można odnosić się do key "which", żeby chcieć coś zrobić, jeśli zostanie wciśnięty wybrany znak, np.  
```
$("input").eq(0).keypress(function(event) {
  if (event.which === 13) {
    $("h3").toggleClass("turnBlue")
})
```
Powyższe oznacza, że za każdym razem, kiedy wcisnę enter w inpucie, klasa turnBlue dla h3 będzie się włączać/wyłączać.   
  
Żeby używać "event" w taki sposób, muszę go dodać do argumentu funkcji.  
  
## On method  
```
$("h1").on("dblclick", function() {
  $(this).toggleClass("turnBlue");
})
```  
  
## Effects and animations  
Chodzi o różnego rodzaju animacje i efekty - np. zanikanie treści:
```
$("input").eq(1).on("click", function() {
  $(".container").fadeOut(3000)
})
```
Powyższe to: jeśli kliknę na drugi na stronie input, to wszystko, co ma klasę "container", zaniknie w ciągu 3000ms.  
Inne animacje - np. slideUp - zawartość przesuwa się do góry (znika).
