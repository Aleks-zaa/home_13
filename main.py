from src.classes import Category, Product
from src.utils import read_json, append_list_product, create_obj_category

file = 'data/products.json'

list_data = read_json(file)

for category in list_data:
    pt = category['products']
    ct = Category(category.get('name'), category.get('description'), pt)
    # ct = create_obj_category()
    print(ct)
    print(len(ct))


    product_data = {'name': 'Samsung S500', 'description': '256GB, Серый', 'price': 7894.0, 'quantity': 10}
# product_data = Product.create_goods()
    new_product_instance = Product.new_product(product_data)
    ct.goods = product_data

# list_obj_goods = ct.list_goods
# print(list_obj_goods)

# print(','.join(list_obj_goods).replace(',', '\n'))
# print(new_product_instance)
