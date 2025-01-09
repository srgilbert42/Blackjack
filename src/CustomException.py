class CustomException(BaseException):
	def __init__(self, message = "Default") -> None:
		self.message = message