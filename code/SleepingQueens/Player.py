from DataType_Positions import HandPosition
import DrawingAndTrashPile, SleepingQueens, Hand
from Game import Game
from typing import List
import EvaluateAttack
import EvaluateNumberedCards
from Cards import CardType, Card

class Player:

    def __init__(self) -> None:
        self._hand: Hand = Hand(Game.getNumOfPlayers())
        Game.addPlayer(self)

    
    def play(self, cardPositions: List[int]) -> None:
        numberOfCards: int = len(cardPositions)
        cards: List[Card] = [self._hand[pos] for pos in cardPositions]

        if numberOfCards == 1 and cards[0].isAttacking():
            # playing attacking card
            # evaluate attack
            typeOfCard = cards[0].type
            eA = EvaluateAttack(type)
            if typeOfCard == CardType.KING:
                eA.play()   # tuto musi ist do argumentu index kralovny ktoru chce hrac zobrat ale do pici
                ...         # odkial mam vediet aky ten index je.. napalim to tam v testoch
            elif typeOfCard == CardType.KNIGHT:
                eA.play()
                ...
            elif typeOfCard == CardType.SLEEPING_POTION:
                eA.play()
                ...
        elif all(list(map(lambda x: x.type == CardType.NUMBER, cards))):
            #musia byt numbered karty
            #evaluate numbered cards
            eN = EvaluateNumberedCards()
            eN.play()
            ...

    def getPlayerState(self) -> None:
        ...

    
