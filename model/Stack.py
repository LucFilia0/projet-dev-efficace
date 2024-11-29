from model.Node import *

class Stack :


	def __init__(self) :

		self.pointer = None


	def push(self, value) -> None :

		newNode = Node(value, self.pointer)
		self.pointer = newNode
	

	def pop(self) -> object :

		value = None
		if self.pointer != None :
			temp = self.pointer
			value = temp.value
			self.pointer = self.pointer.nextNode
			del temp
		return value
	
	
	def read(self) -> object :

		value = None
		if self.pointer != None :
			value = self.pointer.value
		return value


	def isEmpty(self) -> bool :

		return self.pointer == None

	
	def size(self) -> int :

		size = 0
		current = self.pointer
		while current != None :
			size += 1
			current = current.nextNode
		return size
