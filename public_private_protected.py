from accessify import private, protected #инсталлим для вызова методов

class Point():
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private #не сможем вызваать няпрямую методы
    @classmethod #метод класса
    def check_value(cls, x):
        return type(x) in (int, float) #проверка на числа, после вызываем в методе set_coord

    def set_coord(self, x, y):#сеттер
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
           raise ValueError('Входные данные должны быть числами')

    def get_coord(self):#геттер
        return self.__x, self.__y


pt = Point(1, 3)
pt.set_coord(10, 20)
print(dir(pt))
print(pt.get_coord())
pt.check_value() #сможем обратиться через  pt._Poinnt__check_value