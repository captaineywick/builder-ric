from dataclasses import dataclass, field
from typing import List

from app.domain.entities.file import File


@dataclass
class Folder:
    name: str
    subfolders: List["Folder"] = field(default_factory=list)
    files: List[File] = field(default_factory=list)

    def add_subfolder(self, folder: "Folder") -> None:
        self.subfolders.append(folder)

    def add_file(self, file: File) -> None:
        self.files.append(file)

    def show_tree_structure(
        self, prefix: str = "", is_root: bool = True, is_last: bool = True
    ) -> str:
        lines: List[str] = []

        if is_root:
            lines.append(self.name)
        else:
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{self.name}")

        # Update prefix after drawing the connector
        new_prefix = prefix if is_root else (prefix + ("    " if is_last else "│   "))

        # Add subfolders
        for i, subfolder in enumerate(self.subfolders):
            is_last_child = (i == len(self.subfolders) - 1) and not self.files
            lines.append(
                subfolder.show_tree_structure(
                    new_prefix, is_root=False, is_last=is_last_child
                )
            )

        # There is no child for a file so no need to recursive
        for i, file in enumerate(self.files):
            is_last_file = i == len(self.files) - 1
            connector = "└── " if is_last_file else "├── "
            lines.append(f"{new_prefix}{connector}{file.name}")

        return "\n".join(lines)

    def __repr__(self):
        return f"Folder(name={self.name}, subfolders={len(self.subfolders)}, files={len(self.files)})"
