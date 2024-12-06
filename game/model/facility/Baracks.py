from game.model.Facility import Facility
from game.model.Resources import Resources

class Baracks(Facility) :

	def __init__(self) :
		super().__init__("Caserne", Resources(wood=4, stone=6))