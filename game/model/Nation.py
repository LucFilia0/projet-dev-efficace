class Nation :

	def __init__(self, name : str) :
		self.name = name
		self.populationMax = 0
		self.population = 0
	
	def __str__(self) -> str :
		return f"{self.name} : {self.population}/{self.populationMax}"