"""
1. Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию.
"""

# def fibonacci(int_x):
#     a, b = 0, 1
#     for i in range(int_x):
#         yield a
#         a, b = b, a + b
#
# ints = int(input("Введите число, до которого выводить: "))
# for j in fibonacci(ints):
#     print(j, end=" ")


"""
2. Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""

# def cyclic_sequence(ints):
#
#     while True:
#         for i in ints:
#             yield i
#
# ints = input("Введите элементы последовательности через пробел: ").split()
# count = int(input("Введите количество чисел для вывода: "))
#
# generator = cyclic_sequence(ints)
#
# for j in range(count):
#     print(next(generator), end=" ")
# print()

"""
3. Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza.
"""

# class Pizza:
#     def __init__(self, size=None, cheese='', pepperoni="", mushrooms="", onions="", bacon=""):
#         self.size = size
#         self.cheese = cheese
#         self.pepperoni = pepperoni
#         self.mushrooms = mushrooms
#         self.onions = onions
#         self.bacon = bacon
#
#     def __str__(self):
#
#         return (f"Пицца размером {self.size} с начинками:\n"
#                 f"  - Сыр: {self.cheese} г\n"
#                 f"  - Пепперони: {self.pepperoni} г\n"
#                 f"  - Грибы: {self.mushrooms} г\n"
#                 f"  - Лук: {self.onions} г\n"
#                 f"  - Бекон: {self.bacon} г")
#
# class PizzaBuilder:
#     def __init__(self):
#         self._pizza = Pizza()
#
#     def set_size(self, size):
#         self._pizza.size = size
#         return self
#
#     def add_cheese(self, cheese):
#         self._pizza.cheese = cheese
#         return self
#
#     def add_pepperoni(self, pepperoni):
#         self._pizza.pepperoni = pepperoni
#         return self
#
#     def add_mushrooms(self, mushrooms):
#         self._pizza.mushrooms = mushrooms
#         return self
#
#     def add_onions(self, onions):
#         self._pizza.onions = onions
#         return self
#
#     def add_bacon(self, bacon):
#         self._pizza.bacon = bacon
#         return self
#
#     def build(self):
#         return self._pizza
#
#
# class PizzaDirector:
#
#     def __init__(self, builder):
#         self.builder = builder
#
#     def make_pizza(self):
#         return (self.builder
#                 .set_size("большая")
#                 .add_cheese(150)
#                 .add_pepperoni(100)
#                 .add_mushrooms(80)
#                 .add_onions(50)
#                 .add_bacon(120)
#                 .build())
#
# builder = PizzaBuilder()
# custom_pizza = (builder
#                 .set_size("средняя")
#                 .add_cheese(200)
#                 .add_pepperoni(120)
#                 .add_bacon(100)
#                 .build())
#
# print("Кастомная пицца:")
# print(custom_pizza)
#
# director = PizzaDirector(PizzaBuilder())
# standard_pizza = director.make_pizza()
#
# print("\nСтандартная пицца:")
# print(standard_pizza)

"""
4. Паттерн «Фабричный метод»
● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
● Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat).
"""

# class Animal:
#
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "Гав-гав!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Мяу-мяу"
#
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type):
#         if animal_type == "dog":
#             return Dog()
#         elif animal_type == "cat":
#             return Cat()
#
#
# animals = AnimalFactory()
# animal_1 = animals.create_animal("cat")
# animal_2 = animals.create_animal("dog")
# print(animal_1.speak())
# print(animal_2.speak())

"""
5. Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии.
"""

# class Calculator:
#     def __init__(self):
#         self.strategy = None
#
#     def set_strategy(self, strategy):
#         self.strategy = strategy
#
#     def calculate(self, a, b):
#         return self.strategy.execute(a, b)
#
# class Addition:
#     @staticmethod
#     def execute(a, b):
#         return a + b
#
# class Subtraction:
#     @staticmethod
#     def execute(a, b):
#         return a - b
#
# class Multiplication:
#     @staticmethod
#     def execute(a, b):
#         return a - b
#
# class Division:
#     @staticmethod
#     def execute(a, b):
#         if b == 0:
#             raise ValueError("На нуль делить нельзя")
#         return a / b
#
# calc = Calculator()
# calc.set_strategy(Addition())
# print(calc.calculate(2,3))