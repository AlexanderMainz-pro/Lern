class Women:
    title = "Объект класса для поля title"
    photo = "Объект класса для поля photo"
    ordering = "Объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw) #обязательно прописываем, что-бы создать экземпляр класса Meta

    class Meta:#не созаётся, создаем только в момент создания объекта
        ordering = ["id"] #обращаться ко внешним классам нельзя, только при инициализации

        def __init__(self, access):
            self._access = access

w = Women("root", "123")#создаем локально для каждого атрибута, но так-же можем обращаться к классовым методам
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)