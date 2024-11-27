# int_a = int(input("Введите первое число: "))
# int_b = int(input("Введите второе число: "))
# int_c = int(input("Введите третье число: "))
#
# addition: int = (lambda *args: sum(args))(int_a, int_b, int_c)
#
# subtraction: int = (lambda x, y, z: x - y - z) (int_a, int_b, int_c)
#
# print(f"Cумма: {addition}")
# print(f"Разность: {subtraction}")

# def double(function):
#     def inner(argument):
#         return function(function(argument))
#     return inner
#
# def multiply_by_five(x):
#     return x * 5
#
# print(double(multiply_by_five)(3))

# def outer_function(x):
#     def inner_function (y):
#         return x + y
#     return inner_function
#
# closure = outer_function (10)
# print(closure(5))

# def select (input_func):
#     def output_func():
#         print("*****************")
#         input_func()
#         print ("*****************")
#     return output_func
#
# @select
# def hello():
#     print("Hello from the original function")
#
# hello()

"""
1. Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
"""
import time
from functools import reduce

# list_int = [1, 2, 3]
#
# str_abc =list(map(lambda a: str(a), list_int))
#
# print(str_abc)

"""
2. Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""
# list_int = [-5, -1, 5, 123, -9]
# positive_int = list(filter(lambda a: a > 0, list_int))
# print(positive_int)

"""
3. Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)
"""
# list_str = ['asdf', 'asas', 'abccba', 'kjkl', 'poop']
# def search_poli(str):
#    return str == str[::-1]
# list_poli = list(filter(search_poli, list_str))
# print(list_poli)
"""
4. Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""
# def times_function(func):
#     def output_func():
#         start = time.perf_counter()
#         func()
#         finish = time.perf_counter()  - start
#         print(f"Время выполнения функции: {finish:.6f} секунд")
#     return output_func()
#
# @times_function
# def print_hi():
#     print("Hi")

"""
5. Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
"""

# rooms = [
# {"name": "Kitchen", "length": 6, "width": 4},
# {"name": "Room 1", "length": 5.5, "width": 4.5},
# {"name": "Room 2", "length": 5, "width": 4},
# {"name": "Room 3", "length": 7, "width": 6.3},
# ]
#
# areas = list(map(lambda room: room["length"] * room["width"], rooms))
#
# total_area = reduce(lambda s, a: s + a, areas)
#
# print(total_area)