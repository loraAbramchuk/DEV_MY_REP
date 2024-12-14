from Lessons_12.twelve_py_classes import Library


def main():
    library = Library()
    # title = input("Введите название книги: ")
    # author = input("Введите автора книги: ")
    # title = 'Гарри Поттер'
    # author = 'Дж. К. Роулинг'
    # year = 1997
    # library.add_book(title, author, year)
    library.add_book("Гарри Поттер", "Дж. К. Роулинг", 1997)
    library.add_book("Властелин колец", "Дж. Р. Р. Толкин", 1954)
    library.add_book("Мастер и Маргарита", "М. Булгаков", 1967)

    library.list_available_books()

    # Поиск книг по автору
    library.find_books_by_author("Дж. К. Роулинг")

    # Взятие книги
    library.borrow_book(1, "Иван")
    library.borrow_book(2, "Мария")

    # Попытка взять занятую книгу
    library.borrow_book(1, "Иван")

    # Возвращение книги
    library.return_book(1)

    # Удаление книги
    library.remove_book(2)

    # Список доступных книг после удаления
    library.list_available_books()

    # Сохранение в файл
    library.save_library_in_file("library.json")


main()