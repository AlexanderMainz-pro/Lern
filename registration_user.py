class Database:

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя содержащий атрибуты: логин и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Приветствую, выберите действие:\n1 - Вход\n2 - Регистрация\n")
        if choice == 1:
            login = input("Вевиде логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Взод выполненб {login}')
                    break
                else:
                    print("Неверный пароль")
            else:
                print("Пользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "), password:= input("Введите пароль: "),
                        password2:= input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте ещё раз")
                continue
    database.add_user(user.username, user.password)
    print(database.data)
