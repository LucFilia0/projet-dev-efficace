from os import system
from game.model.Campaign import Campaign

def clear() -> None :
	system("cls || clear")

def padNumber(number : int, padding : int) -> str :
	return str(number).zfill(padding)

def userInputInt(msg : str, min : int, max : int) -> int :
	quit = False
	print("\n" + msg)
	while not quit :
		try:
			ret = int(input(">> "))
		except:
			ret = min - 1
		if ret < min or max < ret :
			print(f"-- Entrez une valeur entre {min} et {max}")
		else :
			quit = True
	return ret

def userInputStr(msg : str) -> str :
	quit = False
	while not quit :
		print("\n" + msg)
		ret = str(input(">> "))
		if ret == "\n" :
			print("<-- Les chaînes vides ne sont pas acceptées")
		else :
			quit = True
	return ret

def promptLine() -> None :
	ret = ""
	for i in range(60) :
		ret += "-"
	print(ret)

def screen(title : str) -> None :
	clear()
	print(f"{title}")
	promptLine()

def promptStatus(path : str|None) -> None :
	campaign = Campaign.getInstance()
	player = campaign.currentPlayer
	screen(f"({campaign.currentTurn}/{campaign.maxTurn}) {player.name} | {player.city.name}")
	if path is not None :
		print(f"> {path}")
		promptResources(player)

def promptResources(player) -> None :
	pad = 3
	promptLine()
	population = f"POP {player.city.population}/{player.city.maxPopulation}"
	print(
		f"{population.rjust(60)}\n"
		f"SCORE || DOM {padNumber(player.resources.domination, pad)} | ECO {padNumber(player.resources.wealth, pad)} | SAV {padNumber(player.resources.knowledge, pad)}\n"
		f"CRAFT ||  OR {padNumber(player.resources.gold, pad)} | BOI {padNumber(player.resources.wood, pad)} | PIR {padNumber(player.resources.stone, pad)} | FER {padNumber(player.resources.iron, pad)} | NUR {padNumber(player.resources.food, pad)}"
	)
	promptLine()