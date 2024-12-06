from game.model.techno_tree.AbstractNodes import *

class NodeFactory:
    def create(nodeData : dict) -> TreeNode :
        name = nodeData["name"]
        desc = nodeData["desc"]
        match nodeData["type"]:
            case "TreeNode":
                return TreeNode(name, desc)     
            case "BuyableNode":
                return BuyableNode(name, desc, nodeData["cost"])
            case "TextNode":
                return TextNode(name, desc)
            case _:
                return None