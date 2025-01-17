from game.model.Campaign import Campaign
from game.model.Player import Player
from game.model.City import City
from game.view.prompt import *

# TODO Remove when not needed anymore
def test() -> None :
	cam = Campaign.getInstance()
	cam.name = "La guerre des zikettes"
	cam.maxTurn = 20
	player1 = Player()
	player1.name = "Joueur 1"
	player2 = Player()
	player2.name = "Joueur 2"
	player1.city = City("Cité 1")
	player2.city = City("Cité 2")
	cam.addPlayer(player1)
	cam.addPlayer(player2)
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
	print(f"Nom     : {campaign.name}")
	maxTurn = str(campaign.maxTurn) + " tours" if campaign.maxTurn > 0 else ""
	print(f"Tours   : {maxTurn}")
	if not campaign.playerQueue.isEmpty() :
		playerCount = str(campaign.playerQueue.size()) if campaign.playerQueue.size() > 0 else ""
		print(f"Joueurs : {playerCount}")
		for i in range(campaign.playerQueue.size()) :
			player = campaign.playerQueue.pop()
			print(f"  + {player.name} ({player.city.name})")
			campaign.playerQueue.push(player)
	promptLine()

def promptUserInformations(player : Player|None) -> None :
	name = player.name if player is None or player.name is not None else ""
	city = player.city.name if player is None or player.city is not None else ""
	print(f"Nom  : {name}\nCité : {city}")
	promptLine()

def createCampaign() -> None :
	campaign = Campaign()
	campaignPlayerCount = 0
	i = 0
	while i < 5 :
		screen("NOUVELLE CAMPAGNE")
		promptCampaignInformations(campaign)
		if i == 0 :
			createCampaign_name(campaign)
		elif i == 1 :
			createCampaign_maxTurn(campaign)
		elif i == 2 :
			i = -1 if userInputInt("[1] Valider\n[2] Réécrire", 1, 2) == 2 else i
		elif i == 3 :
			createCampaign_players(campaign)
		else :
			confirmCampaign(campaign)
		i += 1

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
	player = Player()
	i = 0
	while i < 3 :
		screen(f"JOUEUR {index + 1}"	)
		promptUserInformations(player)
		if i == 0 :
			player.name = userInputStr(f"Comment vous appelez vous ?");
		elif i == 1 :
			player.city = City(userInputStr(f"Bonjour \"{player.name}\" ! Quel est le nom de votre cité ?"))
		else :
			i = -1 if userInputInt("[1] Valider\n[2] Réécrire", 1, 2) == 2 else i
		i+=1
	return player

def confirmCampaign(campaign : Campaign) -> None :
	yesOrNoLaJeunesse = userInputInt("Commencer la campagne ?\n[1] Commencer !\n[2] Retour au menu", 1, 2)
	if yesOrNoLaJeunesse == 1 :
		campaign.start()
	else :
		menu()