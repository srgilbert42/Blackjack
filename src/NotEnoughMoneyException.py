from src.CustomException import *

class NotEnoughMoneyException(CustomException):
    def __init__(self, message = "") -> None:
        super().__init__(message)
