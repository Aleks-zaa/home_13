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

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods.append(value)

    def count_goods(self):
        return len(self.__goods)

    @property
    def list_goods(self):
        ls_goods = []
        for i in self.__goods:
            nm = i.get('name')
            price = i.get('price')
            quantity = i.get('quantity')
            ls_goods.append(f'"{nm}" - {price} руб., Остаток: {quantity} шт.')
        return ls_goods

    def __str__(self):
        return f"{self.name}, {self.description}, {self.goods}"


class Product:
    name: str
    description: str
    price: float
    ct: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def count_product(self):
        return self.quantity

    @classmethod
    def create_goods(cls, name, description, price, quantity):
        if name == Category.goods[0]:
            quantity += Category.goods[3]
            return cls(name, description, price, quantity)
        else:
            return cls(name, description, price, quantity)

    @property
    def correct_price(self):
        if self.price <= 0:
            return "цена введена некорректная"
        else:
            return self.price

    @correct_price.setter
    def correct_price(self, value):
        if self.price < value.price:
            new_price = input("Подтвердите понижение цены (Y/N) ")
            if new_price == 'Y'.upper():
                self.price = value.price
        else:
            self.price = value.price
