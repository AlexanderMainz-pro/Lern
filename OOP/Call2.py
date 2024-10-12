import math
class Derivate:
    def __init__(self, func): #вторым аргументом берём функцию
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate #создали декоратор
def df_sin(x):
    return math.sin(x)

#df_sin = Derivate(df_sin) #превратили функцию в экземпляр класса Derivate

class StripChars: #
    def __init__(self, chars): #сделали через класс, а не через замыкание функции
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)


s1 = StripChars('!@#$%/.,') #
s2 = StripChars(" ")
res = s1('Hello World!') #ПРОВЕРКА НА НАЛИЧИЕ СИМВОЛОВ
res2 = s2('Hello World!')

print(res, res2, sep="\n")
print(df_sin(math.pi/3))