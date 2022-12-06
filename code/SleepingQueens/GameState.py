from dataclasses import dataclass
from typing import List, Set, Dict, Optional
from SleepingQueens import SleepingQueens
from DataType_Positions import SleepingQueenPosition, HandPosition, AwokenQueenPostion
from Cards import Card, Queen

@dataclass
class GameState:
    numberOfPlayers: int
    onTurn: int
    sleepingQueens: Set[SleepingQueenPosition]
    awokenQueens: Dict[AwokenQueenPostion, Queen]
    cards: Dict[HandPosition, Optional[Card]]
    cardsDiscardedLastTurn: List[Card]

    def getNumberOfPlayers(self):
        return self.numberOfPlayers