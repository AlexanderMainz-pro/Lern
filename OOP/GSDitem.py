class Student:
    def __init__(self, name, marks):#имя студента и его оценки
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):##смотрим значения
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):#переписываем значения
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть не отрицательным числом")
        if key == len(self.marks):
            off = key + 1 - len(self.marks)#вычисляем сколько нужно добавить
            self.marks.extend([None]*off)#расширяем с помощью экстенд
        self.marks[key] = value#по нужному индексу запишем новые значения

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть не отрицательным числом")

        del self.marks[key]


s1 = Student("Сергей", [4, 5, 3, 4, 2, 5])
s1[3] = 4
print(s1.marks[3])
print(s1[4])#обратились напрямую через метод getitems