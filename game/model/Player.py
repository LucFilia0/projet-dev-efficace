class Player :

	def __init__(self, name : str) :
		self.name = name
		self.nation = None
	
	def __str__(self) -> str :
		return self.name