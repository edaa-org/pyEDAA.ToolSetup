from pathlib import Path
from typing import Optional as Nullable, Dict

from pyTooling.Decorators import export


@export
class ToolInformation:
	_installationDirectory: Path
	_binaryDirectory: Path
	_version: Nullable[str]
	_edition: Nullable[str]

	def __init__(self, installationDirectory: Path, binaryDirectory: Path, version: str = None, edition: str = None):
		self._installationDirectory = installationDirectory
		self._binaryDirectory = binaryDirectory
		self._version = version
		self._edition = edition

	@property
	def InstallationDirectory(self) -> Path:
		return self._installationDirectory

	@property
	def BinaryDirectory(self) -> Path:
		return self._binaryDirectory

	@property
	def Version(self) -> str:
		return self._version

	@property
	def Edition(self) -> str:
		return self._edition


@export
class VendorInformation:
	_installationDirectory: Path

	def __init__(self, installationDirectory: Path):
		self._installationDirectory = installationDirectory

	@property
	def InstallationDirectory(self) -> Path:
		return self._installationDirectory


@export
class ToolInstance(ToolInformation):
	_tool: Nullable["Tool"]

	def __init__(self, installationDirectory: Path, binaryDirectory: Path, version: str = None, edition: str = None, parent: "Tool" = None):
		super().__init__(installationDirectory, binaryDirectory, version, edition)
		self._tool = parent

	@property
	def Tool(self) -> "Tool":
		return self._tool


@export
class Tool:
	_vendor: Nullable["Vendor"]
	_name: str
	_variants: Dict[str, ToolInstance]

	def __init__(self, name: str, parent: "Vendor" = None):
		self._vendor = parent
		self._name = name
		self._variants = {}

	def __contains__(self, key: str) -> bool:
		return key in self._variants

	def __getitem__(self, key: str):
		return self._variants[key]

	@property
	def Vendor(self) -> "Vendor":
		return self._vendor


@export
class Vendor(VendorInformation):
	_installation: Nullable["Installation"]
	_name: str
	_tools: Dict[str, Tool]

	def __init__(self, name: str, installationDirectory: Path, parent: "Installation" = None):
		super().__init__(installationDirectory)
		self._installation = parent
		self._name = name
		self._tools = {}

	def __contains__(self, key: str) -> bool:
		return key in self._tools

	def __getitem__(self, key: str) -> Tool:
		return self._tools[key]

	@property
	def Installation(self) -> "Installation":
		return self._installation


@export
class Installation:
	_vendors: Dict[str, Vendor]

	def __init__(self):
		self._vendors = {}

	def __contains__(self, key: str) -> bool:
		return key in self._vendor

	def __getitem__(self, key: str) -> Vendor:
		return self._vendors[key]
