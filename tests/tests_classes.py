from src.classes import Category, Product, SmartPhone, GrassLawn
import pytest


@pytest.fixture
def category_gadgets():
    ct1 = Category("Смартфоны", "Смартфоны - часть жизни")
    ct2 = Category("Смарт-часы", "Компьютер на руке")
    prod1 = Product("Iphone", "Смартфон Apple", 10_000.30, 6)
    prod2 = Product("Samsung", "Смартфон Samsung", 20_000, 15)
    ct1.add_goods(prod1)
    ct1.add_goods(prod2)
    return ct1, ct2


def test_category(category_gadgets):
    ct1, ct2 = category_gadgets
    assert ct1.name == "Смартфоны"
    assert ct1.description == "Смартфоны - часть жизни"
    assert ct2.count_categories == 2
    assert ct1.count_products == 2
    assert ct2.display_goods == []
    assert str(ct1) == "Смартфоны, количество продуктов: 2 шт"
    assert len(ct1) == 2
    assert ct1.get_goods == 'Iphone, 10000.3 руб руб. Остаток: 6 \nSamsung, 20000 руб руб. Остаток: 15 \n'
    prod3 = Product("Товар", "Проверяющий метод добавления", 1699, 0)
    with pytest.raises(ValueError):
        ct1.add_goods(prod3)  # Ошибка, товар с количеством 0
    assert ct1.average_price() == 15000.15
    assert ct2.average_price() == 0  # Вернет ноль, если список продуктов пуст


@pytest.fixture
def products():
    prod1 = Product("Iphone", "Смартфон Apple", 10_000.30, 6)
    prod2 = Product("Samsung", "Смартфон Samsung", 20_000, 15)
    prod3 = SmartPhone("Xiaomi", "Смартфон на android", 8745.10, 24, 8.6,
                       "Y8", 8, "Silver")
    prod4 = GrassLawn("Canada Green", "Ковер для ваших пальчиков", 15_000, 169,
                      "Canada", 3, "Rich green")
    return prod1, prod2, prod3, prod4


def test_product(products):
    prod1, prod2, prod3, prod4 = products
    assert prod1.name == "Iphone"
    assert prod1.description == "Смартфон Apple"
    assert prod2.quantity == 15
    assert prod1 + prod2 == 360001.8
    assert prod1.price_product == '10000.3 руб'
    assert prod3.price_product == '8745.1 руб'
    with pytest.raises(TypeError):
        prod3 + prod4
