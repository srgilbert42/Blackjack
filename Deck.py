from typing import List
import Card
import random

class Deck:
    def __init__(self, cards: List = []) -> None:
        self.cards = cards
        return

    # TODO change constructor to accept an integer which will represent the number of default decks that will form the deck.
    # i.e., if a 3 is given, then the deck will contain 3 default decks

    def makeDefaultDeck(self) -> None: 
        suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        values = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", 
                  "JACK", "QUEEN", "KING"]
        deck = []

        for i in suits:
            for j in values:
                deck.append(Card.Card(i, j))

        self.cards = deck
        return

    def shuffle(self) -> None:
        self.cards = random.sample(self.cards, len(self.cards))

    def toString(self) -> str:
        string = ""
        count = 1

        for card in self.cards:
            string += str(count) + " " + card.toString() + "\n"
            count += 1

        return string

    def dealCard(self) -> Card:
        return self.cards.pop()
   



