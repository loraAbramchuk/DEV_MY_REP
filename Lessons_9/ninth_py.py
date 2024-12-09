"""
1. Работа с модулем os
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
● Вывести имя вашей ОС
● Вывести путь до папки, в которой вы находитесь
● Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются
все файлы с расширением .txt, то же самое для остальных
расширений
● После рассортировки выводится сообщение типа «в папке
с текстовыми файлами перемещено 5 файлов, их
суммарный размер - 50 гигабайт»
● Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод
сообщения типа «Файл data.txt был переименован в
some_data.txt»
● Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами.
"""

"""

Недоделана! доделаю


"""
import json
import os
import re
import shutil
from collections import Counter
from idlelib.iomenu import encoding
from itertools import count

from docx.document import Document
from lxml.builder import unicode

# def sort_files_by_pc(folder_path):
#     print(f"Операционная система: {os.name}")
#     print(f"Текущая папка: {os.getcwd()}")
#
#     files = {}
#
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#
#         file_extension = os.path.splitext(file_name)[1][1:]
#
#         new_folder = os.path.join(folder_path, file_extension)
#         if not os.path.exists(new_folder):
#             os.makedirs(new_folder)
#
#         new_file_path = os.path.join(new_folder, file_name)
#         shutil.move(file_path, new_file_path)

# path = os.path.join("", "")
# os.path.exists("")
# print(os.getcwd())

"""
2. Замена имён в судебном решении
Написать программу, которая заменит в тексте ФИО
подсудимого на N. Каждое слово в ФИО начинается с
заглавной буквы, фамилия может быть двойная.
Вводимый текст:
Подсудимая Эверт-Колокольцева Елизавета Александровна
в судебном заседании вину инкриминируемого
правонарушения признала в полном объёме и суду показала,
что 14 сентября 1876 года, будучи в состоянии алкогольного
опьянения от безысходности, в связи с состоянием здоровья
позвонила со своего стационарного телефона в полицию,
сообщив о том, что у неё в квартире якобы заложена бомба.
После чего приехали сотрудники полиции, скорая
и пожарные, которым она сообщила, что бомба — это она.
Вывод:
«Подсудимая N в судебном заседании» и далее по тексту.
"""

# def replace_surname(text):
#     fio = r'[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+'
#     result = re.sub(fio, 'N', text, count=1)
#     return result
#
# text = """Подсудимая Эверт-Колокольцева Елизавета Александровна
# в судебном заседании вину инкриминируемого
# правонарушения признала в полном объёме и суду показала,
# что 14 сентября 1876 года, будучи в состоянии алкогольного
# опьянения от безысходности, в связи с состоянием здоровья
# позвонила со своего стационарного телефона в полицию,
# сообщив о том, что у неё в квартире якобы заложена бомба.
# После чего приехали сотрудники полиции, скорая
# и пожарные, которым она сообщила, что бомба — это она. """
#
# print(replace_surname(text))

"""
3. Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке.
"""

# def word_in_text(file_name, new_file_name):
#         try:
#                 with open(file_name, 'r', encoding='utf-8') as file:
#                         lines = file.readlines()
#
#                 if not lines:
#                     raise ValueError("no")
#
#                 result = []
#
#                 for line in lines:
#                     words = line.strip().split()
#                     if not words:
#                             continue
#                     word_count = Counter(words)
#                     most_frequency, count = word_count.most_common(1)[0]
#                     result.append(f"{most_frequency} {count}")
#
#                 with open(new_file_name, 'w', encoding='utf-8') as outfile:
#                         outfile.write("\n".join(result))
#
#                 print(f"Результаты записаны в файл: {new_file_name}")
#
#         except FileNotFoundError:
#                 print(f"Файл {input_file} не найден. Проверьте имя файла.")
#         except ValueError as e:
#                 print(f"Ошибка: {e}")
#         except Exception as e:
#                 print(f"Произошла непредвиденная ошибка: {e}")
#
#
#
# input_file = 'ninth.txt'
# output_file = 'output.txt'
# word_in_text(input_file, output_file)

"""
5. В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.
"""

# def print_surname(file_name, estimate_need):
#         with open(file_name, 'r', encoding='utf-8') as file:
#                 lines = file.readlines()
#                 for line in lines:
#                         student = line.strip().split()
#                         last_name, first_name, estimate = student[0], student[1], student[3]
#
#                         if int(estimate) < estimate_need:
#                                 print(f"{last_name} {first_name}:{estimate}")
#
#
# input_file = 'estimates.txt'
# estimate = 3
# print_surname(input_file, estimate)

"""
6. В файл записано некоторое содержимое (буквы,
цифры, пробелы, специальные символы и т.д.). Числом
назовём последовательность цифр, идущих подряд. Вывести
сумму всех чисел, записанных в файле.
Пример:
Входные данные: 123 ааа456 1x2y3z 4 5 6
Выходные данные: 600
"""

# def sum_number(input_file):
#         with open(input_file, 'r', encoding='utf-8') as file:
#                 lines = file.read()
#                 numbers = re.findall(r'\d+', lines)
#                 sum_numbers = sum(map(int, numbers))
#                 print(sum_numbers)
#
# input_file = 'six.txt'
# sum_number(input_file)

