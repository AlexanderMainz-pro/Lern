class Count:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):# прописали __call__ для экземпляров класса Count
        print("__call__")
        self.__counter += 1
        return self.__counter

c = Count()
c() #экземпляры классы подобно функциям вызывать невозможно, после добавления __call__ можно вызывать
c()
c()
c()
c()
print(type(c))