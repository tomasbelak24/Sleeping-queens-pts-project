from Cards import Queen
from DataType_Positions import SleepingQueenPosition, AwokenQueenPostion
from typing import Dict, Any, Optional, List

class QueenCollection:

    def __init__(self) -> None:
        self.collection: Dict[Any, Queen] = dict()

    def addQueen(self, queen: Queen):
        maxKey = max(self.collection.keys()) + 1
        self.collection[maxKey] = queen
        self.indexRefresh()

    def removeQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        try:
            queen: Queen = self.collection[position]
        except KeyError:
            return
        
        del self.collection[position]
        self.indexRefresh()
        return queen

    def getQueens(self) -> Dict[Any, Queen]:
        return self.collection
    
    def indexRefresh(self) -> None:
        tempColl: Dict[Any, Queen] = dict()
        for i, key in enumerate(self.collection.keys()):
            tempColl[i] = self.collection[key]
        self.collection = tempColl.copy()




