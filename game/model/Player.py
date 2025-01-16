from game.model.Facility import _Facility
from game.model.Facility import Habitation
from game.model.Facility import Farm
from model.List import ListDeCon
from game.view.prompt import padNumber
from game.model.Resources import Resources

class Player :

	def __init__(self) :
		self.name = None
		self.city = None
		self.resources = Resources()
		self.technoTree = None
	
	def __str__(self) -> str :
		return self.name

	def loadStartingResources(self) -> None :
		self.city.facilities.add(Habitation()) # Je suis une merde T-T
		self.city.facilities.add(Farm())
		self.resources.add(Resources(wood=10, stone=5, food=10)) # TODO
	
	def collectResources(self) -> None :
		length = self.city.facilities.len
		for i in range(length) :
			gain = self.city.facilities.get(i).getGain()
			if isinstance(gain, int) :
				self.city.maxPopulation += gain # Case of habitations
			else :
				self.resources.add(gain)
	
	def consumeFood(self) -> None :
		self.resources.food -= self.city.population
		if self.resources.food < 0 :
			self.resources.sub(Resources(domination=1, wealth=1, knowledge=1)) # TODO Change