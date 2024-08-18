import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
suite = unittest.TestSuite()

# Используем TestLoader для загрузки тестов
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

# Создаем TextTestRunner с verbosity=2 и запускаем тесты
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)