from get_all_files_path import get_all_files_path
from get_hash_from_file import get_hash_from_file
import sys
from datetime import datetime
from pathlib import Path

def delete_duplicates(directory):
    hash_set = set()
    paths_equal = dict()
    deleted_files = list()
    for file in get_all_files_path(directory):

        file_hash = get_hash_from_file(file)

        if file_hash in hash_set:
            paths_equal[file_hash].append(file)
            print(f"deleted: {file}")
            deleted_files.append((file_hash,file))
            file.unlink()


        if file_hash not in hash_set:
            hash_set.add(file_hash)
            paths_equal[file_hash] = [file]
    
    return {
        "hash_set":hash_set,
        "paths_equal":paths_equal,
        "deleted_files":deleted_files
    }



if __name__ == "__main__":
    directory = sys.argv[1]

    data = delete_duplicates(directory)

    with open(Path(Path.cwd(), "data.txt"), "a") as metadata:

        metadata.write(f"{str(datetime.now())}---{directory}\n")

        metadata.write("hash_set:\n")
        metadata.write(f"{data['hash_set']}\n")
        metadata.write("paths_equal:\n")
        metadata.write(f"{data['paths_equal']}\n")
        metadata.write("deleted_files:\n")
        metadata.write(f"{len(data['deleted_files'])}\n")
        metadata.write(f"{data['deleted_files']}\n")

        metadata.write("\n")


