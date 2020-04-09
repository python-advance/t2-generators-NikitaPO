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
    first, middle = 0, 1
    for i in range(n):
      yield first
      third = first + middle
      first = middle
      middle = third
      
  
print(*get_fib_nums_lst(10))

