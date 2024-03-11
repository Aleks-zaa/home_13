from src.classes import Category, Product
# from src.category import Category
# from src.product import Product
from src.utils import read_json, append_list_product, create_obj_category

file = 'data/products.json'

list_data = read_json(file)

if __name__ == '__main__':
    for category in list_data:
        pt = category['products']
        ct = Category(category.get('name'), category.get('description'), pt)
        # ct = create_obj_category()
        # print(ct)
        # print(pt)
        print(ct.goods)

        # print(f"{category.get('name')}, общее количество продуктов: {len(ct)} шт")
        for i in pt:
            products = Product(i.get('name'), i.get('description'), i.get('price'), i.get('quantity'), i.get('color'))
            # print(products)



    #
    # product_data = [{'name': 'UMI S500', 'description': '256GB, Серый', 'price': 7894.0, 'quantity': 10,
    #                  "color": "black"}]
    # a1 = Product("Sams", "15GB", 100.0, 0, "black")
    # ct = Category('', '', [])
    # print(ct.add_good(a1))

    # print(type(ct))
    # ct1 = Category.goods(product_data)
    # # product_data = Product.create_goods()
    # new_product_instance = Product.new_product(product_data)
    # print(new_product_instance)
    # ct = Category('name', 'description', append_list_product())
    # ct.goods = product_data
    # print(ct.goods)
    # list_obj_goods = ct.list_goods
    # print(list_obj_goods)
    # print(','.join(list_obj_goods).replace(',', '\n'))
