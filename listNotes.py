from note import Note


class ListNotes:
    listNotes = {}

    def __int__(self):
        self.listNotes = {}

    def __add__(self, note: Note):
        self.listNotes[note.id] = note

    def del_by_id(self, id):
        if id in self.listNotes:
            self.listNotes.pop(id)

