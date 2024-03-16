from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый продукт для общих свойств классов"""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Category:
    name: str
    description: str
    goods: list
    count_categories = 0
    count_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__goods = []

        Category.count_categories += 1

    def add_goods(self, product):
        """Добавляет :product в список goods"""
        if not isinstance(product, Product):
            raise TypeError("Продукт не соответствует классу")
        self.__goods.append(product)
        Category.count_products += 1

    @property
    def get_goods(self):
        """Возвращает goods в нужном формате"""
        list_goods = ''
        for product in self.__goods:
            list_goods += f'{product.name}, {product.price_product} руб. Остаток: {product.quantity} \n'
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


class MixinRepr:
    """Миксин для вывода информации о создании товара в консоль"""

    def __repr__(self):
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attributes})"


class Product(BaseProduct, MixinRepr):
    name: str
    description: str
    price: float
    quantity: int

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
        if self.price <= 0:
            print("Некорректная цена")
        else:
            self.price = price

    def __add__(self, other):
        """Метод сложения товаров одного класса между собой таким образом,
        чтобы результат выполнения сложения двух продуктов был сложением сумм, умноженных на количество на складе."""
        if issubclass(self.__class__, other.__class__):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Ошибка")

    def __str__(self):
        """Для класса Product добавить строковое отображение в следующем виде:
            Название продукта, 80 руб. Остаток: 15 шт."""
        return f"{self.name}, {self.price_product} руб. Остаток: {self.quantity} шт."


class SmartPhone(Product, MixinRepr):
    capacity: float  # производительность (измеряется в герцах)
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, capacity, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        super().__repr__()


class GrassLawn(Product, MixinRepr):
    country_man: str
    germin_per: int
    color: str

    def __init__(self, name, description, price, quantity, country_man, germin_per, color):
        super().__init__(name, description, price, quantity)
        self.country_man = country_man
        self.germin_per = germin_per
        self.color = color
