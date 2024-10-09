class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()  # Возвращаем содержимое файла
        except FileNotFoundError:
            return "Файл не найден"  # Если файл не найден

    def add(self, *products):
        existing_products = self.get_existing_products()

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                # Добавляем новый продукт в файл
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')

    def get_existing_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return {line.split(', ')[0] for line in file}  # Возвращаем множество продуктов по названию
        except FileNotFoundError:
            return set()  # Если файл не найден, возвращаем пустое множество


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())