import threading
from time import sleep
from random import randint as rand

class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.transaction = 1

    def deposit(self):

        for _ in range(100):
            random_number = rand(50, 500)
            with self.lock:
                self.balance += random_number

                print(f'Пополнение: {random_number}. Баланс: {self.balance}.')

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                
            sleep(0.001)

    def take(self):

        for _ in range(100):

            random_number = rand(50, 500)

            print(f'Запрос на {random_number}')

            with self.lock:

                if random_number <= self.balance:
                    self.balance -= random_number
                    print(f"Снятие: {random_number}. Баланс: {self.balance}.")
                else:
                    print(f'Запрос отклонён, недостаточно средств')

            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




