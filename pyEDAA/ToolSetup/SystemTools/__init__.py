from typing import Dict

from pyTooling.Decorators import export

from .. import Tool, Vendor


@export
class Git(Tool):
	pass


@export
class SystemTools(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"Git": Git,
	}

	@property
	def Git(self) -> Git:
		return self.__getitem__("Git")
