class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nbElements = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def is_empty(self):
        return self.head is None
    
    def peek(self):
        value = None
        if (self.head is not None):
            value = self.head.value

        return value

    def add(self, value):
        self.nbElements += 1
        if (self.is_empty()):
            self.head = self.Node(value)
            self.tail = self.head
        
        elif self.head == self.tail:
            node = self.Node(value)
            self.tail = node
            self.tail.prev = self.head
            self.head.next = self.tail
        
        else:
            node = self.Node(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def pop(self):
        if self.head is None:
            return None
        
        self.nbElements -= 1
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None

        elif self.head.next == self.tail:
            value = self.head.value
            self.head = self.tail
            self.head.next = None
            self.head.prev = None
        
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None

        return value
    
    def remove(self, value, all=False, key=None):
        other = MyQueue()
        found = False
        temp_val = value[key] if key is not None and type(value) is dict else value
        while (not self.is_empty()):
            current = self.pop()
            temp_curr = current[key] if key is not None and type(current) is dict else current
            if temp_curr != temp_val or (found and not all):
                other.add(current)
            else:
                found = True

        self.copy(other)
        return found
    
    def clear(self):
        self.head = None
        self.tail = None
        self.nbElements = 0

    def copy(self, other):
        self.head = other.head
        self.tail = other.tail
        self.nbElements = other.nbElements

    def size(self):
        return self.nbElements

    def min(self, key=None):
        other = MyQueue()
        min = self.pop()
        temp_min = min[key] if key is not None and type(min) is dict else min
        if (min is not None):
            other.add(min)
        
        while (not self.is_empty()):
            current = self.pop()
            temp_current = current[key] if key is not None and type(current) is dict else current
            other.add(current)
            if temp_min > temp_current:
                min = current
                temp_min = temp_current

        self.copy(other)
        return min  

    def max(self, key=None):
        other = MyQueue()
        max = self.pop()
        temp_max = max[key] if key is not None and type(max) is dict else max
        if (max is not None):
            other.add(max)
        
        while (not self.is_empty()):
            current = self.pop()
            temp_current = current[key] if key is not None and type(current) is dict else current
            other.add(current)
            if temp_max < temp_current:
                max = current    
                temp_max = temp_current
        
        self.copy(other)
        return max
    
    def sort(self, reverse=False):
        other = MyQueue()
        while (not self.is_empty()):
            value = self.max() if reverse else self.min() 
            other.add(value)
            self.remove(value)

        self.copy(other)

    def contains(self, value, key=None):
        other = MyQueue()
        found = False
        temp_val = value[key] if key is not None and type(value) is dict else value
        while (not found and not self.is_empty()):
            current = self.pop()
            other.add(current)
            temp_curr = current[key] if key is not None and type(current) is dict else current
            if temp_curr == temp_val:
                found = True 
        
        self.copy(other)
        return found
    
    def count(self, value, key=None):
        other = MyQueue()
        count = 0
        temp_val = value[key] if key is not None and type(value) is dict else value
        while (not self.is_empty()):
            current = self.pop()
            other.add(current)
            temp_curr = current[key] if key is not None and type(current) is dict else current
            if temp_curr == temp_val:
                count += 1
        
        self.copy(other)
        return count

    def __str__(self):
        ret = "["
        if (not self.is_empty()):
            other = MyQueue()
            comp = True
            while (comp):
                value = self.pop()
                other.add(value)
                ret += " " + str(value)
                if (self.head is not None):
                    ret += ","
                comp = (self.head is not None)
            
            self.copy(other)

        return ret + " ]"

if __name__ == "__main__":
    f = MyQueue()
    f.add(5)
    f.add(112)
    f.add(12)
    f.add(3)
    f.add(112)
    print(f)  
    print(f.count(112))