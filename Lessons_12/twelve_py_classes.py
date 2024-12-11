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

plaintext
Копировать код
Добро пожаловать в библиотеку!
1. Показать доступные книги
2. Добавить книгу
3. Удалить книгу
4. Найти книги по автору
5. Взять книгу
6. Вернуть книгу
7. Выход

"""
from itertools import count


class Library:

    def __init__(self, books: list):
        self.books = books

    def add_book(self, book):
        self.books.append(book)
        print(f"Добавлена книга {book}")

    def remove_book(self, id):
        for book_id in self.books:
            if id == book_id:
                deleted_book = book_id
                del book_id
                break
        print(f"Удалена книга {deleted_book}")

    def find_books_by_author(author):
        pass
    def list_available_books(self, id):
        pass
    def borrow_book(isbn):
        pass
    def return_book(isbn):
        pass

class Book(Library):

    count_id = 0
    instance = []


    def __init__(self, title, author, year, is_available = True):
        self.title = title
        self.author = author
        self.year = year
        self.id_book = Book.count_id
        self.is_available = is_available
        Book.count_id += 1
        self.__class__.instance.append(self)

    def borrow(self):
        self.is_available = False
        print(f"Книга взята и ее статус: {self.is_available}")

    def return_book(self):
        self.is_available = True
        print(f"Книга доступна и ее статус {self.is_available}")





new_book = Book('title', 'author', 'year')
new_book.borrow()
new_book.return_book()

new_lib = Library([])
new_lib.add_book(new_book.count_id)
new_book_2 = Book('title_2', 'author_2', 'year_2')
new_lib.add_book(new_book_2.count_id)
new_lib.remove_book(1)

for rec in Book.instance:
    print(rec)