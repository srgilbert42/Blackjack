class Card:
    def __init__(self, suit: str = "Default", value: str = "Test"):
        self.suit = suit
        self.value = value

    def toString(self) -> str:
        return self.value + " of " + self.suit

