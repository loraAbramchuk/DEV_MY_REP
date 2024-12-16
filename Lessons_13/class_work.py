"""
Задача: Реализуйте генератор, который построчно считывает текстовый файл (ленивое чтение).

Напишите функцию file_reader(file_path), которая возвращает строки файла по одной.
Не загружайте весь файл в память.
Пример использования:

python
Копировать код
for line in file_reader("example.txt"):
    print(line.strip())
Дополнительно: Реализуйте генератор, который возвращает только строки, содержащие слово "Python".

"""

def open_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if 'друзья' in line.lower():
                    yield line
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


for line in open_file('example.txt'):
    print(line.strip())