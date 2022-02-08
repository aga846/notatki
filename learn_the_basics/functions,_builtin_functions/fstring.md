# Co robi funkcja f  
Funkcja f"" formatuje string.  
W "" można wstawiać wszystko i przeformatuje to na string. Jeśli chce się dodać np. zmienną, listę, słownik itd., należy umieścić je w {}.
  
```
first_date = "03.12.2016"
aga = "Aga Jaskolska"
damian = "Damian Jaskolski"
year = 2016
actual_year = 2022

print(f"{aga} i {damian} są parą od {first_date}, czyli są razem już {actual_year-year} lat")

# 
Aga Jaskolska i Damian Jaskolski są parą od 03.12.2016, czyli są razem już 6 lat
```
