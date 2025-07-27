from app.domain.entities.project_structure import ProjectStructure
from app.application.ports.writer import WriterPort


class WriteProjectStructureUseCase:
    def __init__(self, writer: WriterPort):
        self.writer = writer

    def write(self, project: ProjectStructure, base_path: str = ".") -> None:
        self.writer.write(project, base_path)
