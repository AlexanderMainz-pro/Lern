class Integer: #универсальный инструмент
    @classmethod
    def veryfi_cords(cls, cords):
        if type(int) != int:
            raise TypeError('координата должна быть целым числов')

    def __set_name__(self, owner, name): #owner-ссылка на класс, name- ссылка на объект
        self.name = "_" + name

    def __get__(self , instance, owner):  #instance-ссылка на текущий экземпляр класс
        return  getattr(instance, self.name)

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)

class Point3D:
    x = Integer() #Дескрипторы
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z




p = Point3D(1, 2, 3)
print(p.__dict__)