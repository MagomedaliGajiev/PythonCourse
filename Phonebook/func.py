from os.path import exists

# def create(path):
#     if exists(path):  #проверяет существование файла по указанному пути
#         return False
#     else:
#         with open(path, 'w') as f:
#             return True


def get_all_contacts(file_name):
    with open(file_name, 'r') as f:
        return list(map(lambda line: line.rstrip(), f.readlines()))


def get_contact(file_name, name):  # Возвращает пару (индекс, телефон) 
    with open(file_name, 'r') as f:
        for i, line in enumerate(f.readlines()):
            cur_name, cur_phone = list(map(lambda s: s.strip(), line.split('-'))) # Сплитим строку вида ИМЯ-ТЕЛЕФОН на пару (имя, телефон) с удалением пробелов с концов
            if name.lower() == cur_name.lower():
                return i, cur_phone
        return -1, False


def add_contact(file_name, name, new_phone):
    i, phone = get_contact(file_name, name)
    if phone: # Если у данного пользователя уже есть записанный номер
        return False
    else: # Иначе
        with open(file_name,'a') as f:
            f.write(f'{name} - {new_phone}\n')
        return True


def del_contact(file_name, name):
    i, phone = get_contact(file_name, name)
    if phone:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            lines.pop(i)
        with open(file_name, 'w') as f:
            f.writelines(lines)
        return True
    else:
        return False

def edit_contact(file_name, name, new_phone):
    i, phone = get_contact(file_name, name)
    if phone:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            lines[i] = f'{name} - {new_phone}\n'
        with open(file_name, "w") as f:
            f.writelines(lines)
        return True
    else:
        return False

