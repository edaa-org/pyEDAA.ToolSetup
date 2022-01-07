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
"""Unit tests for a YAML based configuration file."""
from pathlib          import Path
from unittest         import TestCase

from pyEDAA.Configure import Installations


class FromYaml(TestCase):
	_yamlFile = Path(r"tests/configuration.yml")

	def test_AccessByNameAsIndex(self):
		installation = Installations(self._yamlFile)

		aldec = installation["Aldec"]
		self.assertIs(installation, aldec.Installation)
		self.assertEqual(r"C:\Aldec", aldec.InstallationDirectory)

		activeHDL = aldec["Active-HDL"]
		self.assertIs(aldec, activeHDL.Vendor)

		activeHDLVersion = activeHDL["10.3"]
		self.assertIs(activeHDL, activeHDLVersion.Tool)
		# self.assertEqual(r"C:\Aldec\Active-HDL\10.3", activeHDLVersion.InstallationDirectory)
		# self.assertEqual(r"C:\Aldec\Active-HDL\10.3\bin", activeHDLVersion.BinaryDirectory)
		# self.assertEqual(r"10.3", activeHDLVersion.Version)
