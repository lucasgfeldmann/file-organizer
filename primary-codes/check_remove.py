import os
import hashlib


def check_sum_content_file(path):
    with open(path, "rb") as file:
        content_file = file.read()
        return hashlib.sha256(content_file).hexdigest()


def is_content_equal(arr_paths):
    data_set = set()
    for path in arr_paths:
        try:
            content_file = check_sum_content_file(path)
            if content_file not in data_set:
                data_set.add(content_file)
        except Exception as e:
            print(e)
    if len(data_set) != 1:
        return False

    return True


def organize_by_format(diretorio):
    not_equal = list()
    with open(diretorio, 'r') as file:
        for line in file.readlines():
            arr_paths = line.replace('\n','').split(",")
            if is_content_equal(arr_paths):
                for item in arr_paths[1:]:
                    print(item)
                    os.remove(item)
            else:
                print("ERROR: ", arr_paths)
                not_equal.append(arr_paths)
    
    print("ERROR: ", not_equal)


organize_by_format("/media/lucas/SSD/my-data/file_with_hash.csv")