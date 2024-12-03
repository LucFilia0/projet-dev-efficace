<<<<<<< HEAD
=======
from model.Node import Node

>>>>>>> 77d6b7d (caca prout)
class Stack :


	class Node :


		def __init__(self, value, next = None) :
			
			self.value = value
			self.next = next


	def __init__(self) :

		self.top = None
		self.itemCount = 0
	
	def __str__(self):
		other = Stack()
		ret = "["
		while (not self.isEmpty()):
			other.push(self.pop())
			ret += " " + str(other.read())
			if (not self.isEmpty()):
				ret += ","
		
		ret += " ]"
		while (not other.isEmpty()):
			self.push(other.pop())

		del(other)
		return ret

	# Basic methods

	def isEmpty(self) -> bool :

		return self.top is None


	def push(self, value) -> None :

		newNode = self.Node(value, self.top)
		self.top = newNode
		self.itemCount += 1
	

	def pop(self) -> object :

		value = None
		if not self.isEmpty() :
			temp = self.top
			value = temp.value
			self.top = self.top.next
			del temp
		self.itemCount -= 1
		return value
	
	
	def read(self) -> object :

		value = None
		if not self.isEmpty() :
			value = self.top.value
		return value

	
	def size(self) -> int :

		return self.itemCount

	def clear(self) -> None :

		while not self.isEmpty() :
			current = self.top.next
			del self.top
			self.top = current

	# "She asked" methods

	def remove(self, value, all=False, key=None) -> bool :

		other = Stack()
		found = False
		temp_val = value[key] if key is not None and type(value) is dict else value
		while ((all or not found) and not self.isEmpty()):
			current = self.pop()
			temp = current[key] if key is not None and type(current) is dict else current
			if temp != temp_val:
				other.push(current)
			else:
				found = True
		while (not other.isEmpty()):
			self.push(other.pop())
		return found
	
	def count(self, value, key=None) -> int :

		other = Stack()
		count = 0
		temp_val = value[key] if key is not None and type(value) is dict else value
		while (not self.isEmpty()):
			current = self.pop()
			other.push(current)
			temp_curr = current[key] if key is not None and type(current) is dict else current
			if temp_curr == temp_val:
				count += 1
		self.copy(other)
		return count

	def copy(self, other) -> None :

		self.top = other.top
		self.itemCount = other.itemCount

	def contains(self, value, key=None):
		
		other = Stack()
		found = False
		while (not found and not self.isEmpty()):
			current = self.pop()
			temp = current[key] if key is not None and type(current) is dict else current
			other.push(current)
			if temp == value:
				found = True
		
		while (not other.isEmpty()):
			self.push(other.pop())

		return found
	
	def min(self, key=None) -> object :

		other = Stack()
		min = self.pop()
		temp_min = min[key] if key is not None and type(min) is dict else min
		if (min is not None):
			other.push(min)
		
		while (not self.isEmpty()):
			current = self.pop()
			temp_current = current[key] if key is not None and type(current) is dict else current
			other.push(current)
			if temp_min > temp_current:
				min = current
				temp_min = temp_current

		while (not other.isEmpty()):
			self.push(other.pop())

		return min

	def max(self, key=None) -> object :

		other = Stack()
		max = self.pop()
		temp_max = max[key] if key is not None and type(max) is dict else max
		if (max is not None):
			other.push(max)
		
		while (not self.isEmpty()):
			current = self.pop()
			temp_current = current[key] if key is not None and type(current) is dict else current
			other.push(current)
			if temp_max < temp_current:
				max = current    
				temp_max = temp_current
		
		while (not other.isEmpty()):
			self.push(other.pop())

		return max

	def sort(self, reverse=False) -> None :

		res = Stack()
		while (not self.isEmpty()):
			value = self.min() if reverse else self.max() 
			res.push(value)
			self.remove(value)
		self.top = res.top
