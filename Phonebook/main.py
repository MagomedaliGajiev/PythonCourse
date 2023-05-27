# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии
# from func import *


# privet()

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм


# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

from func import *
from interface import *

path = 'phone_book.txt'
enter = 0

while enter != '4':
    enter = interface()
    if enter == '1':
        name = input("Введите ФИО:")
        phone = input("Введите номер телефона:")
        stroka = name + '-' + phone
        add_contact(path, stroka)
    elif enter == '2':
        show_all(path)
    elif enter == '3':
        stroka = input("Введите фамилию: ")
        search(path, stroka)
print("Спасибо!!")

