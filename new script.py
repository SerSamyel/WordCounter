import json
from re import findall, compile
import os
import pathlib
import datetime
import hashlib



pattern_storage = {'RU': compile("[а-яА-ЯёЁ]+"),
                   'EN': compile("'?\w[\w']*(?:-\w+)*'?"),
                   }

def current_date():
    """ Return current data and time"""
    return datetime.datetime.now()

time = current_date()

def has_for_file(file):
    ''' func hash md5 '''
    BLOCK_SIZE = 65536  # The size of each read from the file
    file_hash = hashlib.md5()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file
    return  file_hash.hexdigest()

def analise_sha256_count(path_to_file, language): # RU.JSON EN.JSON etc.
    '''input file path and lang discriptor , return hash md5 and word count'''
    if language in pattern_storage:
        pattern = pattern_storage[language]
    else:
        return 'Not in this version.'

    count = 0
    with open(path_to_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        # для пробы передам открытый файл, чтобы дважды его не открывать
        md5 = has_for_file(path_to_file)
        for key in data['Items']:
            count += len(findall(pattern, data['Items'][key]['t']))
    return {language: {'md5': md5, 'count': count}}
'''
def create_base(filename, ):
    """ create a json file and add to basic data for first data"""
    # NOT READY!!!
    with open("data_file.json", "w") as write_file:
        date[time] =
                    {filename:
                         {'md5': None,
                          'ru': {'md5': None, 'count': None},
                          'en': {'md5': None, 'count': None}}}
        json.dump(data, write_file)
'''
def update_database():
    ''' add new time version of date'''
    pass

def recursive_analize(path):
    for folder_or_file in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder_or_file)):
            print('\n', f"Folder: {folder_or_file}.")
            recursive_analize(os.path.join(path, folder_or_file))
        else:
            file_d, rash = folder_or_file.split('.')
            if rash != 'json':
                continue
            mod_path = os.path.join(path, folder_or_file)
            print(f"    File: {folder_or_file}. Data: {analise_sha256_count(mod_path, file_d)}")


if __name__ == '__main__':
    print(f'Analise data: {time}')
    recursive_analize(pathlib.Path(__file__).parent.absolute())

