class User:
    __instans = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instans is None:#если небыл создан атрибут, то мы запишем ссылку в наш класс
            cls.__instans = super().__new__(cls)
        return cls.__instans#singletone, возвращаем ссылку на класс, из класса objext применяем к нашему классу

    def __init__(self, *args, **kwargs):
        print("Я в ините")
        self.args = args
        for key, value in kwargs.items():#если не знем, сколько знчений, то пробегаемся по всем атрибутаам
            setattr(self, key, value)


other = [1, 2, 3]
user = {'name':'Den', 'age': 25, 'gender': 'male'}

user1 = User(*other, **user)#можно вызывать единожды
#user2 = User()
#print(id(user1), id(user2))#при данном создании все обьекты ведут к одному адресу в памяти
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)