from unittest import TestCase, main, skip, SkipTest
from SleepingQueens import SleepingQueens, Queen


class TestSleeping(TestCase):
    # @skip("generation of deck")
    def test_deckGeneration(self):
        queenDeck = SleepingQueens()
        self.assertEqual(len(queenDeck._sleepingQueensBoard), 12)
        self.assertIsInstance(queenDeck._sleepingQueensBoard[0], Queen)

    # @skip("method wakeQueen")
    def test_wakeQueen(self):
        queenDeck = SleepingQueens()
        awokenQueen = queenDeck.wakeQueen(0)
        self.assertEqual(awokenQueen.points,awokenQueen.getPoints())
        self.assertIsInstance(awokenQueen, Queen)
        self.assertIsInstance(awokenQueen.points, int)
        self.assertIsInstance(awokenQueen.name, str)
        self.assertIsNone(queenDeck.wakeQueen(0))
        self.assertIsNone(queenDeck.wakeQueen(13))
        self.assertIsNone(queenDeck.wakeQueen(-1))

    # @skip("method makeAsleep")
    def test_makeQueenAsleep(self):
        queenDeck = SleepingQueens()
        q00 = queenDeck.wakeQueen(0)
        q06 = queenDeck.wakeQueen(6)
        queenDeck.makeAsleep(q00)
        self.assertIsInstance(queenDeck._sleepingQueensBoard[0], Queen)
        self.assertIsNone(queenDeck._sleepingQueensBoard[6])
        queenDeck.makeAsleep(q06)
        for queen in queenDeck._sleepingQueensBoard:
            self.assertIsInstance(queen, Queen)

    # @skip("method getPositions")
    def test_getPositions(self):
        queenDeck = SleepingQueens()
        q00 = queenDeck.wakeQueen(0)
        q06 = queenDeck.wakeQueen(6)
        self.assertNotIn(0, queenDeck.getPositions())
        self.assertNotIn(6, queenDeck.getPositions())


if __name__ == "__main__":
    main(verbosity=2)
