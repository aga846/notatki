# Czym są templates  
Template zawiera statyczne części strony HTML - czyli części, które są zawsze takie same.  
Tagi templates mają specjalną składnię, która pozwala na wstawianie dynamicznej zawartości, którą produkują views z aplikacji Django, która wpływa na ostateczny HTML.  
  
## Tworzenie templates  
Najpierw należy stworzyć folder templates w głównym folderze projektu i podfoldery dla każdego template każdej aplikacji:   
first_project/templates/first_app  
  
Następnie trzeba dać Django znać o stworzeniu templates przez edytowanie key DIR wewnątrz słownika TEMPLATES znajdującego się w pliku settings.py (poprzez dodanie jako value ścieżki templates).  
Problem: chcemy, żeby projekt był łatwo transferowalny między komputerami, ale key DIR wymaga ścieżki "hard coded". W jego rozwiązaniu pomaga pythonowy Path z modułu "pathlib" i moduł "os".  
W settings.py mam obiekt BASE_DIR, wewnątrz którego znajduje się m.in. __file__. Wyświetlenie file spowoduje wyświetlenie ściżki pliku settings.py, natomiast wyświetlenie BASE_DIR spowoduje wyświetlenie ścieżki folderu, w którym znajduje się plik settings.py.  
Żeby połączyć BASE_DIR z folderem templates (tj. dodać \templates do ścieżki), potrzebuję zimportować moduł os i do zmiennej TEMPLATE_DIR przypisać tę całą ścieżkę:  
```
TEMPLATE_DIR = os.path.join("BASE_DIR, "templates")
```
I tą właśnie zmienną przypisuję jako value do key DIR w słowniku TEMPLATES.  
  
## Tworzenie pliku HTML  
Następnie możemy stworzyć plik HTML wewnątrz templates/first_app. Wewnątrz tego pliku, oprócz normalnego kodu HTML, będziemy wstawiać tagi templates (inaczej: Django Template Variable). Te tagi pozwalają na wstawianie zawartości do HTML bezpośrednio z Django, co dalej oznacza, że będziemy mogli użyć kodu pythonowego, żeby wstawić zawartość z bazy danych.  
Żeby osiągnąć to wszystko, potrzebna jest funkcja render(), wstawiona do oryginalnej funkcji index() wewnątrz pliku view.py.  
  
## Tagi templates  
Składnia:  
{{ zmienna }}  <- to piszę w pliku HTML.  
Teraz trzeba połączyć tę zmienną z projektem i aplikacją - poprzez edytowanie views.py, znajdującego się w folderze aplikacji.  
W views.py mam domyślnie zimportowaną funkcję render.  
Edytujemy funkcję zawartą wcześniej w tym pliku (index(request)):  
```
def index(request):
    my_dict = {'insert_me': "Hello, I am from views.py!"}
    return render(request, "first_app/index.html", context=my_dict)
```
Czyli tworzymy słownik, który za key ma zmienną z pliku HTML, podaną w tagu template, a za value to, co chcemy wyświetlić na stronie.  
Zwracamy wynik funkcji render, która za argumenty przyjmuje:  
- request = template, którego chcemy użyć,  
- plik HTML (razem ze wskazaniem, że znajduje się w folderze first_app),  
- context równy słownikowi, który stworzyliśmy wyżej.  
  
Należy jeszcze dodać ścieżkę do adresu strony - patrz: aplikacje_a_projekt: Mapowanie przy pomocy include().
