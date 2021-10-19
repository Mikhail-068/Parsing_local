import os
import shutil

KEY_SEARCH = 'https:'
path = r'C:\Users\Asus\Desktop\УИИ'
path_copy = r'C:\Users\Asus\Desktop\My_copy'


def search():
    for adress, folders, files in os.walk(path):
        for file in files:
            if file.endswith('link.txt'):
                yield os.path.join(adress, file)


# Поменять кодировку на UTF-8
def change_encoding(file_directory):
    with open(file_directory, mode="r") as fd:
        content = fd.read()
    with open(file_directory, mode="w", encoding="utf8") as fd:
        fd.write(content)


def copy_file(PATH):
    name = PATH.split('\\')[-1]
    count = 1
    while True:
        if os.path.isfile(os.path.join(path_copy, name)):
            if f'{count-1}' in name:
                name = name.replace(f'({count-1}).', '.')
            name = f'({count}).'.join(name.split('.'))
            count += 1
        else:
            break
    try:
        shutil.copyfile(PATH, os.path.join(path_copy, name))
        print(f'файл ({name}) скопирован')
    except:
        print('НЕ скопирован')


def read_file(file_directory):
    with open(file_directory, 'r', encoding='utf8') as f:
        for i in f:
            if KEY_SEARCH in i:
                return copy_file(file_directory)


for i in search():
    try:
        read_file(i)
    except:
        print('Не получилось')

# source = r'C:\Users\Asus\Desktop\УИИ\3 Интеграция в Production\Доп\05 WEB-SCRAPPING\link.txt'
# shutil.copyfile(source, 'new_file.txt')
