from _pytest.config import filter_traceback_for_conftest_import_failure
from src.Card import *
from typing import List

class Player:
    def __init__(self, name: str = "", hand: List = [], money: float = 0.0, isStanding: bool = False) -> None:
        self.name = name
        self.hand = hand
        self.money = money
        self.isStanding = isStanding

    def addMoney(self, amount: float) -> None:
        self.money += amount

    # Returns False is given amount bankrupts player, returns True otherwise
    # TODO : change to raise error instead of returning value
    def subtractMoney(self, amount: float) -> bool:

        # if bankrupted, set money to zero instead of negative
        if self.money < amount:
            self.money = 0
            return False
        else:
            self.money = self.money - amount
            return True

    def addCardToHand(self, card: Card) -> None:
        self.hand.append(card)

    def getHand(self) -> str:
        string = ""
        for card in self.hand:
            string += "[ " + card.toString() + " ] "
        return string


    def toString(self) -> str:
        return " Name: " + self.name + "\nMoney: " + str(self.money) + "\n Hand: " + self.hand.toString() + "\n Value: " + str(self.hand.getHandValue())
    
    def holdingBustedHand(self) -> bool:
        if self.getHandValue() > 21:
            return True
        else:
            return False

    def getHandValue(self) -> int:
        totalValue = 0
        numAces = 0

        for card in self.hand:
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

    def isStanding(self) -> bool:
        return self.isStanding

    def resetState(self) -> None:
        self.isStanding = False

    def getFirstPositionCard(self) -> Card:
        return self.hand[0]

    def setDefaultHand(self) -> None:
        self.hand.cards = []

    def handIsSoft(self) -> bool:
        # for card in self.hand:
        #     if card.value == "ACE":
        #         return True
        # return False

        totalValue = 0
        numAces = 0

        for card in self.hand:
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

        if numAces > 0:
            return True
        else:
            return False

    def handIsSplittable(self) -> bool:
        if len(self.hand) == 2:
            if self.hand[0].value == self.hand[1].value:
                return True
        return False



