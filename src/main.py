from classes import Category, Product
from utils import get_products


def main():
    """Получаем зи файла товары по категориям"""
    p = get_products()
    for product in p:
        category = Category(product['name'], product['description'], product['products'])
        print(f"Категория: {category.name}\nОписание: {category.description}")
        for prod in product['products']:
            prod = Product(prod['name'], prod['description'], prod['price'],
                           prod['quantity'])
            print(f"Название: {prod.name}\nОписание: {prod.description}\n"
                  f"Цена: {prod.price}\nОстаток: {prod.quantity} шт")
            print(f"Количество товаров: {category.number_of_unique_products}")
            print(f"Количество категорий: {category.number_of_categories}")


if __name__ == '__main__':
    main()
