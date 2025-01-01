from typing import List
import Card

class Hand:
    def __init__(self, cards: List = []) -> None:
        self.cards = cards

    def addCard(self, card: Card) -> None:
        self.cards.append(card)
        return 

    def toString(self) -> str:
        string = ""
        for card in self.cards:
            string += "[ " + card.toString() + " ] "
        return string

    def getHandValue(self) -> int:
        totalValue = 0
        numAces = 0

        for card in self.cards:
            if card.value == "ACE":
                totalValue += 11
                numAces += 1
            elif card.value == "TWO":
                totalValue += 2
            elif card.value == "THREE":
                totalValue += 3
            elif card.value == "FOUR":
                totalValue += 4
            elif card.value == "FIVE":
                totalValue += 5
            elif card.value == "SIX":
                totalValue += 6
            elif card.value == "SEVEN":
                totalValue += 7
            elif card.value == "EIGHT":
                totalValue += 8
            elif card.value == "NINE":
                totalValue += 9
            elif card.value == "TEN" or card.value == "JACK" or card.value == "QUEEN" or card.value == "KING":
                totalValue += 10
            else:
                pass

        while totalValue > 21 and numAces > 0:
            totalValue -= 10
            numAces -= 1

        return totalValue