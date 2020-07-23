import json
from re import findall, compile
import os
import pathlib

ru_pattern = compile("[а-яА-ЯёЁ]+")
en_pattern = compile("'?\w[\w']*(?:-\w+)*'?")
total_count_en, total_count_ru  = 0, 0

def open_and_count(filename):
    pattern = ru_pattern if filename.strip('.')[0] == 'RU' else en_pattern
    count = 0
    with open(filename, encoding='utf-8') as json_file:
        data = json.load(json_file)
        for key in data['Items']:
            count += len(findall(pattern, data['Items'][key]['t']))
    return count

def digger(path):
    global total_count_ru
    global total_count_en
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path,i)):
            print('\n',f"Файл: {i}.")
            digger(os.path.join(path,i))
        else:
            if i.split('.')[0] in ('RU', 'EN'):
                mod_path = os.path.join(path,i)
                if i.split('.')[0] == 'RU':
                    temp = open_and_count(mod_path)
                    total_count_ru += temp
                if i.split('.')[0] == 'EN':
                    temp = open_and_count(mod_path)
                    total_count_en += temp
                print(f"    Файл: {i}. Содержит слов: {temp}")
            else:
                continue
    

if __name__ == '__main__':
    digger(pathlib.Path(__file__).parent.absolute())
    print(f"Всего английских слов: {total_count_en}. Всего русских слов: {total_count_ru}.")

