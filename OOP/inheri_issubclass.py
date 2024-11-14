class Geom:#автоматически наследуется от object
    pass

class Line(Geom):
    pass

class Vector(list):#переопределяем стандартный класс list
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
g = Geom()

l = Line()
print(issubclass(Line, Geom))#смотрим что за чем наследуется
