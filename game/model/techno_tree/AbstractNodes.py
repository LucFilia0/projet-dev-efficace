from game.model.Player import Player
from typing import Self
from model.List import List
from colorama import Fore, Style

from model.Stack import Stack

class TreeNode:
    def __init__(self, name : str, desc : str):
        self.name = name
        self.desc = desc
        self.children = List()
        self.unlocked = True

    def addChild(self, node):
        self.children.add(node)

    def nbChild(self) -> int:
        return self.children.len
    
    def isBuyable(self) -> bool:
        return False
    
    def printNodeAndChildren(self, layer : int, color=Fore.WHITE) -> None:
        print(Fore.WHITE, '-'*layer, sep="", end="")
        print(color, str(self), sep="")
        nodeQueue = self.children.getValuesInRange()
        node = nodeQueue.pop()
        while (node is not None):
            node.printNodeAndChildren(layer+1)
            node = nodeQueue.pop()
        print(Style.RESET_ALL, sep="", end="")

    def addChildrenRecur(self, data : dict):
        from game.model.techno_tree.NodeFactory import NodeFactory
        childrenList = data["children"]
        for nodeData in childrenList:
            node = NodeFactory.create(nodeData)
            self.addChild(node)
            node.addChildrenRecur(nodeData)

    def __str__(self):
        return self.name
    
    def getPrintableDescAndChildren(self, hasPrevious : bool) -> str:
        ret = str(self) + " : " + '\n'
        ret += self.desc + '\n\n'
        ind = 1
        
        if self.isBuyable():
            ret += f"{Fore.RED}Vous devez débloquer cette Technologie pour consulter ses débouchés.\nCoût : {self.cost}\n{Style.RESET_ALL}"
        elif (self.children.len == 0):
            ret += "Cette technologie ne débloque rien d'autre\n"
        
        ret += f"[{ind - 1}] Quitter\n"
        while (ind <= self.children.len):
            node = self.children.get(ind - 1)
            if node.unlocked:
                ret += f"[{ind}] {node}\n"
            else:
                ret += f"{Fore.RED}[{ind}] {node}{Style.RESET_ALL}\n"
            ind += 1

        if self.isBuyable():
            ret += f"{Fore.GREEN}[{ind}] Débloquer{Style.RESET_ALL}\n"
            ind += 1

        if hasPrevious:
            ret += f"[{ind}] Retour\n"
            ind += 1

        return ret
    
    def findDirectChild(self, name) -> Self:
        i = 0
        nodeList = self.children.getValuesInRange()
        for node in nodeList:
            if (node.name == name):
                return node
            i += 1
        return None

    def findChild(self, name) -> Self:
        stack = Stack()
        stack.push(self)
        while (not stack.isEmpty()):
            node = stack.pop()
            if (node.name == name):
                return node
            nodeList = node.children.getValuesInRange()
            for node in nodeList:
                stack.push(node)
                
class TextNode(TreeNode):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)

class BuyableNode(TreeNode):
    def __init__(self, name : str, desc : str, cost : int):
        super().__init__(name, desc)
        self.unlocked = False
        self.cost = cost

    def buy(self, player : Player) -> bool:
        if player.resources.knowledge >= self.cost:
            player.resources.knowledge -= self.cost
            self.unlocked = True
            return True
            # TODO Fire unlocked event
        return False
    
    def isBuyable(self) -> bool:
        return not self.unlocked

    def printNode(self) -> None:
        print(self.name.center(30, "="))
        print(f"\"{self.desc}\"")
        if (not self.unlocked):
            print(Fore.RED, f"Cette technologie coûte {self.cost} points de connaissance")
        else:
            print(Fore.GREEN, "Vous avez débloqué cette technologie")
        print(Style.RESET_ALL)