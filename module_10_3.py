import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    # Если баланс превышает или равен 500, разблокируем замок, если он заблокирован
                    if not self.lock.locked():
                        self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            acquired = self.lock.acquire(blocking=False)  # Пытаемся заблокировать замок, не блокируя поток
            if acquired:
                try:
                    if amount <= self.balance:
                        self.balance -= amount
                        print(f"Снятие: {amount}. Баланс: {self.balance}")
                    else:
                        print("Запрос отклонён, недостаточно средств")
                finally:
                    self.lock.release()  # Обязательно разблокируем замок, даже если произошла ошибка
            else:
                print("Не удалось заблокировать замок")
            time.sleep(0.001)

def main():
    bank = Bank()

    deposit_thread = threading.Thread(target=bank.deposit)
    take_thread = threading.Thread(target=bank.take)

    deposit_thread.start()
    take_thread.start()

    deposit_thread.join()
    take_thread.join()

    print(f"Итоговый баланс: {bank.balance}")

if __name__ == "__main__":
    main()
