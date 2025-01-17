import random
import math
from game.model.Stats import Stat, Buff
from model.List import List
from typing import Self

class _Troup:

    defaultStats : Stat = Stat()
    maxUnitCount : int = 0
    cost : int = 0

    def __init__(self):
        self.stats : Stat = Stat.createFromOther(self.__class__.defaultStats) 
        self.currentBuffs : Stat = Stat()
        self.hp : int = self.stats.health
        self.skillCounter : int = 0
        self.buffs : List = List()
        self.skillUnlocked : bool = False
        self.position : int = -1

    def __str__(self):
        return f"{self.__class__.__name__}" 

    def computeBuffs(self):
        self.currentBuffs = Stat()
        curr = self.buffs.head
        while curr is not None:
            # TODO FIX BUFFS DE MERDE
            curr = curr.next
        
        return self.currentBuffs
    
    def lowerDurationOfBuffs(self):
        curr = self.buffs.head
        indexes = List()
        i = 0
        while curr is not None:
            if curr.value.duration <= 1:
                indexes.add(i)
            else:
                curr.value.duration -= 1

            curr = curr.next
            i+= 1

        curr = indexes.head
        while curr is not None:
            self.buffs.remove(curr.value)
            curr = curr.next
    
    def computeAttack(self, baseAttack : int):
        damage = (baseAttack + self.currentBuffs.attack)
        return damage if damage > 0 else 0

    def doAction(self, allies : List, enemies):
        self.computeBuffs()
        if (self.skillCounter == self.stats.cooldown and self.skillUnlocked):
            if self.useSkill(allies, enemies):
                self.skillCounter = 0
        else:
            if self.attack(allies, enemies):
                self.skillCounter += 1

    def resetValues(self):
        self.hp = self.stats.health
        self.skillCounter = 0
        self.buffs = List()
        self.position = -1

    def onDeath(self, allies : List, enemies : List):
        curr = allies.head
        count = 0
        while curr is not None:
            if (count > self.position):
                curr.value.moveForward()
            curr = curr.next
            count += 1

        allies.remove(self.position)
        
    def moveForward(self):
        self.position -= 1

    def loseHP(self, damage : int, piercing : bool, allies : List, enemies : List, source : Self):
        if (damage > 0):
            hpBefore = self.hp
            if (not piercing):
                self.hp -= damage
            else:
                self.hp -= damage - self.stats.defense
            
            if (self.hp <= 0):
                self.hp = 0
                self.onDeath(allies, enemies)
            self.onHPLost(hpBefore - self.hp, allies, enemies, source)
    
    def selectTarget(self, allies : List, enemies : List) -> int:
        effectiveRange = self.stats.range - self.position - 1
        target = -1
        if effectiveRange >= 0:
            if effectiveRange >= enemies.len:
                effectiveRange = enemies.len - 1

            target = random.randint(0, effectiveRange)
        
        return target if target < enemies.len else enemies.len - 1

    def attack(self, allies : List, enemies : List) -> bool:
        target = self.selectTarget(allies, enemies)
        if (target >= 0):
            enemy : _Troup = enemies.get(target)
            enemy.loseHP(self.computeAttack(self.stats.attack), False, allies, enemies, self)

        return target >= 0

    def useSkill(self, allies : List, enemies : List) -> bool:
        return False

    def onHPLost(self, amount : int, allies : List, enemies : List, source : Self):
        pass

    def initCorrectPosition(unitList : List):
        curr = unitList.head
        ind = 0
        while curr is not None:
            curr.value.position = ind
            curr = curr.next
            ind += 1

class Archer(_Troup):

    defaultStats = Stat(5, 2, 4, 0, 2, 3)
    maxUnitCount = 4
    skillDamage = 2

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()

    def computeHealthLeft(self, other : _Troup):
        health = other.stats.health - self.computeAttack(Archer.skillDamage)
        return health if health > 0 else 0

    def smartTargetting(self, enemies):
        """
        Returns the target that would have the least HP left if hit by the skill.
        In case of ties, it will target the furthest unit
        """
        min = 0
        minHealthLeft = -1
        curr = enemies.root
        count = 0
        while curr is not None:
            lowestHealth = self.computeHealthLeft(curr.value)
            if (lowestHealth <= minHealthLeft or minHealthLeft == -1):
                min = count
                minHealthLeft = lowestHealth

            curr = curr.next
            count += 1
        
        return min
    
    def useSkill(self, allies, enemies):
        enemy : _Troup = enemies.get(self.smartTargetting(enemies))
        enemy.loseHP(self.computeAttack(Archer.skillDamage), True, allies, enemies)
        return True

class Warrior(_Troup):

    defaultStats = Stat(8, 3, 1, 1, 2, 1)
    maxUnitCount = 4
    skillDamage = 6

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()

    def useSkill(self, allies, enemies):
        target = self.selectTarget(allies, enemies)
        if (target >= 0):
            enemy : _Troup = enemies.get(target)
            enemy.loseHP(self.computeAttack(self.skillDamage), False, allies, enemies, self)
            self.loseHP(1, True, allies, enemies, self)

        return target >= 0
            
    def onHPLost(self, amount, allies, enemies, source : _Troup):
        if (source is not self and amount >= math.ceil(self.hp)/4):
            buff = Buff(Stat(0, 1, 1, 0, 0, 0), 2)
            if (self.hp <= 2):
                buff.defense = 1
            self.buffs.add(buff)

class Lancer(_Troup):
    defaultStats = Stat(7, 2, 2, 1, 2, 2)
    maxUnitCount = 2
    skillDamage = 1

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()

    def useSkill(self, allies, enemies):
        for i in range(5):
            enemy : _Troup = enemies.get(self.selectTarget(allies, enemies))
            enemy.loseHP(self.computeAttack(self.skillDamage), True, allies, enemies, self)


if __name__ == "__main__":
    allies = List()
    enemies = List()
    allies.add(Warrior())
    allies.add(Archer())
    allies.add(Archer())
    allies.add(Archer())
    enemies.add(Warrior())
    enemies.add(Lancer())
    enemies.add(Archer())
    enemies.add(Archer())


    
