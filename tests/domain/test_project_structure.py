from app.domain.entities.folder import Folder
from app.domain.entities.project_structure import ProjectStructure
from app.domain.entities.file import File


def test_project_structure(project_structure_factory):
    project = project_structure_factory(
        name="my_project",
        folders=[
            {
                "name": "src",
                "subfolders": [{"name": "api", "subfolders": [{"name": "v1"}]}],
            },
            {"name": "tests"},
        ],
        files=[
            {"name": "README.md", "content": "# My Project"},
            {"name": ".gitignore", "content": "venv\n__pycache__"},
        ],
    )
    print(project.show_tree_structure())
    # Root
    assert project.name == "my_project"
    assert type(project) == ProjectStructure

    # Folder
    assert len(project.folders) == 2
    assert project.folders[0].name == "src"

    # Subfolder
    assert project.folders[0].subfolders[0].name == "api"
    assert project.folders[0].subfolders[0].subfolders[0].name == "v1"

    # Root files
    assert project.files[0].name == "README.md"
    assert project.files[0].content == "# My Project"


def test_project_structure_add_folder(project_structure_factory):
    project = project_structure_factory(
        name="my_project",
        folders=[
            {"name": "tests"},
        ],
    )
    project.add_folder(Folder(name="test1", subfolders=[Folder(name="childtest1")]))

    assert project.folders[-1].name == "test1"
    assert project.folders[-1].subfolders[0].name == "childtest1"


def test_project_structure_add_file(project_structure_factory):
    project = project_structure_factory(
        name="my_project",
        files=[
            {"name": "README.md", "content": "# My Project"},
            {"name": ".gitignore", "content": "venv\n__pycache__"},
        ],
    )
    project.add_file(File("__main__.py", "# Main"))

    assert project.files[-1].name == "__main__.py"
    assert project.files[-1].content == "# Main"
