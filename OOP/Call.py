class Count:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):# прописали __call__ для экземпляров класса Count
        print("__call__")
        self.__counter += 1
        return self.__counter

c = Count()
c2 = Count()
c3 = Count()
c() #экземпляры классы подобно функциям вызывать невозможно, после добавления __call__ можно вызывать
c() #объекты классов, которые могут себя так вести называются функторы
c2() #получаем независимые счетчики
c3()
c()
res = c()
res2 = c2()
# print(type(c)
print(res, res2)