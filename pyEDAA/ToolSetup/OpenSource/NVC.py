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
# Copyright 2026-2026 Patrick Lehmann - Bötzingen, Germany                                                             #
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
from pyEDAA.CLITool.NVC import NVC as CLI_NVC


@export
class NVCInstance(ToolInstance, HDLSimulator):
	_platform: str
	_runtime:  str
	_nvc:      CLI_NVC

	def __init__(self, config: Dictionary, parent: 'NVC') -> None:
		super().__init__(config, parent)

		self._nvc = None
		self._platform = config["Platform"]
		self._runtime = config["Runtime"]
		self._backend = config["Backend"]

	@property
	def Platform(self) -> str:
		"""Platform NVC runs on: ``win64``, ``lin64``."""
		return self._platform

	@property
	def Runtime(self) -> str:
		"""Runtime used to run NVC: ``mingw64``, ``ucrt64``, ``lin64``."""
		return self._runtime

	def _CreateNVCCLIInstance(self) -> CLI_NVC:
		if self._nvc is None:
			self._nvc = CLI_NVC(binaryDirectoryPath=self.BinaryDirectory)
		return self._nvc

	def GetNVC(self) -> CLI_NVC:
		return self._CreateNVCCLIInstance()

	def GetVHDLAnalyzer(self) -> Executable:
		return self._CreateNVCCLIInstance().GetNVCAsAnalyzer()

	def GetEloborator(self) -> Executable:
		return self._CreateNVCCLIInstance().GetNVCAsElaborator()

	def GetSimulator(self) -> Executable:
		return self._CreateNVCCLIInstance().GetNVCAsSimulator()


@export
class NVC(Tool, HDLSimulator):
	_vendorKey = "OpenSource"      #: Key of the parent node (vendor) in the configuration structure.
	_key = "NVC"                  #: Key used in the configuration structure.

	_instanceClass = NVCInstance

	@property
	def Default(self) -> NVCInstance:
		return cast(NVCInstance, super().Default)

	def GetVHDLAnalyzer(self) -> Executable:
		raise NotImplementedError(f"")

	def GetEloborator(self) -> Executable:
		raise NotImplementedError(f"")

	def GetSimulator(self) -> Executable:
		raise NotImplementedError(f"")
