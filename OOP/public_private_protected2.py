class Geom:
    __name = "Geom"

    def __init__(self, x1, x2, y1, y2):
        print(f"Инициализатор Geom{self.__class__}")
        self.__verify_coord__()
        self._x1 = x1 #скрытые аргументы жёстко привязанны к ккласу, можно через protected
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._name = self.__name #так можно обращаться

    def __verify_coord__(self, coord):#можно обращаться в классе, где определенна сама функция
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill="red"):
        super().__init__(x1, x2, y1, y2)
        self._fill = fill

    def get_coords(self):
        return (self._x1, self._y1)



r = Rect(0, 0, 10, 20)
#print(r.__dict__) #добавляется префикс базового класса, fill прописан в Rect, где прописан, там и добавляется
r.get_coords()
#print(r._x1)# напрямую обращаться не следует
