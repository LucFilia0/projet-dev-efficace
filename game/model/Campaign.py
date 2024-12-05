from model.Queue import Queue
from game.model.Player import Player
from game.view.prompt import *

class Campaign :

	def __init__(self, name : str, duration : int) :
		self.name = name
		self.currentPlayer = None
		self.playerQueue = Queue()
		if duration == 1 :
			t = 20
		elif duration == 2 :
			t = 40
		else :
			t = 60
		self.turnNumber = t
	
	def addPlayer(self, player : Player) -> None :
		self.playerQueue.push(player)
	
	def nextPlayer(self) -> None :
		self.playerQueue.push(self.currentPlayer)
		self.currentPlayer = self.playerQueue.pop()
	
	def start(self) -> None :
		self.nextPlayer()
		self.preBoard()
	
	def promptStatus(self, title : str, ressources = True) -> None :
		clear()
		print(f"|# {self.currentPlayer} #|\n{self.currentPlayer.nation}")
		if ressources :
			self.promptResources()
		print(f"> {title}")
		
	def promptResources(self) -> None :
		pad = 3
		line = 30
		promptLine(line)
		print(f"SCORE : DOM {padNumber(self.currentPlayer.resources.domination, pad)} | ECO {padNumber(self.currentPlayer.resources.economy, pad)} | SAV {padNumber(self.currentPlayer.resources.knowledge, pad)}")
		print(f"CRAFT :  OR {padNumber(self.currentPlayer.resources.gold, pad)} | BOI {padNumber(self.currentPlayer.resources.wood, pad)} | PIR {padNumber(self.currentPlayer.resources.stone, pad)} | FER {padNumber(self.currentPlayer.resources.iron, pad)} | NUR {padNumber(self.currentPlayer.resources.food, pad)}")
		promptLine(line)

	def preBoard(self) -> None :
		self.promptStatus("...", False)
		userInputInt("\n<-- À toi de jouer ! [0] -->", 0, 0)
		self.board()

	def board(self) -> None :
		self.promptStatus("NATION")
		choice = userInputInt("[1] Batiments\n[2] Troupes\n[0] Finir le tour", 0, 2)
		if choice == 0 :
			self.nextPlayer()
			self.preBoard()
		elif choice == 1 :
			self.promptFacilities()
		elif choice == 2 :
			print("Afficher troupes") #TODO

	def promptFacilities(self) -> None :
		self.promptStatus("BATIMENTS")
		length = self.currentPlayer.facilities.size()
		if length == 0 :
			print("<-- Aucune construction -->")
		else :
			for i in range(length) :
				print(f"{i} | {self.currentPlayer.facilities.get(i)}")
		choice = userInputInt("[1] Construire")
	
	def buildFacility(self) -> None :
		self.promptStatus("BATIMENTS > CONSTRUIRE")
		choice = userInputInt("\n[0] Nom (cout | gain | temps de construction)\n---\n")