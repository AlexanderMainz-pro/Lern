import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda a, b: a == b, first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(f"{data}\n")
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Пример использования
ball = MysticBall(['Да', 'Нет', 'Может быть', 'Определи сам'])
result = ball.__call__()
print(result)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())