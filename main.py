import json
import os
from datetime import datetime


class Note:
    def __init__(self, note_id, title, content, timestamp):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    def __repr__(self):
        return f"ID: {self.note_id}, Title: {self.title}, Content: {self.content}, Timestamp: {self.timestamp}"


class NotesApp:
    def __init__(self, notes_file="notes.json"):
        self.notes_file = notes_file
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as f:
                data = json.load(f)
                for note_data in data:
                    note = Note(note_data['note_id'], note_data['title'], note_data['content'], note_data['timestamp'])
                    self.notes.append(note)

    def save_notes(self):
        data = []
        for note in self.notes:
            data.append({
                'note_id': note.note_id,
                'title': note.title,
                'content': note.content,
                'timestamp': note.timestamp
            })
        with open(self.notes_file, 'w') as f:
            json.dump(data, f, indent=4)

    def create_note(self, title, content):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_id = len(self.notes) + 1
        note = Note(note_id, title, content, timestamp)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        if not self.notes:
            print("Нет доступных заметок.")
            return
        print("Список заметок:")
        for note in self.notes:
            print(note)

    def edit_note(self, note_id, title, content):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.content = content
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        self.save_notes()

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()



notes_app = NotesApp()

while True:
    print("\nВарианты:")
    print("1. Создать новую заметку")
    print("2. Просмотреть список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите ваш выбор: ")

    if choice == "1":
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержание заметки: ")
        notes_app.create_note(title, content)
        print("Заметка успешно создана.")
    elif choice == "2":
        notes_app.read_notes()
    elif choice == "3":
        notes_app.read_notes()
        note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
        title = input("Введите новый заголовок: ")
        content = input("Введите новое содержание: ")
        notes_app.edit_note(note_id, title, content)
        print("Заметка успешно отредактирована.")
    elif choice == "4":
        notes_app.read_notes()
        note_id = int(input("Введите ID заметки, которую хотите удалить: "))
        notes_app.delete_note(note_id)
        print("Заметка успешно удалена.")
    elif choice == "5":
        print("Выход...")
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
