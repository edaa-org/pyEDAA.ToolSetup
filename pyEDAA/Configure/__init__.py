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
# Copyright 2014-2021 Patrick Lehmann - Bötzingen, Germany                                                             #
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
__version__ =   "0.1.0"
__keywords__ =  ["configuration", "eda", "installation", "selection"]


from pathlib import Path

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
class Vendor(DM_Vendor, ConfigurationMixIn):
	def __init__(self, config: Dictionary, parent: "Installations"):
		name = config.Key
		installationDirectory = config["InstallationDirectory"]

		super().__init__(name, installationDirectory, parent=parent)
		ConfigurationMixIn.__init__(self, config)

	def _LoadTool(self, key: str) -> Tool:
		tool = Tool(self._config[key], parent=self)
		self._tools[key] = tool

		return tool


@export
class Installations(DM_Installation):
	_config: Configuration

	def __init__(self, yamlFile: Path):
		super().__init__()
		self._config = Configuration(yamlFile)

	def _LoadVendor(self, key: str) -> Vendor:
		vendor = Vendor(self._config["Installations"][key], parent=self)
		self._vendors[key] = vendor

		return vendor
