class Category:
    name = str
    description = str
    goods = list
    count_categories = 0
    count_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__goods = []

        Category.count_categories += 1
        Category.count_products += len(self.__goods)

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

    def __str__(self):
        """
    Для класса Category добавить строковое отображение в следующем виде:
    Название категории, количество продуктов: 200 шт."""
        return f"{self.name}, количество продуктов: {Category.count_products} шт"

    def __repr__(self):
        return (f"{self.name}"
                f"{self.description}"
                f"{self.__goods}"
                f"{self.count_categories}"
                f"{self.count_products}")


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

    def __add__(self, other):
        """ Для класса Product необходимо добавить возможность складывать объекты между собой таким образом,
        чтобы результат выполнения сложения двух продуктов был сложением сумм, умноженных на количество на складе."""
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        """Для класса Product добавить строковое отображение в следующем виде:
            Название продукта, 80 руб. Остаток: 15 шт."""
        return f"{self.name}, {self.price_product} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return (f"{self.name} "
                f"{self.description} "
                f"{self.price} "
                f"{self.quantity} ")
