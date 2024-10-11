class TreadData:
    """моносостояние. Словарь с атрибутами класса"""
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id'  : 1
        }

    def __init__(self):
        self.__dict__ = self.__shared_attrs #коллекция ссылается на словарь при ккааждом новом создании объекта


th1 = TreadData()