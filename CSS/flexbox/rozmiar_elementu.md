## flex-basis  
Oznacza się w nim początkowy, startowy rozmiar elementu - jeszcze zanim zostanie dodany do "flex containera".  
Flex-basis odnosi się albo do wysokości, albo do szerokości, zależnie od tego, która oś jest główna (flex-direction: row/column).  
  
## flex-grow  
Kontroluje ilość dostępnego miejsca, które element może zająć. Dostępnego, tj. jeśli takie jest.  
Przyjmuje wartości bez jednostek. Jeśli podam 1 - zajmie całe miejsce, które zostało. Jeśli kilku elementom dam 1 - wszystkie podzielą się po równo miejscem, które zostało.  
Jeśli jednemu podam 1, a drugiemu 2 - pierwszy dostanie 1/3, drugi 2/3 miejsca, które zostało.  
Jeśli ustawię flex-wrap: wrap, to przy zmniejszaniu strony elementy będą przechodzić do rzędów. Tak np.: mam 5 kwadratów w rzędzie, wszystkie ustawione na flex-grow: 1, zmniejszam stronę powoli, aż ostatni element nie przeskoczy do kolejnego rzędu i zajmie całe miejce w nowym rzędzie, aż do czasu (ciągle zmniejszam), aż przedostatni element do niego nie przeskoczy i nie zaczną dzielić miejsca na pół. Itd.  
  
## max-width, min-width  
Można ustawić, to jakiej maksymalnie/minimalnie szerokości elementy mogą urosnąć/zmniejszyć się.  
  
## flex-shrink  
Kontroluje, w jakim tempie element ma się kurczyć, jeśli nie ma wystarczająco miejsca - np. 5 elementów o szerokości 500px nie zmieszczą się w section, to jeśli ustawię jednemu z nich flex-shirnk: 2, to ten element będzie 2 razy mniejszy od każdego z pozostałych - ten element będzie kurczył się pierwszy.  
Ustawienie flex-shrink: 0 spowoduje, że element w ogóle nie będzie się kurczył.  
   

## skrót: flex  
Podaje się w kolejności:  
- flex-grow,  
- flex-shrink,  
- flex-basis.  
Jeśli podaję 2 bez jednostek, będzie to flex-grow i flex-shrink.  
Jeśli podaję 2 i jedno z nich jest bez jednostek, drugie z jednostką, to będzie to flex-grow i flex-basis.  
Jedna wartość oznacza flex-grow.  
