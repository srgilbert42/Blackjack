class CustomException(BaseException):
	def __init__(self, message = "Default"):
		self.message = message