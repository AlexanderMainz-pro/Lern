class Meta(type):

    def create_local_attrs(self, *args, **kwargs): #инициализатор<--1
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

#    def __init__(cls, name, bases, attrs):
#
#        cls.class_attrs = attrs
#        cls.__init__ = create_local_attrs #инициализатор класса Women являющийся сылкой на функцию 1-->


class Women(metaclass=Meta):
    class_attrs = {"title":"Заголовок", "content": "Контент", "photo": "Путь к фото"}
    title = "Заголовок"
    content = "Контент"
    photo = "Путь к фото"

    def __init__(self, *args, **kwargs): #инициализатор<--1
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

w = Women()
print(w.__dict__)