Istotne są tutaj właściwości elementów, takie jak inline (niektóre elementy nie tworzą dla siebie kolejnej linijki, jak np. <span>) i block (inne elementy tworzą dla siebie całą linię, np. <h1>).  
  
Dzięki display można zmieniać te właściwości:  
```
h1 {display: inline}
```
Wtedy <h1> nie tworzy sobie nowej linii.  
  
## Inline elements  
Ignorowane są dla nich właściwości (nie da się ich zmienić):  
- width,  
- height,  
  
Działają dla nich, ale inaczej, właściwości:  
- padding - ale działa nie tak, jak dla block elements, tj. nie zajmuje dla siebie więcej miejsca, tylko zakrywa zawartość pod sobą,  
- margin - jest respektowany margines tylko w linii, w wierszu, i to tylko na wysokości, na której jest tekst <spanu>. Od góry i od dołu nie ma marginesu.  
  
## Inline-block value  
Elementowi, który jest block element, można dać dla display wartość inline-block. Wtedy dany element będzie dzielił z innymi elementami rząd, ale nie będzie "ograniczony", tak jak inline elements, tj. będą normalnie respektowane wszystkie właściwości - width, height, paddinh, margin.  
  
## None  
Atrybutowi display można nadać wartość none - wtedy element wciąż będzie w kodzie, ale nie będzie się wyświetlał.  
 
