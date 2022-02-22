from typing import cast

from pyTooling.Decorators import export
from pyTooling.Configuration.YAML import Dictionary

from .. import Tool, ToolInstance
from pyEDAA.CLITool.GHDL import GHDL as CLI_GHDL


@export
class GHDLInstance(ToolInstance):
	_platform: str
	_runtime: str
	_backend: str

	def __init__(self, config: Dictionary, parent: 'GHDL'):
		super().__init__(config, parent)

		self._platform = config["Platform"]
		self._runtime = config["Runtime"]
		self._backend = config["Backend"]

	@property
	def Platform(self) -> str:
		"""Platform GHDL runs on: ``win32``, ``win64``, ``lin64``."""
		return self._platform

	@property
	def Runtime(self) -> str:
		"""Runtime used to run GHDL: ``mingw32``, ``mingw64``, ``ucrt64``, ``gnatgpl32``, ``lin64``."""
		return self._runtime

	@property
	def Backend(self) -> str:
		"""GHDL's backend (``mcode``, ``llvm`` or ``gcc``."""
		return self._backend

	def GetGHDL(self) -> CLI_GHDL:
		return CLI_GHDL(binaryDirectoryPath=self.BinaryDirectory)


@export
class GHDL(Tool):
	_vendorKey = "OpenSource"      #: Key of the parent node (vendor) in the configuration structure.
	_key = "GHDL"                  #: Key used in the configuration structure.

	_instanceClass = GHDLInstance

	@property
	def Default(self) -> GHDLInstance:
		return cast(GHDLInstance, super().Default)
