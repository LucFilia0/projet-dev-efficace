from game.model.Player import Player
from typing import Self
from model.List import ListFromScratch
from colorama import Fore, Style

from model.Stack import Stack

class TreeNode:
    def __init__(self, name : str, desc : str):
        self.name = name
        self.desc = desc
        self.children = ListFromScratch()
        self.unlocked = False

    def addChild(self, node):
        self.children.add(node)

    def nbChild(self) -> int:
        return self.children.len
    
    def printNodeAndChildren(self, layer : int) -> None:
        print('-'*layer + str(self))
        nodeList = self.children.getValuesInRange()
        for node in nodeList:
            node.printNodeAndChildren(layer+1)

    def addChildrenRecur(self, data : dict):
        from game.model.techno_tree.NodeFactory import NodeFactory
        childrenList = data["children"]
        for nodeData in childrenList:
            node = NodeFactory.create(nodeData)
            self.addChild(node)
            node.addChildrenRecur(nodeData)

    def __str__(self):
        return self.name
    
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
        self.cost = cost

    def buy(self, player : Player) -> bool:
        if player.resources.knowledge >= self.cost:
            player.resources.knowledge -= self.cost
            self.unlocked = True
            return True
            # TODO Fire unlocked event
        return False

    def printNode(self) -> None:
        print(self.name.center(30, "="))
        print(f"\"{self.desc}\"")
        if (not self.unlocked):
            print(Fore.RED, f"Cette technologie coûte {self.cost} points de connaissance")
        else:
            print(Fore.GREEN, "Vous avez débloqué cette technologie")
        print(Style.RESET_ALL)