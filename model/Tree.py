from List import *

class Tree:
    class Node:
        def __init__(self, value, ls=None, rs=None):
            self.value = value
            self.ls = ls
            self.rs = rs
        
        def depth(node) -> int:
            if node is None :
                return 0
            else:
                return max(Tree.Node.depth(node.ls), Tree.Node.depth(node.rs)) + 1

        
    def __init__(self):
        self.root = None
        self.itemCount = 0

    def add(self, value) -> bool:
        if (self.root is None):
            self.root = self.Node(value)
            return True
        
        done = False
        current = self.root
        while not done:
            if value < current.value:
                if current.ls is None:
                    current.ls = self.Node(value)
                    done = True
                else:
                    current = current.ls
            elif value > current.value:
                if current.rs is None:
                    current.rs = self.Node(value)
                    done = True
                else:
                    current = current.rs
            else:
                done = False

        return done
    
    def depth(self) -> int:
        return Tree.Node.depth(self.root)
    
        
    
if __name__ == "__main__":
    tree = Tree()
    tree.add(12)
    tree.add(14)
    tree.add(13)
    tree.add(8)
    tree.add(10)
    print(tree.depth())




