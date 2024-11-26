class Goods:
    def __init__(self, name, weight,  prise):
        super().__init__(1)#можно вызвать через супер и всё будет работать, добавляем доп параметр<--1
                           #так-же добавляем параметры от следующих миксенов
        print("Init mixinLog")
        self.name = name
        self.weight = weight
        self.prise = prise

    def prise_info(self):
        print(f"{self.name}, {self.weight}, {self.prise}")

class MixinLog:#дополнительный класс для логирования продаж, независимый класс, премиссии
    ID = 0

    def __init__(self, p1):# для избежания трудностей и проблем следует использовать только self в доп классах
                       #если используются доп параметры, нужно обязательно указывать в super().__init__(1) 1-->
        print("MixingLog")
        self.ID =+1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00")

    def prise_info(self):
        print("вызвался из класса MixinLog")


class NoteBook(Goods, MixinLog):
    def prise_info(self):#ереопределяем, если метод существует в нескольких классах и его нужно вызывать из конкретного
        MixinLog.prise_info(self)#если нужно всегда вызывать этот метод из дочернего класса --2--


n = NoteBook("aser", 1.5, 30000)
n.prise_info()
n.save_sell_log()
print(NoteBook.__mro__) #список классов, которые обходятся при поиске атрибутов
MixinLog.prise_info(n)#если есть одинаковые по названию методы, то конструкция вызова такая --2--
n.prise_info()