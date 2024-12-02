class MyStack:
    def __init__(self):
        self.top = None
        self.count = 0

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
        
        self.count += 1
            
    def pop(self):
        value = None
        if (not self.is_empty()):
            value = self.top.value
            self.top = self.top.next
            self.count -= 1
        
        return value
    
    def remove(self, value, key=None):
        other = MyStack()
        temp_val = value[key] if key is not None and type(value) is dict else value
        while (not self.is_empty()):
            current = self.pop()
            temp = current[key] if key is not None and type(current) is dict else current
            if temp != temp_val:
                other.add(current)
            else:
                found = True
        
        while (not other.is_empty()):
            self.add(other.pop())

        return found

    
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
    
    def clear(self):
        self.top = None
        self.count = 0

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
    
    def min(self, key=None):
        other = MyStack()
        min = self.pop()
        if (min is not None):
            other.add(min)
        
        while (not self.is_empty()):
            current = self.pop()
            temp_current = current[key] if key is not None and type(current) is dict else current
            temp_min = min[key] if key is not None and type(min) is dict else min
            other.add(current)
            if temp_min > temp_current:
                min = current

        while (not other.is_empty()):
            self.add(other.pop())

        return min
    
    def max(self, key=None):
        other = MyStack()
        max = self.pop()
        if (max is not None):
            other.add(max)
        
        while (not self.is_empty()):
            current = self.pop()
            temp_current = current[key] if key is not None and type(current) is dict else current
            temp_max = max[key] if key is not None and type(max) is dict else max
            other.add(current)
            if temp_max < temp_current:
                max = current    
        
        while (not other.is_empty()):
            self.add(other.pop())

        return max
    
    def size(self):
        return self.count
    
    def sort(self, reverse=False):
        res = MyStack()
        while (not self.is_empty()):
            value = self.min() if reverse else self.max() 
            res.add(value)
            self.remove(value)
        
        self.top = res.top

if __name__ == "__main__":
    pass