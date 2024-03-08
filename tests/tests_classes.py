from src.classes import Category, Product


def test_category():
    category = Category(name="Смартфоны", description="Смартфоны - часть жизни")
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны - часть жизни"
    assert type(category.display_goods) == list
    assert category.number_of_categories == 1


def test_product():
    product = Product(name="Iphone", description="Смартфон Apple", price=54_782.30, quantity=6)
    assert product.name == "Iphone"
    assert product.description == "Смартфон Apple"
    assert product.price == 54_782.30
    assert product.quantity == 6
    assert type(product.quantity) == int
    assert type(product.price) == float
