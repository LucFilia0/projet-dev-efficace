from game.model.Campaign import Campaign
from game.model.Player import Player
from game.model.City import City
from game.view.prompt import *

def test() -> None :
	cam = Campaign()
	cam.name = "La guerre des zikettes"
	cam.maxTurn = 20
	player1 = Player("Joueur 1")
	player2 = Player("Joueur 2")
	player1.city = City("Cité 1")
	player2.city = City("Cité 2")
	cam.playerQueue.push(player1)
	cam.playerQueue.push(player2)
	cam.start()
	
def menu() -> None :
	screen("ACCUEIL")
	choice = userInputInt("[1] Nouvelle campagne\n[2] Quitter", 1, 2)
	if choice == 1 :
		createCampaign()
	else :
		quitGame()

def quitGame() -> None :
	clear()
	print("Fin du jeu, à la prochaine o7")

def promptCampaignInformations(campaign : Campaign) -> None :
	print(f"Nom    : {campaign.name}")
	maxTurn = str(campaign.maxTurn) + " tours" if campaign.maxTurn > 0 else ""
	print(f"Tours  : {maxTurn}")
	playerCount = str(campaign.playerQueue.size()) if campaign.playerQueue.size() > 0 else ""
	print(f"Joueurs : {playerCount}")
	for i in range(campaign.playerQueue.size()) :
		player = campaign.playerQueue.pop()
		print(f"  + {player.name} ({player.city.name})")
		campaign.playerQueue.push(player)
	promptLine(60)

def createCampaign() -> None :
	campaign = Campaign()
	for i in range(4) :
		screen("NOUVELLE CAMPAGNE")
		promptCampaignInformations(campaign)
		if i == 0 :
			createCampaign_name(campaign)
		elif i == 1 :
			createCampaign_maxTurn(campaign)
		elif i == 2 :
			createCampaign_players(campaign)
		else :
			confirmCampaign(campaign)

def createCampaign_name(campaign : Campaign) -> None :
	campaign.name = userInputStr("Entrez le nom de la campagne")

def createCampaign_maxTurn(campaign : Campaign) -> None :
	choice = userInputInt("Choisissez le nombre de tours\n[1] 20 tours\n[2] 40 tours\n[3] 60 tours", 1, 3)
	if choice == 1 :
		campaign.maxTurn = 20
	elif choice == 2 :
		campaign.maxTurn = 40
	else :
		campaign.maxTurn = 60

def createCampaign_players(campaign : Campaign) -> None :
	campaignPlayerCount = userInputInt("Entrez le nombre de joueurs (2 - 4)", 2, 4)
	for i in range(campaignPlayerCount) :
		campaign.addPlayer(createPlayer(i))

def createPlayer(index : int) -> Player :
	screen(f"JOUEUR {index + 1}")
	player = Player(userInputStr(f"Comment vous appelez vous ?"))
	player.city = City(userInputStr(f"Bonjour \"{player.name}\" ! Quel est le nom de votre cité ?"))
	return player

def confirmCampaign(campaign : Campaign) -> None :
	yesOrNoLaJeunesse = userInputInt("Commencer la campagne ?\n[1] Commencer !\n[2] Retour au menu", 1, 2)
	if yesOrNoLaJeunesse == 1 :
		campaign.start()
	else :
		menu()