class Category:
    name = str
    description = str
    goods = list
    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(self.goods)

    def __repr__(self):
        return (f"{self.name}"
                f"{self.description}"
                f"{self.goods}"
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

    def __repr__(self):
        return (f"{self.name}"
                f"{self.description}"
                f"{self.price}"
                f"{self.quantity}")