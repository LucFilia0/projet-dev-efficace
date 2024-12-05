from game.model.techno_tree.AbstractNodes import *

class NodeFactory:
    def create(nodeData : dict):
        name = nodeData["name"]
        desc = nodeData["desc"]
        match nodeData["type"]:
            case "TreeNode":
                return TreeNode(name, desc)     
            case "BuyableNode":
                return BuyableNode(name, desc, int(nodeData["cost"]))     