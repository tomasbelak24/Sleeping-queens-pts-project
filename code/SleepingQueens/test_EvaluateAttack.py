from unittest import TestCase, main, skip, SkipTest
from Game import Game
from EvaluateAttack import EvaluateAttack
from Cards import Card, CardType, Queen


class test_EvaluateAttack(TestCase):

    def test1(self):
        game = Game(2)
        eA = EvaluateAttack(1, CardType.KING, game)
        game.players[2].awokenQueens.addQueen(Queen(24, "Ingrid"))
        self.assertTrue(eA.play(1, 2))

    ### zacykleny model.. treba fixnut



if __name__ == "__main__":
    main(verbosity=2)
