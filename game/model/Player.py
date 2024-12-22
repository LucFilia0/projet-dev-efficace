from game.model.Facility import _Facility
from game.model.Facility import Habitation
from game.model.Facility import Farm
from model.List import ListDeCon
from game.view.prompt import padNumber
from game.model.Resources import Resources
from game.view.prompt import clear
from game.view.prompt import userInputInt

from typing import cast

class Player :

	def __init__(self) :
		self.name = None
		self.city = None
		self.resources = Resources()
		self.facilities = ListDeCon()
		self.technoTree = None
	
	def __str__(self) -> str :
		return self.name

	def getFacility(self, index : int) -> _Facility :
		return cast(_Facility, self.facilities.get(index))

	def loadStartingRessources(self) -> None :
		self.facilities.add(Habitation)
		self.facilities.add(Farm)
				
	def createFacility(self, facility : _Facility) -> None :
		if self.resources.isGreaterOrEqualThan(facility.cost) :
			self.facilities.add(facility)
		else :
			promptSep(f"Echec : Créer {facility.type}")
			userInputInt("Vous n'avez pas les ressources suffisantes pour effectuer cette action...\n0 - Retour", 0, 0)
			self.promptBoard