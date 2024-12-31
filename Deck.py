from typing import List
import Card

class Deck:
    def __init__(self, cards: List = []):
        self.cards = cards
        pass

    def makeDefaultDeck(self) -> None: 
        suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        values = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", 
                  "JACK", "QUEEN", "KING"]
        _cards = []
        suitCount = 0
        valueCount = 0

        for i in range(0, 52):
            _cards.append(Card(suits[suitCount], values[valueCount]))
            suitCount += 1
            valueCount += 1

            if suitCount == 4:
                suitCount = 0
            if valueCount == 13:
                valueCount = 0
        self.cards = _cards



