'''Напишите функцию для транспонирования матрицы'''

from random import randint

def transpose(matrix):
    return list(zip(*matrix))

def create(matrix):
    n = int(input('Введите количество строк матрицы n = '))
    m = int(input('Введите количество столбцов матрицы m = '))

    create_matrix = []
    for i in range(n):
        create_matrix.append([0] * m)
    for i in range(n):
        for j in range(m):
            create_matrix[i][j] = randint(1, 9)
    return create_matrix


def beauty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()

matrix = []
new_matrix = (create(matrix))
print('Исходная матрица')
beauty(new_matrix)
print('Транспонированная матрица')
beauty(transpose(new_matrix))
