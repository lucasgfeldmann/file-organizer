import os
import sys


def organize_by_format(diretorio):
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            formato = file.split(".")[-1]
            destino_formato = os.path.join(diretorio, formato)
            if not os.path.exists(destino_formato):
                os.makedirs(destino_formato)
            origem = os.path.join(root, file)
            destino = os.path.join(destino_formato, file)
            print(origem, destino)
            os.rename(origem, destino)


if __name__ == "__main__":
    path = sys.argv[1]
    organize_by_format(path)
