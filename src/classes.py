class Category:
    name = str
    description = str
    goods = list
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(self.__goods)

    def add_goods(self, product):
        """Добавляет :product в список goods"""
        self.__goods.append(product)

    @property
    def get_goods(self):
        """Возвращает goods в нужном формате"""
        for product in self.__goods:
            return f'{product["name"]}, {product["price"]} руб, Остаток: {product["quantity"]} шт.'

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
    def new_product(cls, name=str, description=str, price=float, quantity=int):
        """Создаем новый товар"""
        product = cls(name, description, price, quantity)
        new_product = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity
        }
        return new_product

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

    def __repr__(self):
        return (f"{self.name}"
                f"{self.description}"
                f"{self.price}"
                f"{self.quantity}")
