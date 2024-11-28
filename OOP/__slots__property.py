class Point2D:
    __slots__ = ('x', 'y', '__lenght')#запрещает только локальны свойства

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__lenght = (x * x + y * y) ** 0.5 #будет появляться автоматически, можно определить через декоратор

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, value):
        self.__lenght = value

pt = Point2D(1, 2)
print(pt.lenght)