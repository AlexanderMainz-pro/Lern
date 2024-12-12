class Point:
   MAX_CORD = 100
   MIN_CORD = 0


#def create_class_point(name, base, attrs):#name имя Point, base кортеж из базовых классов attrs все атрибуты <--1
#    attrs.update({"MAX_CORD": 100, "MIN_CORD": 0}) #добавляем в класс параметры
#return type(name, base, attrs) #возвращет меткласс type, учебный пример

class Meta(type):
    def __new__(sls, name, base, attrs):
        attrs.update({"MAX_CORD": 100, "MIN_CORD": 0})
        return type.__new__(sls, name, base, attrs)
#    def __init__(cls, name, base, attrs):#созданный класс, имя класса, кортеж из Б классовб  словарь из атрибутов класса
#        super().__init__(name, base, attrs)#вызываем инициализатор базового класса
#        cls.MAX_CORD = 100#вызываем динамически,т.к класс уже создан
#        cls.MIC_CORD = 0

class Point(metaclass=Meta): #передаём ссылку на соответствующий метакласс,предаём все в функцию 1-->
    def get_cords(self):
        return (0, 0)#все атрибуты попадают в словарь attrs


pt = Point()
print(pt.MAX_CORD)#ччитает атрибут
print(pt.get_cords())#читает метод