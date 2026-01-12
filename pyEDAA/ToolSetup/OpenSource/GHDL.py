from typing import cast

from pyTooling.Decorators import export
from pyTooling.Configuration.YAML import Dictionary
from pyTooling.CLIAbstraction import Executable
from ..          import Tool, ToolInstance
from ..Interface import HDLSimulator
from pyEDAA.CLITool.GHDL import GHDL as CLI_GHDL


@export
class GHDLInstance(ToolInstance, HDLSimulator):
	_platform: str
	_runtime: str
	_backend: str
	_ghdl: CLI_GHDL

	def __init__(self, config: Dictionary, parent: 'GHDL') -> None:
		super().__init__(config, parent)

		self._ghdl = None
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

	def _CreateGHDLCLIInstance(self) -> CLI_GHDL:
		if self._ghdl is None:
			self._ghdl = CLI_GHDL(binaryDirectoryPath=self.BinaryDirectory)
		return self._ghdl

	def GetGHDL(self) -> CLI_GHDL:
		return self._CreateGHDLCLIInstance()

	# def GetLibraryCreator(self) -> Executable:
	# 	raise NotImplementedError(f"")
	#
	# def GetLibraryMapper(self) -> Executable:
	# 	raise NotImplementedError(f"")
	#
	# def GetLibraryDeleter(self) -> Executable:
	# 	raise NotImplementedError(f"")

	def GetVHDLAnalyzer(self) -> Executable:
		return self._CreateGHDLCLIInstance().GetGHDLAsAnalyzer()

	def GetEloborator(self) -> Executable:
		return self._CreateGHDLCLIInstance().GetGHDLAsElaborator()

	def GetSimulator(self) -> Executable:
		return self._CreateGHDLCLIInstance().GetGHDLAsSimulator()


@export
class GHDL(Tool, HDLSimulator):
	_vendorKey = "OpenSource"      #: Key of the parent node (vendor) in the configuration structure.
	_key = "GHDL"                  #: Key used in the configuration structure.

	_instanceClass = GHDLInstance

	@property
	def Default(self) -> GHDLInstance:
		return cast(GHDLInstance, super().Default)

	# def GetLibraryCreator(self) -> Executable:
	# 	raise NotImplementedError(f"")
	#
	# def GetLibraryMapper(self) -> Executable:
	# 	raise NotImplementedError(f"")
	#
	# def GetLibraryDeleter(self) -> Executable:
	# 	raise NotImplementedError(f"")

	def GetVHDLAnalyzer(self) -> Executable:
		raise NotImplementedError(f"")

	def GetEloborator(self) -> Executable:
		raise NotImplementedError(f"")

	def GetSimulator(self) -> Executable:
		raise NotImplementedError(f"")
