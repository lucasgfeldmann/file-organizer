from get_all_files_path import get_all_files_path
from sender_to import sender_to
from pathlib import Path
import sys


def move(origin, destiny):
    for file in get_all_files_path(origin):
        try:
            sender_to(file, destiny)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    origin = sys.argv[1]

    move(origin, Path.cwd())

