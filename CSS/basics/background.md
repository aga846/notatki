# Obrazek jako tło  
Jeśli chcę ustawić obrazek jako tło, muszę podać jego ścieżkę:  
  
```
background-image: url("adres-URL");
```
  
## background-size  
Można dostosować wielkość obrazka (czy ma być rozciągnięty czy przycięty itp.), np.:  
  
```
background-size: contain;
background-size: cover;
background-size: auto;
```
  
- contain - wyskalowanie obrazka, żeby był tak duży jak to możliwe, bez obcinania i rozciągania (dlatego jeśli jest za mały, zostanie powtórzony),  
- cover - wyskalowanie obrazka, żeby był tak duży jak to możliwe, bez rozciągania, ale z obcinaniem.  
  
## background-repeat  
Można ustawić, czy obrazek ma się powtarzać jako tło oraz ile razy.  
  
## background-position  
Można ustawić pozycję obrazka jako tła.  
```
background-position: bottom;
```
Przy bottom - obrazek zaczyna się od dołu, przy top - od góry.  
  
## background  
Połączenie wszystkich własności background (ustawianie wszystkich naraz).  
Generalnie kolejność podawania własności nie ma znaczenia, z wyjątkiem ustawiania rozmiaru - rozmiar powinien być podany zaraz po pozycji, ze znakiem "\/" pomiędzy nimi:  
```
background: "adres-URL" center/80% no-repeat;
background: "adres URL" center/cover;
```
  
## Wiele teł  
Można mieć więcej niż jedno tło, np. jeśli obrazek ustawię na 40%, bez powtórek, to za tym obrazkiem mogę chcieć mieć inne tło:  
```
background: "adres-URL" center/40% no-repeat blue;
```
Wtedy za obrazkiem będzie tło w kolorze niebieskim.  
  
