from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Количество врагов для каждого рыцаря
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Задержка на 1 секунду
            self.enemies -= self.power
            self.days += 1

            # Убедимся, что количество врагов не опустится ниже 0
            remaining_enemies = max(0, self.enemies)
            print(f"{self.name} сражается {self.days}..., осталось {remaining_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дня(ей)!")


# Создание и запуск двух потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ждем завершения обоих потоков
first_knight.join()
second_knight.join()
print("Все битвы закончились")
