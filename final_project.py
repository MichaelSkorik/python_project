import json
import os
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes_data = json.load(file)
            return [Note(**note) for note in notes_data]
    return []

def save_notes(notes):
    notes_data = [{"note_id": note.note_id, "title": note.title, "body": note.body, "timestamp": note.timestamp} for note in notes]
    with open("notes.json", "w") as file:
        json.dump(notes_data, file, indent=2)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_id = len(notes) + 1
    notes.append(Note(note_id, title, body, timestamp))
    save_notes(notes)
    print("Заметка успешно сохранена")

def read_notes(notes_to_display=None):
    if not notes_to_display:
        notes_to_display = notes

    for note in notes_to_display:
        print(f"ID: {note.note_id}",f"Заголовок: {note.title}",f"Дата/время: {note.timestamp}", sep='\n')
        print(f"Тело заметки: {note.body}\n")


def view_note():
    note_id = int(input("Введите ID заметки для просмотра: "))
    for note in notes:
        if note.note_id == note_id:
            print(f"ID: {note.note_id}",f"Заголовок: {note.title}",f"Дата/время: {note.timestamp}", sep='\n')
            print(f"Тело заметки: {note.body}")
            return
    print("Заметка с указанным ID не найдена")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note.note_id == note_id:
            note.title = input("Введите новый заголовок заметки: ")
            note.body = input("Введите новое тело заметки: ")
            note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    global notes

    notes = [note for note in notes if note.note_id != note_id]

    for i, note in enumerate(notes, start=1):
        note.note_id = i

    save_notes(notes)
    print("Заметка успешно удалена")

def filter_by_date():
    date_str = input("Введите дату в формате YYYY-MM-DD для выборки заметок: ")
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        filtered_notes = [note for note in notes if datetime.strptime(note.timestamp, "%Y-%m-%d %H:%M:%S").date() == target_date]
        if filtered_notes:
            print(f"Заметки на {date_str}:")
            read_notes(filtered_notes)
        else:
            print(f"На {date_str} заметок нет.")
    except ValueError:
        print("Некорректный формат даты. Введите дату в формате YYYY-MM-DD.")

notes = load_notes()

while True:
    command = input("Введите команду (add/read/view/edit/delete/filter/exit): ").lower()

    if command == "add":
        add_note()
    elif command == "exit":
        break
    elif command == "read":
        read_notes()
    elif command == "view":
        view_note()
    elif command == "edit":
        edit_note()
    elif command == "delete":
        delete_note()
    elif command == "filter":
        filter_by_date()
    else:
        print("Некорректная команда. Пожалуйста, введите корректную команду.")
