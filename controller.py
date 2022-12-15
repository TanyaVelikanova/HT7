import view
import logger
import model

def run():
    mode = view.choose_mode()
    if mode == '1':
        result = view.find_contact()
        spisok = logger.open_file()
        spisok_contact = model.find_result(result, spisok)
        if spisok_contact == []:
            print('Данных нет')
        else:
            print(spisok_contact)
    if mode == '2':
        result = view.add_contact()
        logger.save_file(result)