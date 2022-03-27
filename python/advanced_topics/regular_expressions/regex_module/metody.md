# Regex module  
Dzięki modułowi regex możemy używać regular expressions w plikach pythonowskich.  
Należy zaimportować moduł re.  
```
import re
```
   
## Metoda compile()  
Wzór wkleja się jako string poprzedzony literą "r" do metody "compile", która tworzy obiekt regexa. Metodę zastosowaną do naszego wzoru (do naszego regular expression) przypisujemy do zmiennej.  
Innymi słowy, poniżej definiujemy regex dla numeru telefonu. Według tego wzoru będą przeszukiwane stringi.  
Litera "r" jest potrzebna, żeby można było w regexie używać backslashów, dlatego że normalnie w pythonie backslashy pozwalają na używanie escape characters, np. nowa linia. Gdyby nie było tej litery, trzeba by używać dwóch backslashów, np. nie \d, tylko \\d.    
```
pattern = re.compile(r"\d{3} \d{3}-\d{4}")
```
  
Następnie do naszego wzoru stosujemy metody.  
  
## Metoda search()  
Metoda search szuka w stringu fragmentu, który pasuje do naszego regexa. Do metody search z wklejonym stringiem, który przeszukujemy pod kątem regexa, przypisujemy zmienną.    
```
result = pattern.search("Call me at 415 555-4242")
```
Zmienna result nie będzie po prostu numerem telefonu (czyli zwróconym wynikiem) tylko obiektem (match object), którego potem możemy prosić o jakieś cechy. Nie jest to string.  
Metoda search() szuka tylko pierwszego wyniku w danym stringu, zatem jeśli mamy w stringu np. dwa numery telefonu, wyszuka tylko pierwszy.  
Jeśli nie będzie żadnego dopasowania, zwraca None. Do tego nie możemy zastosować group().  
  
## Metoda findall()  
Robi to samo co search(), tylko wyszukuje w stringu wszystkie dopasowania.  
```
result = pattern.search("Call me at 415 555-4242 or 423 804-9245")
```  
Zwróci listę pasujących stringów.  
Jeśli nie będzie żadnego dopasowania, zwraca pustą listę.  
Do findall() nie możemy zastosować group() - bo to lista.    
Findall() zwraca tylko zgrupowane w regexie wyrażenia (zgrupowane poprzez nawiasy okrągłe).    
  
## Metoda group()  
Do zmiennej result możemy zastosować funkcję group(), która zwróci rzeczywiste dopasowanie, a nie obiekt:  
```
result.group()    # "415 555-4242"
```
  
## Metoda groups()  
Do zmiennej result możemy zastosować funkcję groups() - zwraca krotkę z pogrupowanych dopasowań, ale nie chodzi tu o wiele dopasowań jednego wzoru (tj. wiele słów "kot", których szukałam - to robi findall()), ale dopasowań pogrupowanych we wzorze (patrz: wstep/znaki_specjalne/nawiasy) - np. jeśli w regexie mam ([A-Za-z]+) ([A-Za-z]+) i przeszukam według tego wzoru string "Mój Mąż to Damian Jaskolski", to groups() zastosowane do zmiennej przypisanej do search, w którym wkleiłam ten string, zwróci mi ("Damian", "Jaskolski").  
  
Jeśli chcę dostać się tylko do któregoś konkretnego dopasowania (np. tylko do nazwiska), używam metody group(), a nie groups():  
- group(0) zwróci to samo, co group() - czyli bez widocznego podziału na grupy, po prostu cały string,  
- group(1) zwróci pierwszy (a nie drugi! Tutaj liczenie zaczyna się od 1) element - tj. element, do którego pasuje pierwsza grupa zaznaczona w regexie - tutaj zwróciłoby "Damian",
itd.  
Grupom można nadawać etykietki (nazwy), w regexie pisząc: ?P<nazwa_grupy>, np.:  
```
r"^Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)
```  
Dzięki nazwom grup mogę odwoływać się do danego elementu dopasowania poprzez nazwę grupy, a nie tylko poprzez indeks, na którym znajduje się dany element - wtedy metodzie group() dostarczam nazwę tej grupy jako string - group("first").  
  
## Metoda fullmatch()  
Pozwala na zwrócenie tylko wyniku pasującego do danego wzoru, tj. bez konieczności pisania anchors and boudaries (^, $, \b).  
  
## Metoda re.search()  
Można, zamiast najpierw kompilowania i przypisywania skomilowanego regexa do zmiennej, a potem do tej zmiennej stosowania search() lub findall(), użyć re.search(), któremu dostarczamy nasz regex oraz string, który chcemy przeszukać:  
```
re.search(r"\d{3} \d{3}-\d{4}", "Call me at 415 555-4242")
```
Można również na koniec dodać jeszcze ".group()".  
Różnicą jest to, że jeśli będziemy używać później naszego wzoru (regexa), to w omawianym przypadku nie mam żadnej zmiennej, której można łatwo użyć.
