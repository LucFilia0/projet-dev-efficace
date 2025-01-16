import json
import os
from game.model.techno_tree.AbstractNodes import *
from game.model.techno_tree.NodeFactory import NodeFactory
from model.Stack import Stack
from game.view.prompt import userInputInt
from colorama import Fore, Style

class TechnologyTree:
    """
    Tree stocking the technologies a player has obtained, and the ones he can 
    unlock throughout the game.
    The data contained in the tree is imported from json files.
    The tree mostly contains recursive calls to functions on the root, which will then propagate the call to its children.
    author : Nathan
    """

    def __init__(self, player : Player):
        self.root : TreeNode = None
        self.player : Player = player

    def printTree(self) -> None:
        if (self.root is not None):
            self.root.printNodeAndChildren(0)
    
    def navigateTree(self) -> None:
        """
        Displays the tree in a little menu that lets the player simply navigate through it, 
        read information about Technologies he has access to, or unlock new ones.
        author : Nathan
        """

        node = self.root
        nodeStack = Stack()
        quit = False
        while not quit:
            maxSelection = node.children.len + 1
            if not nodeStack.isEmpty():
                maxSelection += 1
                
            os.system("cls || clear")
            select = userInputInt(node.getPrintableDescAndChildren(not nodeStack.isEmpty()), 0, maxSelection)
            # Quit option
            if select == 0:
                quit = True

            # Accessing any technology
            if (select <= node.children.len):
                nodeStack.push(node)
                node = node.children.get(select - 1)

            # Unlocking a technology if it is buyable
            elif select == node.children.len + 1 and node.isBuyable():
                #node.buy(self.player)
                # TODO buy node here
                pass

            # Going back to the parent
            else:
                node = nodeStack.pop()

    def buildTree(self) -> bool:    
        """
        Builds the tree from a json file, it will first create the root, then recursively 
        let each node create its children
        author : Nathan
        """ 

        with open(os.getcwd() + "/data/tree.json") as tree_file:
            tree_data = json.load(tree_file)
            root = dict.get(tree_data, "root")
            if root is None:
                return False
            
            self.root = NodeFactory.create(root)
            self.root.addChildrenRecur(root)

            return True
    
    def getNode(self, name) -> TreeNode:
        """
        Finds a node in the Tree
        returns the Node if it exists, None if it doesn't
        """

        if (self.root is not None):
            return self.root.findChild(name)
        return None    
            

if __name__ == "__main__":
    tree = TechnologyTree(None)
    tree.buildTree()
    tree.navigateTree()
        
