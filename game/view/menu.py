from game.model.Campaign import Campaign
from game.model.Player import Player
from game.model.Nation import Nation
from game.view.prompt import *
	
def menu() -> None :
	promptSep("ACCUEIL")
	choice = userInputInt("[1] Nouvelle campagne\n[2] Quitter", 1, 2)
	if choice == 1 :
		createCampaign()
	else :
		quitGame()

def quitGame() -> None :
	clear()
	print("Fin du jeu, à la prochaine o7")

def createCampaign() -> None :
	promptSep("NOUVELLE CAMPAGNE")
	campaign = Campaign(userInputStr("Entrez le nom de la campagne"), userInputInt("Choisissez le nombre de tours\n[1] 20 tours\n[2] 40 tours\n[3] 60 tours", 1, 3))
	campaignPlayerCount = userInputInt("Entrez le nombre de joueurs (2 - 4)", 2, 4)
	for i in range(campaignPlayerCount) :
		campaign.addPlayer(createPlayer(i))
	promptSep("COMMENCER CAMPAGNE")
	print(f"Commencer la campagne \"{campaign.name}\" ?\n\nJoueurs :")
	for i in range(campaignPlayerCount) :
		player = campaign.playerQueue.pop()
		campaign.playerQueue.push(player)
		print(f"+ {player} ({player.nation})")
	yesOrNoLaJeunesse = userInputInt("\n[1] Commencer !\n[2] Retour au menu", 1, 2)
	if yesOrNoLaJeunesse == 1 :
		campaign.start()
	else :
		menu()

def createPlayer(index : int) -> Player :
	promptSep(f"JOUEUR {index + 1}")
	player = Player(userInputStr(f"Comment vous appelez vous ?"))
	player.nation = Nation(userInputStr(f"Bonjour \"{player.name}\" ! Quel est le nom de votre nation ?"))
	return player
	