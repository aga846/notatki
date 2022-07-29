# Parametry fieldów w modelach  
  
## null  
Ustawienie null na True oznacza, że puste wartości będą przechowywane w bazie danych jako wartość NULL.  
Nie zaleca się stosowania do pól stringowych (CharField/TextField).  
  
## blank  
Ustawienie blank na True spowoduje, że dane pole będzie mogło być zostawione puste.  
  
## choices   
Ustawienie opcji, spośród których można wybrać (nic poza nimi nie można wpisać jako wartość w danym polu).  
  
## default  
Ustawienie wartości domyślnej.  
Jeśli jednocześnie blank=True, to jeśli nic nie podamy, będzie przechowywana ta wartość domyślna.  
  
## help_text  
Pomaga w dokumentacji - można wstawić teksty opisujące, co robi dane pole.  
  
## unique  
To pole musi być unikalne (np. id).  
  
  
# Typy fieldów  
  
## CharField i TextField  
Oba służą do przechowywania stringów, przy czym CharField do krótszych, TextField do dłuższych.  
  
## DateTimeField i DateField  
DateTimeField przyjmuje również parametry czasu, DateField - samą datę.  
  
## IntegerField  
Pole do liczby integer.  
  
## DecimalField  
Liczba zmiennoprzecinkowa.  
Przyjmuje paramety max_digits (ile maksymalnie w sumie cyfr) oraz decimal_places (ile liczb po przeciwnku). Max_digits musi być zawsze większe od decimal_places.  
