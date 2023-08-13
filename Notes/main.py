from Vault import Vault

class Interface:
    def __init__(self, dir_path: str):
        self.Vault = Vault(dir_path)

    def get_contents(self):
        contents = []
        last_input = input()
        while last_input.strip() != '/exit':
            contents.append(last_input)
            last_input = input()
            
        return contents


    def commands_list(self):
        print('Ваши заметки:\n')
        for i, name in enumerate(self.Vault.notes):
            print(f'{i}: {name}\n')
        print('0 - создать заметку; 1 - дополнить заметку; 2 - удалить заметку; 3 - выход')

    def handle_command(self, command: int):
        if command == 0:
            name = input('Введите имя заметки: ')
            contents = self.get_contents()
            self.Vault.create_note(name, contents)
        elif command == 1:
            note_id = int(input('Введите номер заметки: '))
            new_contents = self.get_contents()
            self.Vault.change_note(note_id, new_contents)
        elif command == 2:
            note_id = int(input('Введите номер заметки: '))
            self.Vault.remove_note(note_id)

if __name__ == '__main__':
    cmd = -1
    interface = Interface('test_dir')
    while cmd != 3: 
        interface.commands_list()
        cmd = int(input())
        interface.handle_command(cmd)
       