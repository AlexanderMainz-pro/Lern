class Point:
    MAX_COORD = 100#свойства, являются общими для всех экземпляров
    MIN_COORD = 0

    def __init__(self, x, y):#методы
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bount(self, left): #если хотим поменять MIN_COORD
        self.MIN_COORD = left


    def __getattribute__(self, item): #ссылка и атрибут, к которому идёт обращение
        """Если в вашем классе есть метод __getattribute__,
        python вызывает этот метод для каждого атрибута независимо от того, существует он или нет.
        через этот маический метод есть возможность управлять доступом к атрибутам, к Х теперь запрещйн доступ"""
        if item == "x":
            raise  ValueError("Доступ запрещён")
        print("__getattribute__")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """Он атоматически вызывается всякий раз, когда идёт присвоение определённого значения
        (self, атрибут, значение, которое присваивается, можем запретить создавать значения)"""
        if key == "z":
            raise ValueError("Недопустимый атрибут")
        print("__setattr__")
        #object.__setattr__(self, key, value)
        #self.__dict__[key] = value #__dict__ хранит все локальные атрибуты класса

    def __getattr__(self, item):
        """автоматически вызывается, когда идет обращение к несуществующему атрибуту класса"""
        return False

    def __delattr__(self, item):
        """вызывается всякий раз, когда удаляется атрибут класса"""
        print("__delattr__" + item)
        object.__delattr__(self, item)
        



pt = Point(1, 2)
a = pt.y
print(a)

