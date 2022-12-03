from Cards import Queen
from DataType_Positions import SleepingQueenPosition, AwokenQueenPostion
from typing import Dict, Position, Optional

class QueenCollection:

    def __init__(self, type: str) -> None:
        self.collection: Dict[Position, Queen]

    def addQueen(self, key: Position, queen: Queen):
        self.collection[key] = queen

    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        del self.collection[position]

    def getQueens(self) -> Dict[Position, Queen]:
        return self.collection
