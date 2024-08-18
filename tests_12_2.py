import unittest
from runner import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"Test {key}: {result}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results['Усейн vs Ник'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

    def test_andrei_nick(self):
        tournament = Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results['Андрей vs Ник'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

    def test_usain_andrei_nick(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        results = tournament.start()
        TournamentTest.all_results['Усейн vs Андрей vs Ник'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(str(results[max(results)]) == "Ник")

if __name__ == '__main__':
    unittest.main()
