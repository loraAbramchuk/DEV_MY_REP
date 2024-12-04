# try:
#     print ('1' + 1)
#     print (sum)
#     print (1 / 0)
# except NameError:
#     print("sum не существует")
# except ZeroDivisionError:
#     print ("Вы не можете разделить на 0")
# except:
#     print ("Что-то пошло не так...")

"""
1. Реализовать программу для подсчёта индекса массы
тела человека. Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать обработку
исключений.
"""
import math

def calculator_imt(weight, height):
    return weight / math.pow(height, 2)

def title_imt(imt):
    if imt < 18:
        return "Дефицит массы тела"
    elif 18 <= imt < 24.9:
        return "Нормальная масса тела"
    elif 25 <= imt < 29.9:
        return "Избыточная масса тела (предожирение)"
    else:
        return "Ожирение"

try:
    weight = input("Введите свой вес в килограммах: ")
    height = input("Введите свой рост в сантиметрах: ")

    if not weight or not height:
        raise ValueError("Вес и/или рост не могут быть пустыми")

    weight_kg = float(weight)
    height_m = float(height) / 100

    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Вес и/или рост некорректно введены")

    mass = calculator_imt(weight_kg, height_m)
    category = title_imt(mass)

    print(f"Ваш индекс массы тела составляет: {mass:0.2f}, что соответствует: {category}")

except ValueError as e:
    print(f"Ошибка ввода данных: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")

"""
2. Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку
исключений.
"""
# def calc(a, b, operation):
#     if operation == "1":
#         return int(a) + int(b)
#     elif operation == "2":
#         return int(a) - int(b)
#     elif operation == "3":
#         return int(a) * int(b)
#     elif operation == "4":
#         return int(a) / int(b)
#     else:
#         raise ValueError("Некорректная операция")
#
# try:
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     c = input("Выберите операцию : 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление ")
#
#     if b == 0 and c == "4":
#         raise ZeroDivisionError("На нуль делить нельзя")
#
#     result = calc(a, b, c)
#
#     print(result)
#
# except ValueError as e:
#     print(f"Ошибка ввода данных: {e}")
# except ZeroDivisionError:
#     print("Ошибка: На нуль делить нельзя")
# except Exception as e:
#     print(f"Другая ошибка: {e}")