import json
import os
from game.model.techno_tree.AbstractNodes import TreeNode
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
    
    def __init__(self, player):
        self.root : TreeNode = None
        self.player : Player = player
        self.buildTree()


    def printTree(self) -> None:
        if (self.root is not None):
            self.root.printNodeAndChildren(0)

    def buildTree(self) -> bool:    
        """
        Builds the tree from a json file, it will first create the root, then recursively 
        let each node create its children
        author : Nathan
        """ 

        with open(os.getcwd() + "/data/technology.json") as tree_file:
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
    
    def isUnlocked(self, technologyName : str) -> bool|None :
        """
        Returns if the technology is unlocked ot not.
        """
        techNode = self.getNode(technologyName)
        if techNode is not None :
            return techNode.unlocked
        return None