import pytest
from classes import Category, Product


@pytest.fixture
def test_category():
    return Category('Телевизоры',
                    'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                    ['Смартфоны', 'Телевизоры'])


@pytest.fixture
def test_product():
    return Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)


def test_init_category(test_category):
    assert test_category.name == 'Телевизоры'
    assert test_category.description == 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'
    assert test_category.goods == ['Смартфоны', 'Телевизоры']


def test_init_product(test_product):
    assert test_product.name == '55" QLED 4K'
    assert test_product.description == 'Фоновая подсветка'
    assert test_product.price == 123000.0
    assert test_product.count == 7


def test_count_category(test_category):
    assert test_category.count_category() == 4


def test_count_product(test_product):
    assert test_product.count_product() == 2
