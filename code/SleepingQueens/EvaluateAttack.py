from Cards import Card, CardType
from Hand import Hand
from Player import Player
from Game import Game
from DataType_Positions import HandPosition
from typing import Position

class EvaluateAttack:
    
    def __init__(self, cardType: CardType) -> None:
        self.attackingCardType: CardType = cardType
        
        if cardType == CardType.KING:
           self.defenseCardType = None
        
        if cardType == CardType.KNIGHT:
            self.defenseCardType = CardType.DRAGON
        
        if cardType == cardType.SLEEPING_POTION:
            self.defenseCardType = CardType.MAGIC_WAND
        
    
    def play(self,attackingPlayerIdx: int, targetQueen: Position = -1, targetPlayerIdx: int = -1) -> bool:
        if self.attackingCardType == CardType.KING:
            if Game.sleepingQueens.getQueens().keys() and targetQueen in range(12):
                Game.players[attackingPlayerIdx].awokenQueens.addQueen(Game.sleepingQueens._sleepingQueens[targetQueen])
                Game.sleepingQueens._sleepingQueens[targetQueen] = None
        
        if self.attackingCardType == CardType.KNIGHT:
            defenseCardIndex: HandPosition = Game.players[targetPlayerIdx].playerHand.hasCardOfType(self.defenseCardType)
            if defenseCardIndex is None:
                Game.players[attackingPlayerIdx].awokenQueens.addQueen(
                    Game.players[targetPlayerIdx].awokenQueens[targetQueen]
                )
                Game.players[targetPlayerIdx].awokenQueens.removeQueen(targetQueen)
            else:
                Game.players[targetPlayerIdx].playerHand.pickCards([defenseCardIndex])
                Game.players[targetPlayerIdx].playerHand.removePickedCardsAndRedraw(
                    Game.players[targetPlayerIdx].playerHand.returnPickedCards()
                )
        
        if self.attackingCardType == CardType.SLEEPING_POTION:
            defenseCardIndex: HandPosition = Game.players[targetPlayerIdx].playerHand.hasCardOfType(
                self.defenseCardType)
            if defenseCardIndex is None:
                Game.sleepingQueens.addQueen(
                    Game.players[targetPlayerIdx].awokenQueens[targetQueen]
                )
                Game.players[targetPlayerIdx].awokenQueens.removeQueen(
                    targetQueen)
            else:
                Game.players[targetPlayerIdx].playerHand.pickCards(
                    [defenseCardIndex])
                Game.players[targetPlayerIdx].playerHand.removePickedCardsAndRedraw(
                    Game.players[targetPlayerIdx].playerHand.returnPickedCards()
                )
        
        return True 
                

    def playedKing(self):
        return self.defenseCardType is None
