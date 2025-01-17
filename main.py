from game.view.menu import menu
from game.view.menu import test
# menu()
# test()
import math
import random
import os
from game.model.Troups import _Troup, Warrior, UnitGroup, Archer, Lancer
from model.List import List
from game.view.prompt import userInputStr, userInputInt
from colorama import Fore, Style
from game.model.Fight import Fight

from model.Queue import Queue
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