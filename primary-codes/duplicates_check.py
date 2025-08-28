import os
import sys
import csv
import hashlib

TYPES = ["xz", "zip", "tar"]


def organize_by_format(diretorio):
    errors = list()
    data_set = set()
    data_dict = dict()
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            extencion = file.split(".")[-1].lower()
            if extencion not in TYPES:
                path_file = os.path.join(root, file)
                try:
                    with open(path_file, "rb") as opened_file:
                        try:
                            content_file = opened_file.read()
                            content_hash = hashlib.sha256(content_file).hexdigest()
                            if content_hash in data_set:
                                print("IGUAL", content_hash)
                                data_dict[content_hash].append(path_file)
                            else:
                                data_set.add(content_hash)
                                data_dict[content_hash] = [path_file]
                        except Exception as e:
                            print(e)
                            errors.append(path_file)
                except Exception as e:
                    print(e)
                print(len(data_set))

    with open(diretorio + "/file_with_hash.csv", "w") as result_file:
        print("END")
        writer = csv.writer(result_file)
        writer.writerows([item for item in data_dict.values() if len(item) != 1])

    print("ERRORS: ", errors)


organize_by_format("/media/lucas/SSD/my-data")
