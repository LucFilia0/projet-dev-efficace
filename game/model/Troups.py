import random
import math
from game.model.God import _God
from game.model.Stats import Stat, Buff
from model.Queue import Queue
from model.List import List
from typing import Self
from colorama import Fore, Style
from game.model.Resources import Resources

"""
author : Nathan
"""
class UnitGroup:
    def __init__(self, units : List):
        self.units : List = units
        self.ind : int = 0
        self.initCorrectPosition()
        self.damaged : set = set()
        self.selected : _Troup = None

    def initCorrectPosition(self):
        curr = self.units.head
        ind = 0
        while curr is not None:
            curr.value.position = ind
            curr = curr.next
            ind += 1
    
    def __str__(self):
        ret = ""
        current = self.units.head
        while (current is not None):
            if (current.value in self.damaged):
                ret += f"{Fore.RED} {current.value.completeStr()}{Style.RESET_ALL}"
            elif current.value is self.selected:
                ret += f"{Fore.BLUE} {current.value.completeStr()}{Style.RESET_ALL}"
            else:
                ret += f" {current.value.completeStr()}"
            current = current.next
            if (current is not None):
                ret += " <"

        if (len(ret) != 0):
            ret = "<= " + ret

        return ret
    
    def strWithoutColor(self, reverse=False):
        if reverse:
            ret = ""
            current = self.units.tail
            while (current is not None):
                ret += f" {current.value.completeStr()}"
                current = current.prev
                if (current is not None):
                    ret += " >"

            if (len(ret) != 0):
                ret += " =>"
                
            return ret
        else:
            ret = ""
            current = self.units.head
            while (current is not None):
                ret += f" {current.value.completeStr()}"
                current = current.next
                if (current is not None):
                    ret += " <"

            if (len(ret) != 0):
                ret = "<= " + ret

            return ret

    def reverseStr(self):
        ret = ""
        current = self.units.tail
        while (current is not None):
            if (current.value in self.damaged):
                ret += f"{Fore.RED} {current.value.completeStr()}{Style.RESET_ALL}"
            elif current.value is self.selected:
                ret += f"{Fore.BLUE} {current.value.completeStr()}{Style.RESET_ALL}"
            else:
                ret += f" {current.value.completeStr()}"
            current = current.prev
            if (current is not None):
                ret += " >"

        if (len(ret) != 0):
            ret += " =>"
            
        return ret

    def unitDied(self, position : int):
        self.units.remove(position)
        if (self.ind > position):
            self.ind -= 1

    def lowerBuffDuration(self):
        curr = self.units.head
        while curr is not None:
            curr.value.lowerDurationOfBuffs()
            curr = curr.next
        
