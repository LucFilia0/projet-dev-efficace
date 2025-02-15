from model.List import List
from game.model.Facility import _Facility, Baracks, Habitation, Farm, Forge, Temple, Altar, HunterHood, Mine, Sawmill
from game.model.Troups import _Troup

class City :

	def __init__(self, name : str) :
		self.name = name
		self.maxPopulation = 0
		self.population = 2
		self.facilities = List()
	
	def addFacility(self, facility : _Facility) -> bool :
		if self.checkPopulation() :
			self.facilities.add(facility)
			if type(facility) is type(Habitation()) :
				self.maxPopulation += facility.getGain()
			else :
				self.population += 1
				facility.state += 1
			return True
		return False
	
	def checkPopulation(self) -> bool :
		return self.population < self.maxPopulation

	def contains(self, thing : str) -> bool :
		match(thing):
			case "Habitation":
				facility = Habitation()
			case "Ferme":
				facility = Farm()
			case "Caserne" :
				facility = Baracks()
			case "Mine" :
				facility = Mine()
			case "Forge" :
				facility = Forge()
			case "Scierie" :
				facility = Sawmill()
			case "Cabane de chasseur" :
				facility = HunterHood()
			case "Temple" :
				facility = Temple()
			case "Autel" :
				facility = Altar()
		return self.facilities.containsInstanceOf(facility)

	def returnFirstAvailableBaracks(self) -> Baracks|None :
		baracks = self.facilities.onlyInstanceOf(Baracks())
		firstBaracks = None
		i = 0
		while i < baracks.len and firstBaracks is None :
			b = baracks.get(i)
			if b.troups.len < 4 :
				firstBaracks = b
			i += 1
		return firstBaracks

	def addTroup(self, troup : _Troup) -> None :
		b = self.returnFirstAvailableBaracks()
		if b is not None and self.checkPopulation() :
			b.troups.add(troup)
			self.population += 1