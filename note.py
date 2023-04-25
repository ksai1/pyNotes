import uuid
from datetime import datetime


class Note:

    def __int__(self, title='', value='', date='', id=''):
        self.title = title
        self.value = value
        if date == '':
            now = datetime.datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            self.date = formatted_date
        else:
            self.date = date
        self.id = uuid.uuid1()
