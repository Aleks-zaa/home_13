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


list_data = read_json(file)


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


# print(list_category())


def list_product():
    """Функция получения списка продуктов из данных файла."""
    data = read_json(file)
    product = []
    for item in data:
        prod = item['products']
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
    cat = 0
    prod = 0
    for category in data:
        cat += 1
        for product in category['products']:
            # products.append(Product(**product))
            goods.append(product)
            prod += 1
    # print(cat)
    return goods


pt = append_list_product()
goods = []
for category in list_data:
    ct = Category(category.get('name'), category.get('description'), pt)
    # print(category)
    print(ct)
    for product in category['products']:
        # products.append(Product(**product))
        goods.append(product)

    obj_goods = ct.goods
    product_data = {'name': 'Samsung S500', 'description': '256GB, Серый', 'price': 7894.0, 'quantity': 10}
    # product_data = Product.create_goods()
    new_product_instance = Product.new_product(product_data)
# ct.goods = product_data
#     print(obj_goods)



# list_obj_goods = ct.list_goods
# print(list_obj_goods)
# print(obj_goods)
# print(','.join(list_obj_goods).replace(',', '\n'))
# print(new_product_instance)
