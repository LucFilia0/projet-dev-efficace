from typing import Self
from model.Queue import Queue
from model.Stack import Stack

class Campaign :

	_currentCampaign = None

	def __init__(self) :
		self.name = ""
		self.currentPlayer = None
		self.playerQueue = Queue()
		self.currentTurn = 1
		self.currentAction = 0
		self.maxTurn = 0
	
	def getInstance() -> Self :
		if Campaign._currentCampaign is None :
			Campaign._currentCampaign = Campaign()
		return Campaign._currentCampaign
	
	def addPlayer(self, player) -> None :
		player.createStartingFacilities()
		self.playerQueue.push(player)
	
	def nextPlayer(self) -> None :

		if self.currentPlayer is not None :
			self.playerQueue.push(self.currentPlayer)
		self.currentPlayer = self.playerQueue.pop()

		self.currentPlayer.collectResources()
		self.currentPlayer.consumeFood()

		self.currentAction += 1
		if self.currentAction % 2 == 0 :
			self.currentTurn += 1

		self.currentPlayer.startTurn()
	
	def start(self) -> None :
		self.nextPlayer()

	# OUTDATED
	""" def board(self) -> None :
		self.promptStatus("CITE")
		maxOpt = 2
		string = "[0] Finir le tour\n[1] Constructions\n[2] Technologies"
		if(self.currentPlayer.city.containsBaracks()) :
			string += "\n[3] Armée"
			maxOpt = 3
		choice = userInputInt(string, 0, maxOpt)
		match(choice) :
			case 1 :
				self.promptFacilities()
			case 2 :
				self.promptTechnologies()
			case 3 :
				self.promptArmy()
			case _ :
				self.endTurn()

	def promptFacilities(self) -> None :
		self.promptStatus("CITE / CONSTRUCTIONS")
		length = self.currentPlayer.city.facilities.len
		print("Liste des constructions :\n")
		if length == 0 :
			print("<-- Aucune construction -->")
		else :
			for i in range(length) :
				self.currentPlayer.city.facilities.get(i).promptSummary()
		choice = userInputInt("\n[0] Retour\n[1] Nouvelle construction", 0, 1)
		if choice == 1 :
			self.buildFacility()
		else :
			self.board()
	
	def buildFacility(self) -> None :
		self.promptStatus("CITE / BATIMENTS / CONSTRUIRE")
		choice = userInputInt("[0] Retour\n[1] Habitation\n[2] Ferme\n[3] Scierie\n[4] Mine\n[5] Caserne\n[6] Marché", 0, 6)
		chosenFacility = None
		match(choice) :
			case 0 :
				self.promptFacilities()
			case 1 :
				chosenFacility = Habitation()
			case 2 :
				chosenFacility = Farm()
			case 3 :
				chosenFacility = Sawmill()
			case 4 :
				chosenFacility = Mine()
			case 5 :
				chosenFacility = Baracks()
			case 6 :
				print("Créer 'Market' fdp")
		if(choice != 0) :
			self.buyFacility(chosenFacility)
	
	def buyFacility(self, facility : _Facility) -> None :
		self.promptStatus(f"CITE / BATIMENTS / CONSTRUIRE > {facility.name}")
		facility.promptDetails()

		if self.currentPlayer.city.checkPopulation() :
			if self.currentPlayer.resources.isGreaterOrEqualThan(facility.cost) :
				confirm = userInputInt("Confirmer la construction ?\n[0] Retour\n[1] Construire", 0, 1)
			else :
				confirm = userInputInt("Confirmer la construction ?\n[0] Retour\n[X] Construire (ressources insuffisantes)", 0, 0)
		else :
			confirm = userInputInt("Confirmer la construction ?\n[0] Retour\n[X] Construire (population maximale déjà atteinte)", 0, 0)

		if(confirm == 0) :
			self.buildFacility()
		else :
			self.currentPlayer.city.addFacility(facility)
			self.currentPlayer.resources.sub(facility.cost)
			self.promptFacilities()
	
	def promptTechnologies(self) -> None:

		tree = self.currentPlayer.technoTree

		node = tree.root
		nodeStack = Stack()
		done = False

		while not done:
			maxSelection = node.children.len + 1
			if not nodeStack.isEmpty():
				maxSelection += 1

			self.promptStatus("CITE / TECHNOLOGIES")
				
			select = userInputInt(node.getPrintableDescAndChildren(not nodeStack.isEmpty()), 0, maxSelection)
			# Quit option
			if select == 0:
				done = True

			# Accessing any technology
			if (select <= node.children.len):
				nodeStack.push(node)
				node = node.children.get(select - 1)

			# Unlocking a technology if it is buyable
			elif select == node.children.len + 1 and node.isBuyable():
				#node.buy(self.player)
				# TODO buy node here
				pass

			# Going back to the parent
			else:
				node = nodeStack.pop()
		self.board()

	def promptArmy(self) -> None :
		self.promptStatus("CITE / ARMEE")
		self.currentPlayer.city.promptBaracks()
		if self.currentPlayer.city.returnFirstAvailableBaracks() is None :
			choice = userInputInt("[0] Retour\n[X] Former des soldats (plus assez de places, construisez plus de casernes)", 0, 0)
		elif not self.currentPlayer.city.checkPopulation() :
			choice = userInputInt("[0] Retour\n[X] Former des soldats (population max atteinte, construisez plus d'habitations)", 0, 0)
		else :
			choice = userInputInt("[0] Retour\n[1] Former des soldats", 0, 1)
		match(choice) :
			case 1 :
				self.formTroup()
			case _ :
				self.board()

	def formTroup(self) -> None :
		self.promptStatus("CITE / ARMEE / FORMER")
		choice = userInputInt("[0] Retour\n[1] Former un guerrier\n[2] Former un archer\n[3] Former un garde", 0, 3)
		match(choice) :
			case 0 :
				self.promptArmy()
			case 1 :
				troup = Warrior()
			case 2 :
				troup = Archer()
		self.currentPlayer.city.addSoldier(troup)
		self.promptArmy()

	def endTurn(self) -> None :
		screen("FINIR LE TOUR ?")
		q = userInputInt("[0] Retour\n[1] Terminer", 0, 1)
		if q == 1 :
			self.nextPlayer()
		else :
			self.board() """