"""
author : Nathan
"""
class _Troup:

    defaultStats : Stat = Stat()
    maxUnitCount : int = 0
    skillUnlocked : bool = True
    skillName : str = ""
    messages : dict[str, str] = {
        "death" : "{0} est mort des mains de {1}...",
        "attack" : "{0} a fait {1} dégats à {2} !",
        "skill" : "{0} a utilisé {1} sur {2} ! {2} a perdu {3} PV",
        "skill2" : "{0} a utilisé {1} ! Il a fait {2} dégats au total !",
        "knockback" : "{0} a pris {1} dégats de contrecoup",
        "heal" : "{0} a soigné toute les troupes de {1} HP !",
        "buff" : "{0} a augmente la statistique {1} de toute l'unité de {2} points",
        "buffST" : "{0} a augmenté sa statistique {1} de {2} points"
    }

    def __init__(self, name, desc, cost):
        self.stats : Stat = Stat.createFromOther(self.__class__.defaultStats) 
        self.name = name
        self.desc = desc
        self.cost = cost
        self.currentBuffs : Stat = Stat()
        self.hp : int = self.stats.health
        self.skillCounter : int = 0
        self.buffs : List = List()
        self.position : int = -1

    def getMaxHealth(self):
        return max(self.stats.health + self.currentBuffs.health, 1)
    
    def getAttack(self):
        return max(self.stats.attack + self.currentBuffs.attack, 0)
    
    def getSpeed(self):
        return max(self.stats.speed + self.currentBuffs.speed, 0)
    
    def getDefense(self):
        return max(self.stats.defense + self.currentBuffs.defense, 0)
    
    def getCooldown(self):
        return max(1, self.stats.cooldown + self.currentBuffs.cooldown)
    
    def getRange(self):
        return max(1, self.stats.range + self.currentBuffs.range)
    
    def __str__(self):
        return f"{self.name}"
    
    def summary(self) -> str :
        return f"{self.name.ljust(15)}{self.hp}/{self.stats.health} PV"

    def details(self) -> str :
        return (
            f"Coût :          [ {self.cost}]\n"
            f"Vie :           {self.hp}/{self.stats.health} PV"
        )

    def positionStr(self):
        return f"{self.name}[{self.position}]"

    def completeStr(self):
        return f"{self.name}[{self.position}] HP : {self.hp}"

    def computeBuffs(self):
        self.currentBuffs = Stat()
        curr = self.buffs.head
        while curr is not None:
            stats : Stat = curr.value.stats
            self.currentBuffs += stats
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

        curr = indexes.tail
        while curr is not None:
            self.buffs.remove(curr.value)
            curr = curr.prev
    
    def computeAttack(self, baseAttack : int):
        damage = (baseAttack + self.currentBuffs.attack)
        return max(damage, 0)

    def doAction(self, allies : UnitGroup, enemies : UnitGroup) -> Queue:
        self.computeBuffs()
        actionQueue = Queue()
        if (self.skillCounter == self.stats.cooldown and self.__class__.skillUnlocked):
            if self.useSkill(allies, enemies, actionQueue):
                self.skillCounter = 0
        else:
            if self.attack(allies, enemies, actionQueue):
                self.skillCounter += 1

        return actionQueue

    def resetValues(self):
        self.hp = self.stats.health
        self.currentBuffs = Stat()
        self.skillCounter = 0
        self.buffs = List()
        self.position = -1

    def onDeath(self, allies : UnitGroup, enemies : UnitGroup, source : Self, queue : Queue):
        curr = allies.units.head
        count = 0
        queue.push(_Troup.messages.get("death").format(self.positionStr(), source.positionStr()))
        while curr is not None:
            if (count > self.position):
                curr.value.moveForward()
            curr = curr.next
            count += 1
        
        allies.unitDied(self.position)
        
    def moveForward(self):
        self.position -= 1

    def loseHP(self, damage : int, piercing : bool, allies : UnitGroup, enemies : UnitGroup, source : Self, queue : Queue):
        if (damage > 0):
            allies.damaged.add(self)
            hpBefore = self.hp
            if (piercing):
                self.hp -= damage
            else:
                self.hp -= damage - self.getDefense()
            
            if (self.hp <= 0):
                self.hp = 0
                self.onDeath(allies, enemies, source, queue)
            self.onHPLost(hpBefore - self.hp, allies, enemies, source)
    
    def selectTarget(self, allies : UnitGroup, enemies : UnitGroup) -> int:
        effectiveRange = self.stats.range - self.position - 1
        effectiveRange = min(effectiveRange, enemies.units.len - 1)
        target = effectiveRange
        if effectiveRange >= 0:
            if (effectiveRange > 0):
                target = random.randint(0, effectiveRange)
        
        return target

    def attack(self, allies : UnitGroup, enemies : UnitGroup, queue : Queue) -> bool:
        target = self.selectTarget(allies, enemies)
        if (target >= 0):
            enemy : _Troup = enemies.units.get(target)
            damage = self.getAttack() - enemy.getDefense()
            if damage > enemy.hp:
                damage = enemy.hp
            elif damage < 0:
                damage = 0
            enemy.loseHP(self.getAttack(), False, enemies, allies, self, queue)
            queue.push(_Troup.messages.get("attack").format(self.positionStr(), damage, enemy.positionStr()))

        return target >= 0

    def useSkill(self, allies : UnitGroup, enemies : UnitGroup, queue : Queue) -> bool:
        return False

    def onHPLost(self, amount : int, allies : UnitGroup, enemies : UnitGroup, source : Self):
        pass

