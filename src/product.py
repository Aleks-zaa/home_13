class Product:
    name: str
    description: str
    price: float
    color: str
    ct: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

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


class Phone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, power: float, model: str,
                 memory: float, color: str):
        super().__init__(name, description, price, quantity, color)
        self.power = power
        self.model = model
        self.memory = memory


class Grass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, period: float,
                 color: str):
        super().__init__(name, description, price, quantity, color)
        self.period = period
        self.country = country



