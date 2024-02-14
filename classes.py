class Category:
    name:  str
    description: str
    goods: list
    count_category = 0
    common_count_category = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

class Product:
    name:  str
    description: str
    price: float
    count: int

    def __init__(self, name, description, price, count):
        self.name = name
        self.description = description
        self.price = price
        self.count = count  #количество в наличии

