from game.model.Facility import Facility
from model.List import ListDeCon
from game.view.prompt import padNumber
from game.model.Resources import Resources
from game.view.prompt import clear
from game.view.prompt import userInputInt

class Player :

	def __init__(self, name : str) :
		self.name = name
		self.city = None
		self.resources = Resources()
		self.facilities = ListDeCon()
		self.technoTree = None
		self._initBonusGains()
	
	def __str__(self) -> str :
		return self.name
				
	def createFacility(self, facility : Facility) -> None :
		if self.resources.isGreaterOrEqualThan(facility.cost) :
			self.facilities.add(facility)
		else :
			promptSep(f"Echec : Créer {facility.type}")
			userInputInt("Vous n'avez pas les ressources suffisantes pour effectuer cette action...\n0 - Retour", 0, 0)
			self.promptBoard
	
	def _initBonusGains(self):
		self.bonusGains = {
			"domination" : 0,
			"wealth" : 0,
			"knowledge" : 0,
			"wood" : 0,
			"stone" : 0,
			"gold" : 0,
			"iron" : 0,
			"food" : 0,
		}