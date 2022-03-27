# Czym jest text  
Text wyświetla stronę w "języku komputerów". Jest to bardzo dużo informacji, dlatego lepiej używać API.  
  
```
import requests

url = "https://google.com"
response = requests.get(url)
print(response.text)
```
