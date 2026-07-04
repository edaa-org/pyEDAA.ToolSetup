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
"""CLI application for standalone usage of pyEDAA.Configure and for testing."""
from argparse import RawDescriptionHelpFormatter
from textwrap import dedent, wrap
from typing   import Optional as Nullable, ClassVar

from pyTooling.Decorators import export
from pyTooling.Exceptions import ExceptionBase
from pyTooling.TerminalUI import TerminalApplication, Severity, Mode
from pyTooling.Attributes.ArgParse          import Namespace, ArgParseHelperMixin, DefaultHandler, CommandHandler
from pyTooling.Attributes.ArgParse.Argument import StringArgument
from pyTooling.Attributes.ArgParse.Flag     import FlagArgument

from pyEDAA.ToolSetup               import ConfigurationException
from pyEDAA.ToolSetup.CLI.Configure import ConfigureHandlers


@export
class Application(TerminalApplication, ArgParseHelperMixin, ConfigureHandlers):
	"""Program class to implement the command line interface (CLI) using commands and options."""

	HEADLINE:          ClassVar[str] = "pyEDAA.ToolSetup Service Program"

	def __init__(self, sphinx: bool = False) -> None:
		super().__init__(Mode.TextToStdOut_ErrorsToStdErr)

		self.HeadLine = self.HEADLINE

		# Call the constructor of the ArgParseHelperMixin
		textWidth = min(self.Width, 160)

		class HelpFormatter(RawDescriptionHelpFormatter):
			def __init__(self, *args, **kwargs):
				kwargs['max_help_position'] = 30
				kwargs['width'] =             textWidth
				super().__init__(*args, **kwargs)

		ArgParseHelperMixin.__init__(
			self,
			prog="pyedaa-toolsetup",
		  description=dedent('''\
				'pyEDAA.ToolSetup Test Application' to test pyEDAA.ToolSetup capabilities.
				'''),
			epilog="\n".join(wrap(dedent("""\
		  	pyEDAA.ToolSetup is a layer in EDA² to find, configure and select installed EDA tools.
		  	"""), textWidth, replace_whitespace=False)),
		  formatter_class=HelpFormatter,
		  add_help=False
		)

		# If executed in Sphinx to auto-document CLI arguments, exit now
		# --------------------------------------------------------------------------
		if sphinx:
			return

		# Change error and warning reporting
		# --------------------------------------------------------------------------
		self._LOG_MESSAGE_FORMAT__[Severity.Fatal]   = "{DARK_RED}[FATAL] {message}{NOCOLOR}"
		self._LOG_MESSAGE_FORMAT__[Severity.Error]   = "{RED}[ERROR] {message}{NOCOLOR}"
		self._LOG_MESSAGE_FORMAT__[Severity.Warning] = "{YELLOW}[WARNING] {message}{NOCOLOR}"
		self._LOG_MESSAGE_FORMAT__[Severity.Normal]  = "{GRAY}{message}{NOCOLOR}"

	def Run(self) -> None:
		ArgParseHelperMixin.Run(self)

	@DefaultHandler()
	@FlagArgument("-q", "--quiet", dest="quiet", help="Reduce messages to a minimum.")
	@FlagArgument("-v", "--verbose", dest="verbose", help="Print out detailed messages.")
	@FlagArgument("-d", "--debug",   dest="debug",   help="Enable debug mode.")
	def HandleDefault(self, _: Namespace) -> None:
		"""Handle program calls without any command."""
		self._PrintHeadline()
		self._PrintHelp()

	# Common commands
	# ============================================================================
	@CommandHandler("help", help="Display help page(s) for the given command name.", description="Display help page(s) for the given command name.")
	@StringArgument(dest="Command", metaName="Command", optional=True, help="Print help page(s) for a command.")
	def HandleHelp(self, args: Namespace) -> None:
		"""Handle program calls with command ``help``."""
		self._PrintHeadline()
		self._PrintHelp(args.Command)

	@CommandHandler("version", help="Display version information.", description="Display version information.")
	def HandleVersion(self, _: Namespace) -> None:
		"""Handle program calls with command ``version``."""
		import pyEDAA.ToolSetup as DunderModule

		self._PrintHeadline()
		self._PrintVersion(DunderModule, "pyEDAA.ToolSetup")


# main program
def main(): # mccabe:disable=MC0001
	"""
	Entrypoint to start program execution.

	This function should be called either from:
	 * :pycode:`if __name__ == "__main__":` or
	 * ``console_scripts`` entry point configured via ``setuptools`` in ``setup.py``.

	This function creates an instance of :class:`Application` in a ``try ... except`` environment. Any exception caught is
	formatted and printed before the program returns with a non-zero exit code.

  .. todo::

	   1. It extracts common flags from the script's arguments list, before :py:class:`~argparse.ArgumentParser` is fully loaded.
	   2. It creates an instance of VHDLParser and hands over to a class based execution.
	      All is wrapped in a big ``try..except`` block to catch every unhandled exception.
	   3. Shutdown the script and return its exit code.
	"""
	from sys import argv

	program = Application()
	program.Configure(
		verbose=("-v" in argv or "--verbose" in argv),
		debug=(  "-d" in argv or "--debug"   in argv),
		silent=( "-q" in argv or "--quiet"   in argv)
	)

	try:
		program.Run()
	except ConfigurationException as ex:
		program.WriteLineToStdErr(f"{{RED}}[ERROR] {ex}{{NOCOLOR}}".format(**Application.Foreground))
		if ex.__notes__ is not None:
			for note in ex.__notes__:
				program.WriteLineToStdErr(f"{{DARK_YELLOW}} [NOTE] {note}{{NOCOLOR}}".format(**Application.Foreground))

	# except OutputFilterException as ex:
	# 	program.WriteLineToStdErr(f"{{RED}}[ERROR] {ex}{{NOCOLOR}}".format(**Application.Foreground))
	# 	if ex.__cause__ is not None:
	# 		program.WriteLineToStdErr(f"{{DARK_YELLOW}}Because of: {ex.__cause__}{{NOCOLOR}}".format(**Application.Foreground))
	except ExceptionBase as ex:
		program.printExceptionBase(ex)
	except NotImplementedError as ex:
		program.PrintNotImplementedError(ex)
	except Exception as ex:
		program.PrintException(ex)

		app.exit()

	# except (CommonException, ConfigurationException) as ex:
	# 	print("{RED}ERROR:{NOCOLOR} {message}".format(message=ex.message, **Init.Foreground))
	# 	cause = ex.__cause__
	# 	if isinstance(cause, FileNotFoundError):
	# 		print("{YELLOW}  FileNotFound:{NOCOLOR} '{cause}'".format(cause=str(cause), **Init.Foreground))
	# 	elif isinstance(cause, NotADirectoryError):
	# 		print("{YELLOW}  NotADirectory:{NOCOLOR} '{cause}'".format(cause=str(cause), **Init.Foreground))
	# 	elif isinstance(cause, ParserException):
	# 		print("{YELLOW}  ParserException:{NOCOLOR} {cause}".format(cause=str(cause), **Init.Foreground))
	# 		cause = cause.__cause__
	# 		if cause is not None:
	# 			print("{YELLOW}    {name}:{NOCOLOR} {cause}".format(name=cause.__class__.__name__, cause= str(cause), **Init.Foreground))
	#
	# 	if not (verbose or debug):
	# 		print()
	# 		print("{CYAN}  Use '-v' for verbose or '-d' for debug to print out extended messages.{NOCOLOR}".format(**Init.Foreground))
	# 	LineTerminal.exit(1)

# entry point
if __name__ == "__main__":
	main()
