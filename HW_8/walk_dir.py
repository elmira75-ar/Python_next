# Напишите функцию, которая получает на вход директорию 
# и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для 
# директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def get_size(path_1):
    size = 0
    tree = os.walk(path_1)
    # print(list(tree))
    for address, dirs, files in tree:
        # print(address, dirs, files)
        for name in files:
            # print(name)
            fp = os.path.join(address, name)
            # print(fp)
            size = size + os.path.getsize(fp)
    return size

def dir_walker(path_2):
    results = []
    tree = os.walk(path_2)
    # for i in tree:
    #     print(i)
    
    for address, dirs, files in tree:
        for n in files:
            f_p = os.path.join(address, n)
            results.append({'parent_directory': address, 
                            'is_file': 'file',
                            'name': n,
                            'size_in_bytes': os.path.getsize(f_p)})

        for m in dirs:
            f_p = os.path.join(address, m)
            results.append({'parent_directory': address, 
                            'is_file': 'dir',
                            'name': m,
                            'size_in_bytes': get_size(f_p)})

    # print(results)

    with open('result.json', 'w') as j_file:
        json.dump(results, j_file)
    
    with open('result.csv', 'w') as csv_file:
        fieldnames = ['parent_directory', 'is_file', 'name', 'size_in_bytes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    with open('result.pickle', 'wb') as pckl_file:
        pickle.dump(results, pckl_file)


if __name__ == '__main__':
    dir_walker('C:/Users/elmir/OneDrive/Desktop/GB/Python/HW_8')
    