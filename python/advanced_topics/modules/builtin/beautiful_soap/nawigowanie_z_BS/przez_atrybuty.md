Można nawigować po atrybutach:  
- parent/parents,  
- contents,  
- next_sibling/next_siblings,  
- previous_sibling/previous_siblings. 
  
  
## contents  
Mogę dostać się do zawartości danego taga używając contents:  
```
data = soup.body.contents     
print(data)               # zwróci zawartość body jako listę
```
Zwrócona zawartość "contents" to będzie lista, na której elementami będą zawarte w tagu (u nas: w body) najjbardziej zewnętrzne tagi wraz z ich zawartością oraz elementy "\n". Taki element będzie po każdym najbardziej zewnętrznym tagu danej zawartości (u nas: przed i po div, po ol oraz po div):  
```
['\n', <div id="first">                                                    s\modules\builtin\beautiful_soap>
<h3 data-example="yes">hi</h3>
<p>more text.</p>
</div>, '\n', <ol>
<li class="special">This list item is special.</li>
<li class="special">This list item is also special.</li>

<li>This list item is not special.</li>
</ol>, '\n', <div data-example="yes">bye</div>, '\n']
```
Elementami będą więc najbardziej zewnętrzne tagi, a nie wszystkie tagi (tj. tagi-dzieci będą jako jeden element).  
   
Pisząc "print(soup.body.contents[1])", dostanę cały div. Mogę również dostać jego zawartość:  
```
print(soup.body.contents[1].contents)
```
tutaj dostanę listę tagów znajdujących się wewnątrz tego diva.  
  
## next_sibling  
Dostawanie się do elementu, który jest na równi danego taga - z powyższego przykładu dla pierwszego diva w body kolejnym rodzeństwem będzie najpierw pusta linia ("\n"), a potem ol.  
```
print(soup.body.contents[1].next_sibling)
```
Powyższe zwróci pustą zawartość (bo w liście "contents" body następnym elementem po divie jest pusta linia).  
Jeśli chcę dostać się do samego ol'a, mogę przywołać jeszcze kolejne rodzeństwo:  
```
print(soup.body.contents[1].next_sibling.next_sibling)
```
  
## parent  
Dostawanie się do elementu-rodzica. Np. jeśli na ol jest element li, który ma klasę "special super-special", i wyszukam ten element po klasie, to szukając parent względem tego li, zwróci mi całe ol:  
```
print(soup.find(class_="super-special").parent)
```
Wpisując jeszcze kolejny ".parent", dostanę całe body.  
