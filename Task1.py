import json
import datetime

FILE_NAME = "notes.json"

def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open(FILE_NAME, "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": note_title, "body": note_body, "date": note_date}
    notes.append(note)
    save_notes(notes)
    print(f"Заметка {note_id} создана.")

def read_notes():
    notes = load_notes()
    if notes:
        filter_date = input("Введите дату в формате YYYY-MM-DD: ")
        filtered_notes = [note for note in notes if note["date"].startswith(filter_date)]
        if filtered_notes:
            print("Список заметок:")
            for note in filtered_notes:
                print(f"{note['id']}: {note['title']} ({note['date']})")
        else:
            print("Нет заметок для отображения.")
    else:
        print("Нет заметок для отображения.")

def edit_note():
    notes = load_notes()
    note_id = input("Введите id заметки, которую вы хотите отредактировать: ")
    note = next((note for note in notes if note["id"] == int(note_id)), None)
    if note:
        note_title = input("Введите новый заголовок заметки: ")
        note_body = input("Введите новый текст заметки: ")
        note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note["title"] = note_title
        note["body"] = note_body
        note["date"] = note_date
        save_notes(notes)
        print(f"Заметка {note_id} отредактирована.")
    else:
        print("Заметка с таким id не найдена.")

def delete_note():
    notes = load_notes()
    note_id = input("Введите id заметки, которую вы хотите удалить: ")
    note = next((note for note in notes if note["id"] == int(note_id)), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print(f"Заметка {note_id} удалена.")
    else:
        print("Заметка с таким id не найдена.")

def main():
    while True:
        print("Выберите действие:")
        print("1. Создать заметку.")
        print("2. Показать список заметок.")
        print("3. Отредактировать заметку.")
        print("4. Удалить заметку.")
        