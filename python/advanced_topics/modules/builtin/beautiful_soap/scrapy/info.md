# Co robi scrapy?  
Scrapuje ze stron, ma krótszą składnię od BeautifulSoup.  
Należy utworzyć klasę, która dziedziczy z klasy scrapy.Spider.  
Python podczas egzekwowania pliku będzie szukał konkretnych funkcji - np. parse().  
Należy dać yield, nie return.  
  
article.css(".price_color::text") zrobi to samo, co find przy BS, jest ten sam zamysł, co przy selectowaniu po selektorach CSS.    
extract_first() zrobi to, co get_text().  
  
Dzięki scrapy można od razu zapisać dane do pliku wybranego typu - csv, json. Robimy to przy otwieraniu pliku: w konsoli należy napisać:  
```
scrapy runspider -o books.csv book_scraper.py
```
"books.csv" to nazwa pliku, do którego będziemy zapisywać, a "book_scraper.py" to nazwa pliku, w którym mamy kod.  
  
## Przechodzenie do kolejnej strony  
Trzeba sprawdzić, czy jest następna strona.  
Sprawdzamy, gdzie jest button "next" i bierzemy z niego href.  
Jeśli next istnieje, yieldujemy response.follow, wklejamy do niego url (czyli to, co przypisane do zmiennej "next") i stosujemy funkcję parse. Czyli jeśli istnieje next, to robi to samo dla tej kolejnej strony (ściąga informacje).
