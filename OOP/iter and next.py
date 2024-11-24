class FRange:
    def __init__(self, start=0, stop=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step #увеличиваем на длину шага
            return self.value
        else:
            raise StopIteration


class FRange2D:#формирует списки
    def __init__(self, start=0, stop=0, step=0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step) #<--2

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
             self.value +=1
             return iter(self.fr)#Возвращает итератор, в строках появ. значния <--1
        else:
            raise StopIteration


#fr = FRange(0,5,1)
##for x in fr:
#    print(x)

fr2 =FRange2D(0, 5, 1)
for row in fr2: #получаем каждый раз объект из 1-->
    for x in row: #перебираем FRange и получаем конкретные значения 2-->
        print(x, end=" ")
    print()

