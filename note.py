import uuid
from datetime import datetime


class Note:

    def __init__(self, title, text, id='', date=''):
        self.title = title
        self.text = text
        if date == '':
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            self.date = formatted_date
        else:
            self.date = date
        self.id = str(uuid.uuid1()) if id == '' else id

    def __str__(self):
        return '%s - %s\n%s\n%s\n' % (self.id, self.date, self.title, self.text)

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_all(self):
        return [self.id, self.date, self.title, self.text]

    def get_csv(self):
        return f"{self.id};\"{self.date}\";\"{self.title}\";\"{self.text}\""

    def __lt__(self, other):
        return self.date < other.date
