import json
import os
from game.model.techno_tree.AbstractNodes import *
from game.model.techno_tree.NodeFactory import NodeFactory
from model.Stack import Stack

class TechnologyTree:
    def __init__(self):
        self.root = None

    def printTree(self):
        if (self.root is not None):
            self.root.printNodeAndChildren(0)

    def buildTree(self):    
        stack = Stack()
        with open(os.getcwd() + "/data/tree.json") as tree_file:
            tree_data = json.load(tree_file)
            root = dict.get(tree_data, "root")
            if root is None:
                return -1
            
            stack.push(root)
            while (not stack.isEmpty()):
                nodeData = stack.pop()
                node = NodeFactory.create(nodeData)



if __name__ == "__main__":
    tree = TechnologyTree()
    tree.buildTree()
    tree.printTree()
        
