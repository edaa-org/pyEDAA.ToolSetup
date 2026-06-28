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
from typing import Dict

from pyTooling.Decorators import export

from ..             import Tool, Vendor
from ..Aldec        import ActiveHDL
from ..SiemensEDA   import ModelSim


@export
class Diamond(Tool):
	pass


@export
class Lattice(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"Diamond": Diamond,
		"Active-HDL": ActiveHDL,
		"ModelSim": ModelSim,
	}

	@property
	def Diamond(self) -> Diamond:
		return self.__getitem__("Diamond")

	@property
	def ActiveHDL(self) -> ActiveHDL:
		return self.__getitem__("Active-HDL")

	@property
	def ModelSim(self) -> ModelSim:
		return self.__getitem__("ModelSim")
