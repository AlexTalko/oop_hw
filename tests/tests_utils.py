from src.utils import get_products


def test_get_products():
    assert type(get_products()) == list
