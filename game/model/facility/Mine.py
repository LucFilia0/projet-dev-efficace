from game.model.Facility import Facility
from game.model.Resources import Resources

class Mine(Facility) :

	def __init__(self) :
		super().__init__("Mine", Resources(wood=8), 0, 2, 2)