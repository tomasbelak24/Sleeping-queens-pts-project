from Cards import Queen
from typing import Optional, Set

class SleepingQueens:

    def __init__(self) -> None:
        self.sleepingQueensBoard = [Queen(20, "Heart"), Queen(15, "Cat"), Queen(15, "Dog"), Queen(15, "Pancake"),
                          Queen(10, "Ladybug"), Queen(10, "Moon"), Queen(10, "Peacock"), Queen(10,"Sunflower"),
                          Queen(5, "Cake"), Queen(5, "Rainbow"), Queen(5, "Rose"), Queen(5,"Starfish")]

    # neskor metoda, dostane board position co bude zrejme int [0,11]
    def wakeQueen(self, position: int) -> Optional[Queen]:
        awokenQueen: Queen = self.sleepingQueensBoard[position]
        if awokenQueen is None:
            return
        self.sleepingQueensBoard[position] = None
        return awokenQueen

    # Tiez bude treba zmenit int za BoardPosition
    def makeAsleep(self, queen: Queen) -> None:
        firstFreeBoardPosition: int = self.sleepingQueensBoard.index(None)
        self.sleepingQueensBoard[firstFreeBoardPosition] = queen

    # int za BoardPosition
    def getPositions(self) -> Set[int]:
        return set([i for i, q in enumerate(self.sleepingQueensBoard) if q == None])




