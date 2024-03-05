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
        return f"{self.name}, количество продуктов: {len(self.__goods)} шт"

    def __len__(self):
        q = 0
        for i in self.__goods:
            q += i.get('quantity')
        return q

    @property
    def goods(self):
        return self.__goods

    # @goods.setter
    # def goods(self, value):
    #     if isinstance(type(value), self.__class__):
    #         self.__goods.append(value)
    #     print(type(value))
    #     raise TypeError

    @goods.setter
    def goods(self, value):
        self.__goods.append(value)

    @staticmethod
    def add_good(value):
        if isinstance(value, Category):
            Category.__goods.append(value)

        raise TypeError

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
        if issubclass(type(self), type(other)):
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
        self.power = power
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)


class Grass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, period: float,
                 color: str):
        self.period = period
        self.country = country
        super().__init__(name, description, price, quantity, color)


# if __name__ == '__main__':
#     # a = [{"name": "Sams Ul",
#     #       "description": "125GB",
#     #       "price": 1000.0,
#     #       "quantity": 6, "color": "black", "power": 100, "model": "GG", "memory": 200}]
#     #
#     # exp = Category('Смартфоны', 'для удобства жизни', [{
#     #     "name": "Samsung Galaxy C23 Ultra",
#     #     "description": "256GB, Серый цвет, 200MP камера",
#     #     "price": 180000.0,
#     #     "quantity": 5, "color": "black"}])
#     # exp.goods = a
#     # print(exp.goods)
#
#     a1 = Product("Sams Ul", "125GB", 10.0, 2, "black")
#     b1 = Phone("Umi", '555', 50, 2, 500, '7', 125, 'black')
#     res = b1 + b1
#     print(res)