"""
author : Nathan
"""
class Archer(_Troup):

    defaultStats = Stat(5, 2, 4, 0, 2, 3)
    maxUnitCount = 4
    skillDamage = 2
    skillName = "Killer Arrow"

    def __init__(self):
        super().__init__("Archer", "Unité attaquant à distance capable d'éliminer les ennmis à l'arrière.", Resources(wood=2, food=2))

    def __str__(self):
        return super().__str__()

    def computeHealthLeft(self, other : _Troup):
        health = other.hp - self.computeAttack(Archer.skillDamage)
        return health if health > 0 else 0

    def smartTargetting(self, enemies : UnitGroup):
        """
        Returns the target that would have the least HP left if hit by the skill.
        In case of ties, it will target the furthest unit
        """
        min = 0
        minHealthLeft = -1
        curr = enemies.units.head
        count = 0
        while curr is not None:
            lowestHealth = self.computeHealthLeft(curr.value)
            if (lowestHealth <= minHealthLeft or minHealthLeft == -1):
                min = count
                minHealthLeft = lowestHealth

            curr = curr.next
            count += 1
        
        return min
    
    def useSkill(self, allies, enemies, queue):
        enemy : _Troup = enemies.units.get(self.smartTargetting(enemies))
        if enemy is not None:
            damage = self.computeAttack(Archer.skillDamage)
            if damage > enemy.hp:
                damage = enemy.hp
            enemy.loseHP(self.computeAttack(Archer.skillDamage), True, enemies, allies, self, queue)
            queue.push(_Troup.messages.get("skill").format(self.positionStr(), self.skillName, enemy.positionStr(), damage))
            return True
        return False

"""
author : Nathan
"""
class Warrior(_Troup):

    defaultStats = Stat(8, 3, 1, 2, 2, 1)
    maxUnitCount = 4
    skillDamage = 6
    skillName = "Berserk Slash"

    def __init__(self):
        super().__init__("Guerrier", "Combattant au corps à corps gagnant en puissance quand il est affaibli.", Resources(wood=2, food=2))

    def __str__(self):
        return super().__str__()

    def useSkill(self, allies, enemies, queue):
        target = self.selectTarget(allies, enemies)
        if (target >= 0):
            damage = self.computeAttack(Warrior.skillDamage)
            enemy : _Troup = enemies.units.get(target)
            if damage > enemy.hp:
                damage = enemy.hp
            queue.push(_Troup.messages.get("skill").format(self.positionStr(), self.skillName, enemy.positionStr(), damage))
            queue.push(_Troup.messages.get("knockback").format(self.positionStr(), 1))

            enemy.loseHP(self.computeAttack(self.skillDamage), False, enemies, allies, self, queue)
            self.loseHP(2, True, allies, enemies, self, queue)

        return target >= 0
            
    def onHPLost(self, amount, allies, enemies, source : _Troup):
        if (source is not self and amount >= math.ceil(self.hp)/4):
            buff = Buff(Stat(0, 1, 1, 0, 0, 0), 2)
            if (self.hp <= 2):
                buff.defense = 1
            self.buffs.add(buff)


"""
author : Nathan
"""
class Lancer(_Troup):
    defaultStats = Stat(7, 2, 2, 1, 2, 2)
    maxUnitCount = 2
    skillDamage = 1
    skillName = "Flurry Attack"

    def __init__(self):
        super().__init__("Lancier", "Combattant au corps à corps avec une plus grande portée.", Resources(wood=2, stone=1, food=2))

    def __str__(self):
        return super().__str__()

    def useSkill(self, allies, enemies, queue):
        damage = 0
        for i in range(3):
            enemy : _Troup = enemies.units.get(self.selectTarget(allies, enemies))
            if (enemy is not None):
                damage += 1
                enemy.loseHP(self.computeAttack(self.skillDamage), True, enemies, allies, self, queue)
        queue.push(_Troup.messages.get("skill2").format(self.positionStr(), self.skillName, damage))

