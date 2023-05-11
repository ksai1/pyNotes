import json
import csv
from operator import attrgetter


from note import Note


class ListNotes:

    def __init__(self):
        self.listNotes = {}

    def add(self, note: Note):
        self.listNotes[note.id] = note

    def del_by_id(self, id):
        if id in self.listNotes:
            self.listNotes.pop(id)
        else:
            print("Такой заметки не существует")

    def get_all_notes(self):
        self.sort_by_date()
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
                            'text': note.get_text(),
                            'date': note.get_date()}
        return json.dumps(jsondict,
                          sort_keys=False,
                          ensure_ascii=False,
                          separators=(',', ':'))

    def edit_note(self, id):
        if id in self.listNotes:
            self.listNotes.pop(id)
            title = str(input('Введите новый заголовок: '))
            text = str(input('Введите новое содержание: '))
            note = Note(title, text, id)
            self.add(note)
        else:
            print("Такой заметки не существует")

    def save_to_csv_json(self):
        file_name = str(input('Введите имя файла: '))
        while True:
            type_file = str(input('Введите формат - csv/json: '))
            if type_file == 'csv':
                content = self.get_csv()
                break
            elif type_file == 'json':
                content = self.get_json()
                break
        with open(file_name + '.' + type_file, "w", encoding="utf-8") as fl:
            fl.write(content)
        print('Заметки сохранены.')

    def load_from_csv_json(self):
        while True:
            file_name = str(input('Введите имя файла: '))
            try:
                type_file = str(input('Введите формат - csv/json: '))
                if type_file == 'csv':
                    with open(file_name, "r", encoding="utf-8") as fl:
                        csv_reader = csv.reader(fl, delimiter=';', quotechar='"')
                        for line in csv_reader:
                            self.add(Note(title=line[2], text=line[3], id=line[0], date=line[1]))
                    print('Заметки загружены')
                elif type_file == 'json':
                    with open(file_name, "r", encoding="utf-8") as fl:
                        jsondict = json.load(fl)
                        for id, recordict in jsondict.items():
                            title = recordict.get('title')
                            text = recordict.get('text')
                            date = recordict.get('date')
                            self.add(Note(id=id, title=title, text=text, date=date))
                    print('Заметки загружены')
            except:
                print("ошибка записи файла")
            finally:
                return

    def sort_by_date(self):
        tmp = list(self.listNotes.values())
        sorted_list = sorted(tmp, key=attrgetter('date'), reverse=True)
        self.listNotes = {}
        for item in sorted_list:
            self.add(Note(item.get_title(), item.get_text(), item.get_id(), item.get_date()))
