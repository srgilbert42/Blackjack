from abc import abstractclassmethod
from src import HouseRules
from src.Card import *
from src.Player import *
from src.Deck import *
from typing import List
from src.CountLogic import *
from src.HouseRules import *

class CountAI:
    def __init__(self) -> None:
        self.runningCount = 0

    def getCountOfCard(card: Card) -> int:
        if card.getValue() == "TWO" or card.getValue() == "THREE" or card.getValue() == "FOUR" or card.getValue() == "FIVE" or card.getValue == "SIX":
            return 1
        elif card.getValue() == "TEN" or card.getValue() == "JACK" or card.getValue() == "QUEEN" or card.getValue() == "KING":
            return -1
        else:
            return 0

    def getRunningCount(self) -> int:
        return self.runningCount

    def updateRunningCount(self, card: Card) -> None:
        self.runningCount += self.getCountOfCard(card)

    def getTrueRunningCount(self) -> float:
        return self.getRunningCount() / HouseRules.NUM_DECKS_IN_SHOE

    