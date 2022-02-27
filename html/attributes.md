Można nadawać atrybuty danemu tekstowi, który jest ujęty między jakimiś tagami.  
Atrybut zawsze ma nazwę i wartość (zawsze w cudzysłowiach) i jest umieszczany w tagu otwierającym. np.  
  
```
<p align = "left">This is left aligned</p>
```

W powyższym przykładzie atrybutem dla tekstu "This is left aligned" jest "align = "left"".  Jest umieszczony w otwierającym tagu paragrafu, ma nazwę (align) oraz wartość ("left").  
Zarówno nazwy, jak i wartości, są niewrażliwe na wielkość liter, choć rekomenduje się pisanie małymi literami.  
  
Najważniejsze atrybuty w HTMLu:  
- id  
- title  
- class  
- style  
  
## Id  
Używany w celu unikalnego zidentyfikowania jakiegoś elementu na stronie HTML, np. jeśli mam 2 elementy o takiej samej nazwie, to mogę użyć atrybutu id, żeby rozróżnić te elementy. Jednego id używa się na stronie tylko raz.  
  
## Title  
Daje podpowiedź, jak najedzie się kursorem na dany element, np.  
```
<h3 title = "Naprawdę">Kocham Damiana</h3>
```
Wyświetli się "Kocham Damiana", ale jak najadę myszką na ten napis, pojawi się "Naprawdę".  
  
## Class  
Łączy element z arkuszem stylów, precyzuje klasę elementu. Atrybut klasy będzie rozwinięty przy CSS. Class to coś takiego jak id, tylko do wielu elementów.  
```
class = "className1 className2 className3"
```  
  
## Style  
Atrybut stylu pozwala na sprecyzowanie reguł CSS w danym elemencie. Więcej przy CSS.  
```
<p style = "font-family:arial; color: #FF0000;">Some text...</p>
```
  
# Internationalization Attributes  
Istnieją 3 atrybuty internacjonalizacji:  
- dir  
- lang  
- xml:lang  
  
## Dir  
Wskazuje, w którym kierunku tekst powinien być płynąć - dostępne są 2 wartości: ltr (wartość domyślna, od lewej do prawej) i rtl (dla języków, w których czyta się od prawej strony).  
Atrybutu dir używa się wewnątrz tagu \<html\>. Jeśli użyjemy wewnątrz innego tagu, to dir będzie kontrolował kierunek tylko elementu zawartego w tym tagu.  
  
## Lang  
Pozwala na wskazanie, jaki jest główny język używany w danym dokumencie. Również umieszcza się go wewnątrz \<html\>.  
  
## Xml:lang  
To atrybut lang, ale dla XHTML.  
  
# Inne atrybuty  
Przykładowo, dostępne są także:  
1. align - wyrównanie tekstu: do prawej, do lewej, do środka (opcje: right, left, center)  
2. valign - wyrównanie tekstu patrząc pionowo (opcje: top, middle, bottom)  
3. bgcolor - kolor tła za elementem (opcje: numeric, hexidecimal, RGB values)  
4. background - umieszcza obrazek w tle elementu (opcje: URL)  
5. width - szerokość tabel, obrazków, komórek w tabeli (opcje: numeric value)  
6. height - wysokość tabel, obrazków, komórek w tabeli (opcje: numeric value).
  
