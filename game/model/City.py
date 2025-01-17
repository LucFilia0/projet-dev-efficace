from model.List import List
from game.model.Facility import _Facility
from game.model.Facility import Baracks
from game.model.Facility import Habitation
from game.model.Soldier import _Soldier

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
				facility = SawMill()
			case "Cabane de chasseur" :
				facility = HunterHood()
			case "Temple" :
				facility = Temple()
			case "Autel" :
				facility = Altar()
		return self.facilities.containsInstanceOf(facility)

	def promptBaracks(self) -> None :
		baracks = self.facilities.onlyInstanceOf(Baracks())
		for i in range(baracks.len) :
			b = baracks.get(i)
			print(f"Caserne | {b.troups.len}/4")
			for j in range(b.troups.len) :
				print(f"\t{b.troups.get(j)}")
	
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

	def addSoldier(self, soldier : _Soldier) -> None :
		b = self.returnFirstAvailableBaracks()
		if b is not None and self.checkPopulation() :
			b.troups.add(soldier)
			self.population += 1