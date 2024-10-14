from DZ_7_2 import result


def greeed_person(person_name):
    if person_name == 'Воландеморт':
        raise Exception('Мы не любим тебя, Воландеморт')# сгенерировали ошибку, но нигде не перехватили
    print(f"Привет {person_name}, рады тебя видеть")

greeed_person("Ученик")
greeed_person("Воландеморт")

try:
    raise NameError('Привет, ты там?')
except NameError as exp:
    print(f'Исключение типа {type(exp)} пролетело мимо, его параметры {exp.args}')


class ProZero(Exception):
    def __init__(self, messsage, extra_info):
        self.messsage = messsage
        self.extra_info = extra_info

def x(a, b):
    if b == 0:
        raise ProZero('на ноль делить нельзя', {"a": a, "b": b})
    return a / b

try:
    result = x(10, 5)
except ProZero as e:
    print(f'Сегодня хороший день')
    print(f'Сообщение об ошибке{e.messsage}')
    print(f'Дополнительная информация{e.extra_info}')

print(x(5, 0))
