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
"""``configure`` commands for the CLI application for standalone usage of pyEDAA.Configure."""
from argparse  import Namespace

from pyTooling.Decorators                      import export
from pyTooling.MetaClasses                     import ExtendedType
from pyTooling.Attributes.ArgParse             import CommandHandler


@export
class ConfigureHandlers(metaclass=ExtendedType, mixin=True):
	@CommandHandler("configure", help="Configure existing EDA tools on that system.", description="Configure EDA tools.")
	def HandleConfigure(self, args: Namespace) -> None:
		"""Handle program calls with command ``configure``."""
		if not args.quiet:
			self._PrintHeadline()

		raise NotImplementedError("This is a placeholder command.")
