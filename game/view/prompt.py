import os

def clear() -> None :
	os.system("cls || clear")

def padNumber(number : int, padding : int) -> str :
	return str(number).zfill(padding)

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

def promptLine(length : int) -> None :
	ret = ""
	for i in range(length) :
		ret += "-"
	print(ret)