from game.model.techno_tree.AbstractNodes import *
from model.Stack import Stack

class TechnologyTree:
    def __init__(self):
        self.root = TreeNode("Bienvenue dans l'arbre des Technologies", 
                             """Ici vous pourrez débloquer différentes technologies en échange de
                             **POINTS DE COMPETENCES** que vous débloquerez au fur et à mesure de la partie
                             """)
        
    
    def buildTree(self):
        # TODO import from json
        self.root.addChild(BuyableNode("DOUZE", "LE POUVOIR DU DOUZE", 12012))

    def printTree(self):
        layer = 0
        stack = Stack()
        stack.push(self.root)
        while not stack.isEmpty():
            node = stack.pop()
            i = node
