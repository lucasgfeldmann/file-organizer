from get_all_files_path import get_all_files_path
from sender_to import sender_to
from pathlib import Path
import sys


def move_all_files(origin, destiny):
    for file in get_all_files_path(origin):
        try:
            sender_to(file, destiny)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    origin = sys.argv[1]

    move_all_files(origin, Path.cwd())

