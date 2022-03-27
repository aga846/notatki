## Dodawanie navbar  
Do tagu nav trzeba dodać klasę np. "navbar navbar-light bg-light".  
"navbar-light" odnosi się do tekstu, a nie do tła. Do tła odnosi się "bg-light".  
W tagu a należy dodać klasę "navbar-brand".  
  
## Dodawanie kolejnych linków  
Można dodać ul i kolejne li, ale łatwiej jest dodać div i w nim dawać kolejne a. Divovi nadaję klasę "navbar-nav". Tagom a daję klasę "nav-item nav-link".  
Niektórym a można dodać atrybut "active" lub "disabled" (właściwie to podklasa, nie atrybut).  
Wtedy te a, które dodałam w divie, będą w kolumnie, a nie w rzędzie obok głównego, pierwszego przycisku (który dodałam w pierwszym a w podrozdziale "Dodawanie navbar").  
Żeby temu zapobiec, należy cały ten div z klasą "navbar-nav" umieścić w divie z klasą "collapse navbar-collapse".  
Tylko że wtedy te linki będą schowane - nie będzie ich w ogóle widać - chyba że dodamy do głównego tagu nav podklasę "navbar-expand-lg" (lg wskazuje na rozmiar ekranu, od którego elementy mają się rozwinąć, tj. być w rzędzie, a nie schowane).
Jeśli chcę, żeby w mniejszych rozmiarach można było się do nich dostać w rozwijanej liście, muszę dodać toggler.  
  
### Dodawanie togglera  
Chodzi o "hamburgerowy przycisk" - rozwijana lista ze schowanymi tagami a (przyciskami nawigującymi).  
  
Muszę dodać przycisk o klasie "navbar toggler". W środku przycisku dodaję span o klasie "navbar-toggler-icon".  
Póki co toggler się nie rozwija.  
  
Żeby się rozwijał, muszę dodać atrybut "data-target" oraz "data-toggle". Data-toggle ustawiam na "collapse", a "data-target" ustawiam na id obiektu, który chcę rozwijać w togglerze (w moim przypadku div z klasą "collapse", wewnątrz którego znajdują się tagi a).  
  
Do togglera można również dodać np. coś, co się rozwija (ma w sobie "podlinki", formularz).  
  
Można dodać container wewnątrz navbara - wtedy cała zawartość navbara będzie bardziej ściśnięta (będą marginesy po obu stronach).  
  
TRZEBA MIEĆ ZAWARTY SKRYPT JAVASCRIPT.  
  
## fixed  
Domyślnie jest, że jak skroluję stronę, to navbar nie skroluje się razem ze mną (zostaje na górze). Żeby to zmienić, muszę do głównego tagu nav dodać podklasę "fixed-top". Wtedy navbar jedzie razem ze skrolowaniem strony (ciągle jest na górze).  
Może być też na dole strony - "fixed-bottom".  
  
## sticky  
"sticky-top" zrobi to samo, co "fixed-top", ale jest możliwe dodanie czegoś, np. nagłówka, nad navbarem. Wtedy na początku strony nagłówek jest na samej górze, ale wraz ze skrolowaniem, jedzie ze mną tylko navbar.  
