from src.classes import Category, Product, SmartPhone, GrassLawn
import pytest


@pytest.fixture
def category_gadgets():
    ct1 = Category("Смартфоны", "Смартфоны - часть жизни")
    ct2 = Category("Смарт-часы", "Компьютер на руке")
    return ct1, ct2


def test_category(category_gadgets):
    ct1, ct2 = category_gadgets
    assert ct1.name == "Смартфоны"
    assert ct1.description == "Смартфоны - часть жизни"
    assert ct2.name == "Смарт-часы"
    assert ct2.description == "Компьютер на руке"
    assert ct2.count_categories == 2
    assert ct1.display_goods == []


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

