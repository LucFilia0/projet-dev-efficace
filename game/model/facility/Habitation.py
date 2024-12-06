from game.model.Facility import Facility
from game.model.Resources import Resources

class Habitation(Facility) :

	def __init__(self) :
		super().__init__("Habitation", Resources(wood=4, stone=2), 4, 0, 1)
	
	def gain(self) -> Resources|int|None :
		if super().state == 0 :
			super().state = 1
			return super().gain