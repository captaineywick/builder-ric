import pytest

from app.domain.entities.file import File
from app.domain.entities.folder import Folder
from app.domain.entities.project_structure import ProjectStructure


@pytest.fixture
def file_factory():
    def _make_file(name="test_file", content="test_content"):
        return File(name=name, content=content)

    return _make_file


@pytest.fixture
def folder_factory():
    def _make_folder(name="test_folder", subfolders=None, files=None):
        if subfolders is None:
            subfolders = []
        elif not isinstance(subfolders, list):
            raise TypeError("subfolders must be a list of Folder instances or dicts")

        if files is None:
            files = []
        elif not isinstance(files, list):
            raise TypeError("files must be a list of File instances or dicts")

        # Process subfolders
        processed_subfolders = []
        for subfolder in subfolders:
            if isinstance(subfolder, Folder):
                processed_subfolders.append(subfolder)
            elif isinstance(subfolder, dict):
                processed_subfolders.append(_make_folder(**subfolder))
            else:
                raise TypeError("Each subfolder must be a Folder instance or dict")

        # Process files
        processed_files = []
        for file in files:
            if isinstance(file, File):
                processed_files.append(file)
            elif isinstance(file, dict):
                processed_files.append(File(**file))
            else:
                raise TypeError("Each file must be a File instance or dict")

        return Folder(name=name, subfolders=processed_subfolders, files=processed_files)

    return _make_folder


@pytest.fixture
def project_structure_factory(file_factory, folder_factory):
    def _make_project(
        name="test_project",
        folders=None,
        files=None,
    ):
        folders = folders or []
        files = files or []

        # Convert dicts to Folder/File
        processed_folders = []
        for folder in folders:
            if isinstance(folder, Folder):
                processed_folders.append(folder)
            elif isinstance(folder, dict):
                processed_folders.append(folder_factory(**folder))
            else:
                raise TypeError("Each folder must be a Folder instance or dict")

        processed_files = []
        for file in files:
            if isinstance(file, File):
                processed_files.append(file)
            elif isinstance(file, dict):
                processed_files.append(file_factory(**file))
            else:
                raise TypeError("Each file must be a File instance or dict")

        return ProjectStructure(
            name=name, folders=processed_folders, files=processed_files
        )

    return _make_project
