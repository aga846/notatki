import requests
from bs4 import BeautifulSoup
import random

all_quotes = []
base_url = "https://quotes.toscrape.com"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(response.text, "html.parser")
    print(f"Now scraping {base_url}{url}...")
    quotes = soup.select(".quote")

    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
            })

    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None

quote_to_guess = random.choice(all_quotes)
print(f'Here is a quote:\n{quote_to_guess["text"]}')
num_of_guesses = 4
guess = input(f"Who said this? Guesses remaining: {num_of_guesses}. ")
while num_of_guesses > 0:
    if guess != quote_to_guess["author"]:
        num_of_guesses -= 1
        res = requests.get(f'{base_url}{quote_to_guess["bio-link"]}')
        author_page = BeautifulSoup(res.text, "html.parser")
        date = author_page.find(class_="author-born-date").get_text()
        location = author_page.find(class_="author-born-location").get_text()
        print(f"Here's a hint: The author was born on {date} {location}.")
        guess = input(f"Who said this? Guesses remaining: {num_of_guesses}. ")
        if guess != quote_to_guess["author"]:
            num_of_guesses -= 1
            full_name = quote_to_guess["author"]
            print(
                f"Here's a hint: The author's first name starts with {full_name[0]}")
            guess = input(
                f"Who said this? Guesses remaining: {num_of_guesses}. ")
            if guess != quote_to_guess["author"]:
                num_of_guesses -= 1
                print(
                    f"Here's a hint: The author's last name starts with {full_name.split()[1][0]}")
                guess = input(
                    f"Who said this? Guesses remaining: {num_of_guesses}. ")
    if guess == quote_to_guess["author"]:
        print("You guessed correctly! Congratulations!")
    else:
        print(f"Sorry, you've run out of guesses. The answer was {full_name}.")
    answer = input("Would you like to play again (y/n)? ")
    if answer == "n":
        print("OK, goodbye!")
        break
    quote_to_guess = random.choice(all_quotes)
    print(f'Here is a quote:\n{quote_to_guess["text"]}')
    num_of_guesses = 4
    guess = input(f"Who said this? Guesses remaining: {num_of_guesses}. ")
