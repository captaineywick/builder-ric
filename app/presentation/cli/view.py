from app.domain.entities.project_structure import ProjectStructure


class CLIView:
    @staticmethod
    def show_structure(project: ProjectStructure):
        project_name = project.name if project.name != "." else "Current Directory"
        print(f"Project Structure ({project_name}):")
        print(project.show_tree_structure())

    @staticmethod
    def show_message(message: str):
        print(f"[INFO] {message}")
