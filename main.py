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


def append_list_product():
    data = read_json(file)
    products = []
    goods = []
    for category in data:
        for product in category['products']:
            # products.append(Product(**product))
            goods.append(product)
    return goods


pt = append_list_product()
ct = Category("Смартфоны", "Смартфоны, как средство", pt)

obj_goods = ct.goods
new_goods = Product.create_goods()
ct.goods = new_goods
# # new_good = {"name": "UMI", "description": "100GB, Серый цвет, 200MP камера", "price": 777777.0, "quantity": 999}
# ct.goods = new_good


list_obj_goods = ct.list_goods
print(list_obj_goods)
print(obj_goods)
print(','.join(list_obj_goods).replace(',', '\n'))
