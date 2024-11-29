from model.Node import *

class File :


	def __init__(self) :

		self.head = None
		self.tail = None
	

	def push(self, value) -> None :

		newNode = Node(value, None)
		if self.head == None :
			self.head = newNode
		if self.tail != None :
			self.tail.nextNode = newNode
		self.tail = newNode
	

	def pop(self) -> object :
		
		value = None
		if self.head != None :
			temp = self.head
			value = temp.value
			self.head = self.head.nextNode
			del temp
		return value
	

	def read(self) -> object :

		value = None
		if self.head != None :
			value = self.head.value
		return value
	

	def isEmpty(self) -> bool :
		
		return self.head == None

	
	def size(self) -> int :
		
		size = 0
		current = self.head
		while current != None :
			size += 1
			current = current.nextNode
		return size
