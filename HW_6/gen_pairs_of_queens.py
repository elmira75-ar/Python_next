# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел
#  для случайной расстановки ферзей в задаче выше.
#  Проверяйте различный случайные варианты и
#  выведите 4 успешных расстановки.

import random
from val_pairs_of_queens import validate

def generate():
    n = 8
    x = []
    y = []
    i = 0
    while i <= n:
        new_x = random.randint (1, n)
        x.append(new_x)
        new_y = random.randint (1, n)
        y.append(new_y)
        i = i + 1
    return x, y

if __name__=='__main__':
    
    # for guess in range(4):
    while True:
        a, b  = generate()
        # validate(a, b)
        if validate(a, b) == True:
            print(generate())
            # print(validate(a, b))
            break

        # print(generate())
        # a, b  = generate()
        # print(validate(a, b))
        
