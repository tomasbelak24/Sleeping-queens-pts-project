from typing import List, Dict, Any, Optional
from EvaluateAttack import EvaluateAttack
from EvaluateNumberedCards import EvaluateNumberedCards
from Cards import CardType, Card
from Queens import AwokenQueens
from interfaces import PlayerInterface, GameInterface, HandInterface

class Player(PlayerInterface):

    def __init__(self, game: GameInterface, playerHand: HandInterface) -> None:
        #self.playerHand: Hand = Hand(GameState.numberOfPlayers, game.piles)
        super().__init__(game, playerHand)
        self.playerHand = playerHand
        self.awokenQueens: AwokenQueens = AwokenQueens()
        self.game = game

    
    def play(self, cardPositions: List[Any], targetQueen: Any = -1, targetPlayerIdx: int = -1) -> Optional[bool]:
        numberOfCards: int = len(cardPositions)
        cards: List[Card] = [self.playerHand._hand[pos] for pos in cardPositions]

        if numberOfCards == 1 and cards[0].isAttacking():
            typeOfCard: CardType = cards[0].type
            eA: EvaluateAttack = EvaluateAttack(self,typeOfCard, game=self.game)
            attackWasSuccess: bool = eA.play(targetQueen, targetPlayerIdx)
                
            self.playerHand.pickCards(cardPositions)
            self.playerHand.removePickedCardsAndRedraw()
                
        elif numberOfCards == 1 and not cards[0].isAttacking():
            raise "Player is not allowed to play a non-attacking card during his turn"
            
        elif all(list(map(lambda x: x.type == CardType.NUMBER, cards))):
            eN = EvaluateNumberedCards()
            check: bool = eN.play(cards)
            if check:
                self.playerHand.pickCards(cardPositions)
                self.playerHand.removePickedCardsAndRedraw()
                return True
        

    def getPlayerState(self) -> None:
        return (self.playerHand._hand, self.awokenQueens)

    
