from pathlib import Path
from re      import compile as re_compile

from pyTooling.Decorators import export

from pyEDAA.ToolSetup import Tool, ToolInstance


@export
class GHDL(Tool):
	pass


@export
class GHDLInstance(ToolInstance):
	_backend: str

	@property
	def Backend(self) -> str:
		return self._backend
