from Cards import Queen
from QueenCollection import QueenCollection
from random import shuffle

class SleepingQueens(QueenCollection):

    def __init__(self, toBeShuffled: bool = False) -> None:
        super().__init__()
        allQueens = [Queen(20, "Heart"), Queen(15, "Cat"), Queen(15, "Dog"),
                     Queen(15, "Pancake"), Queen(10, "Ladybug"), Queen(10, "Moon"), 
                     Queen(10, "Peacock"), Queen(10, "Sunflower"),Queen(5, "Cake"),
                     Queen(5, "Rainbow"), Queen(5, "Rose"), Queen(5, "Starfish")]
        if toBeShuffled:
            shuffle(allQueens)

        for i, queen in enumerate(allQueens):
            self.addQueen(i, queen)
    
class AwokenQueens(QueenCollection):
    
    def __init__(self) -> None:
        super().__init__()
        