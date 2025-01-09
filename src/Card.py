class Card:
    def __init__(self, value: str = "Default", suit: str = "Test", status: str = "Visible") -> None:
        self.value = value
        self.suit = suit
        self.status = status

    def toString(self) -> str:
        return self.value + " of " + self.suit

    def getValue(self) -> str:
        return self.value