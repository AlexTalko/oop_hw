import json
import os


def get_products():
    """Загружает данные товаров из products.json"""
    dir_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'products.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        file = json.load(f)
        return file

