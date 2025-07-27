import os

from app.application.ports.writer import WriterPort
from app.domain.entities.project_structure import ProjectStructure
from app.domain.entities.folder import Folder


class CliStructureWriter(WriterPort):
    def write(self, project: ProjectStructure, base_path: str = "."):
        project_root = os.path.join(base_path, project.name)
        os.makedirs(project_root, exist_ok=True)

        for file in project.files:
            file_path = os.path.join(project_root, file.name)
            with open(file_path, "w") as f:
                f.write(file.content)

        for folder in project.folders:
            self._write_folder(folder, project_root)

    def _write_folder(self, folder: Folder, base_path: str) -> None:
        folder_path = os.path.join(base_path, folder.name)
        os.makedirs(folder_path, exist_ok=True)

        for file in folder.files:
            with open(os.path.join(folder_path, file.name), "w") as f:
                f.write(file.content)

        for subfolder in folder.subfolders:
            self._write_folder(subfolder, folder_path)
