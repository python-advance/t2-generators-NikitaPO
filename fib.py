# Программирование (Python)
# 6 семестр, тема 2

# Лабораторная работа 6

"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""

def get_fib_nums_lst(n):
    """
    n - количество чисел в списке 

    """
    if ((type(n) == str) or (n <= 0)): 
      return None

    fib_list = [0]
    first = 0
    middle = 1
    while(n > 1): 
      fib_list.append(middle)
      third = first + middle
      first = middle
      middle = third
      n -= 1

    return fib_list


print(get_fib_nums_lst(10))

assert get_fib_nums_lst('0') is None, "неверный аргумент n"
assert get_fib_nums_lst(0) is None, "неверный аргумент n"


assert get_fib_nums_lst(1) == [0], "ряд начинается с 0"
assert get_fib_nums_lst(2) == [0, 1], "ряд длины 2"
assert get_fib_nums_lst(3) == [0, 1, 1], "ряд длины 3"

assert get_fib_nums_lst(5) == [0, 1, 1, 2, 3], "ряд длины 5"

assert get_fib_nums_lst(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "ряд длины 10"