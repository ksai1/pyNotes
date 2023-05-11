from listNotes import ListNotes
from pyNotes.note import Note

menu = '1 - Добавить заметку\n' \
       '2 - Удалить заметку\n' \
       '3 - Редактировать заметку\n' \
       '4 - Показать заметки\n' \
       '5 - Загрузить заметки\n' \
       '6 - Сохранить заметки\n' \
       '0 - Выход'
if __name__ == '__main__':
    ln = ListNotes()
    inpt = ''
    while inpt != '0':
        print(menu)
        inpt = str(input('Введите команду: '))
        match inpt:
            case '1':
                title = str(input('Заголовок: '))
                msg = str(input('Содержание: '))
                ln.add(Note(title, msg))
            case '2':
                id = str(input('Введите id заметки полностью: '))
                ln.del_by_id(id)
            case '3':
                id1 = str(input('Введите id заметки полностью: '))
                ln.edit_note(id1)
            case '4':
                print(ln.get_all_notes())
            case '5':
                ln.load_from_csv_json()
            case '6':
                ln.save_to_csv_json()
print('Выход')

