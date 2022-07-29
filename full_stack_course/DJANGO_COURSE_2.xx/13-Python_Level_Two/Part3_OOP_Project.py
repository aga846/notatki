#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.allcards = [(s, r) for s in suite for r in ranks]

    def shuffle_deck(self):
        shuffle(self.allcards)

    def split_in_half(self):
        l = len(self.allcards) // 2
        return (self.allcards[0:l], self.allcards[l:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, deal):
        self.deal = deal

    def __repr__(self):
        return (f"Contains {len(self.deal)} cards.")

    def add_card(self, added_cards):
        self.deal.extend(added_cards)

    def remove_card(self):
        return self.deal.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed: {drawn_card}")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.deal) < 3:
            return self.hand.deal
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards

    def check(self):
        """Returns number of cards left on the Player's hand"""
        return len(self.hand.deal)


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
deck = Deck()
deck.shuffle_deck()
print(deck)
half1, half2 = deck.split_in_half()

hand1 = Hand(half1)
hand2 = Hand(half2)

name1 = input("Player 1, what is your name? ")
player1 = Player(name1, hand1)

name2 = input("Player 2, what is your name? ")
player2 = Player(name2, hand2)

total_rounds = 0
war_count = 0

while (player1.check()) and (player2.check()):
    total_rounds += 1
    print(f"{player1.name} has the count of: {player1.check()} cards.")
    print(f"{player2.name} has the count of: {player2.check()} cards.")

    table_cards = []

    player1_card = player1.play_card()
    player2_card = player2.play_card()
    table_cards.append(player1_card)
    table_cards.append(player2_card)

    if player1_card[1] == player2_card[1]:
        war_count += 1
        print("War!!!")
        table_cards.extend(player1.remove_war_cards())
        table_cards.extend(player2.remove_war_cards())

        player1_card = player1.play_card()
        player2_card = player2.play_card()
        table_cards.append(player1_card)
        table_cards.append(player2_card)

        if ranks.index(player1_card[1]) > ranks.index(player2_card[1]):
            player1.hand.add_card(table_cards)
        else:
            player2.hand.add_card(table_cards)

    else:
        if ranks.index(player1_card[1]) > ranks.index(player2_card[1]):
            player1.hand.add_card(table_cards)
        else:
            player2.hand.add_card(table_cards)

print(f"Game over, number of rounds: {total_rounds}")
print(f"A war happened {war_count} times")
player1_cards = player1.check()
player2_cards = player2.check()
max(player1_cards, player2_cards)
print(f"{max(player1_cards, player2_cards)} won.")
