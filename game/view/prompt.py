import os

def clear() -> None :
	os.system("cls || clear")

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

def screen(title : str) -> None :
	clear()
	print(f"{title}")
	promptLine()

def promptLine() -> None :
	ret = ""
	for i in range(60) :
		ret += "-"
	print(ret)