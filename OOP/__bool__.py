class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self): #возвращаем длину через магический метод
        print("__len__")
        return  self.x * self.x + self.y * self.y

    def __bool__(self):# проверяем неравенств, возвращает только булевы значения, вызывается неявно, используется
                        #там, где сам экземпляр должен проверять себя на истину
        print("__bool__")
        return self.x == self.y

class Point2:
    pass

p = Point(3, 4)#проверяем координаты на равенство
if p:
    print("объект даёт True")
else:
    print("объект дает False")