"""
7. Дан текстовый файл с несколькими строками.
Зашифровать шифром Цезаря, при этом шаг зависит от
номера строки: для первой строки шаг 1, для второй – 2 и т.д.
Пример:
Входные данные:
Hello
Hello
Hello
Hello
Выходные данные:
Ifmmp
Jgnnq
Khoor
Lipps
"""

# def cezar(input_file):
#         with open(input_file, 'r', encoding='utf-8') as file:
#                 lines = file.readlines()
#
#             for line in lines:
#                     encryption(line, 1)
#
#
# alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#
# def encryption(message, step):
#     result = ''
#     for i in message:
#         if i in alphabet_EU:
#             point = alphabet_EU.find(i)
#             new_point = (point + step) % len(alphabet_EU)
#             result += alphabet_EU[new_point]
#         else:
#             result += i
#     return result

"""
8. JSON и CSV.
Исходные данные:
https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2Xn
JDv9xN2LxusbE?usp=sharing
Пункты задания:
0. Есть данные в формате JSON – взять с диска с
исходными данными.
1. Реализовать функцию, которая считает данные из
исходного JSON-файла и преобразует их в формат CSV
Задания
2. Реализовать функцию, которая сохранит данные в
CSV-файл (данные должны сохраняться независимо от их
количества – если добавить в исходный JSON-файл ещё
одного сотрудника, работа программы не должна
нарушаться).
3. Реализовать функцию, которая добавит информацию о
новом сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные
для записи.
4. Такая же функция для добавления информации о
новом сотруднике в CSV-файл.
5. Реализовать функцию, которая выведет информацию
об одном сотруднике по имени. Имя для поиска вводится с
клавиатуры.
6. Реализовать функцию фильтра по языку: с клавиатуры
вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.
7. Реализовать функцию фильтра по году: ввести с
клавиатуры год рождения, вывести средний рост всех
сотрудников, у которых год рождения меньше заданного.
8. Программа должна представлять собой интерактив –
пользовательское меню с возможностью выбора
определённого действия (действия – функции из
предыдущих пунктов + выход из программы). Пока
пользователь не выберет выход из программы, должен
предлагаться выбор следующего действия.
"""
# import json
# import csv
#
# def format_in_csv(input_file, output_file):
#     with open(input_file, 'r') as json_file:
#         data = json.load(json_file)
#
#     headers = list(data[0].keys())
#
#     with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
#         write = csv.DictWriter(csv_file, fieldnames=headers)
#         write.writeheader()
#         write.writerows(data)
#
# def add_employee(input_file):
#     with open(input_file, 'r') as json_file:
#         data = json.load(json_file)
#         new_person = {}
#
#         for key in data[0].keys():
#             new_person[key] = input(f"Введите значение для ключа '{key}': ")
#
#     data.append(new_person)
#
#     with open(input_file, 'w') as json_file:
#         json.dump(data, json_file, indent=4)
#
# def search_name(input_file, name):
#     with open(input_file, 'r') as json_file:
#         data = json.load(json_file)
#         for item in data:
#             if 'name' in item and item['name'] == name:
#                 print(item)
#
# def search_height(input_file, year):
#     with open(input_file, 'r') as json_file:
#         data = json.load(json_file)
#
#         heights = [item['height'] for item in data if 'birthday' in item and 'height' in item and item['birthday'] < year]
#
#         if heights:
#             avg_height = sum(heights) / len(heights)
#             print(f"Средний рост сотрудников, родившихся до {year}: {avg_height:.2f} см")
#         else:
#             print(f"Нет сотрудников, родившихся до {year}.")
#
#
# def filter_by_language(input_file, language):
#     with open(input_file, 'r') as json_file:
#         data = json.load(json_file)
#         person_language = [item for item in data if 'languages' in item and language in item['languages']]
#         print("Сотрудники, владеющие языком программирования ", language, ":")
#         if person_language:
#             for employee in person_language:
#                 print(employee)
#         else:
#             print("Нет сотрудников с таким языком программирования")
#
#
#
# def menu(input_file, output_file):
#     while True:
#         print("\nВыберите действие:")
#         print("1. Фильтр по имени сотрудника")
#         print("2. Фильтр по языку программирования")
#         print("3. Фильтр по году рождения и расчёт среднего роста")
#         print("4. Перевод из json файла в csv")
#         print("5. Добавление нового сотрудника")
#         print("6. Выход")
#         choice = input("Введите номер действия: ")
#
#         if choice == "1":
#             name = input("Введите имя сотрудника: ").strip()
#             search_name(input_file, name)
#         elif choice == "2":
#             language = input("Введите язык программирования: ").strip().upper()
#             filter_by_language(input_file, language)
#         elif choice == "3":
#             year = input("Введите год рождения: ")
#             search_height(input_file, year)
#         elif choice == "4":
#             format_in_csv(input_file, output_file)
#         elif choice == "5":
#             add_employee(input_file)
#         elif choice == "6":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный ввод. Попробуйте снова.")
#
# json_file = 'employees.json'
# csv_file = 'csv_file.csv'
# menu(json_file, csv_file)

