from pyTooling.Decorators import export

from pyTooling.CLIAbstraction import Executable


@export
class HDLSimulator:
	def GetLibraryCreator(self) -> Executable:
		raise NotImplementedError(f"")

	def GetLibraryMapper(self) -> Executable:
		raise NotImplementedError(f"")

	def GetLibraryDeleter(self) -> Executable:
		raise NotImplementedError(f"")

	def GetVHDLAnalyzer(self) -> Executable:
		raise NotImplementedError(f"")

	def GetVerilogCompiler(self) -> Executable:
		raise NotImplementedError(f"")

	def GetEloborator(self) -> Executable:
		raise NotImplementedError(f"")

	def GetSimulator(self) -> Executable:
		raise NotImplementedError(f"")
