# Authentication  
Sprawdzanie, czy dany użytkownik istnieje w bazie danych (podajemy username i hasło).
  
# Authorization  
Danie jakichś przywilejów konkretnemu użytkownikowi. Sprawdzamy, czy użytkownik ma wszystkie przywileje, żeby oglądać dany rekord, zapisywać, w ogóle używać aplikacji.  
  
# Rodzaje authentication  
W dokumentacji są różne rodzaje, najbardziej popularna: TokenAuthentication.  
  
# TokenAuthentication  
Gdy wysyłamy żądanie username i password, zwracamy token użytkownika. Żeby użytkownik mógł używać mojej aplikacji, musi używać tego tokena.  
  
## Tworzenie tokena  
Należy do INSTALLED_APPS pozycję rest_framework.authtoken.  
Trzeba zrobić migracje.  
Teraz na adminie jest nowa sekcja "AUTH TOKEN", gdzie znajdują się wszystkie wygenerowany tokeny użytkownika.  
Wchodzę w tokeny i tworzę nowy, wybierając użytkownika. Teraz za każdym razem, kiedy ten użytkonik będzie chciał korzystać z mojego API, będzie musiał podać ten token.  
Trzeba jeszcze dodać url (do głównych urls), żeby zrobić autentykację użytkownika.  
```
from rest_framework.authtoken import views 

urlpatterns += [
  path('api-token-auth/', views.obtain_auth_token)]
```
Path można zrobić jaki chcemy.  
Teraz, wchodząc na tę stronę i POSTując username i password danego użytkownika (który ma stworzony token), dostanę w odpowiedzi ten token.  
  
## Tworzenie restrykcji co do używania API (permissions)  
Tworzenie domyślnego permission.  
W settings do REST_FRAMEWORK dodaję  
```
'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated']
```
Oznacza to, że żeby użyć mojego API, user musi być autentykowany - zalogowany.  
Teraz już nie mogę dostać się po prostu do API, dopóki nie wyślę informacji o użytkowniku, czyli wysyłając żądanie do strony, w Headers muszę jako key podać "Authorization", a key "Token cały_token(ciąg znaków)".  
Teraz w views muszę ustawić  
```
from rest_framework.authentication import TokenAuthentication

# w konkretnym ViewSet 
authentication_classes = [TokenAuthentication]
```
  
## Inne metody oprócz IsAuthenticated  
IsAuthenticated oznacza, że żeby coś zobaczyć, user musi być zalogowany.  
Można zmienić na:  
- AllowAny (pozwolenie wszystkim na dostęp),  
- IsAdminUser (czy is_staff danego użytkownika jest True),  
- IsAuthenticatedOrReadOnly (bez autentykacji mogę robić GET, ale nie mogę robić POST, PUT ani DELETE - do tego musiałabym podać token).  
Te metody mogę ustawić jako wersję domyślną dla całej aplikacji, ale w konkretnych modelach mogę dawać inne restrykcje.  
  
### Zmiana permissions na poziomie modeli (w views)  
W konkretnym ViewSet dodaję np.  
```
from rest_framework.persmissions import IsAuthenticated

persmission_classes = [IsAuthenticated]
```
Czyli w głównym ustawieniu w settings mam AllowAny, ale dla tego konkretnego ViewSet mam IsAuthenticated (wszystkie inne ViewSet będą dostępne, oprócz tego jednego).  
  
### DjangoModelPermissions  
Dodaję DjangoModelPermissions do persmission_classes w danym ViewSet, importując je wcześniej z rest_framework.permissions.  
  
Jak wejdę na adminie w danego usera, to na dole mam coś takiego, jak "User permissions", gdzie do każdego modelu mam informacje, jakie są dostępne persmissions ("Available user persmissions"). Zaraz obok mam "Chosen user permissions", do których mogę przerzucać permissions z tych dostępnych - w taki sposób wybieram, do czego ten user jest uprawniony. I to są właśnie te DjangoModelPermissions.
