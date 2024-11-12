import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Создание объекта блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма пополнения
            with self.lock:  # Блокировка при изменении баланса
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    self.lock.release()  # Разблокировка при достижении необходимого баланса
            time.sleep(0.001)  # Имитация скорости выполнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Блокировка при изменении баланса
                if amount <= self.balance:  # Проверка, достаточно ли средств
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокировка при недостатке средств
            time.sleep(0.001)  # Имитация скорости выполнения

# Создание объекта класса Bank
bk = Bank()
# Создание потоков для пополнения и снятия средств
deposit_thread = threading.Thread(target=bk.deposit)
take_thread = threading.Thread(target=bk.take)

# Запуск потоков
deposit_thread.start()
take_thread.start()

# Ожидание завершения потоков
deposit_thread.join()
take_thread.join()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')