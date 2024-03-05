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

    @goods.setter
    def goods(self, value):
        if isinstance(value, self.__class__):
            self.__goods.append(value)
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
