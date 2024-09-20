#  Напишите функцию, которая принимает 
# на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов:
#  путь, имя файла, расширение файла.

import os

def way_to_file(way):
    path, ext = os.path.splitext(way)
    dir, name = os.path.split(path)
    return (dir, name, ext)

print(way_to_file('C:\\Users\elmir\GB\Big_Data\hw_1.txt'))