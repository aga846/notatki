## Wielkość czcionki  
Wielkość czciconki zmienia się za pomocą atrybutu "font-size". Można ją wyrażać na różne sposoby, np.  
px, mm, cm.  
Jednostki, w których podajemy, mogą być względne (m.in. em, rem, vh, vw, %) lub bezwzględne (px, pt, cm, in, mm).
  
## Styl czcionki  
To, czy mogę wybrać daną czcionkę, zależy od tego, czy mam ją zainstalowaną na swoim urządzeniu.  
Istnieją pewne podstawowe czcionki, które raczej są dostępne u każdego (na stronie css.fontstack.com są wypisane czcionki wraz z informacją, na jakim % urządzeń z win lub mac są dostępne).  
Jeśli użyję mało powszechnej czcionki, muszę wiedzieć, że niektórym (lub wielu) użytkownikom tekst nie wyświetli się w takiej czcionce, jak ustawiłam.  
Styl czcionki zmienia się za pomocą atrybutu "font-family".
```
h1 {font-family: Arial}
```
  
Mogę zabezpieczyć się przed sytuacją, że użytkownik nie będzie miał danej czcionki - po przecinku wtedy piszę kolejną czcionkę (lub kolejne czcionki), która ma być użyta w razie braku pierwszej wymienionej. Mogę też zamiast tego podać również rodzinę czcionek, np. sans-serif, fantasy. Mogę też nie wybierać konkretnej czcionki, tylko od razu wskazać rodzinę czcionek (i wtedy zostanie wybrana jedna z tej rodziny).
