from typing import List, Optional
from Cards import Card, CardType
from DrawingAndTrashPile import DrawingAndTrashPile
from DataType_Positions import HandPosition

class Hand:
    
    def __init__(self, playerIdx) -> None:
        self.playerIdx: int = playerIdx
        self._hand: int
    
    
    def pickCards(self, positions: List[int]) -> Optional[List[Card]]:
        howManyPicked: int = len(positions)
        if howManyPicked == 0:
            return

        for pos in positions:
            if pos not in range(5):
                return

        self._pickedCards = [card for i, card in enumerate(
            self._hand) if i in positions]
        return self._pickedCards


    def removePickedCardsAndRedraw(self) -> List[Card]:
        pickedCards = self.returnPickedCards()
        newCards = DrawingAndTrashPile.discardAndDraw(pickedCards)
        return newCards


    def returnPickedCards(self) -> List[Card]:
        return self._pickedCards

    
    def hasCardOfType(self, type: CardType) -> int:
        for i, card in enumerate(self._hand):
            if card.type == type:
                return i
        return
    

    def getGards(self) -> List[Card]:
        return self._hand
