import json
import os
from game.model.techno_tree.AbstractNodes import *
from game.model.techno_tree.NodeFactory import NodeFactory

class TechnologyTree:

    def __init__(self):
        self.root = None

    def printTree(self) -> None:
        if (self.root is not None):
            self.root.printNodeAndChildren(0)

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
    tree.printTree()
        
