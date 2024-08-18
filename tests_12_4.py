import unittest
import logging
from runner import Runner

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            runner = Runner("TestRunner", -5)  # Передаем отрицательное значение для проверки исключения
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
            self.fail(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем некорректный тип данных для проверки исключения
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
            self.fail(f"Неверный тип данных для объекта Runner: {e}")

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
