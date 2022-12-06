from Hand import Hand
from typing import List, Dict, Any
from EvaluateAttack import EvaluateAttack
from EvaluateNumberedCards import EvaluateNumberedCards
from Cards import CardType, Card
from Queens import AwokenQueens
from GameState import GameState
from MoveQueen import MoveQueen
from Game import Game

class Player:

    def __init__(self, game: Game) -> None:
        self.playerHand: Hand = Hand(GameState.numberOfPlayers)
        self.awokenQueens: AwokenQueens = AwokenQueens()
        self.game = game

    
    def play(self, cardPositions: List[Any], targetQueen: Any = -1, targetPlayerIdx: int = -1) -> None:
        numberOfCards: int = len(cardPositions)
        cards: List[Card] = [self.playerHand._hand[pos] for pos in cardPositions]

        if numberOfCards == 1 and cards[0].isAttacking():
            typeOfCard: CardType = cards[0].type
            eA: EvaluateAttack = EvaluateAttack(self.playerHand.playerIdx,typeOfCard, self.game)
            attackWasSuccess: bool = eA.play(targetQueen, targetPlayerIdx)
            if attackWasSuccess and typeOfCard == CardType.KING:
                # ak to nebol kral tak sa to vyhodnoti v EvaluateAttack a cez moveQueen sa mu pripise Q
                # ak bol attack uspesny a bol to kral tak presun kralovien spravim tu
                movingFromSleepingToAwoken: bool = MoveQueen.playKing(targetQueen, self)
                if not movingFromSleepingToAwoken:
                    raise "pri presuvani kralovny niekde nastala chyba"
                
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

    
