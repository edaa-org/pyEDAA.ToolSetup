from typing import Dict

from pyTooling.Decorators import export

from ..             import Tool, Vendor
from ..SiemensEDA   import ModelSim


@export
class Quartus(Tool):
	pass


@export
class IntelFPGA(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"Quartus": Quartus,
		"ModelSim": ModelSim,
	}

	@property
	def Quartus(self) -> Quartus:
		return self.__getitem__("Quartus")

	@property
	def ModelSim(self) -> ModelSim:
		return self.__getitem__("ModelSim")


Altera = IntelFPGA
