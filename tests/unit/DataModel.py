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
# Copyright 2021-2021 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""Unit tests for the abstract configuration data model."""
from pathlib import Path
from unittest             import TestCase

from pyEDAA.Configure.DataModel import ToolInformation, VendorInformation, ToolInstance, Tool, Vendor, Installation


class Layer0(TestCase):
	def test_ToolInformation(self):
		installationPath = Path(r"C:\Tools\GHDL")
		binaryPath = installationPath / "bin"
		version = "2.0.0-dev"

		info = ToolInformation(installationPath, binaryPath, version)

		self.assertEqual(installationPath, info.InstallationDirectory)
		self.assertEqual(binaryPath, info.BinaryDirectory)
		self.assertEqual(version, info.Version)
		self.assertIsNone(info.Edition)

	def test_VendorInformation(self):
		installationPath = Path(r"C:\Tools\GHDL")

		info = VendorInformation(installationPath)

		self.assertEqual(installationPath, info.InstallationDirectory)


class Layer1(TestCase):
	_vendorPath = Path(r"C:\Tools")
	_installationPath = _vendorPath / "GHDL"
	_binaryPath = _installationPath / "bin"
	_version = "2.0.0-dev"

	def test_ToolInstance(self):
		instance = ToolInstance(self._installationPath, self._binaryPath, self._version)

	def test_Tool(self):
		tool = Tool("ghdl")
		instance = ToolInstance(self._installationPath, self._binaryPath, self._version, parent=tool)

	def test_Vendor(self):
		vendor = Vendor("GHDL", self._vendorPath)
		tool = Tool("ghdl", parent=vendor)
		instance = ToolInstance(self._installationPath, self._binaryPath, self._version, parent=tool)

	def test_Installation(self):
		installation = Installation()
		vendor = Vendor("GHDL", self._vendorPath, parent=installation)
		tool = Tool("ghdl", parent=vendor)
		dev = ToolInstance(self._installationPath, self._binaryPath, self._version, parent=tool)
