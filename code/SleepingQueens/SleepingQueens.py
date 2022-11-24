from Cards import Queen
from typing import Optional, Set
from random import shuffle

class SleepingQueens:

    def __init__(self) -> None:
        self._sleepingQueensBoard = [Queen(20, "Heart"), Queen(15, "Cat"), Queen(15, "Dog"), Queen(15, "Pancake"),
                          Queen(10, "Ladybug"), Queen(10, "Moon"), Queen(10, "Peacock"), Queen(10,"Sunflower"),
                          Queen(5, "Cake"), Queen(5, "Rainbow"), Queen(5, "Rose"), Queen(5,"Starfish")]
        shuffle(self._sleepingQueensBoard)

    # neskor metoda, dostane board position co bude zrejme int [0,11]
    def wakeQueen(self, position: int) -> Optional[Queen]:
        if position > 11:
            return
        awokenQueen: Queen = self._sleepingQueensBoard[position]
        if awokenQueen is None:
            return
        self._sleepingQueensBoard[position] = None
        return awokenQueen

    # Tiez bude treba zmenit int za BoardPosition
    def makeAsleep(self, queen: Queen) -> None:
        firstFreeBoardPosition: int = self._sleepingQueensBoard.index(None)
        self._sleepingQueensBoard[firstFreeBoardPosition] = queen

    # int za BoardPosition
    def getPositions(self) -> Set[int]:
        return set([i for i, q in enumerate(self._sleepingQueensBoard) if q != None])




