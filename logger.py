def open_file():
    with open('sprav.txt', 'r', encoding='utf-8') as f:
        spisok = f.read().split('\n')
        return spisok


def save_file(result):
    with open('sprav.txt', 'a', encoding='utf-8') as f:
        f.write(result+'\n')
  