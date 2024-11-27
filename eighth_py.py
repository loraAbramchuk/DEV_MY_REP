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
    weight = input("Введите свой вес в граммах: ")
    height = input("Введите свой рост в сантиметрах: ")

    weight_kg = float(weight) / 1000
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



