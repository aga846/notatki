# Co to jest padding  
Padding to odległość między krawędzią content box a border. Ma takie samo tło, jak content box. Używa się po to, żeby dać trochę miejsca, "oddechu" między zawartością a krawędzią. Mogę chcieć, żeby jakiś element (np. button) zajmował więcej miejsca, ale żeby sam tekst nie był większy.  
Można ustawić górny, dolny, lewy i prawy padding (padding-top, padding-bottom, padding-left, padding-right) lub użyć skrótu (padding:) - używając go, po kolei dodaje się szerokość kolejnych paddingów (można podać jeden dla wszystkich / dwa dla góry-dołu i prawa-lewa / trzy dla: góry, prawa-lewa, dołu / po kolei dla każdego - góra, prawo, dół, lewo):  
```
padding: 0 20px
```
W powyższym przykładzie góra i dół nie mają w ogóle paddingu, ale lewa i prawa strona mają po 20px.  
  
Dzięki paddingowi można ustawić tekst w różnym położeniu w danym elemencie, np. w prawym górnym rogu.  
  
Padding można podawać w różnych jednostkach - px, mm, ems, rems.
