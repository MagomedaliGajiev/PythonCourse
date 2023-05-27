# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии
# from func import *


# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм


# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

from func import *
from interface import *
from os.path import exists

path = 'phone_book.txt'
if not exists(path):
    with open(path, 'w'):
        pass
enter = None

while enter != '6':
    enter = interface()
    if enter == '1':
        name = input("Введите ФИО: ")
        phone = input("Введите номер телефона: ")
        res = add_contact(path, name, phone)
        if res:
            print('Контакт создан!')
        else:
            print('Человек с таким именем уже есть в справочнике.')
    elif enter == '2':
        contacts = get_all_contacts(path)
        for contact in contacts:
            print(contact)
    elif enter == '3':
        name = input("Введите фамилию: ")
        i, phone = get_contact(path, name)
        if phone:
            print(f'Пользователь {name} записан в справочнике с номером {phone}, строка {i+1}')
        else: 
            print('Пользователь не найден.')
    elif enter == '4':
        name = input('Введите имя: ')
        res = del_contact(path, name)
        if res:
            print('Контакт удален!')
        else:
            print('Такого человека нет в справочнике.')
    elif enter == '5':
        name = input('Введите имя: ')
        new_phone = input('Введите новый номер телефона: ')
        res = edit_contact(path, name, new_phone)
        if res:
            print('Контакт изменен!')
        else:
            print('Такого человека нет в справочнике.')
print("Спасибо!!")

