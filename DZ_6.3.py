class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self, dx):
        self.x_distance += dx  # увеличиваем пройденный путь на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy  # увеличиваем высоту полёта на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)  # вызываем метод run() из класса Horse
        self.fly(dy)  # вызываем метод fly() из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # возвращаем положение в виде кортежа

    def voice(self):
        print(self.sound)  # печатаем звук пегаса


# Создаем объект класса Pegasus
pegasus = Pegasus()

# Проверка работы методов
print("Начальные позиции:", pegasus.get_pos())  # Вывод: (0, 0)
pegasus.run(10)  # Лошадь пробежала 10
print("Позиция после бега:", pegasus.get_pos())  # Вывод: (10, 0)
pegasus.fly(20)  # Орел поднялся на 20
print("Позиция после полета:", pegasus.get_pos())  # Вывод: (10, 20)
pegasus.move(5, 15)  # Пегас перемещается на (5, 15)
print("Позиция после движения:", pegasus.get_pos())  # Вывод: (15, 35)
pegasus.voice()  # Вывод: I train, eat, sleep, and repeat



#Необходимо написать 3 класса:
#Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
#x_distance = 0 - пройденный путь.
#sound = 'Frrr' - звук, который издаёт лошадь.
#И методами:
#run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

#Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
#y_distance = 0 - высота полёта
#sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
#И методами:
#fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

#Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
#Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
#Также обладает методами:
#move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
#get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
#voice - который печатает значение унаследованного атрибута sound.
#Пункты задачи:
#Создайте классы родители: Horse и Eagle с методами из описания.
#Создайте класс наследник Pegasus с методами из описания.
#Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.