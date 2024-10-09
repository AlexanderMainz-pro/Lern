class Geom():
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2, fill=None):
        print(f'Инициализация {self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.fill = fill

class Line(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        self.fill = fill

    def draw(self):
        print('Рисование линии')

class Rest(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')

l = Line(0, 0, 10, 20)