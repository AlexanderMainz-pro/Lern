from OOP.Call import Count

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds //60) % 60
        h = (self.seconds // 3600) % 24
        return  f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"#прописываем,
                                    #в каком формате мы хотим сотреть время

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):#возможность добавлять(РАБОТАТЬ С ЭКЗЕМПЛЯРОМ КЛАССа) + заработает
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый оператор должен быть int")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):#сказали что делать, когда записан справа операнд
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правыйоперант должен бытьобьектом int, или объектом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self

c1 = Clock(1000)
c2 = Clock(2000)
c1 = c1 + 100
c3 = c1 + c2
print(c1.get_time())
print(c3.get_time())
