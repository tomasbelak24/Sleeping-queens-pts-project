from DataType_Positions import HandPosition
from Hand import Hand
from Game import Game
from typing import List, Position, Dict
from EvaluateAttack import EvaluateAttack
from EvaluateNumberedCards import EvaluateNumberedCards
from Cards import CardType, Card, Queen
from GameState import GameState
from Queens import AwokenQueens

class Player:

    def __init__(self) -> None:
        self.playerHand: Hand = Hand(GameState.numberOfPlayers)
        self.awokenQueens: Dict[int, Queen] = AwokenQueens()

    
    def play(self, cardPositions: List[Position], targetQueen: Position = -1, targetPlayerIdx: int = -1) -> None:
        numberOfCards: int = len(cardPositions)
        cards: List[Card] = [self.playerHand._hand[pos] for pos in cardPositions]

        if numberOfCards == 1 and cards[0].isAttacking():
            # playing attacking card
            # evaluate attack
            typeOfCard: CardType = cards[0].type
            eA: EvaluateAttack = EvaluateAttack(typeOfCard)
            check: bool = eA.play(self.playerHand.playerIdx,targetQueen, targetPlayerIdx)
            if check:
                self.playerHand.pickCards(cardPositions)
                self.playerHand.removePickedCardsAndRedraw(self.playerHand.returnPickedCards())
                
        elif numberOfCards == 1 and not cards[0].isAttacking():
            raise "Player is not allowed to play a non-attacking card during his turn"
            
        elif all(list(map(lambda x: x.type == CardType.NUMBER, cards))):
            eN = EvaluateNumberedCards(cards)
            check: bool = eN.play()
            if check:
                self.playerHand.pickCards(cardPositions)
                self.playerHand.removePickedCardsAndRedraw(self.playerHand.returnPickedCards())
        

    def getPlayerState(self) -> None:
        return (self.playerHand._hand, self.awokenQueens)

    
