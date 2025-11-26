#!/usr/bin/env python
import os
import logging
import json
import chardet

def create_structure():
    """
    Создаем структуру каталога для домашнего задания:
    project_root/
        ├── data/e
        │   ├── raw/
        │   ├── processed/
        ├── logs/
        ├── backups/
        └── output/
    """
    
    if not os.path.exists('project_root'):
        os.makedirs('project_root')
        #logging.info("Создан каталог:  'project_root'")

    if not os.path.exists('project_root/logs'):
        os.makedirs('project_root/logs')
        #logging.info("Создан каталог:  'project_root/logs'")


    if not os.path.exists('project_root/data'):
        os.makedirs('project_root/data')
        #logging.info("Создан каталог:  'project_root/data'")
        

    if not os.path.exists('project_root/data/raw'):
        os.makedirs('project_root/data/raw')
        #logging.info("Создан каталог:  'project_root/data/raw'")
        
        

    if not os.path.exists('project_root/data/processed'):
        os.makedirs('project_root/data/processed')
        #logging.info("Создан каталог:  'project_root/data/processed'")
        

    
        

    if not os.path.exists('project_root/backups'):
        os.makedirs('project_root/backups')
        #logging.info("Создан каталог:  'project_root/backups'")
        

    if not os.path.exists('project_root/output'):
        os.makedirs('project_root/output')
        #logging.info("Создан каталог:  'project_root/output'")
        


def create_files():
    """
    Создаем файлы в различных кодировках для работы в дальнейшем. Кодировка задается при открытии файла определением кодировки.
    """
    
    if not os.path.exists('project_root/data/raw/text_file_utf8.txt'):
        with open('project_root/data/raw/text_file_utf8.txt', 'w', encoding='UTF-8') as file_1:
            text1 = "В Python логирование осуществляется с помощью встроенного модуля\
            logging, который позволяет настраивать уровни логирования и обрабатывать сообщения о событиях. \
            Пример использования включает импорт модуля, получение логгера, задание уровня и использование \
            методов для записи сообщений, Это предпочтительнее  так как обеспечивает больший контроль и структурированность"
            file_1.write(text1)
            logging.info("Создан  файл :  text_file_utf8.txt")


    if not os.path.exists('project_root/data/raw/text_file_win1251.txt'):
        with open('project_root/data/raw/text_file_win1251.txt', 'w', encoding='windows-1251') as file_2:
            text2 =  "В работе с файлами при программировании на Python одним из важных аспектов\
            является проверка существования файла перед его открытием. Ошибки, возникающие вследствие \
            попытки открыть несуществующий файл, могут приводить к нештатным ситуациям и падению\
            программы. В этом руководстве мы рассмотрим различные методы проверки наличия файла\
            и обработки ошибок при его открытии"
            file_2.write(text2)
            logging.info("Создан  файл :  text_file_win1251.txt")
            
    if not os.path.exists('project_root/data/raw/text_file_CP1251.txt'):
        with open('project_root/data/raw/text_file_CP1251.txt', 'w', encoding='CP1251') as file_3:
            text3 = "В этой статье мы рассмотрели различные способы проверки существования файла перед его открытием, \
            а также методы обработки ошибок при работе с файлами. Используйте метод, который наилучшим образом соответствует\
            вашим требованиям и обеспечивает максимальную надежность вашего кода."
            file_3.write(text3)
            logging.info("Создан  файл :  text_file_CP1251.txt")






################################################################


create_structure()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='project_root/logs/project.log')

#
# Включаем логирование 
#
# Логи после создания каталогов, т.к. нельзя создать файл внутри каталога до его создания!!!
#

logging.info("Создан каталог:  'project_root'")
logging.info("Создан каталог:  'project_root/logs'")
logging.info("Создан каталог:  'project_root/data'")
logging.info("Создан каталог:  'project_root/data/raw'")
logging.info("Создан каталог:  'project_root/data/processed'")
logging.info("Создан каталог:  'project_root/backups'")
logging.info("Создан каталог:  'project_root/output'")

create_files()



logging.info('Вторая часть задания.........')

#
# В цикле  опрашиваем каталог raw для получения файлов и работы с ними, после образотки сохраняем в processed/
#
#

PATH = 'project_root/data/raw/'
SAVE_PATH= 'project_root/data/processed/'
logging.info('Вторая часть задания.........   2.1')
for file_name  in list(os.listdir(PATH)):
    with open(PATH+file_name, 'rb') as current_file:
        tmp_data = current_file.read()
        current_file_charset  = chardet.detect(tmp_data)
        encoding = current_file_charset['encoding']
        result_text = tmp_data.decode(encoding).swapcase()
        print('Имя файла: [', file_name,']',  result_text[1:50] + '...', "Кодировка файла : [", encoding , ']')
        root, extension = os.path.splitext(file_name)  
        with open(SAVE_PATH+root+'_processed' + extension, 'w', encoding=encoding) as new_file:
            new_file.write(result_text)
            print('Файл [' +  SAVE_PATH+root+'_processed' + extension, '] Записан')
  




logging.info('Вторая часть задания.........   2.2')
data_output = {}
i=0

#
# Читаем файлы в цикле , собираем метаданные кодировку, размер файла, даты создания и правки
#
#
#



OUTPUT_PATH ='project_root/output/processed_data.json'
for file_name  in list(os.listdir(SAVE_PATH)):
    with open(SAVE_PATH+file_name, 'rb') as current_file:
        original_text = current_file.read()

    current_file_charset  = chardet.detect(original_text)
    encoding = current_file_charset['encoding']  
    if encoding == None:            #  Грязный хак, но на моей Ubintu 24.04 кодировка одного файла не обрабытывается....
        encoding = 'MacCyrillic'    # 
    processed_text = original_text.decode(encoding, errors='replace')  

    text_size = os.path.getsize(SAVE_PATH+file_name)
    change_data = os.path.getatime(SAVE_PATH+file_name)

#
# Создаем словарь , добавляем их в словарь словарей
#
#
#


    data = {
            "file_name": file_name, 
            "original_text": str(original_text),
            "processed_text": str(processed_text),
            "text_size": text_size,
            "change_data": change_data
    }

    data_output[i] = data
    i+=1
#
# Выгружаем словарь словарей в файл 
#
#
#

with open(OUTPUT_PATH, 'w') as output_file:
    json.dump(data_output, output_file)    



logging.info('Третья часть задания.........   3.1')




