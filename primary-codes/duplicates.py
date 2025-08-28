import os
import sys
import csv

TYPES = [ "jpg"]

def organize_by_format(diretorio):
    data_set = set()
    data_dict = dict()
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            extencion = file.split(".")[-1].lower()
            if True:#extencion in TYPES:
                path_file = os.path.join(root, file)
                with open(path_file, "rb") as opened_file:
                    content_file = opened_file.read()
                    if content_file in data_set:
                        data_dict[content_file].append(path_file)
                    else:
                        data_set.add(content_file)
                        data_dict[content_file] = [path_file]
                print(len(data_set))
                
                        


    with open(diretorio + '/file.csv', 'w') as result_file:
        print("END")
        writer = csv.writer(result_file)
        writer.writerows([item for item in data_dict.values() if len(item) != 1])




organize_by_format("/media/lucas/SSD/my-data")