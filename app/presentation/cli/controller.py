from typing import List

from app.application.use_cases.build_project_structure import (
    BuildProjectStructureUseCase,
)
from app.application.use_cases.write_project_structure import (
    WriteProjectStructureUseCase,
)
from app.presentation.cli.view import CLIView


class CLIController:
    def __init__(
        self,
        builder: BuildProjectStructureUseCase,
        writer: WriteProjectStructureUseCase,
        view: CLIView,
    ):
        self.builder = builder
        self.writer = writer
        self.view = view

    def run(
        self, project_name: str = None, items: List[str] = None, base_path: str = "."
    ) -> None:
        if project_name and items:
            self._handle_command_mode(project_name, items, base_path)
            return

        self._handle_interactive_mode()

    def _handle_command_mode(
        self, project_name: str, items: List[str], base_path: str
    ) -> None:
        project = self.builder(project_name, items)
        self.view.show_structure(project)

        if not self._confirm_write():
            print("Aborted.")
            return

        self.writer.write(project, base_path)
        print("Project structure written successfully.")

    def _handle_interactive_mode(self) -> None:
        name = input("Enter project name: ").strip()
        if not name:
            print("Project name cannot be empty.")
            return

        base_path = (
            input("Enter base path to create project (default '.'): ").strip() or "."
        )

        structure = []
        print("Enter folder/file structure line by line (type 'q' or 'quit' to quit):")
        while True:
            line = input("> ").strip()
            if line.lower() in {"q", "quit"}:
                break
            if line:
                structure.append(line)

        if not structure:
            print("No structure provided. Aborting.")
            return

        project = self.builder(name, structure)
        self.view.show_structure(project)

        if not self._confirm_write():
            print("Aborted.")
            return

        self.writer.write(project, base_path)
        print("Project structure written successfully.")

    @staticmethod
    def _confirm_write() -> bool:
        confirm = input("Proceed with writing to disk? (y/n): ").strip().lower()
        return confirm == "y"
