# ==================================================================================================================== #
#              _____ ____    _        _    _____           _ ____       _                                              #
#  _ __  _   _| ____|  _ \  / \      / \  |_   _|__   ___ | / ___|  ___| |_ _   _ _ __                                 #
# | '_ \| | | |  _| | | | |/ _ \    / _ \   | |/ _ \ / _ \| \___ \ / _ \ __| | | | '_ \                                #
# | |_) | |_| | |___| |_| / ___ \  / ___ \ _| | (_) | (_) | |___) |  __/ |_| |_| | |_) |                               #
# | .__/ \__, |_____|____/_/   \_\/_/   \_(_)_|\___/ \___/|_|____/ \___|\__|\__,_| .__/                                #
# |_|    |___/                                                                   |_|                                   #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2021-2026 Patrick Lehmann - Bötzingen, Germany                                                             #
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
		"""Platform GHDL runs on: ``win64``, ``lin64``."""
		return self._platform

	@property
	def Runtime(self) -> str:
		"""Runtime used to run GHDL: ``mingw64``, ``ucrt64``, ``lin64``."""
		return self._runtime

	@property
	def Backend(self) -> str:
		"""GHDL's backend: ``mcode``, ``llvm`` or ``gcc``."""
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
