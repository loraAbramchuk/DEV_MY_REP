"""
Задание: Чтение и обработка файла с данными
Описание задачи:
Создайте программу, которая:

Считывает данные из текстового файла, имя которого пользователь вводит с клавиатуры.
Обрабатывает содержимое файла, чтобы подсчитать:
Количество строк в файле.
Общее количество слов в файле.
Среднюю длину слов.
Требования:
Обработайте исключения, которые могут возникнуть:

Если файл с указанным именем не найден.
Если файл не может быть открыт (например, отсутствует доступ).
Любые другие ошибки (например, файл пустой или некорректные данные).
Выведите понятные сообщения для пользователя в случае ошибки:

Например, "Файл не найден. Проверьте имя файла и повторите попытку."
Если файл успешно обработан, выведите результаты:

Количество строк.
Количество слов.
Среднюю длину слова.
Добавьте блок finally, чтобы программа в любом случае завершалась сообщением: "Программа завершена."

Дополнительно (по желанию):
Реализуйте возможность повторного ввода имени файла, если была ошибка.
Добавьте проверку, что файл не пустой, и выводите сообщение, если он пустой: "Файл пуст."
Убедитесь, что программа корректно игнорирует пустые строки в файле.
"""