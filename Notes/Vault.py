import os

class Vault:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        self.notes = list(os.listdir(dir_path))

    def get_note_path(self, i: int):
        return os.path.join(self.dir_path, self.notes[i])

    def create_note(self, name: str, content: list[str]):
        self.notes.append(name)
        i = len(self.notes) - 1

        note_path = self.get_note_path(i)
        with open(note_path, 'w') as note_f:
            note_f.writelines(content)

    def remove_note(self, i: int):
        self.notes.pop(i)
        note_path = self.get_note_path(i)
        os.remove(note_path)

    def change_note(self, i:int, new_content: list[str]):
        note_path = self.get_note_path(i)
        with open(note_path, 'a') as note_f:
            note_f.writelines(new_content)

    def get_notes_list(self):
        return self.notes