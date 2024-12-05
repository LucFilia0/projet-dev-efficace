import os

from game.model.Campaign import Campaign
from game.model.Player import Player
from game.model.Nation import Nation

def clear() -> None :
	os.system("cls || clear")

def userInputInt(msg : str, min : int, max : int) -> int :
	quit = False
	while not quit :
		print(msg)
		ret = int(input(">> "))
		if ret < min or max < ret :
			print(f"<-- Entrez une valeur entre {min} et {max} -->")
		else :
			quit = True
	return ret

def userInputStr(msg : str) -> str :
	quit = False
	while not quit :
		print(msg)
		ret = str(input(">> "))
		if ret == "\n" :
			print("<-- Les chaînes vides ne sont pas acceptées")
		else :
			quit = True
	return ret

def promptSep(sep : str) -> None :
	clear()
	print(f"\n#| {sep} |#\n")
	

def promptMenu() -> None :
	promptSep("Accueil")
	choice = userInputInt("1 - Nouvelle campagne\n2 - Quitter", 1, 2)
	if choice == 1 :
		createCampaign()
	else :
		quitGame()

def quitGame() -> None :
	clear()
	print("Fin du jeu, à la prochaine o7")

def createCampaign() -> None :
	promptSep("Nouvelle campagne")
	campaign = Campaign(userInputStr("Entrez le nom de la campagne"))
	campaignPlayerCount = userInputInt("Entrez le nombre de joueurs", 2, 4)
	for i in range(campaignPlayerCount) :
		campaign.addPlayer(createPlayer(i))
	promptSep("Commencer campagne")
	yesOrNoLaJeunesse = userInputInt(f"Commencer la campagne \"{campaign.name}\" ?\n1 - Commencer !\n2 - Retour au menu", 1, 2)
	if yesOrNoLaJeunesse == 1 :
		campaign.start()
	else :
		promptMenu()

def createPlayer(index : int) -> Player :
	promptSep(f"Joueur {index + 1}")
	player = Player(userInputStr(f"Comment vous appelez vous ?"))
	player.nation = Nation(userInputStr(f"Bonjour \"{player.name}\" ! Quel est le nom de votre nation ?"))
	return player
