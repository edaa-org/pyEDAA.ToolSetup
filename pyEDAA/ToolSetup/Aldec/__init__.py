from typing import Dict

from pyTooling.Decorators import export

from .. import Tool, Vendor


@export
class ActiveHDL(Tool):
	pass


@export
class RivieraPRO(Tool):
	pass


@export
class Aldec(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"Active-HDL": ActiveHDL,
		"Riviera-PRO": RivieraPRO,
	}

	@property
	def ActiveHDL(self) -> ActiveHDL:
		return self.__getitem__("Active-HDL")

	@property
	def RivieraPRO(self) -> RivieraPRO:
		return self.__getitem__("Riviera-PRO")
