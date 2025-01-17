from typing import Self
from colorama import Fore, Style

from model.List import List
from model.Stack import Stack

class _TreeNode :

    def __init__(self, name : str, desc : str) -> Self :
        self.name : str = name
        self.desc : str = desc
        self.children = List()
    
    def __str__(self) :
        return self.name

    def nbChildren(self) -> int :
        return self.children.len
    
    def addChild(self, node : Self) -> None :
        self.children.add(node)
    
    def removeChild(self, node : Self) -> None :
        self.children.remove(node)
    
    def removeChildByIndex(self, index : int) -> None :
        """
        Removes a child at the wanted position
        """
        if 0 <= index and index < self.nbChildren() :
            self.children.remove(self.children.get(index))  
    
    def addChildrenRec(self, data : dict) -> None :
        """
        Generates a node from the data contained in a dictionnary
        (extracted from a json).
        The node will then create its children, until the tree is entirely filled.
        author : Nathan
        """
        childrenList = data["children"]
        for nodeData in childrenList:
            node = TreeNodeFactory.create(nodeData)
            self.addChild(node)
            node.addChildrenRec(nodeData)

    def searchChild(self, name : str) -> Self:
        stack = Stack()
        stack.push(self)
        while not stack.isEmpty() :
            node = stack.pop()
            if node.name == name :
                return node
            nodeList = node.children.getValuesInRange()
            for i in range(nodeList.size()):
                stack.push(nodeList.pop())

    def searchDirectChild(self, name : str) -> Self:
        i = 0
        nodeQueue = self.children.getValuesInRange()
        while not nodeQueue.isEmpty():
            node = nodeQueue.pop()
            if (node.name == name):
                return node
            i += 1
        return None

    def printChildren(self, hasPrevious : bool) -> None :

        ret = ""
        ind = 0
        
        if hasPrevious :
            retMsg = "Retour"
        else :
            retMsg = "Finir le tour"

        ret += f"[{ind}] {retMsg}"
        curr = self.children.head
        while curr is not None:
            ret += f"\n[{ind + 1}] {curr.value}"
            ind += 1
            curr = curr.next

        return ret


class TechnologyNode(_TreeNode) :

    def __init__(self, name : str, desc : str, cost : int) -> Self :
        super().__init__(name, desc)
        self.cost : int = cost
        self.unlocked : bool = False
    
    def canLearn(self) -> bool :
        return not self.unlocked
    
    def printNodeAndChildren(self, layer : int, color=Fore.WHITE) -> None :
        """
        Recursively prints the tree in a readable way
        author : Nathan
        """
        
        print(Fore.WHITE, '-'*layer, sep="", end="")
        print(color, str(self), sep="")
        nodeQueue = self.children.getValuesInRange()
        node = nodeQueue.pop()
        while (node is not None):
            node.printNodeAndChildren(layer+1)
            node = nodeQueue.pop()
        print(Style.RESET_ALL, sep="", end="")
    
    def printChildren(self, hasPrevious : bool) -> str:
        """
        Returns a string containing the selection menu relative to every Node
        The menu has a quit option,
        Then an option to access every child,
        If it can be unlocked, it will have an option "Débloquer",
        And finally, if it has a parent, will have an option "Retour", to go back to it.
        author : Nathan
        """
        
        ret = str(self) + " : " + '\n'
        ret += self.desc + '\n\n'
        ind = 1
        
        if self.canLearn():
            ret += f"{Fore.RED}Vous devez débloquer cette Technologie pour consulter ses débouchés.\nCoût : {self.cost}\n{Style.RESET_ALL}"
        elif (self.children.len == 0):
            ret += "Cette technologie ne débloque rien d'autre\n"
        
        ret += f"[{ind - 1}] Quitter\n"
        if self.unlocked:
            while (ind <= self.children.len):
                node = self.children.get(ind - 1)
                if node.unlocked:
                    ret += f"[{ind}] {node}\n"
                else:
                    ret += f"{Fore.RED}[{ind}] {node}{Style.RESET_ALL}\n"
                ind += 1

        if self.canLearn():
            ret += f"{Fore.GREEN}[{ind}] Débloquer{Style.RESET_ALL}\n"
            ind += 1

        if hasPrevious:
            ret += f"[{ind}] Retour\n"
            ind += 1

        return ret

class ActionNode(_TreeNode) :

    def __init__(self, name : str, title : str, desc : str, callback : str, required : list|None) -> Self :
        super().__init__(name, desc)
        self.title : str = title
        self.callback : str = callback
        self.required : list|None = required

class TreeNodeFactory :

    def create(data : dict) -> _TreeNode|None :
        """
        Creates a TreeNode (or inherited child) based on the dictionnary passed as parameter.
        """
        match(data["type"]) :

            case "TreeNode" :
                return _TreeNode(data["name"], data["desc"])
            case "TechnologyNode" :
                return TechnologyNode(data["name"], data["desc"], data["cost"])
            case "ActionNode" :
                return ActionNode(data["name"], data["title"], data["desc"], data["callback"], data["required"])
            case _ :
                return None