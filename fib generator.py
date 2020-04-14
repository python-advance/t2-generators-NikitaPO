# Программирование (Python)
# 6 семестр, тема 2

# Лабораторная работа 6

"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""


def fib_generator():
    """
    n - количество чисел в списке 

    """
    first, middle = 0, 1
    while True:
        yield first
        third = first + middle
        first = middle
        middle = third


fib_lst = fib_generator()

i = 0
while i < 10:
    print(next(fib_lst))
    i += 1
