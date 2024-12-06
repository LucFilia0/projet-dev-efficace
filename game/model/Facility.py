from game.model.Resources import Resources

class Facility :

	def __init__(self, name : str, cost : Resources, gain : Resources|int, frequency : int, constructionTime : int) :
		self.name = name
		self.cost = cost
		self.gain = gain
		self.frequency = frequency
		self.constructionTime = constructionTime
		
		self.state = 0
	
	def gain(self) -> Resources|int|None :
		self.state += 1
		self.state % self.frequency
		if self.state == self.frequency - 1 :
			return self.gain
		else :
			return None