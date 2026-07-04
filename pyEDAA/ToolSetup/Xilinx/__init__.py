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

from .. import Tool, Vendor


@export
class ISE(Tool):
	pass


@export
class Vivado(Tool):
	pass


@export
class VivadoSDK(Tool):
	pass


@export
class Vitis(Tool):
	pass


@export
class Xilinx(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"ISE": ISE,
		"Vivado": Vivado,
		"VivadoSDK": VivadoSDK,
		"Vitis": Vitis,
	}

	@property
	def ISE(self) -> ISE:
		return self.__getitem__("ISE")

	@property
	def Vivado(self) -> Vivado:
		return self.__getitem__("Vivado")

	@property
	def VivadoSDK(self) -> VivadoSDK:
		return self.__getitem__("Vivado-SDK")

	@property
	def Vitis(self) -> Vitis:
		return self.__getitem__("Vitis")
