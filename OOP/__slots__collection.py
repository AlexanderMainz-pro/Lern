import  timeit
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self. y = 0


class Point2:
    __slots__ = ('x', 'y')#определяется через кортеж разрешённые локальные свойства, могут присутствовать только
                            #разрешено только работать только с разрешенными,а не на атрибуты класса
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):#работает чуть быстрее
        self.x += 1
        del self.y
        self. y = 0

p = Point(1, 2)
p2 = Point2(10, 20)

t1 = timeit.timeit(p.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2)