from dataclasses import dataclass, field
from typing import List

from app.domain.entities.folder import Folder
from app.domain.entities.file import File


@dataclass
class ProjectStructure:
    name: str
    folders: List[Folder] = field(default_factory=list)
    files: List[File] = field(default_factory=list)

    def __repr__(self):
        if self.folders or self.files:
            return self.show_tree_structure()
        return f"ProjectStructure(name={self.name}, folders={len(self.folders)}, files={len(self.files)})"

    def add_folder(self, folder: Folder):
        self.folders.append(folder)

    def add_file(self, file: File):
        self.files.append(file)

    def show_tree_structure(self) -> str:
        lines = [self.name]  # project root name

        # Add top-level files
        for i, file in enumerate(self.files):
            connector = "├── " if i < len(self.files) - 1 or self.folders else "└── "
            lines.append(f"{connector}{file.name}")

        # Add top-level folders
        for i, folder in enumerate(self.folders):
            is_last = i == len(self.folders) - 1
            # Determine if we should use └── or ├── depending on files count
            prefix = ""
            folder_tree = folder.show_tree_structure(
                prefix=prefix, is_root=False, is_last=is_last
            )
            lines.append(folder_tree)

        return "\n".join(lines)
