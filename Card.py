class Card:
    def __init__(self, suit: str = "Default", value: str = "Test", status: str = "Visible") -> None:
        self.suit = suit
        self.value = value
        self.status = status

    def toString(self) -> str:
        return self.value + " of " + self.suit

