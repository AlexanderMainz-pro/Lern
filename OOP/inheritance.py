class Geom:
    name = "John"

    def set_cords(self, x1, x2, y1, y2):#self может ссылаться не только на объект класса, но и на дочерний объект
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Line(Geom):#наследуемся от класса
    name = "Line"
    def draw(self):
        print("Рисуем примитива")



class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")



g = Geom()
l = Line()
r = Rect()
l.set_cords(1, 2,3, 4)
r.set_cords(4, 5, 6, 7)
g.set_cords(3, 4, 5, 676)
print(l.name)
print(r.name)
l.draw()
r.draw()