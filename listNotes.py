import json
import csv

from note import Note


class ListNotes:
    # listNotes = {}

    def __init__(self):
        self.listNotes = {}

    def __add__(self, note: Note):
        self.listNotes[note.id] = note

    def del_by_id(self, id):
        if id in self.listNotes:
            self.listNotes.pop(id)
        else:
            print("Такой заметки не существует")

    def get_all_notes(self):
        for note in self.listNotes.values():
            print(note)

    def get_csv(self):
        csv_raw = ""
        for note in self.listNotes.values():
            csv_raw += note.get_csv() + "\n"
        return csv_raw

    def get_json(self):
        note: Note
        jsondict = {}
        for id, note in self.listNotes.items():
            jsondict[id] = {'title': note.get_title(),
                            'text': note.get_msg(),
                            'date': note.get_date()}
        return json.dumps(jsondict,
                          sort_keys=False,
                          ensure_ascii=False,
                          separators=(',', ':'))

    def edit_note(self, id):
        if id in self.listNotes:
            self.listNotes.pop(id)
            title = str(input('Введите новый заголовок: '))
            msg = str(input('Введите новое содержание: '))
            note = Note(title, msg, id)
            self.__add__(note)
        else:
            print("Такой заметки не существует")

    def load_from_csv_json(self) -> int:
        file_name = str(input('Введите имя файла: '))
        type_file = ''
        while type_file != 'csv' or type_file != 'json':
            type_file = str(input('Введите формат - cvs/json: '))
        count_line = 0
        try:
            if type_file == 'csv':
                with open(file_name, "r", encoding="utf-8") as fl:
                    csv_reader = csv.reader(fl, delimiter=',', quotechar='"')
                    for line in csv_reader:
                        self.records.add(Note(title=line[1], text=line[2], id=line[0], date=line[3]))
                        count_line += 1
                return count_line
            else:
                with open(file_name, "r", encoding="utf-8") as fl:
                    jsondict = json.load(fl)
                    for id, recordict in jsondict.items():
                        title = recordict.get('title')
                        text = recordict.get('text')
                        date = recordict.get('date')
                        self.records.add(Note(id=id, title=title, text=text, date=date))
                        count_line += 1
                return count_line
        except:
            print("ошибка в процессе импорта")
            return count_line
