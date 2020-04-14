# Программирование (Python)
# 6 семестр, тема 2

# Лабораторная работа 6

"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""

import functools


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if inner.called >= 0:
            print("Lanch foo")
            res = (func(*args, **kwargs))
            inner.called += 1
            print(inner.called)
        return res

    print('init')
    inner.called = 0
    return inner


@once
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


# fib_lst = fib_generator()

# i = 0
# while i < 10:
#     print(next(fib_lst))
#     i += 1

print(fib_generator())
print(fib_generator())
print(fib_generator())
