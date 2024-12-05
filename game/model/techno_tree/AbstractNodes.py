from game.model.Player import Player
from model.List import List
from colorama import Fore, Style

class TreeNode:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.children = List()

    def addChild(self, node):
        self.children.add(node)

    def nbChild(self) -> int:
        return self.children.size()

class BuyableNode(TreeNode):
    def __init__(self, name : str, desc : str, cost : int):
        super().__init__(name, desc)
        self.cost = cost
        self.unlocked = False

    def buy(self, player : Player):
        if player.resources.knowledge >= self.cost:
            player.resources.knowledge -= self.cost
            self.unlocked = True
            # TODO Fire unlocked event

    def printNode(self):
        print(self.name.center(30, "="))
        print(f"\"{self.desc}\"")
        if (not self.unlocked):
            print(Fore.RED, f"Cette technologie coûte {self.cost} points de connaissance")
        else:
            print(Fore.GREEN, "Vous avez débloqué cette technologie")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    node = BuyableNode("Truc", "Un pouvoir ancien et malveillant", 12)
    node.printNode()
    node.unlocked = True
    node.printNode()