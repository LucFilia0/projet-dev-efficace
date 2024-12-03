from model.Stack import *
from model.File import *

# Stack's tests


stack = Stack()

stack.push(12)
stack.push(1)
stack.push(34)

print(stack)
print(stack.pop())
print(stack)
print(stack.read())
print(stack)


# File's tests

"""
file = File()

file.push(12)
file.push(56)
file.push(43)

for i in range(4) :
	print("---\nsize: ", file.size())
	print("empty: ", file.isEmpty())
	print("value: ", file.pop())
 """