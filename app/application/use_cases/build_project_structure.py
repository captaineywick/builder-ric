from typing import List, Optional

from app.domain.entities.project_structure import ProjectStructure
from app.application.ports.parser import ParserPort


class BuildProjectStructureUseCase:
    def __init__(self, parser: ParserPort):
        self.parser = parser
        self.project: Optional[ProjectStructure] = None

    def __call__(self, project_name: str, args: List[str]) -> ProjectStructure:
        self.project = ProjectStructure(name=project_name)
        self.parser.parse(args=args, project=self.project)
        return self.project

    def __repr__(self) -> str:
        return self.project.show_tree_structure() if self.project else ""
