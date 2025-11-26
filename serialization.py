import json
import os
from datetime import datetime


# Выполнение задания 4.1


PATH = 'project_root/data/processed/'
SAVE_PATH = 'project_root/output/serialization.json'

my_dict= {}
i = 1

class FileInfo():
    def __init__(self, file_name:str, full_file_name: str, file_size: str, file_create: str, file_change: str):
        self.file_name = file_name
        self.file_full_name = full_file_name
        self.file_size = file_size
        self.file_create = file_create
        self.file_change = file_change

    def toJSON(self):
            return {
                "file_name": self.file_name,
                "full_file_name": self.file_full_name,
                "size": self.file_size,
                "file_create": self.file_create,
                "file_change" : self.file_change
            }

#
# Метод toJSON в объекте позволяет его преобразовать стандартными методами модуля json
#  наравне  с методами __str__()  & __repr__()
#
#
# в цикле собираем данные по файлам, создаем объект с методанными, и преобразуем его в json
#

for file_name  in list(os.listdir(PATH)):

    file_size = os.path.getsize(PATH+file_name)
    full_file_name= PATH+file_name
    create_file = os.path.getctime(PATH+file_name)
    change_file = os.path.getatime(PATH+file_name)

    file_object = FileInfo(file_name, full_file_name, file_size, create_file, change_file)
    my_dict[i] = file_object.toJSON() 
    i+=1

#    print(file_size, full_file_name, file_name, change_file, create_file) 


with open(SAVE_PATH, 'w') as output_file:
    json.dump(my_dict, output_file)  


input('Нажмите Enter для продолжения...')


with open(SAVE_PATH, 'rb') as input_file:
    my_dict_2 = json.load(input_file)


print(len(my_dict_2))    


#
#  Получаем первоначальные сведения после чтения из файла 
#




for item in my_dict_2.items():
    print(f"Имя файла:  {item[1]['file_name']} ,  Дата создания :  {item[1]['file_create']} " ) 
           
# Выводим информацию после десериализации.
           







    


    