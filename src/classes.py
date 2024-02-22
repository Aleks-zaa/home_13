class Category:
    name: str
    description: str
    goods: list
    common_count_product = 4
    common_count_category = 2

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

    def count_category(self):
        return len(self.__goods)


class Product:
    name: str
    description: str
    price: float
    ct: int  #количество в наличии

    def __init__(self, name: str, description: str, price: float, ct: int):
        self.name = name
        self.description = description
        self.price = price
        self.ct = ct

    def count_product(self):
        return self.ct
