class DefenderVector:
    def __init__(self, v):
        self.__v = v #ссылается на первый вектор v1

    def __enter__(self):
        self.__temp = self.__v[:]#сылается на копию вектора, создаём копию
        return  self.__temp# ссылается на копию dv 1-->>

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp # копируем, если нет ошибок в __v <<--1.1

        return False

v1 = [1, 2, 3]# если будут ошибки, не меняем, если нет, то вносим изменения
v2 = [3, 4, 3]# если убрать один аргумент, то будет выпадать в ошибку, как мы и задумали

try:
    with DefenderVector(v1) as dv: #<<--1
        for i, a in enumerate(dv):# если здесь ошибок не произойдет, то не меняем
            dv[i] += v2[i]#работаем с копией вектора
except:
    print("Ошибка")

print(v1)
