from typing import List
import Hand
import Card

class Player:
    def __init__(self, name: str, hand: Hand , money: float) -> None:
        self.name = name
        self.hand = hand
        self.money = money

    def addMoney(self, amount: float) -> None:
        self.money = self.money + amount
        return 

    # Returns False is given amount bankrupts player, returns True otherwise
    def subtractMoney(self, amount: float) -> bool:

        # if bankrupted, set money to zero instead of negative
        if self.money < amount:
            self.money = 0
            return False
        else:
            self.money = self.money - amount
            return True

    def addCardToHand(self, card: Card) -> None:
        self.hand.addCard(card)
        return

    def getHand(self) -> str:
        return self.hand.toString()

    def toString(self) -> str:
        return " Name: " + self.name + "\nMoney: " + str(self.money) + "\n Hand: " + self.hand.toString() + "\n Value: " + str(self.hand.getHandValue())