class Priest(_Troup):

    defaultStats = Stat(5, 1, 1, 0, 1, 1)
    maxUnitCount = 1
    skillDamage = 2
    skillName = "Coup de Bâton"

    def __init__(self):
        super().__init__("Prêtre", "Religieux pouvant communier avec son Dieu pour obtenir de puissants pouvoirs.", Resources(food=1, wood=1, knowledge=2))
        self.god = None
        self.updateGod()

    def updateGod(self):
        god = _God.getInstance()
        if (god is not None):
            self.name = f"Prêtre de {god.name}"
            Priest.skillName = self.getSkillName(god.godId)
            self.stats.copy(god.priestStat)
            Priest.skillDamage = god.priestSkillDamage

    def getSkillName(self, godId : int) -> str:
        match(godId):
            case 0:
                return "Bénédiction d'Athéna"
            case 1:
                return "Massacre d'Arès"
            case 2:
                return "Miracle de Démeter"
            case _:
                return "Coup de Bâton"

    def useSkill(self, allies, enemies, queue)-> bool:
        god = _God.getInstance()
        godId = -1 if god is None else god.godId
        res = False
        match(godId):
            case -1:
                res = self.defaultSkill(allies, enemies, queue)
            case 0:
                res = self.athenaSkill(allies, enemies, queue)
            case 1:
                res = self.aresSkill(allies, enemies, queue)
            case 2:
                res = self.demeterSkill(allies, enemies, queue)
        
        return res
        
    def defaultSkill(self, allies : UnitGroup, enemies : UnitGroup, queue : Queue):
        target = self.selectTarget(allies, enemies)
        if (target >= 0):
            damage = self.computeAttack(Archer.skillDamage)
            enemy : _Troup = enemies.units.get(target)
            if damage > enemy.hp:
                damage = enemy.hp
            queue.push(_Troup.messages.get("skill").format(self.positionStr(), self.skillName, enemy.positionStr(), damage))
            enemy.loseHP(damage, False, enemies, allies, self, queue)
        
        return target >= 0

    def demeterSkill(self, allies : UnitGroup, enemies : UnitGroup, queue : Queue):
        curr = allies.units.head
        heal = self.computeAttack(Priest.skillDamage)
        while curr is not None:
            ally : _Troup = curr.value
            newHp = ally.hp + heal
            ally.hp = min(newHp, ally.__class__.defaultStats.health)
            curr = curr.next

        queue.push(_Troup.messages.get("heal").format(self.positionStr(), heal))


    def aresSkill(self, allies : UnitGroup, enemies : UnitGroup, queue : Queue):
        target = math.floor(enemies.units.len/2)
        damageList = List()
        totalDamage = 0
        if (target >= 0):
            damage = self.computeAttack(Priest.skillDamage)
            totalDamage += damage
            enemy : _Troup = enemies.units.get(target)
            damageList.append((enemy, damage))  

            leftInd = enemy.position - 1
            rightInd = enemy.position + 1

            damageDealt = int(math.floor(damage/2))     
            while leftInd >= 0 and damageDealt > 0:
                enemy : _Troup = enemies.units.get(leftInd)
                totalDamage += damageDealt
                damageList.append((enemy, damageDealt))
                damageDealt = int(math.floor(damage/2))
                leftInd -= 1

            damageDealt = int(math.floor(damage/2))
            while rightInd < enemies.units.len and damageDealt > 0:
                enemy : _Troup = enemies.units.get(rightInd)
                totalDamage += damageDealt
                damageList.append((enemy, damageDealt))
                damageDealt = int(math.floor(damage/2))
                rightInd += 1
        
        queue.push(_Troup.messages.get("skill2").format(self.positionStr(), Priest.skillName, totalDamage))
        curr = damageList.head
        while curr is not None:
            enemy, damage = curr.value
            enemy.loseHP(damage, True, enemies, allies, self, queue)
            curr = curr.next
        

        return target >= 0

    def athenaSkill(self, allies : UnitGroup, enemies : UnitGroup, queue : Queue):
        curr = allies.units.head
        while curr is not None:
            ally : _Troup = curr.value
            if (ally.stats.range <= 2):
                ally.buffs.add(Buff(Stat(attack=Priest.skillDamage), 2))
                ally.computeBuffs()
            curr = curr.next

        queue.push("{0} a augmenté l'attaque de toutes les unités au corps à corps de {1}".format(self.positionStr(), Priest.skillDamage))


"""
author : Luc
Unimplemented yet
"""                
class Rider(_Troup) :

    defaultStats = Stat(6, 3, 2, 3, 3, 2)
    maxUnitCount = 2
    skillDamage = 1
    skillName = "Flurry Attack"

    def __init__(self):
        super().__init__("Cavalier", "Combattant en armure et à cheval. Wallou", Resources(wood=2, food=4, iron=3))


    
