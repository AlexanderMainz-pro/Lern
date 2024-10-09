class Human:
    def __init__(self, name, group):#добавляем аргумент group123
        self.name = name
        super().__init__(group)#обращаемся к следующему классу стоящий в цепочке наследования
        super().about()

    def info(self):
        print(f"меня зовут {self.name}")


class StudentGroup():
    def __init__(self, group):#добавляем аргумент group123
        self.group = group

    def about(self):
        print(f"{self.name} учится в группе {self.group}")


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):#добавляем аргумент group123
        #Human.__init__(self, name)#передаём напрямую из класса конструктора
        super().__init__(name, group)#метод супер позволяет обращяться к классу родителю Human
        self.place = place
        super().info()#позволяет обращаться к классу родителю



#human = Human("Денис")
#print(human.name)

student = Student("Макс", "Урбан", "Group")#добавляем аргумент group123
print(StudentGroup.mro())#метод посмотреть глубину наследоваания, не забываем смотреть цепочку
print(Student.mro())