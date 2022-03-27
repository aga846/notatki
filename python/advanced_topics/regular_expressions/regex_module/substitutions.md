# Substitutions  
Służą do wymienienia jakiegoś słowa/litery/wyrażenia na inne.  
UWAGA! Należy sprawdzić, czy w danym przypadku nie będzie prościej użyć jakiejś metody ze stringa, np. replace().  
  
## Metoda sub()  
Do wymieniania słów służy metoda sub(). Stosuje się ją po kompilacji wzoru (regexa). Jako argumenty daje się słowo, na które chce się wymienić oraz słowo, które chce się wymienić:  
```
import re
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.I)
result = pattern.sub("REDACTED", text)
print(result)      # Last night REDACTED and REDACTED murdered REDACTED
```  
  
W powyższym przykładzie wszystkie wyrażenia pasujące do opisanego wzoru zastępowane są słowem "REDACTED".  
Można również zastąpić samo nazwisko - słowem REDACTED albo tylko jego pierwszą literą (tj. "Last night Mrs. D and Mr. W murdered Ms. C"). Należy wykorzystać do tego capture groups (grupy zgrupowane dzięki nawiasom okrągłym - odnoszenie się do nich po indeksie lub po nazwie):    
```
result = pattern.sub("\g<1> REDACTED", text)
```
  
\g<1> oznacza, że grupa pierwsza będzie napisana normalnie (grupa pierwsza to Mr.|Mrs.|Ms.), a dopiero reszta stringa pasującego do wzoru będzie zastąpiona słowem "REDACTED".  
  
W celu zastąpienia nazwiska tylko jego pierwszą literą, należy wyselekcjonować tę pierwszą literę już w regexie - umieścić ją w osobnej grupie:  
```
pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.I)
result = pattern.sub("\g<1> \g<2>", text)
```
  
  
### Przykład ze zmianą kolejności w stringu  
Mając listę "books" z tytułami książek oraz datą ich wydania w nawiasie (wg wzoru: "Significant Others (1987)"), chcę zmienić tę listę w taki sposób, żeby na początku była data - ale bez nawiasów, a potem po myślniku tytuł (wg wzoru: "1987 - Significant Others"); dodatkowo książki mają być posegregowane chronologicznie.  
```
fixed_titles = []
pattern = re.compile(r"(^[\w ]+) \((\d{4})\)")
for book in books:
    result = pattern.sub("\g<2> - \g<1>", book)
    fixed_titles.append(result)
fixed_titles.sort()
```  
- tworzę pustą listę fixed_titles,  
- tworzę pattern - to, co chcę wyszukać: ilekolwiek słów zakończonych spacją, spacja, rok w nawiasach,  
- w pętli: dla każdej książki na liście "books" zamieniam book wg wzoru: grupa druga (czyli rok bez nawiasów), myślnik, grupa pierwsza,   
- dodaję książki wg powyższego wzoru do nowej listy,  
- sortuję nową listę - teraz sortuje się wg daty, bo jest ona pierwsza.
