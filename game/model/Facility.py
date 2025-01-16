from game.model.Resources import Resources
from model.List import List
from random import random

class _Facility :

	def __init__(self, name : str, cost : Resources, gain : Resources|int|None, frequency : int) :
		self.name = name
		self.cost = cost
		self.gain = gain
		self.frequency = frequency
		
		self.state = 0
	
	def promptSummary(self) -> None :
		print(f"{self.name.ljust(20)}| {self.state}/{self.frequency}")

	def promptDetails(self) -> None :
		print(
			f"{self.name}\n\n"
			f"Coût :                    [ {self.cost}]\n"
			f"Gain :                    [ {self.gain}] / {self.frequency} tour(s)\n"
		)
	
	def getGain(self) -> Resources|int|None :
		if self.frequency != 0 :
			if self.state == self.frequency :
				self.state = 1
				return self.gain
			else :
				self.state += 1
				return None

class Baracks(_Facility) :

	def __init__(self) :
		super().__init__("Caserne", Resources(), None, 0)
		self.troups = List()

	def getGain(self) -> Resources|int|None :
		return None
	
	def __str__(self) -> str :
		return f"Barack | CAP {self.troups.len}/4"

class Farm(_Facility) :

	def __init__(self) :
		super().__init__("Ferme", Resources(), Resources(food=6), 3)

class Habitation(_Facility) :

	def __init__(self) :
		super().__init__("Habitation", Resources(), None, 0)
		self.given = False
	
	def getGain(self) -> Resources|int|None :
		if not self.given :
			self.given = True
			return 4
		return None

class Mine(_Facility) :

	def __init__(self) :
		super().__init__("Mine", Resources(), None, 2)
		self.stoneRatio = (random() * 10) % 5 + 1
		self.ironRatio = (random() * 10) % 5 + 1

	def getGain(self) -> Resources|int|None :
		return Resources(stone=self.stoneRatio, iron=self.stoneRatio)

class Sawmill(_Facility) :

	def __init__(self) :
		super().__init__("Scierie", Resources(), Resources(wood=5), 1)