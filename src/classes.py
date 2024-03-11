from abc import ABC, abstractmethod


class SampleOrder(ABC):
    @abstractmethod
    def __init__(self):
        pass


class UserError(Exception):
    """ Пользовательский класс обработки исключения """
    message = ""

    def init(self, *args, **kwargs):
        self.message = args[0] if args else 'Проблемы с параметрами объекта'

    def str(self):
        return self.message


class Category(SampleOrder):
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

    # def __add__(self, other):
    #     if isinstance(other, Product):
    #         self.__goods.append(other)
    #     else:
    #         raise TypeError('Не тот класс(метод в Категории)')

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods.append(value)

    def add_good(self, value):
        if isinstance(value, Product):
            try:
                if value.quantity <= 0:
                    raise UserError
            except UserError as e:
                e.message = "Продукт с нулевым количеством не может быть добавлен"
                print(e)
            else:
                self.__goods.append(value)
                print('Продукт добавлен')
                return self.__goods
            finally:
                print('Обработка завершена')
                return self.__goods
        raise TypeError('Не соответствует классу')

    def avg_price(self):
        total_sum = 0
        total_quantity = 0
        try:
            for item in self.__goods:
                total_sum += item.price * item.quantity
                total_quantity += item.quantity
            return total_sum / total_quantity
        except ZeroDivisionError as e:
            e.message = "Нулевое значение"
            print(e)
            return 0

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


class Order(SampleOrder):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class SampleProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass


class MixinProduct:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes}"


class Product(SampleProduct):
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
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError(f'разные классы')

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


class Phone(Product, MixinProduct):

    def __init__(self, name: str, description: str, price: float, quantity: int, power: float, model: str,
                 memory: float, color: str):
        self.power = power
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)


class Grass(Product, MixinProduct):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, period: float,
                 color: str):
        self.period = period
        self.country = country
        super().__init__(name, description, price, quantity, color)


if __name__ == '__main__':
    a1 = Product("Sams", "15GB", 100.0, 0, "black")
    b1 = Product("ttt", "10GB", 500.0, 2, "red")
    # product_data = [{'name': 'UMI 999', 'description': '000GB, Серый', 'price': 444.0, 'quantity': 10,
    #                  "color": "black"}]
    list_goods = [
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
         'quantity': 5, 'color': 'black'},
        {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8, 'color': 'black'},
        {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14,
         'color': 'black'}]

    pt = Category('port', 'www', list_goods)
    print(pt.avg_price)

    print(pt.goods)
    # print(pt)
    # pt + a1
    # print(pt.goods)
    # pt + 1
    # print(pt.goods)
    # print(pt.add_good(a1))
    # print(pt.add_good(b1))

    # print(pt.goods)
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

    # b1 = Phone("Umi", '555', 50, 2, 500, '7', 125, 'black')
    # c1 = Grass("Лопух", 'Большой', 100, 3, 'Россия', 1, 'black')
    # res = a1 + b1
    # print(res)
    # print(repr(a1))
    # print(repr(b1))
    # print(repr(c1))
