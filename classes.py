class Category:
    name: str
    description: str
    goods: list
    common_count_product = 4
    common_count_category = 2

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

    def count_category(self):
        return 4


class Product:
    name: str
    description: str
    price: float
    count: int

    def __init__(self, name, description, price, count):
        self.name = name
        self.description = description
        self.price = price
        self.count = count  # количество в наличии

    def count_product(self):
        return 2
