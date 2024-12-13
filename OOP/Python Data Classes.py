import dataclasses


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"произошло {self.__dict__}" #смотрим, что мы там написали


@dataclasses
class ThindData:
    name: str #обязательно аннотируем
    weight: int
    price: float


t = Thing("Учебник", 100, 200)
td = Thing("Учебник", 1001, 2002)
print(t)
print(td)