import json
import os


def get_products():
    """Загружает данные товаров из products.json"""
    with open(os.path.join('D:/pythonProject/oop_lesson_1/products.json'), 'r', encoding="utf-8") as f:
        products = json.load(f)
        return products
