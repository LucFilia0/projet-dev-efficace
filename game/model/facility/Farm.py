from game.model.Facility import Facility
from game.model.Resources import Resources

class Farm(Facility) :

	def __init__(self) :
		super().__init__("Ferme", Resources(wood=4, stone=2, food=1), Resources(food=6), 3, 1)