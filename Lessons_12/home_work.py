"""
1. Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене
"""
from itertools import product


class Product:
    def __init__(self, name_product, shop, cost):
        self.__name_product = name_product
        self.__shop = shop
        self.__cost = cost

    @property
    def name_product(self):
        return self.__name_product

    @property
    def shop(self):
        return self.__shop

    @property
    def cost(self):
        return self.__cost

    def __str__(self):
        """Строковое представление товара."""
        return f"Товар: {self.__name_product}, Магазин: {self.__shop}, Цена: {self.__cost} руб."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__cost + other.__cost
        raise TypeError("Сложение возможно только между товарами.")


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)

    def get_product_by_index(self, index):
        if 0 <= index < len(self.__products):
            return str(self.__products[index])
        return "Товара с таким индексом нет"

    def get_product_by_name(self, name):
        product_list = [product for product in self.__products if product.name_product.lower() == name.lower()]
        if product_list:
            return "\n".join(str(product) for product in product_list)
        return f"Товар с названием '{name}' не найден."

    def sort_products(self, var="name"):

        if var == "name":
            self.__products.sort(key=self._sort_by_name)
        elif var == "store":
            self.__products.sort(key=self._sort_by_store)
        elif var == "cost":
            self.__products.sort(key=self._sort_by_price)
        else:
            raise ValueError("Некорректный параметр сортировки. Допустимые значения: 'name', 'store', 'cost'.")

    def _sort_by_name(self, product):
        return product.name.lower()

    def _sort_by_store(self, product):
        return product.store.lower()

    def _sort_by_price(self, product):
        return product.cost

    def __str__(self):
        if self.__products:
            return "\n".join(str(product) for product in self.__products)
        return "Склад пуст."

warehouse = Warehouse()

warehouse.add_product(Product("Ноутбук", "DNS", 50000))
warehouse.add_product(Product("Смартфон", "М.Видео", 30000))
warehouse.add_product(Product("Наушники", "DNS", 5000))






