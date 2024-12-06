from model.Queue import Queue
from game.model.Player import Player
from game.view.prompt import *

class Campaign :

	def __init__(self) :
		self.name = ""
		self.currentPlayer = None
		self.playerQueue = Queue()
		self.currentTurn = 0
		self.maxTurn = 0
	
	def addPlayer(self, player : Player) -> None :
		self.playerQueue.push(player)
	
	def nextPlayer(self) -> None :
		self.playerQueue.push(self.currentPlayer)
		self.currentPlayer = self.playerQueue.pop()
		self.currentTurn += 1
	
	def start(self) -> None :
		self.nextPlayer()
		self.preBoard()
	
	def promptStatus(self, path : str, prompt = True) -> None :
		screen(f"{self.currentPlayer.name} | {self.currentPlayer.city.name}")
		if prompt :
			print(f"> {path}")
			self.promptResources()
		
	def promptResources(self) -> None :
		pad = 3
		line = 60
		promptLine(line)
		print(f"SCORE || DOM {padNumber(self.currentPlayer.resources.domination, pad)} | ECO {padNumber(self.currentPlayer.resources.wealth, pad)} | SAV {padNumber(self.currentPlayer.resources.knowledge, pad)}")
		print(f"CRAFT ||  OR {padNumber(self.currentPlayer.resources.gold, pad)} | BOI {padNumber(self.currentPlayer.resources.wood, pad)} | PIR {padNumber(self.currentPlayer.resources.stone, pad)} | FER {padNumber(self.currentPlayer.resources.iron, pad)} | NUR {padNumber(self.currentPlayer.resources.food, pad)}")
		promptLine(line)

	def preBoard(self) -> None :
		self.promptStatus("", False)
		userInputInt("[1] À toi de jouer !", 1, 1)
		self.board()

	def board(self) -> None :
		self.promptStatus("CITE")
		choice = userInputInt("[1] Batiments\n[2] Troupes\n[3] Finir le tour", 1, 3)
		if choice == 1 :
			self.promptFacilities()
		elif choice == 2 :
			self.promptTroups()
		else :
			self.nextPlayer()
			self.preBoard() #TODO

	def promptFacilities(self) -> None :
		self.promptStatus("CITE / BATIMENTS")
		length = self.currentPlayer.facilities.size()
		if length == 0 :
			print("<-- Aucune construction -->")
		else :
			for i in range(length) :
				print(self.currentPlayer.facilities.get(i))
		choice = userInputInt("[1] Construire")
	
	def buildFacility(self) -> None :
		self.promptStatus("CITE / BATIMENTS / CONSTRUIRE")
		choice = userInputInt("[1] Habitation\n[2] Ferme\n[3] Scierie\n[4] Mine\n[5] Caserne\n[6] Marché", 1, 6)
		if choice == 1 :
			pass #TODO
	
	def promptTroups(self) -> None :
		print("Afficher les troupes")