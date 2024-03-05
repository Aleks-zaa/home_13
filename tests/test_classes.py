import pytest
from src.classes import Category, Product, Phone, Grass


# from src.category import Category
# from src.product import Product


@pytest.fixture
def test_category():
    return Category('Телевизоры',
                    'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                    ['Смартфоны', 'Телевизоры'])


@pytest.fixture
def test_product():
    return Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7, 'red')


@pytest.fixture
def test_phone():
    return Phone('Amoled', 'Новый телефон', 500.0, 2, 100, 'UMI', 125, 'white')


@pytest.fixture
def test_grass():
    return Grass('Grass', 'Травка', 800.0, 4, 'RUS', 1, 'green')


def test_init_category(test_category):
    assert test_category.name == 'Телевизоры'
    assert test_category.description == 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'
    assert test_category.goods == ['Смартфоны', 'Телевизоры']


def test_init_product(test_product):
    assert test_product.name == '55" QLED 4K'
    assert test_product.description == 'Фоновая подсветка'
    assert test_product.price == 123000.0
    assert test_product.quantity == 7
    assert test_product.color == 'red'


def test_init_phone(test_phone):
    assert test_phone.name == 'Amoled'
    assert test_phone.description == 'Новый телефон'
    assert test_phone.price == 500.0
    assert test_phone.quantity == 2
    assert test_phone.power == 100
    assert test_phone.model == 'UMI'
    assert test_phone.memory == 125
    assert test_phone.color == 'white'


def test_init_grass(test_grass):
    assert test_grass.name == 'Grass'
    assert test_grass.description == 'Травка'
    assert test_grass.price == 800.0
    assert test_grass.quantity == 4
    assert test_grass.country == 'RUS'
    assert test_grass.period == 1
    assert test_grass.color == 'green'


def test_count_category(test_category):
    assert test_category.count_goods() == 2


def test_count_product(test_product):
    assert test_product.count_product() == 7
