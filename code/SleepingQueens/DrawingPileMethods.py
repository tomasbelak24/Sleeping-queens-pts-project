from random import shuffle
from typing import List, Tuple, Optional
from Cards import Card
from interfaces import DrawingPileMethodsInterface

class DrawingPileMethod(DrawingPileMethodsInterface):

    def drawingPileMethod1(numberOfDiscards: int, dP: Optional[List[Card]], tP: List[Card]) -> Tuple[List[Card], List[Card], List[Card]]:
        newCards: List[Card] = []
        count: int = 0
        for i in range(numberOfDiscards):
            try:
                card = dP.pop(-1)
                newCards.append(card)
                count += 1
            except IndexError:
                dP = list(tP[::-1])
                shuffle(dP)
                tP.clear()
        
        for i in range(numberOfDiscards - count):
            card = dP.pop(-1)
            newCards.append(card)
        
        return (dP, tP, newCards)


    def drawingPileMethod2(numberOfDiscards: int, dP: Optional[List[Card]], tP: List[Card]) -> Tuple[List[Card], List[Card], List[Card]]:
        newCards: List[Card] = []
        leftInDrawing: int = len(dP)

        if leftInDrawing <= numberOfDiscards:
            shuffle(tP)
            temp: List[Card] = list(dP)
            dP = list(tP)
            tP.clear()
            for card in temp:
                dP.append(card)
        
        for i in range(numberOfDiscards):
            card = dP.pop(-1)
            newCards.append(card)

        return (dP, tP, newCards)
            
