import random
import time
from threading import Thread
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.find_free_table()
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)  # Добавлено для предотвращения излишних нагрузок на цикл

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None


cafe = Cafe(Table(1), Table(2), Table(3))
guests = [Guest('Vasya'), Guest('Petya'), Guest('Masha'), Guest('Sasha')]


cafe.guest_arrival(*guests)
cafe.discuss_guests()


#1. Класс Table: Хранит номер стола и ссылку на гостя.
#2. Класс Guest: Наследуется от Thread, где каждый гость принимает пищу в течение 3–10 секунд.
#3. Класс Cafe:
#   - Атрибуты: очередь гостей и столы.
#   - Метод guest_arrival отвечает за прибытие гостей: если есть свободный стол, гость обрабатывается,
#иначе ставится в очередь.
#   - Метод discuss_guests обслуживает гостей, освобождает столы и назначает гостей из очереди.
#
#Этот код моделирует работу кафе с тремя столами и потоком обслуживания гостей.