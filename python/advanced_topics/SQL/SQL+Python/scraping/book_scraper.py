import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape_books(url):
    """Request URL, Initialize BS"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)


# Save data to database

def save_books(all_books):
    """Save to a database"""
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE books 
        (title TEXT, price REAL, rating INTEGER)''')
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()

# Extract data


def get_title(book):
    """Extract title"""
    return book.find("h3").find("a")["title"]


def get_price(book):
    """Extract price"""
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    """Extract rating"""
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    paragraph = book.select(".star-rating")[0]
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]


scrape_books(
    "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
