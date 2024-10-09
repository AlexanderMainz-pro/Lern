from accessify import private, protected

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property #делет методом класса, можно посмотреть, но чтобы записсать -->
    def old(self):
        return self.__old

    @old.setter #и уже через созданный декоратор get_old вызываем сеттер, должен иметь такое же имя как и гетер
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    #old = property() #get_old, set_oldтеперь обращение к скрытым свойствам идет через имя a.old
    #old = old.setter(set_old) #для работы декораторов
    #old = old.getter(get_old)


a = Person('Sergey', 20)
a.old = 35 #
del a.old  #удаляем
a.old = 4  #создём
print(a.old, a.__dict__)
print(a.old, a.__dict__)