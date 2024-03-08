from src.classes import Category, Product
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
    assert ct2.number_of_categories == 2
    assert ct1.display_goods == []

def test_product():
    product = Product(name="Iphone", description="Смартфон Apple", price=54_782.30, quantity=6)
    assert product.name == "Iphone"
    assert product.description == "Смартфон Apple"
    assert product.price == 54_782.30
    assert product.quantity == 6
    assert type(product.quantity) == int
    assert type(product.price) == float
