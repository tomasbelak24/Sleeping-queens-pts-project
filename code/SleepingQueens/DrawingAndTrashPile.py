from random import shuffle
from typing import List
from Cards import Card, CardType

class DrawingAndTrashPile:
    
    def __init__(self) -> None:
        self._trashPile: List[Card] = []
        self._drawingPile: List[Card] = []
        self.generateCards(self._drawingPile)
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



a = DrawingAndTrashPile()
print(a._drawingPile)
print(a._trashPile)