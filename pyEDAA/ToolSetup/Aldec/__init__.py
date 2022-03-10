from typing import Dict

from pyTooling.Decorators import export

from .. import Vendor, Tool, ToolInstance


@export
class ActiveHDLInstance(ToolInstance):
	pass


@export
class RivieraPROInstance(ToolInstance):
	pass


@export
class ActiveHDL(Tool):
	_instanceClass = ActiveHDLInstance


@export
class RivieraPRO(Tool):
	_instanceClass = RivieraPROInstance


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
