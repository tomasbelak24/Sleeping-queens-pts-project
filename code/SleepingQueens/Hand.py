from typing import List, Optional, Dict
from Cards import Card, CardType
from DrawingAndTrashPile import DrawingAndTrashPile
from DataType_Positions import HandPosition

class Hand:
    
    def __init__(self, playerIdx) -> None:
        self.playerIdx: int = playerIdx
        self._hand: Dict[HandPosition, Card]
    
    
    def pickCards(self, positions: List[HandPosition]) -> Optional[List[Card]]:
        howManyPicked: int = len(positions)
        if howManyPicked == 0:
            return

        for pos in positions:
            if pos.getCardIndex() not in range(5):
                return

        self._pickedCards: List[Card] = []
        for pos in self._hand.keys():
            if pos in positions:
                self._pickedCards.append(self._hand(pos))

        return self._pickedCards


    def removePickedCardsAndRedraw(self) -> Dict(HandPosition, Card):
        pickedCards = self.returnPickedCards()
        newCards = DrawingAndTrashPile.discardAndDraw(pickedCards)
        discardedCards = list(DrawingAndTrashPile.getCardsDiscardedThisTurn())
        for pos in self._hand.keys:
            if self._hand[pos] in discardedCards:
                self._hand[pos] = newCards.pop(0)
        return self._hand


    def returnPickedCards(self) -> List[Card]:
        return self._pickedCards

    
    def hasCardOfType(self, type: CardType) -> HandPosition:
        for pos in self._hand.keys():
            if self._hand[pos].type == type:
                return pos
        return

    def getCards(self) -> List[Card]:
        return list(self._hand.values())
