class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self): #выводит отладочную информацию об объекте
        return f"{self.__class__} : {self.name}"

    def __str__(self): #выводит пользовательскую информацию
        return f"{self.name}"

cat = Cat("васька")
print(cat)

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords) #настраиваем __len__ для того что нам нужно выводить

    def __abs__(self):
        return list(map(abs, self.__coords)) #возвращает модули координат

p = Point(1, -2, -5)
print(len(p))
print(abs(p))