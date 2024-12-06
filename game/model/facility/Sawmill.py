from game.model.Facility import Facility
from game.model.Resources import Resources

class Sawmill(Facility) :

	def __init__(self) :
		super().__init__("Scierie", Resources(wood=12, stone=6, iron=1), Resources(wood=2), 1, 2)