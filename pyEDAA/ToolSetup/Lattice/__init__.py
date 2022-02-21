from typing import Dict

from pyTooling.Decorators import export

from ..             import Tool, Vendor
from ..Aldec        import ActiveHDL
from ..SiemensEDA   import ModelSim


@export
class Diamond(Tool):
	pass


@export
class Lattice(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"Diamond": Diamond,
		"Active-HDL": ActiveHDL,
		"ModelSim": ModelSim,
	}

	@property
	def Diamond(self) -> Diamond:
		return self.__getitem__("Diamond")

	@property
	def ActiveHDL(self) -> ActiveHDL:
		return self.__getitem__("Active-HDL")

	@property
	def ModelSim(self) -> ModelSim:
		return self.__getitem__("ModelSim")
