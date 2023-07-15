# ==================================================================================================================== #
#              _____ ____    _        _      ____             __ _                                                     #
#  _ __  _   _| ____|  _ \  / \      / \    / ___|___  _ __  / _(_) __ _ _   _ _ __ ___                                #
# | '_ \| | | |  _| | | | |/ _ \    / _ \  | |   / _ \| '_ \| |_| |/ _` | | | | '__/ _ \                               #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ | |__| (_) | | | |  _| | (_| | |_| | | |  __/                               #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)____\___/|_| |_|_| |_|\__, |\__,_|_|  \___|                               #
# |_|    |___/                                                     |___/                                               #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2014-2023 Patrick Lehmann - Boetzingen, Germany                                                            #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""Package to support configuring EDA tools for usage with pyEDAA.CLITool."""
__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2014-2023, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.4.0"
__keywords__ =  ["configuration", "eda", "installation", "selection"]


from pathlib import Path
from typing  import Dict, ClassVar, cast

from pyTooling.Configuration import Dictionary
from pyTooling.Decorators import export
from pyTooling.Configuration.YAML import Configuration

from .DataModel import (
	Installation as DM_Installation,
	Vendor as DM_Vendor,
	Tool as DM_Tool,
	ToolInstance as DM_ToolInstance
)


class ConfigurationMixIn:
	_config: Dictionary

	def __init__(self, config: Dictionary):
		self._config = config


@export
class ToolInstance(DM_ToolInstance, ConfigurationMixIn):
	def __init__(self, config: Dictionary, parent: "Tool"):
		name = config.Key
		installationDirectory = Path(config["InstallationDirectory"])
		binaryDirectory = Path(config["BinaryDirectory"])
		version = config["Version"]

		super().__init__(installationDirectory, binaryDirectory, version, parent=parent)
		ConfigurationMixIn.__init__(self, config)


@export
class Tool(DM_Tool, ConfigurationMixIn):
	def __init__(self, config: Dictionary, parent: "Vendor"):
		name = config.Key

		super().__init__(name, parent=parent)
		ConfigurationMixIn.__init__(self, config)

	@property
	def Default(self) -> ToolInstance:
		return self._LoadVariant("Default")

	def _LoadVariant(self, key: str) -> ToolInstance:
		if key not in self._variants:
			instance = self._instanceClass(self._config[key], parent=self)
			self._variants[key] = instance
		else:
			instance = self._variants[key]

		return instance

	def _LoadAllVariants(self) -> None:
		if self._allLoaded:
			return

		for key in self._config:
			if key not in self._variants:
				self._variants[key] = ToolInstance(self._config[key], parent=self)

		self._allLoaded = True


@export
class Vendor(DM_Vendor, ConfigurationMixIn):
	_toolClasses: ClassVar[Dict[str, Tool]]

	def __init__(self, config: Dictionary, parent: "Installations"):
		name = config.Key
		installationDirectory = Path(config["InstallationDirectory"])

		super().__init__(name, installationDirectory, parent=parent)
		ConfigurationMixIn.__init__(self, config)

	def _LoadTool(self, key: str) -> Tool:
		if key not in self._tools:
			cls = self._toolClasses[key]
			tool = cls(self._config[key], parent=self)
			self._tools[key] = tool
		else:
			tool = self._tools[key]

		return tool

	def _LoadAllTools(self) -> None:
		if self._allLoaded:
			return

		for key in self._config:
			if key not in self._tools:
				cls = self._toolClasses[key]
				self._tools[key] = cls(self._config[key], parent=self)

		self._allLoaded = True


@export
class Installations(DM_Installation):
	from .Aldec import ActiveHDL, RivieraPRO, Aldec
	from .OpenSource.GHDL import GHDL
	from .IntelFPGA import Quartus, Altera, IntelFPGA
	from .Lattice import Diamond, Lattice
	from .OpenSource import OpenSource
	from .OpenSource.GTKWave import GTKWave
	from .SiemensEDA import ModelSim, QuestaSim, MentorGraphics
	from .SystemTools import Git, SystemTools
	from .Xilinx import ISE, Vivado, VivadoSDK, Vitis, Xilinx

	_config: Configuration
	_vendorClasses: Dict[str, Vendor] = {
		"Aldec": Aldec,
		"Altera": Altera,
		"IntelFPGA": IntelFPGA,
		"Lattice": Lattice,
		"MentorGraphics": MentorGraphics,
		"Xilinx": Xilinx,
		"SystemTools": SystemTools,
		"OpenSource": OpenSource
	}

	def __init__(self, yamlFile: Path):
		super().__init__()
		self._config = Configuration(yamlFile)

	def _LoadVendor(self, key: str) -> Vendor:
		cls = self._vendorClasses[key]
		vendor = cls(self._config["Installations"][key], parent=self)
		self._vendors[key] = vendor

		return vendor

	def _LoadAllVendors(self) -> None:
		if self._allLoaded:
			return

		for key in self._config["Installations"]:
			if key not in self._vendors:
				cls = self._vendorClasses[key]
				self._vendors[key] = cls(self._config["Installations"][key], parent=self)

		self._allLoaded = True

	@property
	def Aldec(self) -> Aldec:
		from .Aldec import Aldec
		return cast(Aldec, self.__getitem__("Aldec"))

	@property
	def Altera(self) -> Altera:
		from .IntelFPGA import Altera
		return cast(Altera, self.__getitem__("Altera"))

	@property
	def IntelFPGA(self) -> IntelFPGA:
		from .IntelFPGA import IntelFPGA
		return cast(IntelFPGA, self.__getitem__("IntelFPGA"))

	@property
	def Lattice(self) -> Lattice:
		from .Lattice import Lattice
		return cast(Lattice, self.__getitem__("Lattice"))

	@property
	def MentorGraphics(self) -> MentorGraphics:
		from .SiemensEDA import MentorGraphics
		return cast(MentorGraphics, self.__getitem__("MentorGraphics"))

	@property
	def OpenSource(self) -> OpenSource:
		from .OpenSource import OpenSource
		return cast(OpenSource, self.__getitem__("OpenSource"))

	@property
	def SiemensEDA(self) -> SiemensEDA:
		from .SiemensEDA import SiemensEDA
		return cast(SiemensEDA, self.__getitem__("SiemensEDA"))

	@property
	def SystemTools(self) -> SystemTools:
		from .SystemTools import SystemTools
		return cast(SystemTools, self.__getitem__("SystemTools"))

	@property
	def Xilinx(self) -> Xilinx:
		from .Xilinx import Xilinx
		return cast(Xilinx, self.__getitem__("Xilinx"))

	@property
	def ActiveHDL(self) -> ActiveHDL:
		raise NotImplementedError()

	@property
	def RivieraPRO(self) -> RivieraPRO:
		raise NotImplementedError()

	@property
	def Diamond(self) -> Diamond:
		raise NotImplementedError()

	@property
	def Quartus(self) -> Quartus:
		raise NotImplementedError()

	@property
	def ModelSim(self) -> ModelSim:
		raise NotImplementedError()

	@property
	def QuestaSim(self) -> QuestaSim:
		raise NotImplementedError()

	@property
	def Vivado(self) -> Vivado:
		raise NotImplementedError()

	@property
	def VivadoSDK(self) -> VivadoSDK:
		raise NotImplementedError()

	@property
	def Vitis(self) -> Vitis:
		raise NotImplementedError()
