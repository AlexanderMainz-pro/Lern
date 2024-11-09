class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x ==other.x and self.y ==other.y

    def __hash__(self):
        return hash((self.x, self.y))#возвраще мне через self, а через кортеж, подмеили хеш обьекста на хеш точки

p1 = Point(1, 2)#объекты воспринимаются неизменяемые
p2 = Point(1, 2)# объекты с одинаковыми значениями вспринимаются как один обьект, можно сколь скольк угодно с одинаковым хешем



print(hash(p1),hash(p2) , sep="\n") #дня неизменяемых объектов класса можно вычислить хеш