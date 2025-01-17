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