# Czym jest status_code  
Status_code to atrybut, który posiada każde zapytanie wysyłane do strony.  Są 3 rodzaje status_code:  
- 2xx, jeśli strona otwiera się prawidłowo (np. 200),  
- 3xx, jeśli następuje przekierowanie na inną stronę,  
- 4xx, jeśli występuje błąd (po naszej stronie),  
- 5xx, jeśli występuje błąd (po stronie serwera, nie nasza wina).  
Ilustruje to przykład z pliku "get()":  
  
```
import requests

url = "https://google.com"
response = requests.get(url)

print(f"Your request to {url} came back with status code {response.status_code}")
```
