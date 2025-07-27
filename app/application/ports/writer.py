from abc import ABC, abstractmethod

from app.domain.entities.project_structure import ProjectStructure


class WriterPort(ABC):
    @abstractmethod
    def write(self, project: ProjectStructure, base_path: str = ".") -> None:
        pass
