from typing import List, Optional, Dict
from Cards import Card, CardType
from DrawingAndTrashPile import DrawingAndTrashPile

class Hand:
    
    def __init__(self, playerIdx, drawing: DrawingAndTrashPile) -> None:
        self.playerIdx: int = playerIdx
        self._hand: Dict[int, Card] = dict()
        self.drawing: DrawingAndTrashPile = drawing
    
    
    def pickCards(self, positions: List[int]) -> Optional[List[Card]]:
        howManyPicked: int = len(positions)
        if howManyPicked == 0:
            return

        for pos in positions:
            if pos not in range(5):
                return

        self._pickedCards: List[Card] = []
        for pos in self._hand.keys():
            if pos in positions:
                self._pickedCards.append(self._hand[pos])

        return self._pickedCards


    def removePickedCardsAndRedraw(self) -> Dict[int, Card]:
        pickedCards = self.returnPickedCards()
        newCards = self.drawing.discardAndDraw(pickedCards)
        discardedCards = list(self.drawing.getCardsDiscardedThisTurn())
        for pos in self._hand.keys():
            if self._hand[pos] in discardedCards:
                self._hand[pos] = newCards.pop(0)
        return self._hand


    def returnPickedCards(self) -> List[Card]:
        return self._pickedCards

    
    def hasCardOfType(self, type: CardType) -> Optional[int]:
        for pos in self._hand.keys():
            if self._hand[pos].type == type:
                return pos
        return

    def getCards(self) -> List[Card]:
        return list(self._hand.values())

""" dp = DrawingAndTrashPile()
hand = Hand(1, dp)
cards = []
for i in range(1, 6):
    card = Card(CardType.NUMBER, i)
    hand._hand[i] = card
    cards.append(card)

pickedCards = hand.pickCards([1, 2, 3])
hand.removePickedCardsAndRedraw() """
