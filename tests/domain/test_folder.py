from app.domain.entities.folder import Folder
from app.domain.entities.file import File


def test_nested_folder_structure(folder_factory):
    root_folder = folder_factory(
        name="root",
        subfolders=[
            {
                "name": "child1",
                "subfolders": [
                    {
                        "name": "grandchild1",
                        "subfolders": [
                            {"name": "grandgrandchild1"},
                            {"name": "grandgrandchild1"},
                            {"name": "grandgrandchild1"},
                        ],
                    }
                ],
            },
            {
                "name": "child2",
                "subfolders": [{"name": "grandchild1"}, {"name": "grandchild2"}],
            },
        ],
    )

    assert root_folder.name == "root"
    assert len(root_folder.subfolders) == 2
    assert root_folder.subfolders[1].subfolders[0].name == "grandchild1"


def test_show_tree(folder_factory):
    root_folder = folder_factory(
        name="root",
        subfolders=[
            {
                "name": "child1",
                "subfolders": [
                    {
                        "name": "grandchild1",
                        "subfolders": [
                            {"name": "grandgrandchild1"},
                        ],
                    }
                ],
            },
            {
                "name": "child2",
                "subfolders": [{"name": "grandchild1"}, {"name": "grandchild2"}],
            },
            {"name": "child3", "files": [{"name": "README.md"}]},
        ],
    )
    tree = root_folder.show_tree_structure()
    expected_results = [
        "root",
        "├── child1\n│   └── grandchild1\n│       └── grandgrandchild1",
        "├── child2\n│   ├── grandchild1\n│   └── grandchild2",
        "└── child3\n    └── README.md",
    ]
    expected_results = "\n".join(expected_results)
    assert expected_results == tree


def test_add_folder(folder_factory):
    root_folder = folder_factory(
        name="root",
        subfolders=[
            {
                "name": "child1",
            }
        ],
    )

    for folder in root_folder.subfolders:
        folder.add_subfolder(Folder(name="grandchild1"))

    assert root_folder.subfolders[0].subfolders[0].name == "grandchild1"


def test_repr_folder(folder_factory):
    root_folder = folder_factory(
        name="root",
        subfolders=[
            {
                "name": "child1",
            }
        ],
    )
    assert str(root_folder) == "Folder(name=root, subfolders=1, files=0)"


def test_folder_add_file(folder_factory):
    root_folder = folder_factory(
        name="root",
    )
    root_folder.add_file(File("__main__.py", "# Main"))

    assert root_folder.files[-1].name == "__main__.py"
    assert root_folder.files[-1].content == "# Main"
