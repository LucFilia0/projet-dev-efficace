from game.model.Facility import Facility
from model.List import List
from game.view.prompt import padNumber
from game.model.Resources import Resources
from game.view.prompt import clear
from game.view.prompt import userInputInt

class Player :

	def __init__(self, name : str) :
		self.name = name
		self.city = None
		self.resources = Resources()
		self.facilities = List()
		self.technoTree = None
	
	def __str__(self) -> str :
		return self.name
				
	def createFacility(self, facility : Facility) -> None :
		if self.resources.isGreaterOrEqualThan(facility.cost) :
			self.facilities.add(facility)
		else :
			promptSep(f"Echec : Créer {facility.type}")
			userInputInt("Vous n'avez pas les ressources suffisantes pour effectuer cette action...\n0 - Retour", 0, 0)
			self.promptBoard