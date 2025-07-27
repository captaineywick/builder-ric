from typing import List, Union

from app.domain.entities.project_structure import ProjectStructure
from app.domain.entities.folder import Folder
from app.domain.entities.file import File
from app.application.ports.parser import ParserPort


class CliStructureParser(ParserPort):
    def parse(self, args: List[str], project: ProjectStructure) -> ProjectStructure:
        """Parses a list of CLI-style arguments to build a project structure.

        Args:
            args (List[str]): A list of strings representing folders and files. Supported formats:
                - 'folder:filename1,filename2' to define files within a folder.
                - 'folder/subfolder' to define nested folders.
                - 'file.ext' to define a file at the root level.
            project (ProjectStructure): The root project structure to populate.

        Returns:
            ProjectStructure: The modified project structure with parsed folders and files.

        Examples:
            >>> arguments = ["src/utils:helpers.py,parser.py", "tests", "README.md"]
            This would result in the following structure:
            project/
            ├── src/
            │   └── utils/
            │       ├── helpers.py
            │       └── parser.py
            ├── tests/
            └── README.md
        """
        for arg in args:
            # : splits the folder and files
            if ":" in arg:
                folder_path, files_str = arg.split(":")
                folder: Folder = self._ensure_nested_folder(
                    project=project, path=folder_path
                )

                for filename in self._split_files(files_str):
                    self._add_files(container=folder, filename=filename)
            elif "." in arg:
                if "," in arg:
                    for filename in self._split_files(arg):
                        self._add_files(container=project, filename=filename)
                else:
                    project.add_file(File(name=arg.strip()))
            else:
                self._ensure_nested_folder(project, arg.strip())
        return project

    @staticmethod
    def _split_files(files_str: str) -> List[str]:
        return [f.strip() for f in files_str.split(",") if f.strip()]

    @staticmethod
    def _add_files(
        container: Union[ProjectStructure, Folder],
        filename: str,
    ):
        filename = filename.strip()
        container.add_file(File(name=filename))

        if filename.endswith(".py"):
            existing = container.files
            if not any(f.name == "__init__.py" for f in existing):
                container.add_file(File(name="__init__.py"))

    @staticmethod
    def _ensure_nested_folder(project: ProjectStructure, path: str) -> Folder:
        parts = path.strip("/").split(
            "/"
        )  # remove trailing/leading and split the folders

        current_folder = None
        folders = project.folders
        for part in parts:
            found_folder = next((f for f in folders if f.name == part), None)
            if not found_folder:
                found_folder = Folder(name=part)
                folders.append(found_folder)
            folders = found_folder.subfolders
            current_folder = found_folder
        return current_folder
