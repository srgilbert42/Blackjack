from src.CustomException import *

class NotEnoughMoneyException(CustomException):
    def __init__(self, message = ""):
        super().__init__(message)
