Można nawigować przez szukanie:    
- find_next_sibling/find_next_siblings,  
- find_previous_sibling/find_previous_siblings,  
- find_parent/find_parents.  
  
  
## find_next_sibling  
  
```
soup.find(id="first").find_next_sibling()
```
  
W odróżnieniu od szukania po atrybucie "next_sibling", w find_next_sibling() nie zostanie zwrócone puste miejsce, ale rzeczywiste kolejne rodzeństwo (dla przykładu powyżej: id="first" ma pierwszy div, więc jego kolejne rodzeństwo to ol).  
  
Można również poszukać jeszcze kolejnego rodzeństwa, dodając po prostu kolejne ".find_next_sibling()":  
```
soup.find(id="first").find_next_sibling().find_next_sibling()
```
  
## find_previous_sibling  
Działa jak find_next_sibling(), tylko odwrotnie - szuka poprzedniego rodzeństwa:  
```
soup.select("[data-example]")[1].find_previous_sibling()
```
soup.select("[data-example]")[1] znajdzie ostatnie div w body, więc find_previous_sibling() znajdzie poprzedzającą go ol.  
  
Można również poszukać jeszcze poprzedniego rodzeństwa - tak jak przy nexcie.  
  
Zarówno dla find_next_sibling, jak i dla find_previous_sibling mogę dawać argumenty, żeby sprecyzować, czego szukam (znajdź kolejne rodzeństwo o danej klasie), np. załózmy, że w ol mam zamienioną kolejność, tj. trzecie li (to bez klasy) jest na drugim miejscu. Za pomocą find() wyszukam pierwsze li, o klasie "special super-special", i do niego dam find_next_sibling(class_="special") - wtedy wskaże trzecie li, a nie drugie:   
```
soup.find(class_="super-special").find_next_sibling(class_="special")
```
  
## find_parent  
Szuka elementu-rodzica, np. wyszukuję h3 i dla niego rodzica (w naszym przypadku zwróci div):  
```
soup.find("h3").find_parent()
```   
Można również podać argument w find_parent, jak np. "html" - znajdzie najbliższego rodzica, który ma w tagu "html" (co jest akurat głupie, bo zawsze jest tylko jeden tag html). 
