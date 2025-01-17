from game.model.Facility import _Facility, Habitation, Farm
from game.model.Resources import Resources
from game.model.tree.Tree import TechnologyTree, ActionTree
from game.model.tree.TreeNode import TechnologyNode
from game.view.prompt import userInputInt, promptStatus

class Player :
	"""
	This class represents a player which is playing the game.
	A player has a name, a city, resources, technologies and bonuses.
	"""

	def __init__(self) :
		self.name = None
		self.city = None
		self.resources = Resources(wood=10, stone=5, food=10, knowledge=3) #Starting resources
		self.technoTree = TechnologyTree(self)
		self.actionTree = ActionTree(self)
		self.bonus = Resources()
	
	def __str__(self) -> str :
		return self.name

	def startTurn(self) -> None :
		promptStatus(None)
		userInputInt(f"À toi de jouer, {self.name} !\n[0] Commencer", 0, 0)
		self.actionTree.navigate()

	# RESOURCES

	def createStartingFacilities(self) -> None :
		self.city.facilities.add(Habitation()) # Je suis une merde T-T
		self.city.facilities.add(Farm())
	
	def collectResources(self) -> None :
		"""
		Collects all the resources generated by each of its facilities.
		This function is called each turn.
		"""
		length = self.city.facilities.len
		for i in range(length) :
			gain = self.city.facilities.get(i).getGain()
			if isinstance(gain, int) :
				self.city.maxPopulation += gain # Case of habitations
			else :
				self.resources.add(gain)
			self.resources.knowledge += 1
	
	def consumeFood(self) -> bool :
		"""
		Deduces the food amount, based on the current player's city's population.
		:return: bool True if there is no food available, else False if everything is ok
		"""
		self.resources.food -= self.city.population
		if self.resources.food < 0 :
			return True
		return False

	# FACILITIES

	def promptFacilities(self) -> None :
		facilities = self.city.facilities
		for i in range(facilities.len) :
			facilities.get(i).promptSummary()
	
	def buildFacility(self, facility : _Facility) -> None :

		facility.promptDetails()

		if not self.city.checkPopulation() :
			select = userInputInt("[0] Retour\n[X] Construire (Population maximale déjà atteinte)", 0, 0)
		if self.resources.isGreaterOrEqualThan(facility.cost) :
			select = userInputInt("[0] Retour\n[X] Construire (Ressources insuffisantes)", 0, 0)
		else :
			select = userInputInt("[0] Retour\n[1] Construire", 0, 1)
		
		if select == 1 :
			self.city.addFacility(facility)

	# TECHNOLOGIES
	
	def learnTechnology(self, technology : TechnologyNode) -> bool :
		if self.resources.knowledge >= technology.cost :
			self.resources.knowledge -= technology.cost
			technology.unlocked = True
			return True
		return False
	
	# ARMY

	def promptTroups(self) -> None :
		baracks = self.city.facilities.onlyInstanceOf(Baracks())
		if baracks is not None :
			for i in range(baracks.len) :
				b = baracks.get(i)
				print(b)
				for j in range(b.troups.len) :
					print(b.troups.get(j))