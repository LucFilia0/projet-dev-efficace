from model.Queue import Queue

class ListDeCon:
    
    # Exercice 1

    def __init__(self):
        self.list = []

    def add(self, value):
        self.list.append(value)

    def remove(self, value):
        try:
            self.list.remove(value)
        except:
            print(f"La valeur {value} n'est pas présente dans la liste")
    
    def get(self, index):
        try:
            return self.list[index]
        except:
            print(f"Accès à l'indice {index} impossible, hors limite")

    def size(self):
        return len(self.list)    
    
    def find_index(self, value):
        try:
            return self.list.index(value)
        except:
            print(f"La valeur {value} n'est pas présente dans la liste")
        
    def print_list(self):
        print(self.list)

    # Exercice 2

    def reverse(self):
        self.list.reverse()
    
    def clear(self):
        del self.list
        self.list = []

    def contains(self, valeur, cle = None):
        i = 0
        for element in self.list:
            element = element[cle] if cle is not None and type(element) is dict else element
            if (element == valeur):
                return True
        return False


    def count(self, valeur, cle = None):
        i = 0
        count = 0
        for element in self.list:
            element = element[cle] if cle is not None and type(element) is dict else element
            if (element == valeur):
                count += 1

        return count

    
    def sort(self, cle = None):
        self.list.sort(key=lambda x : x[cle] if cle != None and type(x) is dict else x)
    
    # Exercice 3

    # Renvoie un set contenant tous les doublons
    def find_duplicates(self, cle=None):
        trouve = set()
        doublons = set()
        for element in self.list:
            element = element[cle] if cle is not None and type(element) is dict else element
            if (element in trouve):
                doublons.add(element)
            else:
                trouve.add(element)

        return doublons

    # Retire tous les doublons de la liste
    def remove_duplicates(self, cle = None):
        returnSet = set()
        for element in self.list:
            element = element = element[cle] if cle is not None and type(element) is dict else element
            returnSet.add(element)
        return list(returnSet)

    def insert_sorted(self, valeur, cle = None):
        i = 0
        while (i < self.size()):
            element = self.list[i][cle] if cle is not None and type(self.list[i]) is dict else self.list[i]
            if (element > valeur):
                self.list.insert(i, valeur)
                return
            i += 1
        self.add(valeur)
    
    def k_biggest(self, k, cle = None):
        # Liste ordonnée par odre croissant contenant au plus k éléments
        count = ListDeCon()
        for element in self.list:
            element = element[cle] if cle is not None and type(element) is dict else element
            
            # Si il n'y a pas encore k éléments, on insère simplement au bon endroit
            if count.size() < k:
                count.insert_sorted(element, cle)

            # Sinon on retire le plus petit, et insère le nouvel élément au bon endroit
            else:
                if count.get(0) < element:
                    count.list.pop(0)
                    count.insert_sorted(element, cle)

        # On renvoie le 1er élément de la liste, soit le k-eme plus petit
        return count.get(0)

    # Fusionne 2 listes triées en une grand liste triée
    def merge(self, other, cle = None):
        i, j = 0, 0
        res = ListDeCon()
        while (i < self.size() and j < other.taille()):
            elemSelf = self.list[i][cle] if cle is not None and type(self.list[i]) is dict else self.list[i]
            elemOther = other.list[j][cle] if cle is not None and type(other.list[j]) is dict else other.list[j]

            if (elemSelf <= elemOther):
                res.add(self.list[i])
                i += 1
            else:
                res.add(other.list[j])
                j += 1
        
        while (i < self.size()):
            res.add(self.list[i])
            i += 1

        while (j < other.taille()):
            res.add(other.list[j])
            j += 1

        self.list = res.list


    # Met tous les pairs devant, puis met tous les impairs
    def arrange_even_odd(self, cle = None):
        res = []
        middle = 0

        for element in self.list:
            elementComp = element[cle] if cle is not None and type(element) is dict else element
            if (elementComp % 2) == 0:
                res.insert(middle, element)
                middle += 1
            else:
                res.append(element)
        
        self.list = res

    def intertwine(self, other):
        i, j = 0, 0
        res = []
        while (i < self.size() and j < other.taille()):
            res.append(self.list[i])
            res.append(other.list[j])

            i, j = i+1, j+1
        
        while (i < self.size()):
            res.append(self.list[i])
            i += 1

        while (j < other.taille()):
            res.append(other.list[j])
            j += 1

        self.list = res

