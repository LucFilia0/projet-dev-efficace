from typing import Self

"""
author : Nathan
"""
class Stat:
    def __init__(self, health = 0, attack = 0, speed = 0, defense = 0, cooldown = 0, range = 0):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.defense = defense
        self.cooldown = cooldown
        self.range = range

    def __add__(self, other : Self):
        self.health += other.health
        self.attack += other.attack
        self.speed += other.speed
        self.defense += other.defense
        self.cooldown += other.cooldown
        self.range += other.range
        return self

    def __sub__(self, other):
        self.health -= other.health
        self.attack -= other.attack
        self.speed -= other.speed
        self.defense -= other.defense
        self.cooldown -= other.cooldown
        self.range -= other.range
        return self

    def __str__(self):
        return f"|  HP {self.health} | ATK {self.attack} | SPD {self.speed} |\n| DEF {self.defense} | DWN {self.cooldown} | RAN {self.range} |"

    def copy(self, other):
        self.health = other.health
        self.attack = other.attack
        self.speed = other.speed
        self.defense = other.defense
        self.cooldown = other.cooldown
        self.range = other.range

    @classmethod
    def createFromOther(cls, other):
        return Stat(other.health, other.attack, other.speed, 
                    other.defense, other.cooldown, other.range)

"""
author : Nathan
"""
class Buff:
    def __init__(self, stats : Stat = Stat(), duration : int = 0):
        self.stats : Stat = Stat.createFromOther(stats)
        self.duration : int = duration

    def __str__(self):
        return f"STATS :\n{self.stats}\nDURATION : {self.duration}"