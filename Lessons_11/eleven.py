"""
1. Создайте класс Soda (газировка). Для инициализации
есть параметр, который определяет вкус газировки. При
инициализации этот параметр можно задавать, а можно и не
задавать. Реализовать метод строковой репрезентации,
который возвращает строку вроде «У вас газировка с
<клубничным> вкусом», если вкус задан. Если вкус не задан,
метод должен возвращать строку «У вас обычная газировка».
"""
import math
from itertools import count
from pickle import STRING

# class Soda:
#     def __init__(self, taste=None):
#         self.taste = taste
#
#
#     def __str__(self):
#         if self.taste:
#             return f"У вас газировка с {self.taste} вкусом"
#         return "У вас обычная газировка"
#
#
# one_soda = Soda("Клубничным")
# two_soda = Soda()
# print(one_soda)
# print(two_soda)


"""
2. Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
"""

# class Math:
#     def addition(self, a, b):
#         result = a + b
#         print(f"Сумма {a} и {b} равна {result}")
#
#     def subtraction(self, a, b):
#         result = a - b
#         print(f"Разность {a} и {b} равна {result}")
#
#     def multiplication(self, a, b):
#         result = a * b
#         print(f"Произведение {a} и {b} равно {result}")
#
#     def division(self, a, b):
#         if b == 0:
#             print("Ошибка: Делить на нуль нельзя.")
#         else:
#             result = a / b
#             print(f"Деление {a} на {b} равно {result}")
#
#
# math = Math()
# int_a = int(input("Введите число а: "))
# int_b = int(input("Введите число b: "))
#
# math.addition(int_a, int_b)
# math.subtraction(int_a, int_b)
# math.multiplication(int_a, int_b)
# math.division(int_a, int_b)


"""
3. Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета.
"""

# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#
#
#     def starting_car(self):
#         print("Автомобиль заведён")
#
#     def turnedoff_car(self):
#         print("Автомобиль заглушен")
#
#     def year_car(self, year):
#         self.year = year
#         print(f"Год автомобиля {year}")
#
#
#     def type_car(self, type):
#         self.type = type
#         print(f"Типо кузова автомобиля {type}")
#
#     def color_car(self, color):
#         self.color = color
#         print(f"Цвет автомобиля {color}")
#
#
# new_car = Car("blue", "sedan", 2020)
#
# new_car.starting_car()
# new_car.turnedoff_car()
# new_car.year_car(2023)
# new_car.type_car("Купе")
# new_car.color_car("Белый")


"""
4. Программа с классом Sphere для представления сферы
в трёхмерном пространстве. Реализовать методы:
● конструктор, принимающий 4 числа: радиус и координаты
центра сферы x, y, z. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом
и центром в начале координат. Если конструктор
вызывается только с радиусом, создать объект с
соответствующим радиусом и центром в начале
координат
● метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
● метод get_square(), возвращающий число – площадь
внешней поверхности сферы
● метод get_radius(), возвращающий число – радиус текущей
сферы
● метод get_center(), возвращающий кортеж с координатами
центра сферы
● метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и ничего
не возвращает
● метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
● метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того,
находится ли точка внутри сферы
"""
#
# class Sphere:
#     def __init__(self, r = 1, x = 0, y = 0, z = 0):
#         self.r = r
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def get_volume(self):
#         return (4 / 3) * math.pi * self.r ** 3
#
#     def get_square(self):
#         return 4 * math.pi * self.r ** 2
#
#     def get_radius(self):
#         return self.r
#
#     def get_center(self):
#         return self.x, self.y, self.z
#
#     def set_radius(self, r):
#         self.r = r
#
#     def set_center(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def is_point(self, x, y, z):
#
#         distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2)
#         return distance <= self.r
#
#
# int_r = int(input("Введите радиус сферы: "))
# int_x = int(input("Введите координату 'x' сферы: "))
# int_y = int(input("Введите координату 'y' сферы: "))
# int_z = int(input("Введите координату 'z' сферы: "))
#
# sphere = Sphere(int_r, int_x, int_y, int_z)
#
# print(f"Объём: {sphere.get_volume():.2f}")
# print(f"Площадь поверхности: {sphere.get_square():.5f}")
# print(f"Радиус: {sphere.get_radius()}")
# print(f"Центр: {sphere.get_center()}")
#
# sphere.set_radius(10)
# print(f"Новый радиус: {sphere.get_radius()}")
#
# sphere.set_center(1, 1, 1)
# print(f"Новый центр: {sphere.get_center()}")
#
# point_inside = sphere.is_point(0, 0, 5)
# print(f"Точка (0, 0, 5) внутри сферы? {point_inside}")
#
# point_outside = sphere.is_point(15, 0, 0)
# print(f"Точка (15, 0, 0) внутри сферы? {point_outside}")

"""
5. Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
● метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
● метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""

# class SuperStr(str):
#     def is_repeatance(self, s):
#         if not s or not self:
#             return False
#         return len(self) % len(s) == 0 and self == s * (len(self) // len(s))
#
#     def is_palindrom(self):
#         return self == self[::-1]
#
#
# s = SuperStr("abcabc")
# print(s.is_palindrom())
# print(s.is_repeatance("abc"))