class List:

    class Node:
        
        def __init__(self, value, next=None, prev=None) -> None:
            self.value = value
            self.next = next
            self.prev = prev

        def __str__(self) -> str:
            return str(self.value)

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def isEmpty(self):
        return (self.len == 0)

    def add(self, value, index=0) -> bool:
        if index > self.len or index < 0:
            return False

        if self.len == 0:
            self.head = self.Node(value)
            self.tail = self.head
            
        elif index == 0:
            node = self.Node(value, self.head, None)
            if (self.head is not None):
                self.head.prev = node
            self.head = node

        elif index == self.len:
            node = self.Node(value, None, self.tail)
            if (self.tail is not None):
                self.tail.next = node
            self.tail = node

        else:
            current = self.getNode(index)
            node = self.Node(value, current, current.prev)
            
            current.prev.next = node
            current.prev = node               

        self.len += 1
        return True
    
    def get(self, index):
        node = self.getNode(index)
        return node if node is None else node.value

    def getNode(self, index : int) -> Node:
        if index < 0 or index >= self.len:
            return None

        if index > self.len/2:
            i = self.len-1
            current = self.tail
            while (i > index):
                i -= 1
                current = current.prev
        else:
            i = 0
            current = self.head
            while (i < index):
                i += 1
                current = current.next
        
        return current
    
    def getNodes(self, indexSet : set) -> Queue:
        i = 0
        ret = Queue()
        current = self.head
        while (i < self.len):
            if (i in indexSet):
                ret.push(current)
            current = current.next
            i+= 1

        return ret     
    
    def getValuesInRange(self, indexStart : int = 0, indexEnd : int | None = None) -> Queue:
        queue = self.getNodesInRange(indexStart, indexEnd)
        for i in range(queue.size()):
            queue.push(queue.pop().value)
        return queue
            

    def getNodesInRange(self, indexStart : int = 0, indexEnd : int | None = None) -> Queue:
        indexEnd = self.len-1 if indexEnd is None else indexEnd

        ret = Queue()
        if indexStart < 0 or indexStart >= self.len or indexEnd < 0 or indexEnd > self.len or indexEnd < indexStart:
            return ret

        if (indexStart <= self.len/2):
            i = 0
            current = self.head
            while (i <= indexEnd):
                if i >= indexStart:
                    ret.push(current)
                current = current.next
                i += 1
        else:
            i = self.len-1
            current = self.tail
            while (i >= indexStart):
                if i <= indexEnd:
                    ret.push(current)
                current = current.prev
                i -= 1

        return ret  

    
    def remove(self, index : int) -> bool:
        if index >= self.len or index  < 0 or self.len == 0:
            return False

        if self.len == 1:
            self.head = None
            self.tail = None
        
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        
        elif index == self.len-1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            current = self.getNode(index)
            current.prev.next = current.next
            current.next.prev = current.prev
            
            del current

        self.len -= 1
        return True

    def __str__(self) -> str:
        ret = "["
        current = self.head
        while (current is not None):
            ret += f" {current.value}"
            current = current.next
            if (current is not None):
                ret += ","
        
        return ret + " ]"
    
    def printReverse(self):
        current = self.tail
        while (current is not None):
            print(current, end = " ")
            current = current.prev

    def swap(self, index1 : int, index2 : int) -> bool:
        if (index1 < 0 or index2 < 0 or index1 > self.len or index2 > self.len):
            return False
        
        if (index1 == index2):
            return True
        
        nodeQueue = self.getNodes(set([index1, index2]))
        node1 = nodeQueue.pop()
        node2 = nodeQueue.pop()
        temp = node1.value
        node1.value = node2.value
        node2.value = temp

        return True

    def containsInstanceOf(self, thing : any) -> bool :
        contains = False
        
        if self.head != None :
            if type(self.head.value) is type(thing) :
                contains = True
            elif self.head.next is not None :
                current = self.head.next
                while current.next is not None and not contains :
                    if type(current.value) == type(thing) :
                        contains = True
                    current = current.next

        return contains
        
    def onlyInstanceOf(self, thing : any) :
        filteredList = List()

        if self.head is not None :
            if type(self.head.value) is type(thing) :
                filteredList.add(self.head.value)
            if self.head.next is not None :
                current = self.head.next
                while current.next is not None :
                    if type(current.value) is type(thing) :
                        filteredList.add(current.value)
                    current = current.next

        return filteredList