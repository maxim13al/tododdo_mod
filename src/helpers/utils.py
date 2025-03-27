import os


def get_project_root() -> str:
    """
    Возвращает путь к корневому каталогу проекта.
    """
    return os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
