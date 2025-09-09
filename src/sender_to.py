from pathlib import Path


def sender_to(origin_file, destiny_path):
    origin_file = Path(origin_file)
    if not origin_file.is_file():
        raise Exception("A origem não é um arquivo")

    destiny_path = Path(destiny_path)
    if not destiny_path.is_dir():
        raise Exception("O destino não é um diretório")

    new_destiny_file = Path(destiny_path, origin_file.name)
    if new_destiny_file.exists():
        raise Exception(f"Arquivo '{new_destiny_file.name}' já existe no diretório de destino")

    origin_file.rename(new_destiny_file)


if __name__ == "__main__":
    sender_to("/home/lucas/Projects/file-organizer/teste/origem/arquivo.txt", "/home/lucas/Projects/file-organizer/teste/destino/")
