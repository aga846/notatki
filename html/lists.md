## <li> </li>   
List item. Dodawanie kolejnych elementów na liście.  
  
  
## <ul> </ul>
Unordered list. Elementy na liście będą wyświetlone pod zwykłymi punktami (np. *, kropka, -. Dla wyboru punktu służy atrybut "type" - square, disc, circle). Nie są w żadnej specjalnej kolejności.  
```
<ul type = "square">
  <li>Beetrot</li>
  <li>Ginger</li>
  <li>Potato</li>
</ul>
```
  
  
## <ol> </ol>  
Ordered list. Elementy na liście będą wyświetlone pod numerami. Domyślnym numerem startowym jest 1. Można wybrać numerowanie:  
- 1, 2, 3  
- I, II, III  
- i, ii, iii  
- A, B, C  
- a, b, c  
Numerowanie wybiera się poprzez użycie atrybutu "type" - "1", "I", "i", "A", "a".  
Można też wybrać numer startowy poprzez użycie atrybutu "start". Przy atrybucie start używamy tylko numerów arabskich, niezależnie od tego, jaki typ wybraliśmy, tj. nawet jeśli chcę, żeby numeracja była wielkimi literami, ale zaczynała się od "E", to piszę: type = "A", start = "5", a nie start = "E":  
```
<ol type = "i", start = 4">
  <li>Beetrot</li>
  <li>Ginger</li>
</ol>
```
  
## <dl> </dl>  
Definition list. Wstawia się słowo oraz jego definicję. Używane tagi:  
- <dl> i </dl> - zdefiniowanie początku i końca słownika  
- <dt> i </dt> - wstawienie terminu  
- <dd> i </dd> - wstawienie definicji  
```
<dl>
  <dt><b>HTML</b></dt>
  <dd>This stand for HyperText Markup Language</dd>
</dl>
```  
  
  
Można zagnieżdżać listy w sobie (w elemencie listy można zrobić listę).
