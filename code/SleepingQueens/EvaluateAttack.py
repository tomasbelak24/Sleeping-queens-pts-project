from Cards import CardType
from Hand import Hand
from DataType_Positions import HandPosition
from typing import Any
from MoveQueen import MoveQueen
from interfaces import EvaluateAttackInterface, GameInterface, PlayerInterface

class EvaluateAttack(EvaluateAttackInterface):
    
    def __init__(self, player: PlayerInterface,cardType: CardType, game: GameInterface) -> None:
        self.attackingCardType: CardType = cardType
        self.player: PlayerInterface = player
        self.game: GameInterface = game
        
        if cardType == CardType.KING:
           self.defenseCardType = None
        
        if cardType == CardType.KNIGHT:
            self.defenseCardType = CardType.DRAGON
        
        if cardType == cardType.SLEEPING_POTION:
            self.defenseCardType = CardType.MAGIC_WAND
        
    
    def play(self, targetQueen: Any = -1, targetPlayerIdx: int = -1) -> bool:
        check: bool = False
        if self.attackingCardType == CardType.KING:
            if self.game.sleepingQueens.getQueens().keys() and targetQueen in range(12):
                check = MoveQueen.playKing(targetQueen, self.player)
            return check
        

        if self.attackingCardType == CardType.KNIGHT:
            targetPlayerHand: Hand = self.game.players[targetPlayerIdx].playerHand
            defenseCardIndex: HandPosition = targetPlayerHand.hasCardOfType(
                self.defenseCardType)
            if defenseCardIndex is not None:
                targetPlayerHand.pickCards(
                    [defenseCardIndex])
                targetPlayerHand.removePickedCardsAndRedraw()
                return False
            
            check: bool = MoveQueen.playKnight(targetQueen, targetPlayerIdx, self.player)
            return check
                
        
        if self.attackingCardType == CardType.SLEEPING_POTION:
            targetPlayerHand: Hand = self.game.players[targetPlayerIdx].playerHand
            defenseCardIndex: HandPosition = targetPlayerHand.hasCardOfType(
                self.defenseCardType)
            if defenseCardIndex is not None:
                targetPlayerHand.pickCards(
                    [defenseCardIndex])
                targetPlayerHand.removePickedCardsAndRedraw()
                return False

            check: bool = MoveQueen.playSleepingPotion(targetQueen, targetPlayerIdx, self.player)
            return check
