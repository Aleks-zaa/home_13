import json
import os
from src.classes import Category, Product

file = 'data/products.json'


def read_json(path: str):
    """Функция чтения json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


def list_category():
    """Функция получения списка категорий из данных файла."""
    data = read_json(file)
    cat = []
    for item in data:
        if item.get('name') in cat:
            continue
        else:
            cat.append(item.get('name'))
    return cat


def list_product():
    """Функция получения списка продуктов из данных файла."""
    data = read_json(file)
    product = []
    for item in data:
        prod = item['products']
        print(prod)
        for i in prod:
            if i.get('name') in product:
                continue
            else:
                product.append(i.get('name'))
    return product


def append_list_product():
    data = read_json(file)
    products = []
    goods = []
    for category in data:
        for product in category['products']:
            # products.append(Product(**product))
            goods.append(product)
    return goods


def create_obj_category():
    list_data = read_json(file)
    for category in list_data:
        pt = category['products']
        ct = Category(category.get('name'), category.get('description'), pt)
        # print(pt)
        return ct

