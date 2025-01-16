class _Soldier :

    def __init__(self, name : str, attack : int, health : int) :
        self.name = name
        self.attack = attack
        self.health = health
        self.maxHealth = health

    def __str__(self) -> str :
        return f"{self.name.ljust(20)}{self.health}/{self.maxHealth}"
    
    def takeDamage(self, damage : int) -> bool :
        self.health -= damage
        if self.health > 0 :
            return False
        self.health = 0
        return True
    
    def attack(self, target) -> None :
        target.takeDamage(self.attack)
    
class Warrior(_Soldier) :

    def __init__(self) :
        super().__init__("Guerrier", 3, 5)

class Garde(_Soldier) :

    def __init__(self) :
        super().__init__("Garde", 1, 8)
    
class Archer(_Soldier) :

    def __init__(self) :
        super().__init__("Archer", 2, 4)