from typing import List
from src.Card import *
import random

class Deck:
    def __init__(self, numDecks: int = 1) -> None:
        self.cards = []

        for i in range(0, numDecks):
            self.cards += self.makeDefaultDeck()

    def makeDefaultDeck(self) -> List: 
        suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        values = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", 
                  "JACK", "QUEEN", "KING"]
        deck = []

        for i in suits:
            for j in values:
                deck.append(Card(j, i))

        return deck

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

    def getSize(self) -> int:
        return len(self.cards)
   



