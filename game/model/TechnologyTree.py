import json
import os
from game.model.techno_tree.AbstractNodes import *
from game.model.techno_tree.NodeFactory import NodeFactory
from model.Stack import Stack
from game.view.prompt import userInputInt
from colorama import Fore, Style

class TechnologyTree:

    def __init__(self):
        self.root : TreeNode = None
        self.player : Player = None

    def printTree(self) -> None:
        if (self.root is not None):
            self.root.printNodeAndChildren(0)
    
    def navigateTree(self) -> None:
        node = self.root
        nodeStack = Stack()
        quit = False
        while not quit:
            maxSelection = node.children.len + 1
            if not nodeStack.isEmpty():
                maxSelection += 1
                
            os.system("cls || clear")
            select = userInputInt(node.getPrintableDescAndChildren(not nodeStack.isEmpty()), 0, maxSelection)
            if select == 0:
                quit = True
            if (select <= node.children.len):
                nodeStack.push(node)
                node = node.children.get(select - 1)
            elif select == node.children.len + 1:
                node = nodeStack.pop()
            else:
                node.buy(self.player)

            
        
    def buildTree(self) -> bool:    
        with open(os.getcwd() + "/data/tree.json") as tree_file:
            tree_data = json.load(tree_file)
            root = dict.get(tree_data, "root")
            if root is None:
                return False
            
            self.root = NodeFactory.create(root)
            self.root.addChildrenRecur(root)

            return True
        
    def getNode(self, name) -> TreeNode:
        if (self.root is not None):
            return self.root.findChild(name)
        return None    
            

if __name__ == "__main__":
    tree = TechnologyTree()
    tree.buildTree()
    tree.navigateTree()
        
