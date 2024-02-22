import json
from src.classes import Category, Product

file = 'data/products.json'


def load_data(file):
    """Функция из JSON в Python для загрузки данных из файла."""
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        cat = []
        product = []

        for item in data:
            if item.get('name') in cat:
                continue
            else:
                cat.append(item.get('name'))

        for item in data:
            prod = item['products']
            for i in prod:
                if i.get('name') in product:
                    continue
                else:
                    product.append(i.get('name'))

        return cat, product


d = load_data(file)
print(d)
# cat = Category()
# prod = Product()
