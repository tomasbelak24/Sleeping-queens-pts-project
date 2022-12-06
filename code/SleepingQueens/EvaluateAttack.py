from Cards import CardType
from Hand import Hand
from Game import Game
from DataType_Positions import HandPosition
from typing import Any
from MoveQueen import MoveQueen

class EvaluateAttack:
    
    def __init__(self, playerIdx: int,cardType: CardType, game: Game) -> None:
        self.attackingCardType: CardType = cardType
        self.playerIdx: int = playerIdx
        self.game = game
        
        if cardType == CardType.KING:
           self.defenseCardType = None
        
        if cardType == CardType.KNIGHT:
            self.defenseCardType = CardType.DRAGON
        
        if cardType == cardType.SLEEPING_POTION:
            self.defenseCardType = CardType.MAGIC_WAND
        
    
    def play(self, targetQueen: Any = -1, targetPlayerIdx: int = -1) -> bool:
        if self.attackingCardType == CardType.KING:
            if self.game.sleepingQueens.getQueens().keys() and targetQueen in range(12):
                return True
        

        if self.attackingCardType == CardType.KNIGHT:
            targetPlayerHand: Hand = self.game.players[targetPlayerIdx].playerHand
            defenseCardIndex: HandPosition = targetPlayerHand.hasCardOfType(
                self.defenseCardType)
            if defenseCardIndex is not None:
                targetPlayerHand.pickCards(
                    targetPlayerHand._hand[defenseCardIndex])
                targetPlayerHand.removePickedCardsAndRedraw()
                return False
            
            check: bool = MoveQueen.playKnight(targetQueen, targetPlayerIdx)
            return check
                
        
        if self.attackingCardType == CardType.SLEEPING_POTION:
            targetPlayerHand: Hand = self.game.players[targetPlayerIdx].playerHand
            defenseCardIndex: HandPosition = targetPlayerHand.hasCardOfType(
                self.defenseCardType)
            if defenseCardIndex is not None:
                targetPlayerHand.pickCards(
                    targetPlayerHand._hand[defenseCardIndex])
                targetPlayerHand.removePickedCardsAndRedraw()
                return False

            check: bool = MoveQueen.playSleepingPotion(targetQueen, targetPlayerIdx)
            return check
