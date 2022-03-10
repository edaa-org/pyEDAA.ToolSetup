from typing import Dict

from pyTooling.Decorators import export

from .. import Vendor, Tool
from ..OpenSource.GHDL import GHDL
from ..OpenSource.GTKWave import GTKWave


@export
class OpenSource(Vendor):
	_vendorName = "Open Source"
	_vendorKey = "OpenSource"
	_toolClasses: Dict[str, Tool] = {
		"GHDL": GHDL,
		"GTKWave": GTKWave,
	}

	@property
	def GHDL(self) -> GHDL:
		return self.__getitem__("GHDL")

	@property
	def GTKWave(self) -> GTKWave:
		return self.__getitem__("GTKWave")
