import math
import random
import os
from game.model.Troups import _Troup, Warrior, UnitGroup, Archer, Lancer
from model.List import List
from game.view.prompt import userInputStr, userInputInt
from colorama import Fore, Style

from model.Queue import Queue

class Fight:

    def __init__(self, player1Units : UnitGroup, player2Units : UnitGroup):
        self.p1Units = player1Units
        self.p2Units = player2Units
    
    def regenerateInstance(cls, player1Units, player2Units):
        cls.instance = Fight(player1Units, player2Units)

    def printInfo(self):
        terminal = math.floor(os.get_terminal_size().columns/3)
        player1str = f"⚔️  {self.p1Units.units.len} Units Left"
        centerStr = "J1 vs J2"
        player2str = f"{self.p2Units.units.len} Units Left ⚔️"
        header = player1str.rjust(terminal) + centerStr.center(terminal) + player2str
        print(header)

    def printTroups(self, padding):
        allowedSpace = math.floor(os.get_terminal_size().columns/2) - padding
        str1 = self.p1Units.reverseStr()
        str2 = str(self.p2Units)
        currentFight = " "*(allowedSpace - len(self.p1Units.strWithoutColor(True)))  + str1 + " "*padding*2 + str2
        print(currentFight)

    def getNextAttacker(self) -> tuple:
        if (self.p1Units.ind >= self.p1Units.units.len):
            return self.p2Units.units.get(self.p2Units.ind), 2
        if self.p2Units.ind >= self.p2Units.units.len:
            return self.p1Units.units.get(self.p1Units.ind), 1
        
        p1Unit = self.p1Units.units.get(self.p1Units.ind)
        p2Unit = self.p2Units.units.get(self.p2Units.ind)
        
        p1SPD = p1Unit.getSpeed()
        p2SPD = p2Unit.getSpeed() 
        if (p1SPD > p2SPD or (p1SPD == p2SPD and random.randint(0,1) == 0)):
            return p1Unit, 1
        return p2Unit, 2

    def fightLoop(self, padding):
        os.system("clear || cls")
        self.p1Units.damaged.clear()
        self.p2Units.damaged.clear()
        queue = self.currentUnitAction()

        print("\n\n")
        self.printInfo()

        print("")
        self.printTroups(padding)
        
        if queue is not None and not queue.isEmpty():
            print("")
            while not queue.isEmpty():
                print(queue.pop())

            input("\nAppuyez sur Entrée pour passer à la suite >> ")

    def fight(self):
        troupPadding = max(math.floor(os.get_terminal_size().columns/12), 6)

        while self.p1Units.units.len != 0 and self.p2Units.units.len != 0:
            self.p1Units.ind = 0
            self.p2Units.ind = 0

            self.p1Units.lowerBuffDuration()
            self.p2Units.lowerBuffDuration()
            while (self.p1Units.ind < self.p1Units.units.len or self.p2Units.ind < self.p2Units.units.len):
                self.fightLoop(troupPadding)
            
        if (self.p1Units.units.len > 0):
            return 1
        elif (self.p2Units.units.len > 0):
            return 2
        else:
            return 0
        
    def currentUnitAction(self) -> Queue:
        currentUnit, player = self.getNextAttacker()
        currentUnit : _Troup
        queue = None
        if (currentUnit is not None):
            if (player == 1):
                self.p1Units.selected = currentUnit
                self.p2Units.selected = None
                queue = currentUnit.doAction(self.p1Units, self.p2Units)
            else:
                self.p1Units.selected = None
                self.p2Units.selected = currentUnit
                queue = currentUnit.doAction(self.p2Units, self.p1Units)

            if (currentUnit.hp > 0):
                if (player == 1):
                    self.p1Units.ind += 1
                else:
                    self.p2Units.ind += 1

        return queue

if __name__ == "__main__":
    p1Units = List()
    p2Units = List()

    p1Units.append(Warrior())
    p1Units.append(Lancer())
    p1Units.append(Archer())
    p1Units.append(Archer())

    p2Units.append(Warrior())
    p2Units.append(Lancer())
    p2Units.append(Archer())
    p2Units.append(Archer())

    fight = Fight(UnitGroup(p1Units), UnitGroup(p2Units))
    print(fight.fight())

