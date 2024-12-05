class Resources:

    def __init__(self, domination=0, economy=0, knowledge=0, gold=0, wood=0, stone=0, iron=0, food=0):
        # Score points
        self.domination = domination
        self.economy = economy
        self.knowledge = knowledge
        # Crafting points
        self.gold = gold
        self.wood = wood
        self.stone = stone
        self.iron = iron
        self.food = food
    
    def __str__(self) -> str :
        ret = ""
        if self.domination != 0 :
            ret += f"DOM {self.domination} "
        if self.economy != 0 :
            ret += f"ECO {self.economy} "
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
        return self.domination >= resources.domination and self.economy >= resources.economy and self.knowledge >= resources.knowledge and self.gold >= resources.gold and self.wood >= resources.wood and self.stone >= resources.stone and self.iron >= resources.iron and self.food >= resources.food 

        