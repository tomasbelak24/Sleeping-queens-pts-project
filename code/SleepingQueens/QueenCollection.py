from Cards import Queen
from DataType_Positions import SleepingQueenPosition, AwokenQueenPostion
from typing import Dict, Any, Optional

class QueenCollection:

    def __init__(self) -> None:
        self.collection: Dict[Any, Queen] = dict()

    def addQueen(self, key: Any, queen: Queen):
        self.collection[key] = queen

    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        try:
            queen: Queen = self.collection[position]
        except KeyError:
            return
        
        del self.collection[position]

        return queen

    def getQueens(self) -> Dict[Any, Queen]:
        return self.collection
