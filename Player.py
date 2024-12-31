from typing import List
import Hand
import Card

class Player:
    def __init__(self, hand: Hand = Hand(), money: float = 0.0):
        self.hand = hand
        self.money = money

    def addMoney(self, amount: float) -> None:
        self.money = self.money + amount
        return 

    # Returns False is given amount bankrupts player, returns True otherwise
    def subtractMoney(self, amount: float) -> bool:
        if self.money < amount:
            self.money = 0
            return False
        else:
            self.money = self.money - amount
            return True

    def addCardToHand(self, card: Card) -> None:
        self.hand.addCard(card)
        return


