import json
import os

data = []


def load_data(path):
    """Загружает данные из json файла"""
    global data
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    return data


def search_content(search_key):
    """Совершает поиск по ключевым словам и вовращает посты содержащие эти слова"""
    results = []
    for item in data:
        if search_key.lower() in item['content'].lower() or search_key in item['content']:
            results.append(item)
    if len(results) > 0:
        return results
    else:
        return None


def save_data_to_json(dict_results):
    """Сохраняет пост в json файл"""
    if os.path.isfile("posts.json"):
        with open("posts.json", "r", encoding="utf-8") as file_:
            data_ = json.loads(file_.read())
    else:
        data_ = []

    with open("posts.json", "w", encoding="utf-8") as file_:
        data_.append(dict_results)
        json.dump(data_, file_, indent=4, ensure_ascii=False)
