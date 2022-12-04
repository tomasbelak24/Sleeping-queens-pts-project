from typing import List, Any
from Cards import Card

class GameAdaptor:

    def __init__(self, cards: List[Card], targetQueen: Any, targetPlayer: int) -> None:
        self.command: List[Any] = [cards, targetQueen, targetPlayer]


    def getGameArguments(self) -> List[Any]:
        return self.command
