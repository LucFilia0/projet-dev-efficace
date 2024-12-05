class List:
    
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
        count = List()
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
        res = List()
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








