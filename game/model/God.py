from typing import Self
from game.view.prompt import userInputInt
from game.model.Stats import Stat
class _God:
    instance = None

    def __init__(self, godId : int, name : str, priestStat : Stat, priestSkillDamage : int):
        self.godId = godId
        self.name = name
        self.priestStat = priestStat
        self.priestSkillDamage = priestSkillDamage

    def getInstance():
        return _God.instance

    def create(godId) -> Self:
        match(godId):
            case 0:
                _God.instance = Athena()
            case 1:
                _God.instance = Ares()
            case 2:
                _God.instance = Demeter()

        return _God.instance

    def unlockGod(godId) -> bool:
        match(godId):
            case 0:
                god = "Athéna"
            case 1:
                god = "Arès"
            case 2:
                god = "Démeter"
            
        select = userInputInt("[0] Quitter\n[1] Choisir", 0, 1)
        if (select == 1):
            input(f"Vous avez prêté allégeance à {god} !\n>> ")
            _God.instance = _God.create(godId)
        return select == 1
    
class Athena(_God):
    def __init__(self):
        super().__init__(0, "Athéna", Stat(5, 2, 5, 0, 1, 3), 1)

class Ares(_God):
    def __init__(self):
        super().__init__(1, "Arès", Stat(5, 3, 0, 0, 1, 3), 4)

class Demeter(_God):
    def __init__(self):
        super().__init__(2, "Démeter", Stat(5, 1, 3, 2, 1, 3), 2)


