from src.CustomException import *

class AmountLowerThanMinimumException(CustomException):
    def __init__(self, message = ""):
        super().__init__(message)
