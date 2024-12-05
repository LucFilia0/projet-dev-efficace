def userInput(msg : str, min : int, max : int) -> int :
	ret = min - 1
	while ret < min or max < ret :
		print(msg)
		ret = int(input(">> "))
		if ret < min or max < ret :
			print(f"<-- Entrez une valeur entre {min} et {max} -->")
	return ret

def promptTitle() -> None :
	title = "ZIKETE"
	ret = "#|"
	length = 20
	half_length = (length - 2 - len(title)) // 2 
	for i in range(length) :
		ret += "="
	ret += "|#\n#|"
	for i in range(half_length) :
		ret += "="
	if half_length % 2 == 1 :
		ret += "="
	ret += f" {title} "
	for i in range(half_length) :
		ret += "="
	ret += "|#\n#|"
	for i in range(length) :
		ret += "="
	ret += "|#"
	print(ret)
	

def promptMenu() -> None :
	promptTitle()
	choice = userInput("1 - Nouvelle partie\n2 - Quitter", 1, 2)
	if choice is 1 :
		createGame() # TODO
	else :
		quitGame() # TODO

def quitGame() -> None :
	print("Fin du jeu, à la prochaine o7")

def createGame() -> None :
	print("Nouvelle partie")
	userInput("Entrez le nombre de joueurs :", 2, 4)