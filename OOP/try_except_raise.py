class PrintData:# собственно печатает данные
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):#отправляет данные на печать
        if not self.send_to_print(data):
            raise Exception("принтер не отвечает")

    def send_to_print(self, data):#проверяет, може печатать данные или нет
        return False
