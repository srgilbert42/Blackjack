from typing import List
import Card

class Hand:
    def __init__(self, cards: List):
        self.cards = cards

    def addCard(self, card: Card) -> None:
        self.cards.append(card)
        return 
