from game.model.Resources import Resources

class Facility :

	def __init__(self, name : str, cost : Resources, gain : Resources) :
		self.name = name
		self.cost = cost
		self.gain = gain
		self.constructTime = constructTime
	
	def __str__(self) -> str :
		return f"{self.name} ({self.cost} | {self.gain}/ tour | {self.constructTime})"