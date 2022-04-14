import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):

    def test_run_doesnt_do_much(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run()

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "I don't do much, yet.\n")

    def test_still_life_block(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        input = "1,1 1,2 2,1 2,2"
        expected = "1,1 1,2 2,1 2,2"

        with contextlib.redirect_stdout(fake_stdout):
            game.run(input)

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, expected)

    def test_oscillator_blinker(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        input = "1,2 2,2 3,2"
        expected = "2,1 2,2 2,3"

        with contextlib.redirect_stdout(fake_stdout):
            game.run(input)

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, expected)


    #def test_still_life_block(self):
        # 1,1 1,2 2,1 2,2
        # 1,2 2,1 2,3  3,1 3,3 4,2 

    #    self.assertEqual(True, False)