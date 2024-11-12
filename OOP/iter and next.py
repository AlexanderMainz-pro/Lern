class FRange:
    def _init__(self, start=0.0, stop=0.0, step=0.5):
        self.start = start
        self.stop =  stop
        self.step = step


    def __iter__(self):
        self.value = self.start - self.step
        return self


    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.stop
            return self.value
        else:
            raise StopIteration

class FRange2D:#формирует списки
    def _init__(self, start=0.0, stop=0.0, step=0.5, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        self.value +=1
        return iter (self.fr)#Возвращает итератор, в строках появ. значния

fr = FRange(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x)




