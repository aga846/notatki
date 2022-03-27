## display property    
W pliku box_model/display_property.md są opisane 3 własności display property (inline, block, inline-block). Kolejną jest flex.  
Jeśl ustawimy wartość "flex" dla atrybutu "display", to dany element (dany blok) będzie miał dwie osie:  
- main - domyślnie jest pozioma, od lewej do prawej;  
- cross - domyślnie jest pionowa.  
Chodzi tu o to, w jakim kierunku będą ustawiane elementy w danym elemencie.  
  
## flex direction
Można zmienić domyślność za pomocą właściwości "flex-direction" (domyślnie ten atrybut ma wartość "row"), ustawiając dla tego atrybutu inną wartość:  
- row-reverse: główna oś będzie pozioma, ale od prawej do lewej,  
- column: główna oś będzie pionowa, od góry do dołu; zostaje zmieniona wysokość elementów, bo elementy wewnątrz są elastyczne i zależne (dopasowują się) od elementu-rodzica. Np. jeśli \<section\> mam ustawione na wysokość 500px, a 5 divów w nim na 200px x 200px, to ustawiając "flex-direction" na "column", divy będą miały mniej niż 200px wysokości - żeby dopasować się do section. Ale jeśli wysokość section ustawię na wystarczająco dużo, np. 1200px, to divy będą miały po 200px,   
- column-reverse: główna oś będzie pionowa, od dołu do góry.
