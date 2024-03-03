class Category:
    name: str
    description: str
    goods: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.category_count += 1
        Category.product_count += len(self.__goods)

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.product_count} шт"

    def __len__(self):
        q = 0
        for i in self.__goods:
            q += i.quantity
        return q

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

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quntity

    def count_product(self):
        return self.quantity

    @staticmethod
    def create_goods():
        goods = {}
        name = input("Введите название - ")
        goods['name'] = name
        description = input("Введите описание - ")
        goods['description'] = description
        price = input("Введите цену - ")
        goods['price'] = price
        quantity = input("Ведите количество - ")
        goods['quantity'] = quantity
        return goods

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)

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
