import hashlib
import sys

def get_hash_from_file(path_file) -> str:
    with open(path_file, "rb") as opened_file:
        content_file = opened_file.read()
        return hashlib.sha256(content_file).hexdigest()


if __name__ == "__main__":
    path_file = sys.argv[1]

    hash = get_hash_from_file(path_file)

    print(hash)