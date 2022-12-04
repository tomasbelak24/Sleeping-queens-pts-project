from random import shuffle
from typing import List
from Cards import Card, CardType

class DrawingAndTrashPile:
    
    def __init__(self, toBeShuffled: bool = False) -> None:
        self._trashPile: List[Card] = []
        self._drawingPile: List[Card] = []
        self.generateCards(self._drawingPile)
        if toBeShuffled:
            shuffle(self._drawingPile)


    def generateCards(self, arr: List[Card]) -> None:
        for i in range(8):
            arr.append(
                Card(CardType.KING, i+1))
        for i in range(4):
            arr.append(
                Card(CardType.KNIGHT, i+1))
        for i in range(4):
            arr.append(
                Card(CardType.SLEEPING_POTION, i+1))
        for i in range(3):
            arr.append(
                Card(CardType.MAGIC_WAND, i+1))
        for i in range(3):
            arr.append(
                Card(CardType.DRAGON, i+1))
        for i in range(4):
            for j in range(1, 11,1):
                arr.append(Card(CardType.NUMBER, j))
    

    def discardAndDraw(self, discard: List[Card]) -> List[Card]:
        for card in discard:
            self._trashPile.append(card)
        numberOfDiscards: int = len(discard)
        self.cardsDiscardedThisTurn: List[Card] = list(discard)
        return [self._drawingPile.pop(0) for i in range(numberOfDiscards)]
           
    
    def newTurn(self):
        self.cardsDiscardedThisTurn.clear()

    
    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self.cardsDiscardedThisTurn

        