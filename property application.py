from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verity_fio(fio)
        self.verity_old(old)
        self.verity_weight(weight)
        self.verity_ps(ps)

        self.__fio = fio.split()
        self.__old = old #при сеттерах можно убрать сокрытие, тогда можно убрать и сами методы, работа нпрямую
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verity_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()#без пробелов
        if len(f)!= 3:
            raise TypeError("Неверный формат ФИО")

        letter = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER #сформировали разрешённые ФИО
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя-бы один символ")
            if len(s.strip(letter)) != 0:
                raise TypeError("В ФИО можно использовать буквы и дефиз")

    @classmethod
    def verity_old(cls, old):
        if type(old) != int or old < 14 or old < 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне")

    @classmethod
    def verity_weight(cls, weight):
        if type(weight) != float or weight < 120:
            raise TypeError("Вес должен быть вещественным числом и в диапазоне")

    @classmethod
    def verity_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if les(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise  TypeError("Серия и номер должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verity_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verity_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verity_ps(ps)
        self.__passport = ps


#p = Person("Иванов Иван Иванович", 35, "12 3434 567234", 80)
print(p)
