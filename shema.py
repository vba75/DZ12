from jsonschema import validate, ValidationError
import json
SAVE_PATH = 'project_root/output/serialization.json'

# Выполнение задания 4.2


#
# Созадем схему  для валидации json используемый ранее
#
#
#




schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string"
                },
                "full_file_name": {
                    "type": "string"
                },
                "size": {
                    "type": "integer",
                    "minimum": 0
                },
                "file_create": {
                    "type": "number",
                },
                "file_change": {
                    "type": "number",
                }
            },
            "required": ["file_name", "full_file_name" , "size", "file_create", "file_change"]
        }

#
# Загружаем файл json  валидируем его созданной схемой
#
#
#
with open(SAVE_PATH, 'rb') as input_file:
    my_dict = json.load(input_file)

for item in my_dict.items():

    try:
        validate(instance=item[1], schema=schema)
        print("Документ валиден")
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")

#
# конструкция except ValidationError as e:    print(f"Ошибка валидации: {e}") 
# выводит все возможные ошщибки, правда на языке создателя....
#
#       