## Icons  
Icons to ikony (strzałki, kosze, nutki, itd.). Do naszego pliku wkleja się po prostu link do nich. Znajdę je na icons.getbootstrap.com.  
Ikony są w tagu \<svg\>.  
To nie jest link do obrazka, to jest tylko ikona, która jest opisana w tym linku. Można zmieniać rozmiar, kolor. To coś jak litera, której można zmienić czcionkę. Ikony są więc trochę jak tekst.  
Można np. wkleić ikonę kosza na śmieci w przycisku "Delete". Kiedy zmienimy wielkość przycisku, ikona kosza sie również skaluje (skaluje się względem wielkości elementu-rodzica).  
Zmienia się również razem z kolorem elementu-rodzica.
  
### Input group  
W input group często używa się ikon.  
Dodając przed input group, używa się klasy "input-group-prepend", dodając po input group, używa się klasy "input-group-append".  
Dodając:  
```
<div class="input-group">
  <div class="input-group-prepend">
    <span class="input-group-text">$</span>
  </div>
  <input type="text" class="form-control">
</div>
```
doda mi się znak dolara jakby jako ikona, przed inputem tekstowym.  
Tutaj zamiast wpisania znaku dolara mogę wkleić link z daną ikoną, po prostu jako \<svg\> wewnątrz spana.  
  
  
Na stronie fontawesome.com jest dużo więcej ikon.
