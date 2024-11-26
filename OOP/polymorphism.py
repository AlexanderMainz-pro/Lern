class Geom: #если забудем где-нибуть указать метод, по умолчанию вызовется метод базового класса
    def get_pt(self):
        raise  NotImplementedError("В дочернем классе должен быть переопределён метод get_pt")

class Rectangle(Geom):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_pr(self): #метод должен называться одинаково во всех объектах, тот самый полиморфизм
        return 2 * (self.x + self.y)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(10, 20)

s1 = Square(5)
s2 = Square(10)

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]# можно сразу запихивать в список, более красиво и лаконично

#for g in geom: #можно решить в лоб, но не лучшая реализация
#        print(g.get_rect_pr())
#    else:
#        print(g.get_sq_pr())

for g in geom:
    print(g.get_pr())# Единый интерфейс, через который мы обращаемся к разным объектам


