from model.Queue import Queue
from game.model.Player import Player
from game.view.promt import promptSep

class Campaign :

	def __init__(self, name : str) :
		self.name = name
		self.currentPlayer = None
		self.playerQueue = Queue()
	
	def addPlayer(self, player : Player) -> None :
		self.playerQueue.push(player)
	
	def nextPlayer(self) -> None :
		self.players.push(self.currentPlayer)
		self.currentPlayer = self.playerQueue.pop()
	
	def start(self) -> None :
		print("Début campagne")
	