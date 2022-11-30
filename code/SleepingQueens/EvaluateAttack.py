from Cards import Card, CardType
from Hand import Hand
from Player import Player

class EvaluateAttack:
    
    def __init__(self, cardType: CardType) -> None:
        if cardType == CardType.KING:
           self.defenseCardType = None
        
        if cardType == CardType.KNIGHT:
            self.defenseCardType = CardType.DRAGON
        
        if cardType == cardType.SLEEPING_POTION:
            self.defenseCardType = CardType.MAGIC_WAND
        
    
    def play(self, Queen: int = -1, targetPlayerIdx: int = -1) -> bool:
        ...

    def playedKing(self):
        return self.defenseCardType is None
