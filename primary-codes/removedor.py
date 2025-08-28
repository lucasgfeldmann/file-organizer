import os
import sys
import csv


def organize_by_format(diretorio):
    with open(diretorio, 'r') as file:
        for line in file.readlines():
            deletar = line.replace('\n','').split(",")[1:]
            for item in deletar:
                print(item)
                os.remove(item)
                



organize_by_format("/media/lucas/SSD/my-data/lucas/compactados/xz/file.csv")