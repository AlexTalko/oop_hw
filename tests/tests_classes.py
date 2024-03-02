from src.classes import Category, Product


def test_category():
    category = Category(name="Смартфоны", description="Смартфоны - часть жизни", goods=["Iphone", "Samsung"])
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны - часть жизни"
    assert category.goods == ["Iphone", "Samsung"]
    assert type(category.goods) == list
    assert category.number_of_categories == 1
    assert category.number_of_unique_products == 2


def test_product():
    product = Product(name="Iphone", description="Смартфон Apple", price=54_782.30, quantity=6)
    assert product.name == "Iphone"
    assert product.description == "Смартфон Apple"
    assert product.price == 54_782.30
    assert product.quantity == 6
    assert type(product.quantity) == int
    assert type(product.price) == float
