#
# File handling routines
#
import json

def read_text_file(filename):

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    
    return text


def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def write_json_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
