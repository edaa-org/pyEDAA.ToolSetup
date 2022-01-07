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
# Copyright 2014-2021 Patrick Lehmann - Boetzingen, Germany                                                            #
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
__copyright__ = "2014-2021, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.2.0"
__keywords__ =  ["configuration", "eda", "installation", "selection"]


from pathlib import Path
from typing  import Dict, ClassVar

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
	def __init__(self, config: Dictionary, parent: "Vendor"):
		name = config.Key
		installationDirectory = config["InstallationDirectory"]
		binaryDirectory = config["BinaryDirectory"]
#		version = config["Version"]

		super().__init__(installationDirectory, binaryDirectory, parent=parent)
		ConfigurationMixIn.__init__(self, config)


@export
class Tool(DM_Tool, ConfigurationMixIn):
	def __init__(self, config: Dictionary, parent: "Vendor"):
		name = config.Key

		super().__init__(name, parent=parent)
		ConfigurationMixIn.__init__(self, config)

	def _LoadVariant(self, key: str) -> ToolInstance:
		instance = ToolInstance(self._config[key], parent=self)
		self._variants[key] = instance

		return instance


@export
class ActiveHDL(Tool):
	pass


@export
class RivieraPRO(Tool):
	pass


@export
class Vendor(DM_Vendor, ConfigurationMixIn):
	_toolClasses: ClassVar[Dict[str, Tool]]

	def __init__(self, config: Dictionary, parent: "Installations"):
		name = config.Key
		installationDirectory = config["InstallationDirectory"]

		super().__init__(name, installationDirectory, parent=parent)
		ConfigurationMixIn.__init__(self, config)

	def _LoadTool(self, key: str) -> Tool:
		cls = self._toolClasses[key]
		tool = cls(self._config[key], parent=self)
		self._tools[key] = tool

		return tool


@export
class Aldec(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"Active-HDL": ActiveHDL,
		"Riviera-PRO": RivieraPRO,
	}

	@property
	def ActiveHDL(self) -> Tool:
		return self.__getitem__("Active-HDL")

	@property
	def RivieraPRO(self) -> Tool:
		return self.__getitem__("Riviera-PRO")


@export
class Altera(Vendor):
	@property
	def Quartus(self) -> Tool:
		return self.__getitem__("Quartus")

	@property
	def ModelSim(self) -> Tool:
		return self.__getitem__("ModelSim")


@export
class IntelFPGA(Vendor):
	@property
	def Quartus(self) -> Tool:
		return self.__getitem__("Quartus")

	@property
	def ModelSim(self) -> Tool:
		return self.__getitem__("ModelSim")


@export
class Lattice(Vendor):
	@property
	def Diamond(self) -> Tool:
		return self.__getitem__("Diamond")

	@property
	def ActiveHDL(self) -> Tool:
		return self.__getitem__("Active-HDL")


@export
class MentorGraphics(Vendor):
	@property
	def ModelSim(self) -> Tool:
		return self.__getitem__("ModelSim")

	@property
	def QuestaSim(self) -> Tool:
		return self.__getitem__("QuestaSim")


@export
class Xilinx(Vendor):
	@property
	def ISE(self) -> Tool:
		return self.__getitem__("ISE")

	@property
	def Vivado(self) -> Tool:
		return self.__getitem__("Vivado")

	@property
	def VivadoSDK(self) -> Tool:
		return self.__getitem__("Vivado-SDK")

	@property
	def Vitis(self) -> Tool:
		return self.__getitem__("Vitis")


@export
class SystemTools(Vendor):
	@property
	def Git(self) -> Tool:
		return self.__getitem__("Git")


@export
class OpenSource(Vendor):
	@property
	def GHDL(self) -> Tool:
		return self.__getitem__("GHDL")

	@property
	def GTKWave(self) -> Tool:
		return self.__getitem__("GTKWave")


@export
class Installations(DM_Installation):
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

	@property
	def Aldec(self) -> Vendor:
		return self.__getitem__("Aldec")

	@property
	def Altera(self) -> Vendor:
		return self.__getitem__("Altera")

	@property
	def IntelFPGA(self) -> Vendor:
		return self.__getitem__("IntelFPGA")

	@property
	def Lattice(self) -> Vendor:
		return self.__getitem__("Lattice")

	@property
	def MentorGraphics(self) -> Vendor:
		return self.__getitem__("MentorGraphics")

	@property
	def Xilinx(self) -> Vendor:
		return self.__getitem__("Xilinx")

	@property
	def SystemTools(self) -> Vendor:
		return self.__getitem__("SystemTools")

	@property
	def OpenSource(self) -> Vendor:
		return self.__getitem__("OpenSource")

	@property
	def ActiveHDL(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def RivieraPRO(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def Diamond(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def Quartus(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def ModelSim(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def QuestaSim(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def Vivado(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def VivadoSDK(self) -> ToolInstance:
		raise NotImplementedError()

	@property
	def Vitis(self) -> ToolInstance:
		raise NotImplementedError()
