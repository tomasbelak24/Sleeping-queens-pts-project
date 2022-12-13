from unittest import TestCase, main, skip, SkipTest
from Game import Game
from EvaluateAttack import EvaluateAttack
from Cards import CardType, Queen


class test_EvaluateAttack(TestCase):

    def test1(self):
        game = Game(2)
        eA = EvaluateAttack(1, CardType.KING, game)
        game.players[1].awokenQueens.addQueen(Queen(24, "Ingrid"))
        self.assertTrue(eA.play(1, 2))

    ### zacykleny model.. treba fixnut
    ### fixnute

    def test2(self):
        game = Game(3)
        eA = EvaluateAttack(2, CardType.KING, game)
        game.players[2].awokenQueens.addQueen(Queen(24, "Ingrid"))
        self.assertTrue(eA.play(2,1))





if __name__ == "__main__":
    main(verbosity=2)
