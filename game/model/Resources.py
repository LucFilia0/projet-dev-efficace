class Resources:
    """
    This class represents all the available resources in the game,
    and allows to easily perform comparaison and operations.
    """ 

    def __init__(self, domination=0, wealth=0, knowledge=0, gold=0, wood=0, stone=0, iron=0, food=0):
        # Score points
        self.domination = domination
        self.wealth = wealth
        self.knowledge = knowledge
        # Crafting points
        self.wood = wood
        self.stone = stone
        self.gold = gold
        self.iron = iron
        self.food = food

    def __str__(self) -> str :
        ret = ""
        if self.domination != 0 :
            ret += f"DOM {self.domination} "
        if self.wealth != 0 :
            ret += f"ECO {self.wealth} "
        if self.knowledge != 0 :
            ret += f"SAV {self.knowledge} "
        if self.gold != 0 :
            ret += f"OR {self.gold} "
        if self.wood != 0 :
            ret += f"BOI {self.wood} "
        if self.stone != 0 :
            ret += f"PIR {self.stone} "
        if self.iron != 0 :
            ret += f"FER {self.iron} "
        if self.food != 0 :
            ret += f"NUR {self.food} "
        return ret
    
    def isGreaterOrEqualThan(self, resources) -> bool :
        return (self.domination >= resources.domination 
            and self.wealth >= resources.wealth 
            and self.knowledge >= resources.knowledge 
            and self.gold >= resources.gold 
            and self.wood >= resources.wood 
            and self.stone >= resources.stone 
            and self.iron >= resources.iron 
            and self.food >= resources.food)

    def add(self, resources) -> None :
        if(resources is not None) :
            self.domination += resources.domination
            self.wealth     += resources.wealth
            self.knowledge  += resources.knowledge
            self.gold       += resources.gold
            self.wood       += resources.wood
            self.stone      += resources.stone
            self.iron       += resources.iron
            self.food       += resources.food

    def sub(self, resources) -> bool :
        if(self.isGreaterOrEqualThan(resources)) :
            self.domination -= resources.domination
            self.wealth     -= resources.wealth
            self.knowledge  -= resources.knowledge
            self.gold       -= resources.gold
            self.wood       -= resources.wood
            self.stone      -= resources.stone
            self.iron       -= resources.iron
            self.food       -= resources.food
            return True
        return False

        