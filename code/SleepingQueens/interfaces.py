from typing import List, Optional, Tuple, Dict, Any
from Cards import Card, CardType, Queen
from GameState import GameState



class DrawingPileMethodsInterface:

    def drawingPileMethod1(numberOfDiscards: int, dP: Optional[List[Card]], tP: List[Card]) -> Tuple[List[Card], List[Card], List[Card]]:
        pass

    def drawingPileMethod2(numberOfDiscards: int, dP: Optional[List[Card]], tP: List[Card]) -> Tuple[List[Card], List[Card], List[Card]]:
        pass


class DrawingAndTrashPileInterface:

    def __init__(self, toBeShuffled: bool = False, reloadMethod: DrawingPileMethodsInterface = DrawingPileMethodsInterface.drawingPileMethod1) -> None:
        pass
    
    def discardAndDraw(self, discard: List[Card]) -> List[Card]:
        pass
    
    def newTurn(self):
        pass

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        pass


class HandInterface:
    
    def __init__(self, playerIdx, drawing: DrawingAndTrashPileInterface) -> None:
        pass

    def pickCards(self, positions: List[int]) -> Optional[List[Card]]:
        pass

    def removePickedCardsAndRedraw(self) -> Dict[int, Card]:
        pass

    def returnPickedCards(self) -> List[Card]:
        pass

    def hasCardOfType(self, type: CardType) -> Optional[int]:
        pass

    def getCards(self) -> List[Card]:
        pass


class QueenCollectionInterface:

    def __init__(self) -> None:
        pass

    def addQueen(self, queen: Queen):
        pass

    def removeQueen(self, position: Any) -> Optional[Queen]:
        pass

    def getQueens(self) -> Dict[Any, Queen]:
        pass

    def indexRefresh(self) -> None:
        pass


class GameInterface:
    def __init__(self, numOfPlayers: int, otherDiscardPileMethod: bool = False) -> None:
        pass

    def game(self):
        pass

    def play(self, playerIdx: int, cards: List[Any], targetQueen: Any, targetPlayerIdx: int) -> Optional[GameState]:
        pass

    def getTurn(self) -> int:
        pass

    def dealCardsToPlayers(self) -> None:
        pass

class EvaluateNumberedCardsInterface:

    def play(self, cards: List[Card]) -> bool:
        pass

class EvaluateAttackInterface:

    def __init__(self, playerIdx: int,cardType: CardType) -> None:
        pass

    def play(self, targetQueen: Any = -1, targetPlayerIdx: int = -1) -> bool:
        pass

class PlayerInterface:

    def __init__(self, game: GameInterface, playerHand: HandInterface) -> None:
        pass

    def play(self, cardPositions: List[Any], targetQueen: Any = -1, targetPlayerIdx: int = -1) -> None:
        pass

    def getPlayerState(self) -> None:
        pass

    



