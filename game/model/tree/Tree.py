from typing import Self
from json import load
from os import getcwd

from game.model.tree.TreeNode import _TreeNode
from game.model.tree.TreeNode import *
from game.model.Campaign import *
from game.model.Facility import *
from game.model.Troups import *

from game.view.prompt import *

class _Tree :

    def __init__(self, player, jsonPath : str|None = None) -> Self :
        self.root : _TreeNode|None = None
        self.player = player
        self._build(jsonPath)

    def _build(self, jsonPath : str|None) -> bool :
        """
        Builds the tree from a json file, it will first create the root, then recursively 
        let each node create its children
        author : Nathan
        """ 
        if jsonPath is not None :
            with open(getcwd() + jsonPath) as jsonFile :
                data = load(jsonFile)
                root = data["root"]
                if root is None :
                    return False
                
                self.root = TreeNodeFactory.create(root)
                if self.root is None :
                    print("self.root est nul.")
                else :
                    self.root.addChildrenRec(root)

    def getNodeByName(self, name : str) -> _TreeNode|None :
        """
        Finds a node in the Tree
        returns the Node if it exists, None if it doesn't
        """
        if self.root is not None :
            return self.root.searchChild(name)
        return None

    def navigate(self) -> None :
        """
		Displays the tree in a little menu that lets the player simply navigate through it, 
		read information about Technologies he has access to, or unlock new ones.
		author : Nathan
		"""
        if self.root is None :
            print("L'arbre est vide...")
        else :
            self._processNavigation()
    
    def _processNavigation(self) -> None :
        print("La navigation de l'arbre est non définie.")

class TechnologyTree(_Tree) :

    def __init__(self, player, jsonPath : str = "/data/technology.json") -> Self :
        super().__init__(player, jsonPath)
        self.root.unlocked = True
    
    def isUnlocked(self, technologyName : str|None) -> bool|None :
        """
        Returns True if the technology is unlocked, else False.
        Must enter the technology name.
        """
        node = self.getNodeByName(technologyName)
        if node is not None :
            return node.unlocked
        return True
    
    def _processNavigation(self) -> None :

        node = self.root
        nodeStack = Stack()
        done = False

        while not done:
            maxSelection = node.children.len + 1
            stackNotEmpty = not nodeStack.isEmpty()
            if stackNotEmpty:
                maxSelection += 1

            promptStatus(node.name)
                
            select = userInputInt(node.printChildren(stackNotEmpty), 0, maxSelection)
            # Quit option
            if select == 0:
                done = True

            # Accessing any technology
            if (select <= node.children.len):
                nodeStack.push(node)
                node = node.children.get(select - 1)

            # Unlocking a technology if it is buyable
            elif select == node.children.len + 1 and node.canLearn():
                self.player.learnTechnology(node)

            # Going back to the parent
            else:
                node = nodeStack.pop()

class ActionTree(_Tree) :

    def __init__(self, player, jsonPath : str = "/data/action.json") -> Self :
        super().__init__(player, jsonPath)
    
    def _processNavigation(self) -> None :

        node = self.root
        nodeStack = Stack()
        done = False

        nodeStack.push(node)

        while not nodeStack.isEmpty() :

            promptStatus(node.title)
            print(node.desc + "\n")

            self._execCallback(node, nodeStack)

            unlockedNodes = self._getUnlockedChildren(node)
                
            select = userInputInt(unlockedNodes.printChildren(nodeStack.size() != 1), 0, unlockedNodes.children.len)

            # Get back
            if select == 0 :
                node = nodeStack.pop()
                done = True if nodeStack.isEmpty() else False
            else :
                nodeStack.push(node)
                node = unlockedNodes.children.get(select - 1)

        Campaign.getInstance().nextPlayer()
    
    def _getUnlockedChildren(self, node : ActionNode) -> ActionNode :

        unlockedChildren = ActionNode(node.name, node.title, node.desc, node.callback, node.required)

        for i in range(node.nbChildren()) :
            n = node.children.get(i)
            if n.required is None or (n.required[0] is None or self.player.technoTree.isUnlocked(n.required[0])) and (n.required[1] is None or self.player.city.contains(n.required[1])) :
                unlockedChildren.children.add(n)

        return unlockedChildren
    
    def _execCallback(self, node : ActionNode, stack : Stack) -> None :

        match(node.callback) :

            case "promptFacilities" :
                self.player.promptFacilities()

            case "buildFacility" :
                match(node.name) :

                    case "Habitation" :
                        facility = Habitation()
                    case "Ferme" :
                        facility = Farm()
                    case "Caserne" :
                        facility = Baracks()
                    case "Mine" :
                        facility = Mine()
                    case "Forge" :
                        facility = Forge()
                    case "Scierie" :
                        facility = SawMill()
                    case "Cabane de chasseur" :
                        facility = HunterHood()
                    case "Temple" :
                        facility = Temple()
                    case "Autel" :
                        facility = Altar()
                    
                self.player.buildFacility(facility)
                promptStatus(node.title)
                print(node.desc)
            
            case "addTroup" :
                match(node.name) :

                    case "Guerrier" :
                        troup = Warrior()
                    case "Archer" :
                        troup = Archer()
                    case "Lancier" :
                        troup = Lancer()
                    case "Cavalier" :
                        troup = Rider()
                    case "Prêtre" :
                        pass
                        # troup = Priest()
                
                if self.player.canAddTroup() :
                    self.player.addTroup(troup)

                promptStatus(node.title)
                print(node.desc)
            
            case "promptTroups" :
                self.player.promptTroups()
            
            case "technologyTreeNavigate" :
                self.player.technoTree.navigate()
                promptStatus(node.title)
                print(node.desc)
            
            case "declareWar" :
                self.player.declareWar()