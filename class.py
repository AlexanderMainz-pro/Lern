class Human:
    head = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birsday(self):
        self.age += 1
        print(f'У меня день олждения, мне теперь {self.age}')

    def __str__(self):#выыодим имя вместо непонятных символов
        return f'{self.name}'

    def __len__(self):#возвращает len
        return self.age

    def __lt__(self, other):#перегружаем оператор, оператор меньше
        return self.age < other.age

    def __gt__(self, other):#перегружаем оператор,оператор больше
        return self.age > other.age

    def __eq__(self, other):#перегружаем оператор, оператор сравнения
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    def __del__(self):#деструктор
        print(f'{self.name} ушёл')#объекты существуют, пока есть хотябы одна ссылка на него


den = Human('Денис', 12)
max = Human('Максим', 23)

if den:#если объект существует, вызываем методы
    den.say_info()

print(den.name, den.age)
den.surename = 'Попов'
print(max.name, max.age)
print(den.name, den.surename,  den.age )
den.say_info()
max.say_info()
max.birsday()

print(Human.head)
input()