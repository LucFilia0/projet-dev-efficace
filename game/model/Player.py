class Player :

	def __init__(self, name : str) :
		self.name = name
		self.nation = None
		self.technoTree = None
	
	def __str__(self) -> str :
		return self.name