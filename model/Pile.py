class MyStack:
    def __init__(self):
        self.top = None
        self.nbElements = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        val = None
        if not self.is_empty():
            val = self.top.value
        return val

    def add(self, value):
        if (self.is_empty()):
            self.top = self.Node(value)
        else:
            node = self.Node(value)
            node.next = self.top
            self.top = node
        
        self.nbElements += 1
            
    def pop(self):
        value = None
        if (not self.is_empty()):
            value = self.top.value
            self.top = self.top.next
            self.nbElements -= 1
        
        return value
    
    def remove(self, value, all=False, key=None):
        other = MyStack()
        found = False
        temp_val = value[key] if key is not None and type(value) is dict else value
        while ((all or not found) and not self.is_empty()):
            current = self.pop()
            temp = current[key] if key is not None and type(current) is dict else current
            if temp != temp_val:
                other.add(current)
            else:
                found = True
        
        while (not other.is_empty()):
            self.add(other.pop())

        return found
    
    def clear(self):
        self.top = None
        self.nbElements = 0

    def contains(self, value, key=None):
        other = MyStack()
        found = False
        while (not found and not self.is_empty()):
            current = self.pop()
            temp = current[key] if key is not None and type(current) is dict else current
            other.add(current)
            if temp == value:
                found = True
        
        while (not other.is_empty()):
            self.add(other.pop())

        return found
    
    def count(self, value, key=None):
        other = MyStack()
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
    
    def min(self, key=None):
        other = MyStack()
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

        while (not other.is_empty()):
            self.add(other.pop())

        return min
    
    def max(self, key=None):
        other = MyStack()
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
        
        while (not other.is_empty()):
            self.add(other.pop())

        return max
    
    def copy(self, other):
        self.top = other.top
        self.nbElements = other.nbElements

    def size(self):
        return self.nbElements
    
    def sort(self, reverse=False):
        res = MyStack()
        while (not self.is_empty()):
            value = self.min() if reverse else self.max() 
            res.add(value)
            self.remove(value)
        
        self.top = res.top

    def __str__(self):
        other = MyStack()
        ret = "["
        while (not self.is_empty()):
            other.add(self.pop())
            ret += " " + str(other.peek())
            if (not self.is_empty()):
                ret += ","
        
        ret += " ]"
        while (not other.is_empty()):
            self.add(other.pop())

        del(other)
        return ret

if __name__ == "__main__":
    p = MyStack()
    p.add(5)
    p.add(12)
    p.add(3)
    p.add(12)
    print(p)
    print(p.count(12))