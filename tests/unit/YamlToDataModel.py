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
# Copyright 2021-2025 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""Unit tests for a YAML based configuration file."""
from pathlib            import Path
from unittest           import TestCase

from pyTooling.Platform import CurrentPlatform

from pyEDAA.ToolSetup   import Installations


class Aldec(TestCase):
	_variant = "posix" if CurrentPlatform.IsPOSIX else "windows"
	_prefix = "/opt/" if CurrentPlatform.IsPOSIX else "C:\\"
	_yamlFile = Path(f"tests/configuration.{_variant}.yml")

	def test_AccessByNameAsIndex(self) -> None:
		aldecPath = Path(self._prefix) / "Aldec"
		activePath = aldecPath / "Active-HDL"
		active103Path = activePath / "10.3"

		installation = Installations(self._yamlFile)

		aldec = installation["Aldec"]
		self.assertIs(installation, aldec.Installation)
		self.assertEqual(aldecPath, aldec.InstallationDirectory)

		activeHDL = aldec["Active-HDL"]
		self.assertIs(aldec, activeHDL.Vendor)

		activeHDLVersion = activeHDL["10.3"]
		self.assertIs(activeHDL, activeHDLVersion.Tool)
		self.assertEqual(active103Path, activeHDLVersion.InstallationDirectory)
		self.assertEqual(active103Path / "bin", activeHDLVersion.BinaryDirectory)
#		self.assertEqual(r"10.3", activeHDLVersion.Version)

	def test_AccessByProperty(self) -> None:
		aldecPath = Path(self._prefix + "Aldec")

		installation = Installations(self._yamlFile)

		aldec = installation.Aldec
		self.assertIs(installation, aldec.Installation)
		self.assertEqual(aldecPath, aldec.InstallationDirectory)
