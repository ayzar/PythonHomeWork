import unittest
from runner import Runner, Tournament

def skip_if_frozen(is_frozen):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_frozen:
                return unittest.skip('Тесты в этом кейсе заморожены')(func)(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen(is_frozen)
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen(is_frozen)
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen(is_frozen)
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen(is_frozen)
    def test_first_tournament(self):
        usain = Runner("Usain", 10)
        nick = Runner("Nick", 3)
        tournament = Tournament(90, usain, nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results)]) == "Nick")

    @skip_if_frozen(is_frozen)
    def test_second_tournament(self):
        andrei = Runner("Andrei", 9)
        nick = Runner("Nick", 3)
        tournament = Tournament(90, andrei, nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results)]) == "Nick")

    @skip_if_frozen(is_frozen)
    def test_third_tournament(self):
        usain = Runner("Usain", 10)
        andrei = Runner("Andrei", 9)
        nick = Runner("Nick", 3)
        tournament = Tournament(90, usain, andrei, nick)
        results = tournament.start()
        self.assertTrue(str(results[max(results)]) == "Nick")

if __name__ == '__main__':
    unittest.main()
