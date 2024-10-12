class _Humane:    #если импортировать, то импортируются только наследующие вещи, кроме самого класса
                 #так работает со всеми типами
    head = True
    _legs = True #нижнее подчеркивание может ограничить переменную до локального использования
    __arms = True

    def say_hello(self):
        print("Привет")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)#подставляется класс



class Student(_Humane):
    def about(self):
        print("Я студент")


class Teacher(_Humane):
    pass

humane = _Humane()
humane.about()

student = Student()
student.about()

print(student._Humane__arms)#доступ к приватным переменным