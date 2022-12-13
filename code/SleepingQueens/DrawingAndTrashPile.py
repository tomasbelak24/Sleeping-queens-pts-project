from random import shuffle
from typing import List
from Cards import Card, CardType
from DrawingPileMethods import DrawingPileMethod
from interfaces import DrawingAndTrashPileInterface

class DrawingAndTrashPile(DrawingAndTrashPileInterface):
    
    def __init__(self, toBeShuffled: bool = False, reloadMethod: DrawingPileMethod = DrawingPileMethod.drawingPileMethod1) -> None:
        super().__init__(toBeShuffled, reloadMethod)
        self.trashPile: List[Card] = []
        self.drawingPile: List[Card] = []
        self.generateCards(self.drawingPile)
        self.reloadMethod: DrawingPileMethod = reloadMethod
        if toBeShuffled:
            shuffle(self.drawingPile)


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
            self.trashPile.append(card)
        numberOfDiscards: int = len(discard)
        self.cardsDiscardedThisTurn: List[Card] = list(discard)
        newCards = []
        try:
            self.drawingPile, self.trashPile, newCards = self.reloadMethod(numberOfDiscards, dP = self.drawingPile, tP=self.trashPile)
        except Exception as e:
                    print("Doslo ku chybe pri drawingPileMetode", e)
        return newCards
           
    
    def newTurn(self):
        self.cardsDiscardedThisTurn.clear()

    
    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self.cardsDiscardedThisTurn

        