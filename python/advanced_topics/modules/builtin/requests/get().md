# Co robi funkcja get  
Funkcja get() wysyła żądanie do strony - tak jak wpisywanie adresu strony w address bar.  
Należy rozróżnić get() od post(). W get() chcemy jedynie dostać się do strony. W post() chcemy coś na niej robić, np. wpisać login i hasło.  

Składnia:  
get(adres_strony)  <- adres musi być poprzedzony https://  

```
import requests

url = "https://google.com"
response = requests.get(url)

print(f"Your request to {url} came back with status code {response.status_code}")
```
