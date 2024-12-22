from game.model.Resources import Resources

class _Facility :

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

class Baracks(_Facility) :

	def __init__(self) :
		super().__init__("Caserne", Resources(wood=4, stone=6))

class Farm(_Facility) :

	def __init__(self) :
		super().__init__("Ferme", Resources(wood=4, stone=2, food=1), Resources(food=6), 3, 1)

class Habitation(_Facility) :

	def __init__(self) :
		super().__init__("Habitation", Resources(wood=4, stone=2), 4, 0, 1)
	
	def gain(self) -> Resources|int|None :
		if super().state == 0 :
			super().state = 1
			return super().gain

class Mine(_Facility) :

	def __init__(self) :
		super().__init__("Mine", Resources(wood=8), 0, 2, 2)

class Sawmill(_Facility) :

	def __init__(self) :
		super().__init__("Scierie", Resources(wood=12, stone=6, iron=1), Resources(wood=2), 1, 2)