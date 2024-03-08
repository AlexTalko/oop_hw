class Category:
    name = str
    description = str
    goods = list
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__goods = []

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(self.__goods)

    def add_goods(self, product):
        """Добавляет :product в список goods"""
        if not isinstance(product, Product):
            raise TypeError("Ошибка")
        self.__goods.append(product)

    @property
    def get_goods(self):
        """Возвращает goods в нужном формате"""
        list_goods = ''
        for product in self.__goods:
            list_goods += f'{product.name}, {product.price_product} руб. Остаток: {product.quantity}\n'
        return list_goods

    @property
    def display_goods(self):
        return self.__goods

    def __len__(self):
        """Вернет количество товаров в списке"""
        return len(self.__goods)

    def __repr__(self):
        return (f"{self.name}"
                f"{self.description}"
                f"{self.__goods}"
                f"{self.number_of_categories}"
                f"{self.number_of_unique_products}")


class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Создаем новый товар"""

        product = cls(**product_data)
        return product

    @property
    def price_product(self):
        """Возвращает цену товара"""
        return f'{self.price} руб'

    @price_product.setter
    def price_product(self, price):
        """Устанавливает цену товара"""
        self.price = price
        if self.price <= 0:
            print("Некорректная цена")

    def __str__(self):
        return f"{self.name}, {self.price_product} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return (f"{self.name} "
                f"{self.description} "
                f"{self.price} "
                f"{self.quantity} ")
