# Ograniczenia w formularzu  
Mogę wymagać, żeby np. użytkownik wpisał minimalną ilość znaków.  
   
## required  
Required to atrybut w input. Jeśli go dam, nie będzie można zasubmitować formularza, jeśli dane pole będzie niewypełnione.  
  
## minlength i maxlength  
Min i max to atrybuty w input, oznaczają minimalną i maxymalną liczbę znaków.  
```
<label for="username">Username</label>
<input type="text" id="username" name="username" minlength="5" maxlength="20">
```
  
## min i max  
Odnosi się do numerów.  
  
## Domyślne ograniczenia  
Są pewne regular expressions istniejące dla pewnych inputów, np. dla type="email" - jeśli damy required, automatycznie sprawdza, czy jest @ w adresie email. Sprawdza też np. url.  
Można skorzystać z atrybutu "pattern", żeby ustawić własny wzór.
