from unittest import TestCase, main, skip, SkipTest
from QueenCollection import QueenCollection
from Queens import SleepingQueens, AwokenQueens
from Cards import Queen

class testQueenCollection(TestCase):
    
    def test_init(self):
        qC = QueenCollection()
        qC.addQueen(Queen(24, "Ingrid"))
        self.assertEqual("Ingrid", qC.collection[0].name)
        self.assertEqual(24, qC.collection[0].points)
    
    def test_removal(self):
        qC = QueenCollection()
        q: Queen = Queen(24, "Ingrid")
        qC.addQueen(q)
        self.assertEqual("Ingrid", qC.collection[0].name)
        self.assertEqual(24, qC.collection[0].points)
        self.assertEqual(q, qC.removeQueen(0))
        self.assertEqual(0, len(qC.getQueens().keys()))

    def test_wrongRemoval(self):
        qC = QueenCollection()
        qC.addQueen(Queen(24, "Ingrid"))
        self.assertEqual("Ingrid", qC.collection[0].name)
        self.assertEqual(24, qC.collection[0].points)
        self.assertIsNone(qC.removeQueen(2))
        self.assertEqual(1, len(qC.getQueens().keys()))


class testQueens(TestCase):

    def test_initSleepingQueens(self):
        sQ = SleepingQueens(toBeShuffled=False)
        self.assertEqual(12, len(sQ.getQueens().keys()))

    def test_initAwokenQueens(self):
        aQ = AwokenQueens()
        self.assertEqual(0, len(aQ.getQueens().keys()))

    

    






    

if __name__ == "__main__":
    main(verbosity=2)
