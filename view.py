def choose_mode():
    import os
    os.system('cls||clear')
    print('1: Найти контакт / 2: Добавить контакт')
    return input('Выберите опцию 1 или 2: ')


def add_contact():
    contact = input('Введите ФИО//номер телефона для добавления: ')
    return contact

def find_contact():
    contact = input('Введите ФИО или номер телефона для поиска: ')
    return contact


