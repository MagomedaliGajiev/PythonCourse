def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_contact(file_name, data):
    file1 = open(file_name, 'a')
    file1.write(data + '\n')
    file1.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, data):
    have_search = False
    fille1 = open(file_name, 'r')
    for line in fille1:
        if data in fille1:
            print(line)
            have_search = True
            break
    if have_search == False:
        print('не найдено')
    fille1.close()

