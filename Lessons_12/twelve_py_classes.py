"""
Создайте приложение для управления виртуальной библиотекой. В библиотеке есть книги, которые могут быть взяты на чтение или возвращены. Книги имеют следующие характеристики:

Название
Автор
Год издания
Уникальный идентификатор (например,  id)
Статус (доступна/взята)
Требования:

Класс Book:

Свойства: title, author, year, isbn, is_available.
Методы:
borrow(): меняет статус книги на "взята".
return_book(): меняет статус книги на "доступна".

Класс Library:

Свойства:
books — список объектов Book.
Методы:
add_book(book): добавляет книгу в библиотеку.
remove_book(isbn): удаляет книгу из библиотеки по ISBN.
find_books_by_author(author): возвращает список книг автора.
list_available_books(): выводит список всех доступных книг.
borrow_book(isbn): выдает книгу по ISBN, если она доступна.
return_book(isbn): возвращает книгу в библиотеку.
Напишите программу, которая:

Создает библиотеку.
Добавляет в нее несколько книг.
Позволяет пользователю взаимодействовать с библиотекой через меню (например, брать книги, возвращать, искать по автору и т.д.).
Дополнительно (для усложнения):

Добавьте возможность сохранять состояние библиотеки в файл и загружать его.
Реализуйте управление датами (например, чтобы книги можно было брать на ограниченный срок).
Добавьте учёт пользователей и сделайте возможным отслеживание, кто взял какую книгу.
Пример взаимодействия с библиотекой:

Добро пожаловать в библиотеку!
1. Показать доступные книги
2. Добавить книгу
3. Удалить книгу
4. Найти книги по автору
5. Взять книгу
6. Вернуть книгу
7. Выход

"""
import json
from itertools import count


class Library:

    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author, year):
        book = Book(title, author, year, self.next_id)
        self.books.append(book)
        self.next_id += 1
        print(f"Добавлена книга: {book} ")

    def remove_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                self.books.remove(book)
                print(f"Удалена книга: {book}")
                return

    def find_books_by_author(self, author):
        found = [book for book in self.books if book.author.lower() == author.lower()]
        if found:
            for book in found:
                print(book)
        else:
            print(f"Книги автора {author} не найдены.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("Нет доступных книг.")

    def borrow_book(self, id_book, user):
        for book in self.books:
            if book.id_book == id_book:
                if book.is_available:
                    book.borrow(user)
                else:
                    print(f"Книга '{book.title}' уже занята.")
                return
        print(f"Книга с ID {id_book} не найдена.")

    def return_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                if not book.is_available:
                    book.return_book()
                else:
                    print(f"Книга '{book.title}' уже доступна.")
                return
        print(f"Книга с ID {id_book} не найдена.")

    def save_library_in_file(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump([{
                'id_book': book.id_book,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'is_available': book.is_available,
                'who_took': book.who_took
            } for book in self.books], file, ensure_ascii=False, indent=4)
        print(f"Библиотека сохранена в файл '{file_name}'.")

    def load_library_from_file(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)

                if not data:
                    print("Файл пуст. Библиотека не загружена.")
                    return

                self.books = [
                    Book(
                        item['title'],
                        item['author'],
                        item['year'],
                        item['id_book'],
                        item['is_available'],
                        item['who_took']
                    ) for item in data
                ]
                print(f"Библиотека загружена из файла '{file_name}'.")
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке: {e}")


class Book:

    # count_id = 0
    # instance = []

    def __init__(self, title, author, year, id_book, is_available = True):
        self.title = title
        self.author = author
        self.year = year
        # self.id_book = Book.count_id
        self.id_book = id_book
        self.is_available = is_available
        # Book.count_id += 1
        # self.__class__.instance.append(self)
        self.who_took = None

    def borrow(self, user):
        self.is_available = False
        self.who_took = user
        print(f"Книга {self.title} взята {self.who_took} и ее статус: {self.is_available}")

    def return_book(self):
        self.is_available = True
        self.who_took = None
        print(f"Книга {self.title} доступна и ее статус {self.is_available}")

    def __str__(self):
        status = "Доступна" if self.is_available else f"Занята ({self.who_took})"
        return f"'{self.title}' - {self.author}, {self.year} (ID: {self.id_book}, {status})"










# new_book = Book('title', 'author', 'year')
# new_book.borrow()
# new_book.return_book()

# new_lib = Library([])
# new_lib.add_book(new_book.title, new_book.author, new_book.count_id)
# new_book_2 = Book('title_2', 'author_2', 'year_2')
# new_lib.add_book(new_book_2.title, new_book_2.author, new_book_2.count_id)
# new_lib.remove_book(1)

# for rec in Book.instance:
#     print(rec)
#
# new_lib.list_available_books()