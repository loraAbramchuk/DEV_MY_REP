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