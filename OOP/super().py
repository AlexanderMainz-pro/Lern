class Geom:
    name = "Geom"

    def __init__(self, x1, x2, y1, y2):#общий класса, который вызывается для обоих дочерних классов
        print(f"инициализытор{self.__class__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Line(Geom):

    def draw(self): #Расширение базового класс
        print("Прямая линия")

class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):#инициализвтор базового класса следует вызывать в первую очередь
        Geom.__init__(self, x1, x2, y1, y2)#super вызывает объект, а через него вызыввает метод инит
        print("Инициализатор Rect")
        self.fill = fill

    def draw(self):  # Расширение базового класс
                print("Рисование прямоугольника")

l = Line(2, 3, 4, 5)
r = Rect(3, 4, 5, 6)
print(l.__dict__)
print(r.__dict__)

