from pathlib import Path
from typing import Generator


def get_all_files_path(directory: str | Path) -> Generator[Path, None, None]:
    """Gera o caminho de cada arquivo em um diretório, de forma recursiva."""

    path_obj = Path(directory)

    for path in path_obj.rglob("*"):
        if path.is_file():
            yield path


if __name__ == "__main__":
    paths_generator = get_all_files_path(Path.cwd())
    
    for path in paths_generator:
        print(path)
