class ExceptionPrint(Exception):
    pass #можем выстраивать свою иерархию исключений и работать с ними

class ExpectionPrintSendData(ExceptionPrint):
    def __init__(self, *args):
        self.message = args[0] if args else None#

    def __str__(self):
        return f"сообщение {self.message}"# отображаем наше исключение ExpectionPrintSendData
"""Класс при отправке данных принтеру"""

class PrintData:# собственно печатает данные
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):#отправляет данные на печать
        if not self.send_to_print(data):
            raise ExpectionPrintSendData("принтер не отвечает") #можем отлавливать исключения

    def send_to_print(self, data): #проверяет, может печатать данные или нет
        return False

p = PrintData()
try:
    p.print("123")
except ExpectionPrintSendData: #можем отлавливать своё же исключение
    print("Принтер не отвечает")
except ExceptionPrint:
    print("Общая ошибка печати")

