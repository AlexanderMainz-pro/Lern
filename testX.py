class Variable:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def value(self):
        print(self._name, 'GET', self._value)
        return self._value

    @value.setter
    def value(self, value):
        print(self._name, 'SET', self._value)
        self._value = value

var_1 = Variable('var_1', 'val_1')
var_2 = Variable('var_2', 'val_2')
var_1.value, var_2.value = var_2.value, var_1.value