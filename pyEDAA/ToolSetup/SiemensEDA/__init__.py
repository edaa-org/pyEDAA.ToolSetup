from typing import Dict

from pyTooling.Decorators import export

from .. import Tool, Vendor


@export
class ModelSim(Tool):
	pass


@export
class QuestaSim(Tool):
	pass


@export
class SiemensEDA(Vendor):
	_toolClasses: Dict[str, Tool] = {
		"ModelSim": ModelSim,
		"QuestaSim": QuestaSim,
	}

	@property
	def ModelSim(self) -> ModelSim:
		return self.__getitem__("ModelSim")

	@property
	def QuestaSim(self) -> QuestaSim:
		return self.__getitem__("QuestaSim")


MentorGraphics = SiemensEDA
