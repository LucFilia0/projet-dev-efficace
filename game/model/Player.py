from game.view.prompt import promptSep

class Player :

	def __init__(self, name : str) :
		self.name = name
		self.nation = None
		self.technoTree = None
	
	def __str__(self) -> str :
		return self.name
	
	def promptBoard(self) -> None :
		promptSep(self)
		print(f"Nation de {self.nation.name}")