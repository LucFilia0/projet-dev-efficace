import os

def clear() -> None :
	os.system("cls || clear")

def padNumber(number : int, padding : int) -> str :
	return str(number).zfill(padding)

def selectOnlyInt(line : str) -> int :
	i = "0"
	for c in line :
		if 47 < ord(c) and ord(c) < 58 :
			i += c
	return int(i)

def userInputInt(msg : str, min : int, max : int) -> int :
	quit = False
	print(msg)
	while not quit :
		ret = selectOnlyInt(input(">> "))
		if ret < min or max < ret :
			print(f"-- Entrez une valeur entre {min} et {max}")
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

def screen(title : str) -> None :
	clear()
	print(f"{title}")
	promptLine(60)

def promptLine(length : int) -> None :
	ret = ""
	for i in range(length) :
		ret += "-"
	print(ret)