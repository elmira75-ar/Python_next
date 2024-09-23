# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os
from pathlib import Path

def change_name(new_name, digits, pre_ext, after_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(pre_ext):
            old_name = os.path.splitext(filename)[0] 
            # print(old_name)
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ''
            # print (old_name_substring)
            new_filename = f'{old_name_substring}{new_name}{str(counter).zfill(digits)}{after_ext}'
            # print(new_filename)
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1


if __name__ == '__main__':
    # print(Path.cwd())
    change_name('new_name', 3, '.csv', '.txt', [2, 5], 'C:/Users/elmir/OneDrive/Desktop/GB/Python/HW_7')