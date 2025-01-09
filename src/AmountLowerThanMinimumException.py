from src.CustomException import *

class AmountLowerThanMinimumException(CustomException):
    def __init__(self, message = "") -> None:
        super().__init__(message)
