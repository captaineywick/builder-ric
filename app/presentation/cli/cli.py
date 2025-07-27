import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Build a project structure",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "project_name",
        nargs="?",
        help=(
            "Name of the project.\n"
            "- Leave empty to enter interactive mode.\n"
            "- Use '.' to use the current directory name."
        ),
    )
    parser.add_argument(
        "items",
        nargs="*",
        help=(
            "Folder/file structure to create."
            "\n\nFormat:\n"
            "- file.py: creates a file\n"
            "- /folder: creates a folder\n"
            "- /folder:file.py: creates folder with a file inside\n"
            "- /folder:file1.py,README.md: creates folder with multiple files\n"
            "\nExamples:\n"
            "/app:main.py,utils.py /docs:README.md LICENSE"
        ),
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Base path where project structure will be created (default: current directory).",
    )
    args = parser.parse_args()

    from app.application.use_cases.build_project_structure import (
        BuildProjectStructureUseCase,
    )
    from app.application.use_cases.write_project_structure import (
        WriteProjectStructureUseCase,
    )
    from app.adapters.cli_writer import CliStructureWriter
    from app.adapters.cli_parser import CliStructureParser
    from app.presentation.cli.controller import CLIController
    from app.presentation.cli.view import CLIView

    cli_writer = CliStructureWriter()
    cli_parser = CliStructureParser()
    view = CLIView()
    builder = BuildProjectStructureUseCase(cli_parser)
    writer = WriteProjectStructureUseCase(cli_writer)
    controller = CLIController(builder, writer, view)

    controller.run(
        project_name=args.project_name,
        items=args.items if args.project_name else None,
        base_path=args.path,
    )
