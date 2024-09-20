#  Создайте функцию генератор чисел Фибоначчи

def fibo(x):
    fib1, fib2 = 0, 1
    print(fib1, fib2, end=' ')
    for i in range(2, x):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


n = int(input('Введите количество чисел Фибоначчи: '))
fibo(n)
