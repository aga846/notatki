# Czym są headers  
Headers to dodatkowe informacje o nadawcy żądania wysłanego do strony internetowej - na temat tego, jakiego typu danych oczekuje nadawca. To "metadane" na temat żądania.  

```
import requests

url = "https://google.com"
response = requests.get(url)
print(response.headers)
```
