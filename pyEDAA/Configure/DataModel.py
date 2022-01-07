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
# Copyright 2021-2021 Patrick Lehmann - Bötzingen, Germany                                                             #
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
"""Abstract data model for tool configurations."""
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

	def __getitem__(self, key: str) -> ToolInstance:
		try:
			return self._variants[key]
		except KeyError:
			return self._LoadVariant(key)

	@property
	def Vendor(self) -> "Vendor":
		return self._vendor

	def _LoadVariant(self, key: str) -> ToolInstance:
		raise NotImplementedError()


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
		try:
			return self._tools[key]
		except KeyError:
			return self._LoadTool(key)

	def _LoadTool(self, key: str) -> Tool:
		raise NotImplementedError()

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
		try:
			return self._vendors[key]
		except KeyError:
			return self._LoadVendor(key)

	def _LoadVendor(self, key: str) -> Vendor:
		raise NotImplementedError()
