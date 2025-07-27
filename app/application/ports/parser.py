from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.project_structure import ProjectStructure


class ParserPort(ABC):
    @abstractmethod
    def parse(self, args: List[str], project: ProjectStructure) -> ProjectStructure:
        pass
