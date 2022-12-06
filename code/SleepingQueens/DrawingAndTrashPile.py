from random import shuffle
from typing import List
from Cards import Card, CardType

class DrawingAndTrashPile:
    
    def __init__(self, toBeShuffled: bool = False, otherReloadMethod: bool = False) -> None:
        self._trashPile: List[Card] = []
        self._drawingPile: List[Card] = []
        self.generateCards(self._drawingPile)
        self.otherReloadMethod: bool = otherReloadMethod
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
        newCards = []
        if not self.otherReloadMethod:
            for i in range(numberOfDiscards):
                try:
                    card = self._drawingPile.pop(0)
                except IndexError:
                    self._drawingPile = list(self._trashPile[::-1])
                    shuffle(self._drawingPile)
                    self._trashPile.clear()
                    card = self._drawingPile.pop(0)
                newCards.append(card)
        else:
            leftInDrawing: int = len(self._drawingPile)
            if leftInDrawing <= numberOfDiscards:
                shuffle(self._trashPile)
                temp: List[Card] = list(self._drawingPile)
                self._drawingPile = list(self._trashPile)
                self._trashPile.clear()
                for card in temp:
                    self._drawingPile.append(card)
            for i in range(numberOfDiscards):
                newCards.append(self._drawingPile.pop(0))
    
        return newCards
           
    
    def newTurn(self):
        self.cardsDiscardedThisTurn.clear()

    
    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self.cardsDiscardedThisTurn

        