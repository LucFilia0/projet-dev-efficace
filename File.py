class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

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
        self.count += 1
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
        
        self.count -= 1
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
        self.count = 0

    def copy(self, other):
        self.head = other.head
        self.tail = other.tail
        self.count = other.count

    def size(self):
        return self.count

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
    print(f.size())
    print(f)