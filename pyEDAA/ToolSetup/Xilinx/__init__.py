from typing import Dict

from pyTooling.Decorators import export

from .. import Tool, Vendor


@export
class ISE(Tool):
	pass


@export
class Vivado(Tool):
	pass


@export
class VivadoSDK(Tool):
	pass


@export
class Vitis(Tool):
	pass


@export
class Xilinx(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"ISE": ISE,
		"Vivado": Vivado,
		"VivadoSDK": VivadoSDK,
		"Vitis": Vitis,
	}

	@property
	def ISE(self) -> ISE:
		return self.__getitem__("ISE")

	@property
	def Vivado(self) -> Vivado:
		return self.__getitem__("Vivado")

	@property
	def VivadoSDK(self) -> VivadoSDK:
		return self.__getitem__("Vivado-SDK")

	@property
	def Vitis(self) -> Vitis:
		return self.__getitem__("Vitis")
